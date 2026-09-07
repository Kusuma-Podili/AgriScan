import { apiClient } from './apiClient';
import { MandiMarketPrice, MarketCommoditySummary } from '../types/market';

export const marketService = {
  async getMandiPrices(category?: string, state?: string): Promise<MandiMarketPrice[]> {
    const params = new URLSearchParams();
    if (category) params.append('category', category);
    if (state) params.append('state', state);
    const query = params.toString() ? `?${params.toString()}` : '';
    return apiClient<MandiMarketPrice[]>(`/market/mandi-prices${query}`);
  },

  async getCommoditySummary(cropId: string): Promise<MarketCommoditySummary> {
    return apiClient<MarketCommoditySummary>(`/market/commodity-summary/${cropId}`);
  },
};
