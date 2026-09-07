export interface SensorTelemetryPayload {
  sensor_id: string;
  farm_id: string;
  field_parcel_id: string;
  timestamp_epoch: number;
  raw_moisture_vol_pct: number;
  filtered_moisture_vol_pct: number;
  raw_ec_ds_m: number;
  filtered_ec_ds_m: number;
  soil_temperature_c: number;
  battery_level_pct: number;
  is_anomaly: boolean;
}
