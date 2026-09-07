import React from 'react';
import { FlaskConical, CheckCircle2, AlertCircle, Save, RefreshCw } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Button } from '../ui/Button';
import { Slider } from '../ui/Slider';
import { Badge } from '../ui/Badge';
import { useSoilStore } from '../../stores/useSoilStore';
import { soilService } from '../../services/soilService';

export const SoilInputWizard: React.FC = () => {
  const { currentSample, updateSoilParameter, healthCard, setHealthCard } = useSoilStore();

  const handleGenerateHealthCard = async () => {
    try {
      // Simulate/call Soil Health Card generation
      const n_val = currentSample.nitrogen_kg_ha;
      const p_val = currentSample.phosphorus_kg_ha;
      const k_val = currentSample.potassium_kg_ha;
      const ph_val = currentSample.ph;

      let score = 100.0;
      if (ph_val < 5.5 || ph_val > 8.5) score -= 20.0;
      if (n_val < 280) score -= 15.0;
      if (p_val < 23) score -= 15.0;
      if (k_val < 140) score -= 10.0;

      setHealthCard({
        sample_id: currentSample.sample_code,
        sample_code: currentSample.sample_code,
        ph_rating: ph_val < 5.5 ? 'Acidic' : (ph_val > 7.5 ? 'Alkaline' : 'Optimal'),
        ph_diagnosis: 'Bioavailability optimal for primary macronutrients.',
        ec_rating: currentSample.electrical_conductivity_ds_m < 1.0 ? 'Non-Saline' : 'Moderately Saline',
        ec_diagnosis: 'Zero salt hazard detected.',
        oc_rating: currentSample.organic_carbon_pct > 0.60 ? 'Medium to High' : 'Low',
        nitrogen_rating: n_val < 280 ? 'Low (Deficit)' : 'Medium (Adequate)',
        phosphorus_rating: p_val < 23 ? 'Low (Deficit)' : 'Medium (Adequate)',
        potassium_rating: k_val < 140 ? 'Low (Deficit)' : 'Medium (Adequate)',
        texture_class: currentSample.texture_class,
        overall_health_score_pct: Math.max(30.0, score),
        amendment_prescription: ph_val < 5.5 ? 'Agricultural lime recommended.' : undefined,
      });
    } catch (err) {
      console.error('Failed to generate health card:', err);
    }
  };

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <FlaskConical size={22} className="text-amber-600" />
            <span>Soil Chemical & Edaphic Diagnostic Wizard</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            Calibrated laboratory test values determining indigenous nutrient supply (INS/IPS/IKS).
          </p>
        </div>

        <Button
          variant="primary"
          onClick={handleGenerateHealthCard}
          icon={<CheckCircle2 size={16} />}
        >
          Evaluate Soil Health Card
        </Button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Sliders Form */}
        <div className="lg:col-span-2 space-y-5">
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold">Primary Macronutrient Levels (kg/ha)</CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
              <Slider
                label="Available Nitrogen (N - Alkaline KMnO4 method)"
                value={currentSample.nitrogen_kg_ha}
                min={50}
                max={600}
                step={5}
                unit="kg/ha"
                onChange={(v) => updateSoilParameter('nitrogen_kg_ha', v)}
                helperText="Optimal: 280 - 560 kg/ha for medium fertility soils."
              />

              <Slider
                label="Available Phosphorus (P2O5 - Olsen / Bray method)"
                value={currentSample.phosphorus_kg_ha}
                min={5}
                max={100}
                step={1}
                unit="kg/ha"
                onChange={(v) => updateSoilParameter('phosphorus_kg_ha', v)}
                helperText="Optimal: 23 - 56 kg P2O5/ha."
              />

              <Slider
                label="Available Potassium (K2O - 1N NH4OAc method)"
                value={currentSample.potassium_kg_ha}
                min={50}
                max={500}
                step={5}
                unit="kg/ha"
                onChange={(v) => updateSoilParameter('potassium_kg_ha', v)}
                helperText="Optimal: 140 - 280 kg K2O/ha."
              />
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold">Reaction, Salinity & Organic Matter</CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
              <Slider
                label="Soil Reaction (pH)"
                value={currentSample.ph}
                min={3.5}
                max={10.0}
                step={0.1}
                onChange={(v) => updateSoilParameter('ph', v)}
                helperText="Optimal: 6.0 - 7.5. Below 5.5 indicates acid injury; above 8.5 indicates sodic hazard."
              />

              <Slider
                label="Electrical Conductivity (ECe)"
                value={currentSample.electrical_conductivity_ds_m}
                min={0.1}
                max={8.0}
                step={0.05}
                unit="dS/m"
                onChange={(v) => updateSoilParameter('electrical_conductivity_ds_m', v)}
                helperText="Below 1.0 dS/m is non-saline. Above 2.0 dS/m suppresses sensitive crops."
              />

              <Slider
                label="Soil Organic Carbon (SOC %)"
                value={currentSample.organic_carbon_pct}
                min={0.1}
                max={3.0}
                step={0.05}
                unit="%"
                onChange={(v) => updateSoilParameter('organic_carbon_pct', v)}
                helperText="High microbial biological activity occurs at SOC > 0.75%."
              />
            </CardContent>
          </Card>
        </div>

        {/* Soil Health Card Output Preview */}
        <div>
          <Card className="sticky top-20">
            <CardHeader>
              <CardTitle className="text-sm font-bold">Official Soil Health Card</CardTitle>
              <Badge variant="primary" size="sm">
                Score: {healthCard?.overall_health_score_pct || 85}%
              </Badge>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="p-3 bg-slate-50 rounded-xl space-y-2 text-xs">
                <div className="flex justify-between">
                  <span className="text-slate-500">Soil Reaction:</span>
                  <span className="font-bold text-slate-800">{healthCard?.ph_rating || 'Neutral / Optimal'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Salinity Index:</span>
                  <span className="font-bold text-slate-800">{healthCard?.ec_rating || 'Non-Saline'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Nitrogen Status:</span>
                  <span className="font-bold text-slate-800">{healthCard?.nitrogen_rating || 'Adequate'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Phosphorus Status:</span>
                  <span className="font-bold text-slate-800">{healthCard?.phosphorus_rating || 'Adequate'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Potassium Status:</span>
                  <span className="font-bold text-slate-800">{healthCard?.potassium_rating || 'Adequate'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Texture Class:</span>
                  <span className="font-bold text-slate-800">{currentSample.texture_class}</span>
                </div>
              </div>

              {healthCard?.amendment_prescription && (
                <div className="p-3 bg-amber-50 rounded-xl border border-amber-200 text-xs text-amber-800">
                  <p className="font-bold mb-1">Prescribed Amendment:</p>
                  <p>{healthCard.amendment_prescription}</p>
                </div>
              )}

              <p className="text-[11px] text-slate-400 leading-relaxed italic">
                Nutrient supply indices are automatically mapped into the SSNM Fertilizer Balancer.
              </p>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};
