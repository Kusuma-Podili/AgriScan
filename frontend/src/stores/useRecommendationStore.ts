import { create } from 'zustand';
import {
  RecommendationRequest,
  RecommendationDetailResponse,
  CompositeRecommendation,
  WhatIfScenarioResponse,
} from '../types/recommendation';

interface RecommendationState {
  queryParams: RecommendationRequest;
  setQueryParams: (params: Partial<RecommendationRequest>) => void;
  results: RecommendationDetailResponse | null;
  setResults: (results: RecommendationDetailResponse | null) => void;
  selectedCrop: CompositeRecommendation | null;
  setSelectedCrop: (crop: CompositeRecommendation | null) => void;
  whatIfResult: WhatIfScenarioResponse | null;
  setWhatIfResult: (res: WhatIfScenarioResponse | null) => void;
  isGenerating: boolean;
  setIsGenerating: (gen: boolean) => void;
}

const DEFAULT_QUERY: RecommendationRequest = {
  n_kg_ha: 295.0,
  p_kg_ha: 32.0,
  k_kg_ha: 195.0,
  ph: 6.8,
  organic_carbon_pct: 0.62,
  ec_ds_m: 0.65,
  soil_texture: 'loam',
  temperature_c: 27.5,
  humidity_pct: 68.0,
  rainfall_mm: 850.0,
  elevation_m: 160.0,
  category_filter: '',
  top_k: 8,
};

export const useRecommendationStore = create<RecommendationState>((set) => ({
  queryParams: DEFAULT_QUERY,
  setQueryParams: (params) =>
    set((state) => ({
      queryParams: { ...state.queryParams, ...params },
    })),
  results: null,
  setResults: (results) => set({ results }),
  selectedCrop: null,
  setSelectedCrop: (crop) => set({ selectedCrop: crop }),
  whatIfResult: null,
  setWhatIfResult: (whatIfResult) => set({ whatIfResult }),
  isGenerating: false,
  setIsGenerating: (isGenerating) => set({ isGenerating }),
}));
