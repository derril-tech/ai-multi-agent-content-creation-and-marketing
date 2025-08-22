"""
Database connection and session management for the AI Multi-Agent Content Creation & Marketing System.

This module handles database initialization, connection pooling, and session management
using SQLAlchemy 2.0 with async/await support.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool
import structlog

from app.core.config import settings

logger = structlog.get_logger()

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    poolclass=NullPool,  # Use NullPool for async operations
    future=True,
)

# Create async session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for all models
Base = declarative_base()

async def init_db():
    """
    Initialize database connection and create tables.
    
    This function should be called during application startup.
    """
    try:
        # Test database connection
        async with engine.begin() as conn:
            await conn.run_sync(lambda sync_conn: sync_conn.execute("SELECT 1"))
        
        logger.info("Database connection established successfully")
        
        # Create tables (in production, use migrations instead)
        if settings.ENVIRONMENT == "development":
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            logger.info("Database tables created successfully")
            
    except Exception as e:
        logger.error("Failed to initialize database", error=str(e))
        raise

async def get_db() -> AsyncSession:
    """
    Dependency to get database session.
    
    This function is used as a FastAPI dependency to provide database sessions
    to API endpoints.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            logger.error("Database session error", error=str(e))
            raise
        finally:
            await session.close()

async def close_db():
    """
    Close database connections.
    
    This function should be called during application shutdown.
    """
    await engine.dispose()
    logger.info("Database connections closed")
