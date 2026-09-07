import { apiClient } from './apiClient';
import {
  RecommendationRequest,
  RecommendationDetailResponse,
  WhatIfScenarioRequest,
  WhatIfScenarioResponse,
} from '../types/recommendation';

export const recommendationService = {
  async runRecommendation(request: RecommendationRequest): Promise<RecommendationDetailResponse> {
    return apiClient<RecommendationDetailResponse>('/recommendations/run', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  },

  async runWhatIfSimulation(request: WhatIfScenarioRequest): Promise<WhatIfScenarioResponse> {
    return apiClient<WhatIfScenarioResponse>('/recommendations/what-if', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  },
};
