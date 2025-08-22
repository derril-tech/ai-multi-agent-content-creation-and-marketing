"""
Main FastAPI application entry point for the AI Multi-Agent Content Creation & Marketing System.

This module initializes the FastAPI application with all necessary middleware,
routers, and configuration for the multi-agent content creation platform.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
import time
import structlog
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.api import api_router
from app.core.database import init_db
from app.core.redis import init_redis

# Setup structured logging
setup_logging()
logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager for startup and shutdown events.
    
    Handles:
    - Database initialization
    - Redis connection setup
    - Graceful shutdown of connections
    """
    # Startup
    logger.info("Starting AI Multi-Agent Content Creation & Marketing System")
    
    try:
        # Initialize database connection
        await init_db()
        logger.info("Database connection established")
        
        # Initialize Redis connection
        await init_redis()
        logger.info("Redis connection established")
        
        logger.info("Application startup completed successfully")
    except Exception as e:
        logger.error("Failed to initialize application", error=str(e))
        raise
    
    yield
    
    # Shutdown
    logger.info("Shutting down AI Multi-Agent Content Creation & Marketing System")
    # Add any cleanup logic here

# Create FastAPI application instance
app = FastAPI(
    title="AI Multi-Agent Content Creation & Marketing System",
    description="""
    Next-generation AI-driven content automation platform with multi-agent orchestration.
    
    ## Features
    
    * **Multi-Agent Orchestration**: Coordinate multiple AI agents for content creation
    * **Content Generation**: AI-powered content creation with GPT-4 and Claude
    * **Marketing Automation**: Automated distribution across multiple channels
    * **Real-time Collaboration**: Live editing and team collaboration features
    * **Analytics & Insights**: Comprehensive performance tracking and optimization
    * **Enterprise Security**: SOC 2 compliant with end-to-end encryption
    
    ## API Endpoints
    
    * `/api/v1/auth` - Authentication and user management
    * `/api/v1/content` - Content creation and management
    * `/api/v1/agents` - AI agent orchestration
    * `/api/v1/marketing` - Marketing automation and distribution
    * `/api/v1/analytics` - Analytics and performance tracking
    * `/api/v1/websocket` - Real-time WebSocket connections
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add trusted host middleware for security
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS,
)

# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Middleware to add request processing time to response headers.
    
    This helps with performance monitoring and debugging.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log all incoming requests for monitoring and debugging.
    """
    start_time = time.time()
    
    # Log request details
    logger.info(
        "Incoming request",
        method=request.method,
        url=str(request.url),
        client_ip=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent"),
    )
    
    response = await call_next(request)
    
    # Log response details
    process_time = time.time() - start_time
    logger.info(
        "Request completed",
        method=request.method,
        url=str(request.url),
        status_code=response.status_code,
        process_time=process_time,
    )
    
    return response

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Global exception handler for unhandled errors.
    
    Logs the error and returns a generic error response to avoid exposing
    sensitive information in production.
    """
    logger.error(
        "Unhandled exception",
        error=str(exc),
        method=request.method,
        url=str(request.url),
        exc_info=True,
    )
    
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "error_code": "INTERNAL_ERROR",
        },
    )

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring and load balancers.
    
    Returns basic system status information.
    """
    return {
        "status": "healthy",
        "service": "AI Multi-Agent Content Creation & Marketing System",
        "version": "1.0.0",
        "timestamp": time.time(),
    }

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint with basic API information.
    """
    return {
        "message": "AI Multi-Agent Content Creation & Marketing System API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }

# Include API router with versioning
app.include_router(api_router, prefix="/api/v1")

# WebSocket endpoint for real-time features
@app.websocket("/ws")
async def websocket_endpoint(websocket):
    """
    WebSocket endpoint for real-time features like live collaboration.
    
    This is a placeholder - actual WebSocket logic will be implemented
    in the WebSocket manager.
    """
    await websocket.accept()
    try:
        while True:
            # Echo received messages (placeholder)
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except Exception as e:
        logger.error("WebSocket error", error=str(e))
    finally:
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info" if not settings.DEBUG else "debug",
    )
