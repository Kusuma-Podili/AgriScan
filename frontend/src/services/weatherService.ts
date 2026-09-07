import { apiClient } from './apiClient';
import { WeatherCurrentResponse, IrrigationAdvisoryResponse } from '../types/weather';

export const weatherService = {
  async getCurrentWeather(lat: number, lon: number, elevation?: number): Promise<WeatherCurrentResponse> {
    const params = new URLSearchParams({
      latitude: lat.toString(),
      longitude: lon.toString(),
    });
    if (elevation) params.append('elevation_m', elevation.toString());
    return apiClient<WeatherCurrentResponse>(`/weather/current?${params.toString()}`);
  },

  async getIrrigationAdvisory(
    cropId: string,
    stage: string = 'mid',
    soilMoisturePct: number = 28.0,
    lat: number = 20.5
  ): Promise<IrrigationAdvisoryResponse> {
    const params = new URLSearchParams({
      crop_id: cropId,
      stage,
      soil_moisture_pct: soilMoisturePct.toString(),
      latitude: lat.toString(),
    });
    return apiClient<IrrigationAdvisoryResponse>(`/weather/irrigation-advisory?${params.toString()}`);
  },
};
