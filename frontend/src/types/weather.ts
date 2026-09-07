export interface DailyForecast {
  forecast_date: string;
  temp_max_c: number;
  temp_min_c: number;
  humidity_pct: number;
  rainfall_prob_pct: number;
  expected_rainfall_mm: number;
  wind_speed_m_s: number;
  et0_mm_day: number;
  condition_summary: string;
  heat_stress_alert: boolean;
  frost_alert: boolean;
}

export interface WeatherCurrentResponse {
  latitude: number;
  longitude: number;
  temperature_c: number;
  temp_max_c: number;
  temp_min_c: number;
  humidity_pct: number;
  wind_speed_m_s: number;
  rainfall_mm: number;
  et0_reference_mm_day: number;
  condition: string;
  observed_at: string;
  forecast_7day: DailyForecast[];
}

export interface IrrigationAdvisoryResponse {
  crop_id: string;
  growth_stage: string;
  current_et0_mm_day: number;
  crop_coefficient_kc: number;
  crop_evapotranspiration_etc_mm_day: number;
  effective_rainfall_mm: number;
  net_irrigation_depth_mm: number;
  recommended_drip_runtime_hours: number;
  irrigation_urgency: 'Critical' | 'Recommended' | 'Adequate' | 'None';
  soil_moisture_depletion_pct: number;
}
