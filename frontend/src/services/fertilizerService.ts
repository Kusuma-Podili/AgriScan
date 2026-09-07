import { apiClient } from './apiClient';
import { FertilizerRecommendationSchedule, CommercialFertilizerProduct } from '../types/fertilizer';

export const fertilizerService = {
  async getFertilizerCatalog(category?: string): Promise<CommercialFertilizerProduct[]> {
    const query = category ? `?category=${category}` : '';
    return apiClient<CommercialFertilizerProduct[]>(`/fertilizer/catalog${query}`);
  },

  async calculateSSNMSchedule(params: {
    crop_id: string;
    target_yield_ton_ha?: number;
    strategy?: string;
    soil_n?: number;
    soil_p?: number;
    soil_k?: number;
    ph?: number;
    soil_oc?: number;
    soil_ec?: number;
    soil_texture?: string;
  }): Promise<FertilizerRecommendationSchedule> {
    const searchParams = new URLSearchParams();
    Object.entries(params).forEach(([key, val]) => {
      if (val !== undefined && val !== null) {
        searchParams.append(key, val.toString());
      }
    });
    return apiClient<FertilizerRecommendationSchedule>(`/fertilizer/calculate-ssnm?${searchParams.toString()}`, {
      method: 'POST',
    });
  },
};
