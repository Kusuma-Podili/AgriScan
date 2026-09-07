from datetime import date
from typing import List, Optional
from fastapi import APIRouter, Query, HTTPException
from app.schemas.market import MandiMarketPrice, MarketCommoditySummary
from app.ml.data.crop_database import CROP_DATABASE, get_crop_by_id

router = APIRouter()


@router.get("/mandi-prices", response_model=List[MandiMarketPrice])
def get_mandi_market_prices(
    category: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
):
    """
    Simulates real-time agricultural mandi commodity market prices, modal rates, and 7-day price momentum.
    """
    today = date.today()
    prices: List[MandiMarketPrice] = []

    mandi_samples = [
        ("rice", "Paddy (Common)", "Karnal Grain Market", "Haryana", 285.0, 260.0, 310.0, 2.4, 450.0),
        ("wheat", "Wheat (Sharbati)", "Khanna Mandi", "Punjab", 270.0, 250.0, 290.0, -0.8, 1200.0),
        ("maize", "Yellow Corn", "Gulabbagh Mandi", "Bihar", 235.0, 215.0, 255.0, 3.1, 800.0),
        ("chickpea", "Desi Chana", "Latur APMC", "Maharashtra", 710.0, 680.0, 750.0, 1.5, 340.0),
        ("soybean", "Soybean Yellow", "Indore Mandi", "Madhya Pradesh", 530.0, 500.0, 560.0, -1.9, 650.0),
        ("cotton", "Medium Staple Cotton", "Rajkot APMC", "Gujarat", 840.0, 800.0, 890.0, 4.2, 520.0),
        ("tomato", "Hybrid Tomato", "Kolar Market", "Karnataka", 195.0, 150.0, 240.0, 12.5, 280.0),
        ("potato", "Jyoti Potato", "Agra Mandi", "Uttar Pradesh", 185.0, 160.0, 210.0, -3.2, 950.0),
        ("onion", "Nasik Red Onion", "Lasalgaon Mandi", "Maharashtra", 255.0, 220.0, 300.0, 8.4, 1100.0),
        ("turmeric", "Salem Finger Turmeric", "Nizamabad APMC", "Telangana", 1250.0, 1180.0, 1340.0, 5.6, 180.0),
        ("black_pepper", "Garbled Black Pepper", "Kochi Terminal", "Kerala", 6300.0, 6100.0, 6600.0, 1.1, 45.0),
    ]

    for cid, name, mandi, st, modal, p_min, p_max, trend, arr in mandi_samples:
        if state and st.lower() != state.lower().strip():
            continue
        crop = get_crop_by_id(cid)
        if category and crop and crop.category.lower() != category.lower().strip():
            continue

        prices.append(
            MandiMarketPrice(
                crop_id=cid,
                commodity_name=name,
                mandi_name=mandi,
                state=st,
                modal_price_usd_per_ton=modal,
                min_price_usd_per_ton=p_min,
                max_price_usd_per_ton=p_max,
                price_trend_7day_pct=trend,
                arrival_quantity_ton=arr,
                reported_date=today,
            )
        )

    return prices


@router.get("/commodity-summary/{crop_id}", response_model=MarketCommoditySummary)
def get_commodity_market_summary(crop_id: str):
    """
    Returns annual 52-week price volatility, high/low range, and forward market outlook.
    """
    crop = get_crop_by_id(crop_id)
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")

    base_price = crop.market_price_usd_per_ton
    high_52 = round(base_price * 1.35, 1)
    low_52 = round(base_price * 0.78, 1)

    outlook = "Stable"
    if crop.risk_volatility_index > 0.35:
        outlook = "Bullish / High Volatility"
    elif crop.risk_volatility_index < 0.20:
        outlook = "Stable / Steady Demand"

    return MarketCommoditySummary(
        commodity_name=crop.name,
        average_price_usd_ton=base_price,
        high_52week_usd=high_52,
        low_52week_usd=low_52,
        volatility_score=crop.risk_volatility_index,
        market_outlook=outlook,
    )
