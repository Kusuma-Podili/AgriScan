from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel


class MandiMarketPrice(BaseModel):
    crop_id: str
    commodity_name: str
    mandi_name: str
    state: str
    modal_price_usd_per_ton: float
    min_price_usd_per_ton: float
    max_price_usd_per_ton: float
    price_trend_7day_pct: float  # +2.4%, -1.2%
    arrival_quantity_ton: float
    reported_date: date


class MarketCommoditySummary(BaseModel):
    commodity_name: str
    average_price_usd_ton: float
    high_52week_usd: float
    low_52week_usd: float
    volatility_score: float
    market_outlook: str  # Bullish, Bearish, Stable
