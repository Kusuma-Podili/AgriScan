"""
AgroPulse Pydantic Schemas for API Serialization and Input Validation.
"""

from app.schemas.user import UserCreate, UserUpdate, UserResponse, Token, TokenPayload
from app.schemas.farm import FarmCreate, FarmUpdate, FarmResponse, FieldParcelCreate, FieldParcelResponse
from app.schemas.soil import SoilSampleCreate, SoilSampleResponse, SoilHealthCardSummary
from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationDetailResponse,
    WhatIfScenarioRequest,
    WhatIfScenarioResponse,
)
from app.schemas.weather import WeatherCurrentResponse, DailyForecast, IrrigationAdvisoryResponse
from app.schemas.market import MandiMarketPrice, MarketCommoditySummary

__all__ = [
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    "Token",
    "TokenPayload",
    "FarmCreate",
    "FarmUpdate",
    "FarmResponse",
    "FieldParcelCreate",
    "FieldParcelResponse",
    "SoilSampleCreate",
    "SoilSampleResponse",
    "SoilHealthCardSummary",
    "RecommendationRequest",
    "RecommendationDetailResponse",
    "WhatIfScenarioRequest",
    "WhatIfScenarioResponse",
    "WeatherCurrentResponse",
    "DailyForecast",
    "IrrigationAdvisoryResponse",
    "MandiMarketPrice",
    "MarketCommoditySummary",
]
