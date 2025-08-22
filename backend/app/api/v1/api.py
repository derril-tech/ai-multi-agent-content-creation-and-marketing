"""
Main API router for the AI Multi-Agent Content Creation & Marketing System.

This module combines all API endpoint routers into a single router for the application.
"""

from fastapi import APIRouter

# Import all endpoint routers
from app.api.v1.endpoints import auth, content, agents, marketing, analytics, websocket

# Create main API router
api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    content.router,
    prefix="/content",
    tags=["Content Management"]
)

api_router.include_router(
    agents.router,
    prefix="/agents",
    tags=["AI Agents"]
)

api_router.include_router(
    marketing.router,
    prefix="/marketing",
    tags=["Marketing Automation"]
)

api_router.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["Analytics"]
)

api_router.include_router(
    websocket.router,
    prefix="/websocket",
    tags=["WebSocket"]
)
