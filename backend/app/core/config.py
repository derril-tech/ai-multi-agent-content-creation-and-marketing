"""
Configuration settings for the AI Multi-Agent Content Creation & Marketing System.

This module defines all configuration settings using Pydantic Settings for
environment variable management and validation.
"""

from typing import List, Optional
from pydantic import BaseSettings, validator
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    All settings are validated and have sensible defaults for development.
    """
    
    # Application settings
    APP_NAME: str = "AI Multi-Agent Content Creation & Marketing System"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 1
    
    # Security settings
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS settings
    ALLOWED_HOSTS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    @validator("ALLOWED_HOSTS", pre=True)
    def assemble_cors_origins(cls, v):
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    # Database settings
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/ai_multi_agent"
    DATABASE_ECHO: bool = False
    
    # Redis settings
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    
    # AI API settings
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    
    # Cloud storage settings
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET: Optional[str] = None
    
    # Email settings
    SENDGRID_API_KEY: Optional[str] = None
    EMAIL_FROM: str = "noreply@ai-multi-agent.com"
    
    # SMS settings
    TWILIO_ACCOUNT_SID: Optional[str] = None
    TWILIO_AUTH_TOKEN: Optional[str] = None
    TWILIO_PHONE_NUMBER: Optional[str] = None
    
    # Monitoring settings
    ENABLE_METRICS: bool = True
    METRICS_PORT: int = 9090
    
    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    RATE_LIMIT_PER_HOUR: int = 1000
    
    # File upload settings
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_FILE_TYPES: List[str] = [
        "image/jpeg",
        "image/png",
        "image/gif",
        "application/pdf",
        "text/plain",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]
    
    # Content generation settings
    MAX_CONTENT_LENGTH: int = 5000
    DEFAULT_CONTENT_TONE: str = "professional"
    DEFAULT_CONTENT_STYLE: str = "informative"
    
    # Agent settings
    MAX_CONCURRENT_AGENTS: int = 10
    AGENT_TIMEOUT_SECONDS: int = 300
    
    # Marketing settings
    ENABLE_SOCIAL_MEDIA: bool = True
    ENABLE_EMAIL_MARKETING: bool = True
    ENABLE_SEO_OPTIMIZATION: bool = True
    
    # Analytics settings
    ENABLE_ANALYTICS: bool = True
    ANALYTICS_RETENTION_DAYS: int = 365
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

# Create global settings instance
settings = Settings()

# Validate required settings in production
def validate_production_settings():
    """
    Validate that all required settings are present in production.
    
    This function should be called during application startup in production.
    """
    if settings.ENVIRONMENT == "production":
        required_settings = [
            "SECRET_KEY",
            "DATABASE_URL",
            "REDIS_URL",
            "OPENAI_API_KEY",
            "ANTHROPIC_API_KEY",
        ]
        
        missing_settings = []
        for setting in required_settings:
            if not getattr(settings, setting):
                missing_settings.append(setting)
        
        if missing_settings:
            raise ValueError(
                f"Missing required settings in production: {', '.join(missing_settings)}"
            )

# Database URL validation
@validator("DATABASE_URL")
def validate_database_url(cls, v):
    """Validate database URL format."""
    if not v.startswith(("postgresql://", "postgresql+asyncpg://")):
        raise ValueError("DATABASE_URL must be a PostgreSQL URL")
    return v

# Redis URL validation
@validator("REDIS_URL")
def validate_redis_url(cls, v):
    """Validate Redis URL format."""
    if not v.startswith("redis://"):
        raise ValueError("REDIS_URL must be a Redis URL")
    return v

# Security key validation
@validator("SECRET_KEY")
def validate_secret_key(cls, v):
    """Validate secret key strength."""
    if len(v) < 32:
        raise ValueError("SECRET_KEY must be at least 32 characters long")
    return v
