import { create } from 'zustand';
import { SoilSample, SoilHealthCardSummary } from '../types/soil';

interface SoilState {
  currentSample: SoilSample;
  updateSoilParameter: (param: keyof SoilSample, value: any) => void;
  healthCard: SoilHealthCardSummary | null;
  setHealthCard: (card: SoilHealthCardSummary | null) => void;
  savedSamples: SoilSample[];
  setSavedSamples: (samples: SoilSample[]) => void;
}

const DEFAULT_SAMPLE: SoilSample = {
  farm_id: 'farm_alpha_01',
  sample_code: 'SHC-2026-N904',
  depth_cm: 15.0,
  nitrogen_kg_ha: 295.0,
  phosphorus_kg_ha: 32.0,
  potassium_kg_ha: 195.0,
  ph: 6.8,
  electrical_conductivity_ds_m: 0.65,
  organic_carbon_pct: 0.62,
  texture_class: 'Loam',
  sand_pct: 42.0,
  silt_pct: 38.0,
  clay_pct: 20.0,
  zinc_ppm: 0.72,
  boron_ppm: 0.58,
  iron_ppm: 5.4,
  laboratory_name: 'Regional Precision Soil Testing Laboratory',
};

export const useSoilStore = create<SoilState>((set) => ({
  currentSample: DEFAULT_SAMPLE,
  updateSoilParameter: (param, value) =>
    set((state) => ({
      currentSample: { ...state.currentSample, [param]: value },
    })),
  healthCard: null,
  setHealthCard: (card) => set({ healthCard: card }),
  savedSamples: [DEFAULT_SAMPLE],
  setSavedSamples: (samples) => set({ savedSamples: samples }),
}));
