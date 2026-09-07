from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    farms,
    soil_analysis,
    crops,
    recommendations,
    weather,
    fertilizer,
    market_prices,
    telemetry,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication & RBAC"])
api_router.include_router(farms.router, prefix="/farms", tags=["Farms & Field Parcels (GIS)"])
api_router.include_router(soil_analysis.router, prefix="/soil", tags=["Soil Analysis & Health Cards"])
api_router.include_router(crops.router, prefix="/crops", tags=["Crop Agronomic Knowledge Base"])
api_router.include_router(recommendations.router, prefix="/recommendations", tags=["Crop Recommendation & What-If Engine"])
api_router.include_router(weather.router, prefix="/weather", tags=["Agro-Meteorology & Evapotranspiration"])
api_router.include_router(fertilizer.router, prefix="/fertilizer", tags=["Fertilizer Advisory & SSNM"])
api_router.include_router(market_prices.router, prefix="/market", tags=["Market Mandi Prices & Economics"])
api_router.include_router(telemetry.router, prefix="/telemetry", tags=["IoT Sensor Telemetry"])
