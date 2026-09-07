export interface FertilizerDoseItem {
  product_id: string;
  product_name: string;
  rate_kg_ha: number;
  rate_kg_acre: number;
  bags_50kg_ha: number;
  bags_50kg_acre: number;
  timing_stage: string;
  application_method: string;
  estimated_cost_usd: number;
}

export interface NutrientBalanceSheet {
  target_yield_ton_ha: number;
  total_demand_n_kg: number;
  total_demand_p2o5_kg: number;
  total_demand_k2o_kg: number;
  indigenous_supply_n_kg: number;
  indigenous_supply_p2o5_kg: number;
  indigenous_supply_k2o_kg: number;
  net_deficit_n_kg: number;
  net_deficit_p2o5_kg: number;
  net_deficit_k2o_kg: number;
  fertilizer_requirement_n_kg: number;
  fertilizer_requirement_p2o5_kg: number;
  fertilizer_requirement_k2o_kg: number;
}

export interface FertilizerRecommendationSchedule {
  crop_id: string;
  crop_name: string;
  yield_goal_ton_ha: number;
  strategy_name: string;
  balance_sheet: NutrientBalanceSheet;
  doses: FertilizerDoseItem[];
  micronutrient_advisories: string[];
  total_estimated_fertilizer_cost_usd_ha: number;
  total_estimated_fertilizer_cost_usd_acre: number;
  soil_amendment_recommendation?: string;
}

export interface CommercialFertilizerProduct {
  id: string;
  name: string;
  chemical_formula: string;
  category: string;
  n_pct: number;
  p2o5_pct: number;
  k2o_pct: number;
  s_pct: number;
  ca_pct: number;
  mg_pct: number;
  zn_pct: number;
  fe_pct: number;
  b_pct: number;
  physical_state: string;
  solubility_g_per_l_20c: number;
  salt_index: number;
  acid_base_equivalent_kg_caco3: number;
  recommended_methods: string[];
  timing_rules: string;
  handling_notes: string;
}
