import { apiClient } from './apiClient';
import { CropAgronomicProfile } from '../types/crop';

export const cropService = {
  async getAllCrops(category?: string, search?: string): Promise<CropAgronomicProfile[]> {
    const params = new URLSearchParams();
    if (category) params.append('category', category);
    if (search) params.append('search', search);
    const queryString = params.toString() ? `?${params.toString()}` : '';
    return apiClient<CropAgronomicProfile[]>(`/crops/${queryString}`);
  },

  async getCropCategories(): Promise<string[]> {
    return apiClient<string[]>('/crops/categories/all');
  },

  async getCropById(cropId: string): Promise<CropAgronomicProfile> {
    return apiClient<CropAgronomicProfile>(`/crops/${cropId}`);
  },
};
