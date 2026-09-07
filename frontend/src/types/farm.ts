export interface FieldParcel {
  id: string;
  farm_id: string;
  name: string;
  area_hectares: number;
  current_crop?: string;
  sowing_date?: string;
  irrigation_system: string;
  polygon_geojson?: string;
  created_at: string;
}

export interface Farm {
  id: string;
  owner_id: string;
  name: string;
  state: string;
  district: string;
  latitude: number;
  longitude: number;
  elevation_m: number;
  total_area_hectares: number;
  irrigation_source: string;
  soil_type_primary: string;
  polygon_geojson?: string;
  created_at: string;
  fields: FieldParcel[];
}
