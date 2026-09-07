import os
from typing import List, Optional, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Global Application Settings & Configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow",
    )

    # Project Information
    PROJECT_NAME: str = "AgroPulse"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Security & Tokens
    SECRET_KEY: str = "c7d2e89b4f6a1e3d5c7b9a0f2e4d6c8b1a3e5f7d9b0c2e4a6f8b0d2e4f6a8b0c"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 30 days

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "https://agropulse.app",
    ]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        return []

    # Database
    DATABASE_URL: str = "sqlite:///./agropulse.db"
    DATABASE_ECHO: bool = False
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10

    # Redis Cache & Background Tasks
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_ENABLED: bool = True
    CACHE_EXPIRE_WEATHER_HOURS: int = 3
    CACHE_EXPIRE_RECOMMENDATION_DAYS: int = 14

    # External Meteorology APIs
    WEATHER_API_KEY: Optional[str] = None
    WEATHER_API_PROVIDER: str = "mock"  # Options: openweather, visualcrossing, era5, mock
    WEATHER_API_BASE_URL: str = "https://api.openweathermap.org/data/2.5"

    # ML & Agronomy Model Engine
    MODEL_DIR: str = os.path.join(os.path.dirname(__file__), "..", "ml", "models_storage")
    DEFAULT_CROP_COUNT: int = 120
    ENSEMBLE_CONFIDENCE_THRESHOLD: float = 0.65
    ENABLE_PYTORCH_MODELS: bool = True
    ENABLE_LIGHTGBM_MODELS: bool = True

    # Agronomic Calculation Norms
    DEFAULT_SOIL_DEPTH_CM: float = 30.0
    DEFAULT_BULK_DENSITY_G_CM3: float = 1.35
    REFERENCE_LATITUDE_DEG: float = 20.5937  # Central Agro-climatic zone default
    SOLAR_CONSTANT_MJ_M2_MIN: float = 0.0820

    # Notification & IoT Settings
    IOT_TELEMETRY_INTERVAL_SECONDS: int = 30
    IOT_ALERT_SOIL_MOISTURE_LOW_PCT: float = 20.0
    IOT_ALERT_SOIL_MOISTURE_HIGH_PCT: float = 85.0
    IOT_ALERT_EC_MAX_DS_M: float = 4.0
    IOT_ALERT_TEMP_FROST_C: float = 3.0
    IOT_ALERT_TEMP_HEAT_STRESS_C: float = 40.0


settings = Settings()
