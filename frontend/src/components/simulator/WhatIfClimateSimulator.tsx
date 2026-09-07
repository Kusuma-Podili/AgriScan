import React, { useState } from 'react';
import { Sliders, RefreshCw, ArrowRight, TrendingUp, AlertCircle, Droplets, Thermometer } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Button } from '../ui/Button';
import { Slider } from '../ui/Slider';
import { Badge } from '../ui/Badge';
import { useRecommendationStore } from '../../stores/useRecommendationStore';
import { recommendationService } from '../../services/recommendationService';

export const WhatIfClimateSimulator: React.FC = () => {
  const { queryParams, whatIfResult, setWhatIfResult } = useRecommendationStore();

  const [rainDeltaPct, setRainDeltaPct] = useState<number>(-25.0);
  const [tempDeltaC, setTempDeltaC] = useState<number>(2.0);
  const [irrigationMm, setIrrigationMm] = useState<number>(50.0);
  const [budgetDeltaPct, setBudgetDeltaPct] = useState<number>(0.0);
  const [isSimulating, setIsSimulating] = useState<boolean>(false);

  const handleSimulate = async () => {
    setIsSimulating(true);
    try {
      const response = await recommendationService.runWhatIfSimulation({
        base_request: queryParams,
        simulated_rainfall_delta_pct: rainDeltaPct,
        simulated_temperature_delta_c: tempDeltaC,
        supplemental_irrigation_mm: irrigationMm,
        additional_fertilizer_budget_pct: budgetDeltaPct,
      });
      setWhatIfResult(response);
    } catch (err) {
      console.error('Simulation error:', err);
    } finally {
      setIsSimulating(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Sliders size={22} className="text-sky-600" />
            <span>Interactive Agro-Climatic "What-If" Scenario Studio</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            Simulate drought events, monsoon delays, heatwaves, or supplemental irrigation to stress-test crop choices.
          </p>
        </div>

        <Button
          variant="primary"
          onClick={handleSimulate}
          isLoading={isSimulating}
          icon={<RefreshCw size={16} />}
        >
          Compute Scenario Trajectory
        </Button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Scenario Parameter Sliders */}
        <div className="lg:col-span-1 space-y-4">
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold flex items-center gap-2">
                <Droplets size={16} className="text-sky-500" />
                <span>Precipitation Modulation</span>
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <Slider
                label="Rainfall Shift Percentage"
                value={rainDeltaPct}
                min={-50}
                max={50}
                step={5}
                unit="%"
                onChange={setRainDeltaPct}
                helperText="-25% represents moderate monsoon drought."
              />

              <Slider
                label="Supplemental Irrigation Capacity"
                value={irrigationMm}
                min={0}
                max={250}
                step={10}
                unit="mm"
                onChange={setIrrigationMm}
                helperText="Drip or tube well water reserve to buffer dry spells."
              />
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold flex items-center gap-2">
                <Thermometer size={16} className="text-amber-500" />
                <span>Thermal & Economic Adjusters</span>
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <Slider
                label="Mean Temperature Delta"
                value={tempDeltaC}
                min={-4.0}
                max={5.0}
                step={0.5}
                unit="°C"
                onChange={setTempDeltaC}
                helperText="+2.0°C models terminal heat stress."
              />

              <Slider
                label="Fertilizer Budget Adjustment"
                value={budgetDeltaPct}
                min={-30}
                max={50}
                step={5}
                unit="%"
                onChange={setBudgetDeltaPct}
              />
            </CardContent>
          </Card>
        </div>

        {/* Results & Comparative Diff */}
        <div className="lg:col-span-2 space-y-5">
          {whatIfResult ? (
            <>
              {/* Top Shift Comparison Banner */}
              <div className="p-6 bg-slate-900 text-white rounded-2xl shadow-md flex flex-col sm:flex-row items-center justify-between gap-6">
                <div className="text-center sm:text-left">
                  <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Baseline Optimal</span>
                  <h3 className="text-xl font-bold text-white mt-1">{whatIfResult.baseline_top_crop}</h3>
                  <p className="text-xs text-agro-400 font-semibold">{whatIfResult.baseline_suitability}% Suitability</p>
                </div>

                <div className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white shrink-0">
                  <ArrowRight size={20} />
                </div>

                <div className="text-center sm:text-right">
                  <span className="text-[11px] font-bold text-sky-300 uppercase tracking-wider">Simulated Optimal</span>
                  <h3 className="text-xl font-bold text-white mt-1">{whatIfResult.simulated_top_crop}</h3>
                  <p className="text-xs text-sky-400 font-semibold">{whatIfResult.simulated_suitability}% Suitability</p>
                </div>
              </div>

              {/* Agronomic Insight Alert */}
              <div className="p-4 bg-sky-50 rounded-xl border border-sky-200 text-xs text-sky-900 flex items-start gap-3">
                <AlertCircle size={18} className="shrink-0 text-sky-600 mt-0.5" />
                <div>
                  <p className="font-bold">Agronomic Simulation Takeaway:</p>
                  <p className="mt-0.5 leading-relaxed">{whatIfResult.summary_insight}</p>
                </div>
              </div>

              {/* Transitioned Crop Rankings Table */}
              <Card>
                <CardHeader>
                  <CardTitle className="text-sm font-bold">Adjusted Recommendation Ranking</CardTitle>
                </CardHeader>
                <CardContent className="p-0">
                  <table className="w-full text-left text-xs">
                    <thead className="bg-slate-50 text-slate-600 uppercase tracking-wider border-b border-slate-100">
                      <tr>
                        <th className="py-2.5 px-4">New Rank</th>
                        <th className="py-2.5 px-4">Crop</th>
                        <th className="py-2.5 px-4">Simulated Suitability</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {whatIfResult.rank_changes.map((rc) => (
                        <tr key={rc.crop_id} className="hover:bg-slate-50">
                          <td className="py-3 px-4 font-bold text-slate-800">#{rc.new_rank}</td>
                          <td className="py-3 px-4 font-semibold text-slate-900">{rc.crop_name}</td>
                          <td className="py-3 px-4 font-bold text-agro-700">{rc.new_suitability_score}%</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </CardContent>
              </Card>
            </>
          ) : (
            <Card className="h-full flex items-center justify-center p-12 text-center">
              <div>
                <Sliders size={36} className="mx-auto text-slate-300 mb-3" />
                <h4 className="font-bold text-slate-700">No Simulation Active</h4>
                <p className="text-xs text-slate-400 mt-1 max-w-sm">
                  Adjust sliders on the left to configure weather shifts and click "Compute Scenario Trajectory".
                </p>
              </div>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
};
