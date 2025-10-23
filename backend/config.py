"""
Application configuration settings
"""

from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API Keys
    anthropic_api_key: str = ""
    perplexity_api_key: str = ""
    dataforseo_login: str = ""
    dataforseo_password: str = ""

    # Google OAuth
    google_client_id: str = ""
    google_client_secret: str = ""

    # JWT
    jwt_secret: str = "your-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440  # 24 hours

    # Database
    database_url: str = "sqlite:///./leadgear.db"

    # Redis
    redis_url: str = "redis://localhost:6379"

    # App URLs
    frontend_url: str = "http://localhost:3000"
    backend_url: str = "http://localhost:8000"

    # DataForSEO API Configuration
    dataforseo_api_url: str = "https://api.dataforseo.com"

    # Claude API Configuration
    claude_model: str = "claude-3-5-sonnet-20241022"
    claude_max_tokens: int = 4096
    claude_temperature: float = 1.0

    # Perplexity API Configuration
    perplexity_model: str = "sonar"

    # Content Generation Settings
    default_target_word_count: int = 2200
    min_word_count: int = 1000
    max_word_count: int = 5000

    # Quality Check Thresholds
    min_readability_score: float = 60.0
    max_readability_score: float = 70.0
    min_keyword_density: float = 0.5
    max_keyword_density: float = 1.5
    target_seo_score: float = 85.0

    # SERP Analysis Settings
    serp_num_results: int = 10
    serp_scrape_timeout: int = 30  # seconds

    # Celery Settings
    celery_broker_url: Optional[str] = None
    celery_result_backend: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = False


# Create global settings instance
settings = Settings()

# Set Celery URLs from Redis URL if not explicitly set
if not settings.celery_broker_url:
    settings.celery_broker_url = settings.redis_url
if not settings.celery_result_backend:
    settings.celery_result_backend = settings.redis_url
