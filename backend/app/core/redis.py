"""
Redis connection and caching for the AI Multi-Agent Content Creation & Marketing System.

This module handles Redis connection, caching operations, and session management.
"""

import aioredis
import structlog
from typing import Optional, Any

from app.core.config import settings

logger = structlog.get_logger()

# Global Redis connection
redis_client: Optional[aioredis.Redis] = None

async def init_redis():
    """
    Initialize Redis connection.
    
    This function should be called during application startup.
    """
    global redis_client
    
    try:
        redis_client = aioredis.from_url(
            settings.REDIS_URL,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD,
            encoding="utf-8",
            decode_responses=True
        )
        
        # Test connection
        await redis_client.ping()
        logger.info("Redis connection established successfully")
        
    except Exception as e:
        logger.error("Failed to connect to Redis", error=str(e))
        raise

async def get_redis() -> aioredis.Redis:
    """
    Get Redis client instance.
    
    This function is used as a dependency to provide Redis client
    to other parts of the application.
    """
    if redis_client is None:
        raise RuntimeError("Redis client not initialized")
    return redis_client

async def close_redis():
    """
    Close Redis connection.
    
    This function should be called during application shutdown.
    """
    global redis_client
    
    if redis_client:
        await redis_client.close()
        logger.info("Redis connection closed")

# Cache utility functions
async def cache_get(key: str) -> Optional[str]:
    """Get value from cache."""
    try:
        redis = await get_redis()
        return await redis.get(key)
    except Exception as e:
        logger.error("Cache get error", key=key, error=str(e))
        return None

async def cache_set(key: str, value: str, expire: int = 3600) -> bool:
    """Set value in cache with expiration."""
    try:
        redis = await get_redis()
        await redis.set(key, value, ex=expire)
        return True
    except Exception as e:
        logger.error("Cache set error", key=key, error=str(e))
        return False

async def cache_delete(key: str) -> bool:
    """Delete value from cache."""
    try:
        redis = await get_redis()
        await redis.delete(key)
        return True
    except Exception as e:
        logger.error("Cache delete error", key=key, error=str(e))
        return False

async def cache_exists(key: str) -> bool:
    """Check if key exists in cache."""
    try:
        redis = await get_redis()
        return await redis.exists(key) > 0
    except Exception as e:
        logger.error("Cache exists error", key=key, error=str(e))
        return False
