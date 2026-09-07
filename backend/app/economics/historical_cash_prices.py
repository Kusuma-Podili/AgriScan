"""
AgriScan Terminal Market Physical Cash Price Time Series.
Provides 10-year monthly historical spot cash prices ($/MT) across 50 major regional markets.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class MonthlyCashMarketPrice(BaseModel):
    year: int
    month: int
    cash_price_usd_per_ton: float
    trading_volume_metric_tons: float


class RegionalMarketPriceSeries(BaseModel):
    market_id: str
    market_name: str
    commodity_name: str
    state_or_province: str
    currency: str
    historical_monthly_prices: List[MonthlyCashMarketPrice]


REGIONAL_CASH_PRICE_DATABASE: Dict[str, RegionalMarketPriceSeries] = {
    "MKT_US_IL_01": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_01",
        market_name="Illinois River Terminal Facility #1",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=230.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=231.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=217.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=201.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=197.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=209.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=226.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=232.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=222.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=205.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=197.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=205.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=242.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=243.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=229.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=213.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=209.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=221.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=238.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=244.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=234.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=217.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=209.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=217.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=254.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=255.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=241.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=225.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=221.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=233.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=250.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=256.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=246.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=229.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=221.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=229.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=266.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=267.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=253.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=237.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=233.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=245.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=262.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=268.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=258.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=241.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=233.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=241.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=278.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=279.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=265.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=249.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=245.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=257.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=274.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=280.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=270.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=253.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=245.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=253.34, trading_volume_metric_tons=22000.0,
            ),
        ],
    ),
    "MKT_US_IL_02": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_02",
        market_name="Illinois River Terminal Facility #2",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=235.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=236.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=222.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=206.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=202.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=214.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=231.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=237.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=227.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=210.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=202.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=210.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=247.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=248.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=234.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=218.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=214.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=226.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=243.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=249.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=239.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=222.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=214.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=222.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=259.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=260.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=246.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=230.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=226.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=238.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=255.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=261.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=251.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=234.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=226.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=234.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=271.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=272.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=258.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=242.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=238.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=250.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=267.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=273.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=263.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=246.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=238.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=246.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=283.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=284.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=270.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=254.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=250.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=262.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=279.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=285.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=275.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=258.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=250.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=258.34, trading_volume_metric_tons=23000.0,
            ),
        ],
    ),
    "MKT_US_IL_03": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_03",
        market_name="Illinois River Terminal Facility #3",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=240.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=241.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=227.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=211.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=207.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=219.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=236.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=242.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=232.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=215.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=207.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=215.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=252.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=253.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=239.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=223.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=219.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=231.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=248.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=254.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=244.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=227.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=219.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=227.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=264.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=265.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=251.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=235.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=231.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=243.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=260.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=266.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=256.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=239.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=231.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=239.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=276.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=277.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=263.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=247.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=243.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=255.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=272.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=278.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=268.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=251.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=243.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=251.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=288.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=289.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=275.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=259.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=255.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=267.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=284.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=290.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=280.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=263.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=255.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=263.34, trading_volume_metric_tons=24000.0,
            ),
        ],
    ),
    "MKT_US_IL_04": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_04",
        market_name="Illinois River Terminal Facility #4",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=245.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=246.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=232.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=216.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=212.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=224.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=241.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=247.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=237.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=220.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=212.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=220.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=257.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=258.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=244.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=228.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=224.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=236.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=253.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=259.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=249.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=232.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=224.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=232.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=269.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=270.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=256.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=240.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=236.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=248.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=265.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=271.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=261.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=244.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=236.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=244.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=281.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=282.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=268.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=252.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=248.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=260.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=277.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=283.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=273.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=256.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=248.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=256.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=293.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=294.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=280.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=264.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=260.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=272.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=289.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=295.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=285.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=268.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=260.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=268.34, trading_volume_metric_tons=25000.0,
            ),
        ],
    ),
    "MKT_US_IL_05": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_05",
        market_name="Illinois River Terminal Facility #5",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=250.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=251.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=237.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=221.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=217.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=229.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=246.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=252.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=242.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=225.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=217.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=225.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=262.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=263.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=249.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=233.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=229.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=241.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=258.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=264.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=254.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=237.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=229.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=237.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=274.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=275.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=261.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=245.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=241.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=253.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=270.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=276.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=266.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=249.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=241.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=249.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=286.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=287.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=273.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=257.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=253.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=265.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=282.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=288.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=278.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=261.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=253.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=261.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=298.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=299.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=285.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=269.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=265.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=277.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=294.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=300.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=290.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=273.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=265.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=273.34, trading_volume_metric_tons=26000.0,
            ),
        ],
    ),
    "MKT_US_IL_06": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_06",
        market_name="Illinois River Terminal Facility #6",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=255.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=256.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=242.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=226.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=222.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=234.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=251.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=257.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=247.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=230.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=222.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=230.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=267.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=268.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=254.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=238.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=234.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=246.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=263.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=269.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=259.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=242.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=234.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=242.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=279.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=280.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=266.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=250.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=246.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=258.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=275.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=281.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=271.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=254.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=246.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=254.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=291.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=292.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=278.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=262.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=258.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=270.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=287.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=293.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=283.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=266.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=258.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=266.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=303.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=304.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=290.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=274.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=270.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=282.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=299.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=305.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=295.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=278.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=270.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=278.34, trading_volume_metric_tons=27000.0,
            ),
        ],
    ),
    "MKT_US_IL_07": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_07",
        market_name="Illinois River Terminal Facility #7",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=260.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=261.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=247.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=231.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=227.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=239.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=256.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=262.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=252.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=235.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=227.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=235.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=272.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=273.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=259.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=243.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=239.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=251.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=268.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=274.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=264.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=247.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=239.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=247.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=284.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=285.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=271.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=255.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=251.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=263.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=280.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=286.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=276.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=259.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=251.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=259.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=296.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=297.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=283.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=267.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=263.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=275.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=292.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=298.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=288.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=271.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=263.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=271.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=308.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=309.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=295.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=279.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=275.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=287.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=304.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=310.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=300.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=283.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=275.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=283.34, trading_volume_metric_tons=28000.0,
            ),
        ],
    ),
    "MKT_US_IL_08": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_08",
        market_name="Illinois River Terminal Facility #8",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=265.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=266.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=252.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=236.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=232.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=244.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=261.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=267.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=257.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=240.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=232.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=240.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=277.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=278.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=264.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=248.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=244.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=256.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=273.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=279.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=269.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=252.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=244.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=252.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=289.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=290.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=276.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=260.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=256.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=268.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=285.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=291.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=281.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=264.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=256.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=264.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=301.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=302.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=288.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=272.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=268.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=280.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=297.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=303.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=293.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=276.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=268.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=276.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=313.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=314.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=300.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=284.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=280.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=292.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=309.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=315.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=305.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=288.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=280.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=288.34, trading_volume_metric_tons=29000.0,
            ),
        ],
    ),
    "MKT_US_IL_09": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_09",
        market_name="Illinois River Terminal Facility #9",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=270.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=271.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=257.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=241.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=237.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=249.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=266.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=272.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=262.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=245.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=237.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=245.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=282.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=283.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=269.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=253.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=249.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=261.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=278.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=284.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=274.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=257.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=249.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=257.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=294.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=295.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=281.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=265.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=261.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=273.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=290.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=296.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=286.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=269.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=261.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=269.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=306.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=307.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=293.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=277.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=273.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=285.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=302.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=308.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=298.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=281.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=273.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=281.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=318.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=319.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=305.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=289.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=285.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=297.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=314.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=320.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=310.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=293.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=285.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=293.34, trading_volume_metric_tons=30000.0,
            ),
        ],
    ),
    "MKT_US_IL_10": RegionalMarketPriceSeries(
        market_id="MKT_US_IL_10",
        market_name="Illinois River Terminal Facility #10",
        commodity_name="Corn",
        state_or_province="Illinois",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=275.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=276.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=262.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=246.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=242.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=254.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=271.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=277.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=267.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=250.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=242.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=250.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=287.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=288.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=274.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=258.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=254.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=266.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=283.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=289.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=279.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=262.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=254.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=262.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=299.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=300.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=286.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=270.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=266.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=278.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=295.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=301.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=291.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=274.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=266.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=274.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=311.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=312.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=298.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=282.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=278.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=290.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=307.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=313.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=303.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=286.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=278.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=286.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=323.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=324.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=310.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=294.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=290.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=302.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=319.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=325.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=315.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=298.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=290.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=298.34, trading_volume_metric_tons=31000.0,
            ),
        ],
    ),
    "MKT_US_KS_01": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_01",
        market_name="Dodge City Grain Hub Facility #1",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=230.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=231.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=217.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=201.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=197.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=209.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=226.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=232.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=222.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=205.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=197.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=205.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=242.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=243.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=229.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=213.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=209.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=221.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=238.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=244.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=234.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=217.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=209.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=217.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=254.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=255.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=241.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=225.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=221.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=233.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=250.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=256.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=246.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=229.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=221.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=229.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=266.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=267.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=253.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=237.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=233.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=245.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=262.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=268.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=258.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=241.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=233.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=241.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=278.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=279.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=265.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=249.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=245.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=257.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=274.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=280.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=270.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=253.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=245.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=253.34, trading_volume_metric_tons=22000.0,
            ),
        ],
    ),
    "MKT_US_KS_02": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_02",
        market_name="Dodge City Grain Hub Facility #2",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=235.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=236.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=222.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=206.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=202.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=214.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=231.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=237.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=227.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=210.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=202.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=210.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=247.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=248.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=234.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=218.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=214.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=226.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=243.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=249.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=239.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=222.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=214.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=222.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=259.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=260.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=246.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=230.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=226.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=238.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=255.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=261.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=251.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=234.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=226.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=234.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=271.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=272.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=258.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=242.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=238.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=250.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=267.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=273.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=263.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=246.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=238.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=246.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=283.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=284.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=270.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=254.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=250.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=262.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=279.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=285.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=275.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=258.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=250.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=258.34, trading_volume_metric_tons=23000.0,
            ),
        ],
    ),
    "MKT_US_KS_03": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_03",
        market_name="Dodge City Grain Hub Facility #3",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=240.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=241.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=227.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=211.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=207.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=219.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=236.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=242.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=232.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=215.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=207.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=215.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=252.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=253.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=239.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=223.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=219.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=231.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=248.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=254.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=244.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=227.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=219.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=227.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=264.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=265.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=251.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=235.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=231.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=243.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=260.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=266.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=256.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=239.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=231.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=239.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=276.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=277.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=263.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=247.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=243.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=255.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=272.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=278.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=268.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=251.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=243.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=251.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=288.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=289.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=275.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=259.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=255.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=267.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=284.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=290.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=280.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=263.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=255.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=263.34, trading_volume_metric_tons=24000.0,
            ),
        ],
    ),
    "MKT_US_KS_04": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_04",
        market_name="Dodge City Grain Hub Facility #4",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=245.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=246.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=232.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=216.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=212.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=224.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=241.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=247.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=237.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=220.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=212.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=220.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=257.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=258.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=244.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=228.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=224.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=236.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=253.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=259.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=249.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=232.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=224.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=232.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=269.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=270.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=256.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=240.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=236.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=248.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=265.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=271.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=261.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=244.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=236.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=244.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=281.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=282.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=268.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=252.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=248.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=260.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=277.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=283.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=273.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=256.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=248.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=256.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=293.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=294.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=280.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=264.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=260.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=272.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=289.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=295.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=285.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=268.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=260.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=268.34, trading_volume_metric_tons=25000.0,
            ),
        ],
    ),
    "MKT_US_KS_05": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_05",
        market_name="Dodge City Grain Hub Facility #5",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=250.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=251.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=237.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=221.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=217.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=229.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=246.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=252.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=242.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=225.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=217.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=225.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=262.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=263.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=249.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=233.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=229.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=241.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=258.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=264.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=254.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=237.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=229.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=237.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=274.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=275.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=261.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=245.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=241.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=253.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=270.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=276.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=266.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=249.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=241.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=249.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=286.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=287.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=273.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=257.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=253.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=265.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=282.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=288.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=278.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=261.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=253.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=261.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=298.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=299.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=285.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=269.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=265.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=277.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=294.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=300.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=290.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=273.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=265.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=273.34, trading_volume_metric_tons=26000.0,
            ),
        ],
    ),
    "MKT_US_KS_06": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_06",
        market_name="Dodge City Grain Hub Facility #6",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=255.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=256.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=242.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=226.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=222.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=234.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=251.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=257.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=247.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=230.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=222.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=230.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=267.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=268.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=254.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=238.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=234.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=246.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=263.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=269.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=259.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=242.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=234.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=242.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=279.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=280.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=266.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=250.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=246.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=258.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=275.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=281.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=271.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=254.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=246.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=254.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=291.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=292.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=278.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=262.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=258.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=270.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=287.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=293.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=283.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=266.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=258.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=266.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=303.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=304.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=290.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=274.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=270.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=282.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=299.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=305.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=295.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=278.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=270.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=278.34, trading_volume_metric_tons=27000.0,
            ),
        ],
    ),
    "MKT_US_KS_07": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_07",
        market_name="Dodge City Grain Hub Facility #7",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=260.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=261.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=247.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=231.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=227.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=239.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=256.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=262.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=252.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=235.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=227.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=235.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=272.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=273.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=259.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=243.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=239.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=251.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=268.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=274.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=264.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=247.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=239.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=247.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=284.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=285.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=271.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=255.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=251.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=263.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=280.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=286.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=276.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=259.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=251.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=259.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=296.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=297.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=283.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=267.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=263.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=275.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=292.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=298.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=288.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=271.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=263.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=271.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=308.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=309.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=295.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=279.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=275.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=287.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=304.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=310.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=300.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=283.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=275.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=283.34, trading_volume_metric_tons=28000.0,
            ),
        ],
    ),
    "MKT_US_KS_08": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_08",
        market_name="Dodge City Grain Hub Facility #8",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=265.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=266.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=252.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=236.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=232.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=244.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=261.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=267.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=257.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=240.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=232.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=240.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=277.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=278.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=264.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=248.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=244.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=256.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=273.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=279.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=269.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=252.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=244.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=252.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=289.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=290.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=276.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=260.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=256.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=268.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=285.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=291.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=281.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=264.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=256.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=264.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=301.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=302.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=288.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=272.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=268.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=280.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=297.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=303.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=293.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=276.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=268.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=276.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=313.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=314.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=300.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=284.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=280.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=292.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=309.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=315.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=305.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=288.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=280.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=288.34, trading_volume_metric_tons=29000.0,
            ),
        ],
    ),
    "MKT_US_KS_09": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_09",
        market_name="Dodge City Grain Hub Facility #9",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=270.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=271.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=257.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=241.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=237.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=249.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=266.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=272.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=262.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=245.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=237.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=245.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=282.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=283.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=269.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=253.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=249.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=261.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=278.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=284.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=274.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=257.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=249.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=257.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=294.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=295.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=281.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=265.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=261.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=273.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=290.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=296.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=286.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=269.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=261.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=269.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=306.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=307.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=293.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=277.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=273.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=285.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=302.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=308.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=298.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=281.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=273.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=281.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=318.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=319.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=305.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=289.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=285.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=297.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=314.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=320.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=310.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=293.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=285.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=293.34, trading_volume_metric_tons=30000.0,
            ),
        ],
    ),
    "MKT_US_KS_10": RegionalMarketPriceSeries(
        market_id="MKT_US_KS_10",
        market_name="Dodge City Grain Hub Facility #10",
        commodity_name="Hard Red Winter Wheat",
        state_or_province="Kansas",
        currency="USD",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=275.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=276.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=262.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=246.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=242.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=254.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=271.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=277.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=267.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=250.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=242.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=250.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=287.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=288.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=274.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=258.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=254.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=266.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=283.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=289.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=279.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=262.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=254.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=262.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=299.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=300.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=286.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=270.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=266.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=278.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=295.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=301.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=291.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=274.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=266.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=274.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=311.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=312.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=298.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=282.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=278.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=290.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=307.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=313.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=303.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=286.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=278.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=286.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=323.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=324.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=310.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=294.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=290.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=302.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=319.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=325.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=315.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=298.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=290.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=298.34, trading_volume_metric_tons=31000.0,
            ),
        ],
    ),
    "MKT_IN_PB_01": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_01",
        market_name="Khanna Grain Market Facility #1",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=230.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=231.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=217.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=201.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=197.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=209.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=226.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=232.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=222.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=205.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=197.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=205.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=242.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=243.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=229.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=213.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=209.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=221.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=238.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=244.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=234.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=217.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=209.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=217.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=254.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=255.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=241.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=225.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=221.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=233.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=250.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=256.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=246.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=229.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=221.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=229.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=266.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=267.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=253.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=237.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=233.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=245.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=262.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=268.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=258.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=241.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=233.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=241.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=278.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=279.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=265.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=249.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=245.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=257.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=274.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=280.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=270.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=253.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=245.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=253.34, trading_volume_metric_tons=22000.0,
            ),
        ],
    ),
    "MKT_IN_PB_02": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_02",
        market_name="Khanna Grain Market Facility #2",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=235.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=236.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=222.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=206.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=202.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=214.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=231.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=237.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=227.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=210.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=202.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=210.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=247.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=248.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=234.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=218.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=214.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=226.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=243.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=249.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=239.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=222.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=214.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=222.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=259.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=260.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=246.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=230.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=226.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=238.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=255.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=261.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=251.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=234.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=226.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=234.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=271.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=272.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=258.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=242.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=238.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=250.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=267.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=273.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=263.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=246.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=238.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=246.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=283.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=284.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=270.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=254.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=250.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=262.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=279.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=285.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=275.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=258.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=250.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=258.34, trading_volume_metric_tons=23000.0,
            ),
        ],
    ),
    "MKT_IN_PB_03": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_03",
        market_name="Khanna Grain Market Facility #3",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=240.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=241.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=227.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=211.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=207.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=219.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=236.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=242.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=232.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=215.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=207.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=215.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=252.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=253.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=239.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=223.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=219.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=231.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=248.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=254.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=244.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=227.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=219.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=227.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=264.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=265.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=251.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=235.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=231.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=243.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=260.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=266.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=256.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=239.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=231.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=239.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=276.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=277.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=263.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=247.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=243.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=255.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=272.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=278.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=268.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=251.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=243.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=251.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=288.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=289.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=275.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=259.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=255.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=267.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=284.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=290.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=280.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=263.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=255.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=263.34, trading_volume_metric_tons=24000.0,
            ),
        ],
    ),
    "MKT_IN_PB_04": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_04",
        market_name="Khanna Grain Market Facility #4",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=245.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=246.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=232.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=216.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=212.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=224.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=241.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=247.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=237.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=220.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=212.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=220.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=257.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=258.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=244.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=228.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=224.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=236.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=253.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=259.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=249.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=232.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=224.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=232.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=269.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=270.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=256.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=240.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=236.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=248.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=265.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=271.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=261.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=244.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=236.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=244.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=281.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=282.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=268.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=252.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=248.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=260.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=277.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=283.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=273.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=256.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=248.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=256.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=293.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=294.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=280.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=264.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=260.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=272.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=289.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=295.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=285.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=268.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=260.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=268.34, trading_volume_metric_tons=25000.0,
            ),
        ],
    ),
    "MKT_IN_PB_05": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_05",
        market_name="Khanna Grain Market Facility #5",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=250.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=251.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=237.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=221.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=217.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=229.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=246.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=252.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=242.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=225.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=217.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=225.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=262.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=263.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=249.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=233.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=229.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=241.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=258.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=264.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=254.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=237.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=229.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=237.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=274.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=275.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=261.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=245.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=241.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=253.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=270.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=276.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=266.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=249.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=241.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=249.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=286.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=287.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=273.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=257.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=253.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=265.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=282.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=288.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=278.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=261.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=253.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=261.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=298.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=299.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=285.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=269.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=265.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=277.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=294.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=300.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=290.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=273.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=265.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=273.34, trading_volume_metric_tons=26000.0,
            ),
        ],
    ),
    "MKT_IN_PB_06": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_06",
        market_name="Khanna Grain Market Facility #6",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=255.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=256.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=242.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=226.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=222.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=234.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=251.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=257.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=247.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=230.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=222.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=230.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=267.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=268.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=254.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=238.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=234.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=246.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=263.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=269.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=259.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=242.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=234.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=242.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=279.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=280.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=266.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=250.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=246.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=258.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=275.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=281.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=271.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=254.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=246.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=254.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=291.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=292.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=278.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=262.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=258.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=270.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=287.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=293.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=283.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=266.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=258.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=266.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=303.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=304.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=290.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=274.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=270.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=282.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=299.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=305.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=295.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=278.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=270.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=278.34, trading_volume_metric_tons=27000.0,
            ),
        ],
    ),
    "MKT_IN_PB_07": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_07",
        market_name="Khanna Grain Market Facility #7",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=260.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=261.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=247.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=231.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=227.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=239.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=256.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=262.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=252.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=235.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=227.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=235.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=272.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=273.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=259.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=243.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=239.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=251.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=268.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=274.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=264.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=247.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=239.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=247.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=284.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=285.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=271.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=255.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=251.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=263.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=280.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=286.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=276.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=259.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=251.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=259.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=296.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=297.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=283.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=267.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=263.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=275.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=292.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=298.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=288.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=271.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=263.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=271.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=308.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=309.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=295.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=279.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=275.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=287.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=304.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=310.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=300.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=283.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=275.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=283.34, trading_volume_metric_tons=28000.0,
            ),
        ],
    ),
    "MKT_IN_PB_08": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_08",
        market_name="Khanna Grain Market Facility #8",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=265.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=266.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=252.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=236.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=232.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=244.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=261.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=267.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=257.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=240.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=232.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=240.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=277.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=278.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=264.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=248.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=244.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=256.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=273.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=279.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=269.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=252.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=244.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=252.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=289.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=290.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=276.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=260.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=256.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=268.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=285.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=291.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=281.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=264.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=256.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=264.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=301.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=302.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=288.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=272.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=268.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=280.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=297.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=303.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=293.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=276.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=268.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=276.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=313.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=314.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=300.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=284.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=280.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=292.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=309.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=315.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=305.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=288.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=280.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=288.34, trading_volume_metric_tons=29000.0,
            ),
        ],
    ),
    "MKT_IN_PB_09": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_09",
        market_name="Khanna Grain Market Facility #9",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=270.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=271.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=257.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=241.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=237.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=249.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=266.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=272.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=262.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=245.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=237.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=245.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=282.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=283.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=269.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=253.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=249.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=261.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=278.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=284.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=274.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=257.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=249.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=257.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=294.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=295.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=281.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=265.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=261.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=273.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=290.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=296.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=286.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=269.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=261.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=269.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=306.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=307.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=293.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=277.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=273.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=285.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=302.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=308.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=298.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=281.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=273.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=281.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=318.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=319.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=305.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=289.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=285.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=297.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=314.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=320.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=310.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=293.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=285.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=293.34, trading_volume_metric_tons=30000.0,
            ),
        ],
    ),
    "MKT_IN_PB_10": RegionalMarketPriceSeries(
        market_id="MKT_IN_PB_10",
        market_name="Khanna Grain Market Facility #10",
        commodity_name="Paddy Rice",
        state_or_province="Punjab",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=275.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=276.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=262.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=246.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=242.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=254.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=271.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=277.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=267.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=250.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=242.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=250.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=287.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=288.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=274.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=258.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=254.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=266.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=283.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=289.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=279.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=262.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=254.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=262.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=299.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=300.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=286.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=270.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=266.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=278.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=295.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=301.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=291.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=274.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=266.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=274.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=311.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=312.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=298.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=282.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=278.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=290.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=307.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=313.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=303.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=286.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=278.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=286.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=323.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=324.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=310.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=294.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=290.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=302.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=319.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=325.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=315.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=298.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=290.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=298.34, trading_volume_metric_tons=31000.0,
            ),
        ],
    ),
    "MKT_IN_MP_01": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_01",
        market_name="Indore Mandi Terminal Facility #1",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=230.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=231.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=217.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=201.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=197.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=209.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=226.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=232.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=222.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=205.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=197.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=205.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=242.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=243.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=229.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=213.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=209.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=221.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=238.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=244.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=234.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=217.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=209.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=217.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=254.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=255.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=241.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=225.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=221.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=233.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=250.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=256.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=246.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=229.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=221.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=229.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=266.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=267.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=253.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=237.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=233.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=245.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=262.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=268.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=258.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=241.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=233.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=241.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=278.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=279.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=265.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=249.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=245.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=257.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=274.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=280.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=270.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=253.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=245.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=253.34, trading_volume_metric_tons=22000.0,
            ),
        ],
    ),
    "MKT_IN_MP_02": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_02",
        market_name="Indore Mandi Terminal Facility #2",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=235.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=236.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=222.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=206.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=202.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=214.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=231.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=237.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=227.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=210.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=202.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=210.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=247.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=248.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=234.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=218.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=214.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=226.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=243.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=249.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=239.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=222.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=214.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=222.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=259.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=260.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=246.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=230.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=226.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=238.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=255.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=261.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=251.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=234.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=226.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=234.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=271.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=272.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=258.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=242.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=238.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=250.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=267.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=273.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=263.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=246.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=238.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=246.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=283.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=284.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=270.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=254.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=250.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=262.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=279.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=285.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=275.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=258.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=250.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=258.34, trading_volume_metric_tons=23000.0,
            ),
        ],
    ),
    "MKT_IN_MP_03": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_03",
        market_name="Indore Mandi Terminal Facility #3",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=240.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=241.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=227.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=211.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=207.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=219.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=236.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=242.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=232.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=215.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=207.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=215.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=252.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=253.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=239.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=223.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=219.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=231.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=248.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=254.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=244.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=227.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=219.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=227.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=264.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=265.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=251.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=235.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=231.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=243.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=260.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=266.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=256.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=239.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=231.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=239.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=276.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=277.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=263.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=247.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=243.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=255.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=272.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=278.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=268.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=251.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=243.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=251.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=288.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=289.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=275.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=259.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=255.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=267.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=284.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=290.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=280.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=263.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=255.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=263.34, trading_volume_metric_tons=24000.0,
            ),
        ],
    ),
    "MKT_IN_MP_04": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_04",
        market_name="Indore Mandi Terminal Facility #4",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=245.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=246.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=232.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=216.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=212.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=224.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=241.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=247.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=237.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=220.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=212.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=220.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=257.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=258.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=244.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=228.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=224.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=236.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=253.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=259.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=249.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=232.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=224.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=232.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=269.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=270.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=256.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=240.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=236.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=248.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=265.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=271.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=261.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=244.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=236.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=244.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=281.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=282.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=268.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=252.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=248.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=260.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=277.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=283.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=273.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=256.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=248.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=256.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=293.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=294.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=280.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=264.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=260.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=272.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=289.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=295.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=285.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=268.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=260.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=268.34, trading_volume_metric_tons=25000.0,
            ),
        ],
    ),
    "MKT_IN_MP_05": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_05",
        market_name="Indore Mandi Terminal Facility #5",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=250.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=251.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=237.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=221.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=217.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=229.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=246.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=252.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=242.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=225.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=217.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=225.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=262.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=263.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=249.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=233.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=229.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=241.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=258.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=264.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=254.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=237.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=229.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=237.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=274.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=275.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=261.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=245.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=241.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=253.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=270.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=276.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=266.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=249.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=241.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=249.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=286.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=287.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=273.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=257.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=253.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=265.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=282.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=288.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=278.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=261.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=253.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=261.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=298.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=299.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=285.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=269.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=265.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=277.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=294.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=300.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=290.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=273.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=265.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=273.34, trading_volume_metric_tons=26000.0,
            ),
        ],
    ),
    "MKT_IN_MP_06": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_06",
        market_name="Indore Mandi Terminal Facility #6",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=255.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=256.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=242.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=226.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=222.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=234.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=251.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=257.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=247.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=230.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=222.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=230.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=267.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=268.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=254.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=238.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=234.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=246.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=263.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=269.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=259.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=242.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=234.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=242.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=279.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=280.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=266.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=250.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=246.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=258.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=275.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=281.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=271.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=254.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=246.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=254.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=291.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=292.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=278.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=262.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=258.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=270.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=287.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=293.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=283.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=266.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=258.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=266.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=303.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=304.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=290.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=274.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=270.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=282.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=299.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=305.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=295.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=278.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=270.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=278.34, trading_volume_metric_tons=27000.0,
            ),
        ],
    ),
    "MKT_IN_MP_07": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_07",
        market_name="Indore Mandi Terminal Facility #7",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=260.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=261.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=247.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=231.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=227.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=239.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=256.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=262.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=252.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=235.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=227.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=235.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=272.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=273.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=259.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=243.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=239.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=251.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=268.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=274.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=264.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=247.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=239.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=247.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=284.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=285.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=271.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=255.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=251.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=263.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=280.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=286.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=276.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=259.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=251.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=259.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=296.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=297.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=283.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=267.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=263.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=275.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=292.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=298.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=288.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=271.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=263.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=271.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=308.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=309.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=295.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=279.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=275.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=287.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=304.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=310.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=300.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=283.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=275.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=283.34, trading_volume_metric_tons=28000.0,
            ),
        ],
    ),
    "MKT_IN_MP_08": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_08",
        market_name="Indore Mandi Terminal Facility #8",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=265.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=266.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=252.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=236.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=232.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=244.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=261.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=267.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=257.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=240.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=232.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=240.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=277.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=278.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=264.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=248.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=244.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=256.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=273.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=279.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=269.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=252.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=244.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=252.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=289.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=290.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=276.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=260.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=256.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=268.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=285.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=291.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=281.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=264.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=256.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=264.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=301.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=302.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=288.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=272.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=268.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=280.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=297.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=303.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=293.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=276.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=268.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=276.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=313.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=314.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=300.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=284.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=280.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=292.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=309.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=315.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=305.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=288.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=280.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=288.34, trading_volume_metric_tons=29000.0,
            ),
        ],
    ),
    "MKT_IN_MP_09": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_09",
        market_name="Indore Mandi Terminal Facility #9",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=270.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=271.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=257.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=241.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=237.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=249.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=266.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=272.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=262.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=245.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=237.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=245.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=282.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=283.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=269.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=253.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=249.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=261.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=278.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=284.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=274.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=257.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=249.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=257.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=294.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=295.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=281.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=265.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=261.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=273.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=290.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=296.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=286.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=269.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=261.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=269.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=306.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=307.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=293.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=277.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=273.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=285.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=302.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=308.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=298.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=281.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=273.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=281.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=318.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=319.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=305.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=289.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=285.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=297.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=314.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=320.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=310.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=293.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=285.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=293.34, trading_volume_metric_tons=30000.0,
            ),
        ],
    ),
    "MKT_IN_MP_10": RegionalMarketPriceSeries(
        market_id="MKT_IN_MP_10",
        market_name="Indore Mandi Terminal Facility #10",
        commodity_name="Soybean",
        state_or_province="Madhya Pradesh",
        currency="INR",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=275.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=276.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=262.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=246.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=242.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=254.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=271.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=277.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=267.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=250.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=242.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=250.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=287.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=288.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=274.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=258.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=254.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=266.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=283.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=289.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=279.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=262.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=254.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=262.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=299.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=300.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=286.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=270.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=266.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=278.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=295.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=301.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=291.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=274.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=266.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=274.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=311.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=312.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=298.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=282.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=278.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=290.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=307.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=313.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=303.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=286.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=278.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=286.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=323.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=324.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=310.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=294.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=290.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=302.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=319.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=325.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=315.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=298.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=290.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=298.34, trading_volume_metric_tons=31000.0,
            ),
        ],
    ),
    "MKT_BR_PR_01": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_01",
        market_name="Paranagua Port Terminal Facility #1",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=230.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=231.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=217.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=201.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=197.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=209.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=226.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=232.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=222.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=205.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=197.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=205.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=242.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=243.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=229.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=213.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=209.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=221.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=238.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=244.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=234.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=217.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=209.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=217.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=254.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=255.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=241.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=225.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=221.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=233.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=250.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=256.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=246.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=229.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=221.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=229.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=266.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=267.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=253.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=237.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=233.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=245.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=262.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=268.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=258.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=241.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=233.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=241.34, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=278.15, trading_volume_metric_tons=16500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=279.37, trading_volume_metric_tons=17000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=265.54, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=249.38, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=245.74, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=257.97, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=274.83, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=280.81, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=270.42, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=253.21, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=245.0, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=253.34, trading_volume_metric_tons=22000.0,
            ),
        ],
    ),
    "MKT_BR_PR_02": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_02",
        market_name="Paranagua Port Terminal Facility #2",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=235.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=236.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=222.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=206.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=202.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=214.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=231.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=237.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=227.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=210.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=202.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=210.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=247.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=248.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=234.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=218.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=214.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=226.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=243.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=249.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=239.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=222.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=214.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=222.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=259.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=260.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=246.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=230.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=226.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=238.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=255.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=261.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=251.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=234.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=226.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=234.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=271.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=272.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=258.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=242.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=238.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=250.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=267.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=273.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=263.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=246.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=238.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=246.34, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=283.15, trading_volume_metric_tons=17500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=284.37, trading_volume_metric_tons=18000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=270.54, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=254.38, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=250.74, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=262.97, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=279.83, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=285.81, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=275.42, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=258.21, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=250.0, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=258.34, trading_volume_metric_tons=23000.0,
            ),
        ],
    ),
    "MKT_BR_PR_03": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_03",
        market_name="Paranagua Port Terminal Facility #3",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=240.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=241.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=227.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=211.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=207.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=219.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=236.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=242.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=232.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=215.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=207.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=215.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=252.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=253.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=239.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=223.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=219.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=231.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=248.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=254.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=244.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=227.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=219.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=227.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=264.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=265.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=251.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=235.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=231.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=243.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=260.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=266.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=256.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=239.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=231.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=239.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=276.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=277.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=263.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=247.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=243.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=255.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=272.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=278.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=268.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=251.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=243.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=251.34, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=288.15, trading_volume_metric_tons=18500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=289.37, trading_volume_metric_tons=19000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=275.54, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=259.38, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=255.74, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=267.97, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=284.83, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=290.81, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=280.42, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=263.21, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=255.0, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=263.34, trading_volume_metric_tons=24000.0,
            ),
        ],
    ),
    "MKT_BR_PR_04": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_04",
        market_name="Paranagua Port Terminal Facility #4",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=245.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=246.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=232.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=216.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=212.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=224.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=241.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=247.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=237.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=220.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=212.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=220.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=257.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=258.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=244.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=228.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=224.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=236.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=253.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=259.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=249.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=232.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=224.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=232.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=269.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=270.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=256.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=240.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=236.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=248.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=265.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=271.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=261.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=244.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=236.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=244.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=281.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=282.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=268.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=252.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=248.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=260.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=277.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=283.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=273.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=256.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=248.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=256.34, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=293.15, trading_volume_metric_tons=19500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=294.37, trading_volume_metric_tons=20000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=280.54, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=264.38, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=260.74, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=272.97, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=289.83, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=295.81, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=285.42, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=268.21, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=260.0, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=268.34, trading_volume_metric_tons=25000.0,
            ),
        ],
    ),
    "MKT_BR_PR_05": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_05",
        market_name="Paranagua Port Terminal Facility #5",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=250.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=251.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=237.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=221.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=217.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=229.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=246.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=252.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=242.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=225.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=217.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=225.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=262.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=263.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=249.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=233.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=229.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=241.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=258.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=264.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=254.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=237.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=229.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=237.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=274.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=275.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=261.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=245.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=241.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=253.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=270.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=276.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=266.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=249.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=241.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=249.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=286.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=287.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=273.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=257.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=253.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=265.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=282.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=288.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=278.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=261.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=253.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=261.34, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=298.15, trading_volume_metric_tons=20500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=299.37, trading_volume_metric_tons=21000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=285.54, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=269.38, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=265.74, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=277.97, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=294.83, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=300.81, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=290.42, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=273.21, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=265.0, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=273.34, trading_volume_metric_tons=26000.0,
            ),
        ],
    ),
    "MKT_BR_PR_06": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_06",
        market_name="Paranagua Port Terminal Facility #6",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=255.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=256.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=242.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=226.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=222.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=234.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=251.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=257.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=247.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=230.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=222.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=230.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=267.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=268.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=254.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=238.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=234.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=246.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=263.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=269.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=259.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=242.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=234.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=242.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=279.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=280.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=266.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=250.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=246.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=258.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=275.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=281.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=271.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=254.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=246.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=254.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=291.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=292.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=278.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=262.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=258.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=270.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=287.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=293.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=283.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=266.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=258.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=266.34, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=303.15, trading_volume_metric_tons=21500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=304.37, trading_volume_metric_tons=22000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=290.54, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=274.38, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=270.74, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=282.97, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=299.83, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=305.81, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=295.42, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=278.21, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=270.0, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=278.34, trading_volume_metric_tons=27000.0,
            ),
        ],
    ),
    "MKT_BR_PR_07": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_07",
        market_name="Paranagua Port Terminal Facility #7",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=260.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=261.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=247.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=231.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=227.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=239.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=256.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=262.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=252.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=235.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=227.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=235.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=272.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=273.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=259.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=243.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=239.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=251.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=268.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=274.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=264.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=247.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=239.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=247.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=284.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=285.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=271.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=255.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=251.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=263.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=280.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=286.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=276.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=259.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=251.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=259.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=296.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=297.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=283.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=267.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=263.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=275.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=292.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=298.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=288.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=271.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=263.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=271.34, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=308.15, trading_volume_metric_tons=22500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=309.37, trading_volume_metric_tons=23000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=295.54, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=279.38, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=275.74, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=287.97, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=304.83, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=310.81, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=300.42, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=283.21, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=275.0, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=283.34, trading_volume_metric_tons=28000.0,
            ),
        ],
    ),
    "MKT_BR_PR_08": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_08",
        market_name="Paranagua Port Terminal Facility #8",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=265.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=266.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=252.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=236.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=232.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=244.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=261.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=267.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=257.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=240.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=232.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=240.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=277.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=278.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=264.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=248.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=244.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=256.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=273.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=279.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=269.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=252.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=244.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=252.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=289.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=290.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=276.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=260.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=256.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=268.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=285.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=291.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=281.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=264.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=256.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=264.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=301.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=302.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=288.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=272.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=268.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=280.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=297.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=303.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=293.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=276.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=268.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=276.34, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=313.15, trading_volume_metric_tons=23500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=314.37, trading_volume_metric_tons=24000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=300.54, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=284.38, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=280.74, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=292.97, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=309.83, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=315.81, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=305.42, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=288.21, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=280.0, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=288.34, trading_volume_metric_tons=29000.0,
            ),
        ],
    ),
    "MKT_BR_PR_09": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_09",
        market_name="Paranagua Port Terminal Facility #9",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=270.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=271.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=257.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=241.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=237.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=249.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=266.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=272.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=262.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=245.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=237.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=245.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=282.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=283.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=269.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=253.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=249.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=261.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=278.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=284.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=274.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=257.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=249.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=257.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=294.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=295.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=281.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=265.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=261.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=273.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=290.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=296.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=286.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=269.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=261.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=269.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=306.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=307.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=293.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=277.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=273.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=285.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=302.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=308.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=298.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=281.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=273.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=281.34, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=318.15, trading_volume_metric_tons=24500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=319.37, trading_volume_metric_tons=25000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=305.54, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=289.38, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=285.74, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=297.97, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=314.83, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=320.81, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=310.42, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=293.21, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=285.0, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=293.34, trading_volume_metric_tons=30000.0,
            ),
        ],
    ),
    "MKT_BR_PR_10": RegionalMarketPriceSeries(
        market_id="MKT_BR_PR_10",
        market_name="Paranagua Port Terminal Facility #10",
        commodity_name="Soybean Export",
        state_or_province="Parana",
        currency="BRL",
        historical_monthly_prices=[
            MonthlyCashMarketPrice(
                year=2020, month=1, cash_price_usd_per_ton=275.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=2, cash_price_usd_per_ton=276.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=3, cash_price_usd_per_ton=262.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=4, cash_price_usd_per_ton=246.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=5, cash_price_usd_per_ton=242.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=6, cash_price_usd_per_ton=254.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=7, cash_price_usd_per_ton=271.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=8, cash_price_usd_per_ton=277.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=9, cash_price_usd_per_ton=267.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=10, cash_price_usd_per_ton=250.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=11, cash_price_usd_per_ton=242.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2020, month=12, cash_price_usd_per_ton=250.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=1, cash_price_usd_per_ton=287.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=2, cash_price_usd_per_ton=288.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=3, cash_price_usd_per_ton=274.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=4, cash_price_usd_per_ton=258.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=5, cash_price_usd_per_ton=254.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=6, cash_price_usd_per_ton=266.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=7, cash_price_usd_per_ton=283.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=8, cash_price_usd_per_ton=289.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=9, cash_price_usd_per_ton=279.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=10, cash_price_usd_per_ton=262.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=11, cash_price_usd_per_ton=254.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2021, month=12, cash_price_usd_per_ton=262.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=1, cash_price_usd_per_ton=299.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=2, cash_price_usd_per_ton=300.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=3, cash_price_usd_per_ton=286.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=4, cash_price_usd_per_ton=270.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=5, cash_price_usd_per_ton=266.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=6, cash_price_usd_per_ton=278.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=7, cash_price_usd_per_ton=295.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=8, cash_price_usd_per_ton=301.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=9, cash_price_usd_per_ton=291.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=10, cash_price_usd_per_ton=274.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=11, cash_price_usd_per_ton=266.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2022, month=12, cash_price_usd_per_ton=274.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=1, cash_price_usd_per_ton=311.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=2, cash_price_usd_per_ton=312.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=3, cash_price_usd_per_ton=298.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=4, cash_price_usd_per_ton=282.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=5, cash_price_usd_per_ton=278.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=6, cash_price_usd_per_ton=290.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=7, cash_price_usd_per_ton=307.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=8, cash_price_usd_per_ton=313.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=9, cash_price_usd_per_ton=303.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=10, cash_price_usd_per_ton=286.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=11, cash_price_usd_per_ton=278.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2023, month=12, cash_price_usd_per_ton=286.34, trading_volume_metric_tons=31000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=1, cash_price_usd_per_ton=323.15, trading_volume_metric_tons=25500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=2, cash_price_usd_per_ton=324.37, trading_volume_metric_tons=26000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=3, cash_price_usd_per_ton=310.54, trading_volume_metric_tons=26500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=4, cash_price_usd_per_ton=294.38, trading_volume_metric_tons=27000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=5, cash_price_usd_per_ton=290.74, trading_volume_metric_tons=27500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=6, cash_price_usd_per_ton=302.97, trading_volume_metric_tons=28000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=7, cash_price_usd_per_ton=319.83, trading_volume_metric_tons=28500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=8, cash_price_usd_per_ton=325.81, trading_volume_metric_tons=29000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=9, cash_price_usd_per_ton=315.42, trading_volume_metric_tons=29500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=10, cash_price_usd_per_ton=298.21, trading_volume_metric_tons=30000.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=11, cash_price_usd_per_ton=290.0, trading_volume_metric_tons=30500.0,
            ),
            MonthlyCashMarketPrice(
                year=2024, month=12, cash_price_usd_per_ton=298.34, trading_volume_metric_tons=31000.0,
            ),
        ],
    ),
}

def get_market_cash_prices(market_id: str) -> Optional[RegionalMarketPriceSeries]:
    return REGIONAL_CASH_PRICE_DATABASE.get(market_id)

def list_all_market_series() -> List[RegionalMarketPriceSeries]:
    return list(REGIONAL_CASH_PRICE_DATABASE.values())
