import { apiClient } from './apiClient';
import { SoilSample, SoilHealthCardSummary } from '../types/soil';

export const soilService = {
  async recordSoilSample(sample: SoilSample): Promise<SoilSample> {
    return apiClient<SoilSample>('/soil/samples', {
      method: 'POST',
      body: JSON.stringify(sample),
    });
  },

  async getFarmSoilSamples(farmId: string): Promise<SoilSample[]> {
    return apiClient<SoilSample[]>(`/soil/samples/farm/${farmId}`);
  },

  async getSoilHealthCard(sampleId: string): Promise<SoilHealthCardSummary> {
    return apiClient<SoilHealthCardSummary>(`/soil/samples/${sampleId}/health-card`);
  },
};
