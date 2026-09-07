export interface CompositeRecommendation {
  rank: number;
  crop_id: string;
  crop_name: string;
  category: string;
  composite_suitability_score: number;
  ml_confidence_pct: number;
  ecocrop_score: number;
  fao_suitability_class: string;
  estimated_yield_ton_ha: number;
  estimated_gross_revenue_usd_ha: number;
  estimated_cultivation_cost_usd_ha: number;
  estimated_net_profit_usd_ha: number;
  economic_roi_pct: number;
  risk_level: string;
  primary_limiting_factor: string;
  agronomic_advisory: string;
}

export interface RecommendationRequest {
  farm_id?: string;
  field_parcel_id?: string;
  soil_sample_id?: string;
  n_kg_ha: number;
  p_kg_ha: number;
  k_kg_ha: number;
  ph: number;
  organic_carbon_pct: number;
  ec_ds_m: number;
  soil_texture: string;
  temperature_c: number;
  temp_max_c?: number;
  temp_min_c?: number;
  humidity_pct: number;
  rainfall_mm: number;
  elevation_m: number;
  category_filter?: string;
  top_k: number;
  target_budget_usd_ha?: number;
}

export interface RecommendationDetailResponse {
  crop_rankings: CompositeRecommendation[];
  top_crop_fertilizer_schedule: any;
  top_crop_yield_risk_analysis: any;
  top_crop_pest_alerts: any;
  ensemble_metadata: Record<string, number>;
  query_timestamp: string;
}

export interface WhatIfScenarioRequest {
  base_request: RecommendationRequest;
  simulated_rainfall_delta_pct: number;
  simulated_temperature_delta_c: number;
  supplemental_irrigation_mm: number;
  additional_fertilizer_budget_pct: number;
}

export interface WhatIfScenarioResponse {
  baseline_top_crop: string;
  baseline_suitability: number;
  simulated_top_crop: string;
  simulated_suitability: number;
  rank_changes: Array<{
    crop_id: string;
    crop_name: string;
    new_rank: number;
    new_suitability_score: number;
  }>;
  water_stress_shift_pct: number;
  summary_insight: string;
}
