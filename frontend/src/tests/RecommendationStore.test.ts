import { describe, it, expect, beforeEach } from 'vitest';
import { useRecommendationStore } from '../stores/useRecommendationStore';

describe('useRecommendationStore', () => {
  beforeEach(() => {
    useRecommendationStore.setState({
      queryParams: {
        n_kg_ha: 280,
        p_kg_ha: 30,
        k_kg_ha: 180,
        ph: 6.8,
        organic_carbon_pct: 0.55,
        ec_ds_m: 0.7,
        soil_texture: 'loam',
        temperature_c: 26.0,
        humidity_pct: 65.0,
        rainfall_mm: 750.0,
        elevation_m: 150.0,
        top_k: 10,
      },
      results: null,
      selectedCrop: null,
      whatIfResult: null,
      isGenerating: false,
    });
  });

  it('updates query parameters correctly', () => {
    const { setQueryParams } = useRecommendationStore.getState();
    setQueryParams({ rainfall_mm: 950.0, temperature_c: 30.5 });

    const state = useRecommendationStore.getState();
    expect(state.queryParams.rainfall_mm).toBe(950.0);
    expect(state.queryParams.temperature_c).toBe(30.5);
  });

  it('sets selected crop and tracks selection', () => {
    const { setSelectedCrop } = useRecommendationStore.getState();
    const mockCrop = {
      rank: 1,
      crop_id: 'wheat',
      crop_name: 'Wheat',
      category: 'Cereals',
      composite_suitability_score: 94.5,
      ml_confidence_pct: 92.0,
      ecocrop_score: 96.0,
      fao_suitability_class: 'S1 - Highly Suitable',
      estimated_yield_ton_ha: 5.2,
      estimated_gross_revenue_usd_ha: 1352.0,
      estimated_cultivation_cost_usd_ha: 520.0,
      estimated_net_profit_usd_ha: 832.0,
      economic_roi_pct: 160.0,
      risk_level: 'Low Risk',
      primary_limiting_factor: 'None',
      agronomic_advisory: 'Standard crown root initiation irrigation at 21 DAS.',
    };

    setSelectedCrop(mockCrop);
    const state = useRecommendationStore.getState();
    expect(state.selectedCrop?.crop_id).toBe('wheat');
    expect(state.selectedCrop?.composite_suitability_score).toBe(94.5);
  });
});
