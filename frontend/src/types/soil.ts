export interface SoilSample {
  id?: string;
  farm_id: string;
  field_parcel_id?: string;
  sample_code: string;
  sampling_date?: string;
  depth_cm: number;
  nitrogen_kg_ha: number;
  phosphorus_kg_ha: number;
  potassium_kg_ha: number;
  ph: number;
  electrical_conductivity_ds_m: number;
  organic_carbon_pct: number;
  texture_class: string;
  sand_pct?: number;
  silt_pct?: number;
  clay_pct?: number;
  sulphur_ppm?: number;
  zinc_ppm?: number;
  boron_ppm?: number;
  iron_ppm?: number;
  laboratory_name?: string;
  notes?: string;
}

export interface SoilHealthCardSummary {
  sample_id: string;
  sample_code: string;
  ph_rating: string;
  ph_diagnosis: string;
  ec_rating: string;
  ec_diagnosis: string;
  oc_rating: string;
  nitrogen_rating: string;
  phosphorus_rating: string;
  potassium_rating: string;
  texture_class: string;
  overall_health_score_pct: number;
  amendment_prescription?: string;
}
