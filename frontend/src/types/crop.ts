export interface CropKcStages {
  initial: number;
  mid: number;
  end: number;
}

export interface NutrientUptakeRate {
  n_kg_per_ton: number;
  p2o5_kg_per_ton: number;
  k2o_kg_per_ton: number;
  s_kg_per_ton?: number;
  zn_g_per_ton?: number;
  fe_g_per_ton?: number;
}

export interface CropAgronomicProfile {
  id: string;
  name: string;
  scientific_name: string;
  family: string;
  category: 'Cereals' | 'Pulses' | 'Oilseeds' | 'Commercial' | 'Spices' | 'Vegetables' | 'Fruits' | 'Plantation' | 'Fodder' | string;
  climatic_zone: string;
  temp_min_c: number;
  temp_opt_min_c: number;
  temp_opt_max_c: number;
  temp_max_c: number;
  rainfall_min_mm: number;
  rainfall_opt_min_mm: number;
  rainfall_opt_max_mm: number;
  rainfall_max_mm: number;
  ph_min: number;
  ph_opt_min: number;
  ph_opt_max: number;
  ph_max: number;
  salinity_tolerance_ds_m: number;
  drainage_preference: string[];
  suitable_soil_textures: string[];
  growing_period_days_min: number;
  growing_period_days_max: number;
  base_temperature_c: number;
  kc_stages: CropKcStages;
  nutrient_uptake: NutrientUptakeRate;
  benchmark_yield_ton_ha: number;
  typical_water_req_mm: number;
  cost_of_cultivation_usd_ha: number;
  market_price_usd_per_ton: number;
  risk_volatility_index: number;
  primary_pests: string[];
  primary_diseases: string[];
  agronomic_advisory: string;
}
