export interface MandiMarketPrice {
  crop_id: string;
  commodity_name: string;
  mandi_name: string;
  state: string;
  modal_price_usd_per_ton: number;
  min_price_usd_per_ton: number;
  max_price_usd_per_ton: number;
  price_trend_7day_pct: number;
  arrival_quantity_ton: number;
  reported_date: string;
}

export interface MarketCommoditySummary {
  commodity_name: string;
  average_price_usd_ton: number;
  high_52week_usd: number;
  low_52week_usd: number;
  volatility_score: number;
  market_outlook: string;
}
