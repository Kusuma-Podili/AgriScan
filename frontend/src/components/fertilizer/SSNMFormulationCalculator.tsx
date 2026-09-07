import React, { useState, useEffect } from 'react';
import { Beaker, Calculator, PackageCheck, DollarSign, AlertCircle } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Button } from '../ui/Button';
import { Badge } from '../ui/Badge';
import { useSoilStore } from '../../stores/useSoilStore';
import { fertilizerService } from '../../services/fertilizerService';
import { FertilizerRecommendationSchedule } from '../../types/fertilizer';

export const SSNMFormulationCalculator: React.FC = () => {
  const { currentSample } = useSoilStore();

  const [selectedCropId, setSelectedCropId] = useState<string>('wheat');
  const [strategy, setStrategy] = useState<string>('dap_urea_mop');
  const [targetYield, setTargetYield] = useState<number>(5.0);
  const [schedule, setSchedule] = useState<FertilizerRecommendationSchedule | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const calculateSchedule = async () => {
    setLoading(true);
    try {
      const res = await fertilizerService.calculateSSNMSchedule({
        crop_id: selectedCropId,
        target_yield_ton_ha: targetYield,
        strategy,
        soil_n: currentSample.nitrogen_kg_ha,
        soil_p: currentSample.phosphorus_kg_ha,
        soil_k: currentSample.potassium_kg_ha,
        ph: currentSample.ph,
        soil_oc: currentSample.organic_carbon_pct,
        soil_ec: currentSample.electrical_conductivity_ds_m,
      });
      setSchedule(res);
    } catch (err) {
      console.error('Error calculating fertilizer:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    calculateSchedule();
  }, [selectedCropId, strategy, targetYield]);

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Beaker size={22} className="text-emerald-600" />
            <span>Site-Specific Nutrient Management (SSNM) Calculator</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            Calculates exact commercial fertilizer bags and growth-stage split applications based on indigenous soil reserves.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={selectedCropId}
            onChange={(e) => setSelectedCropId(e.target.value)}
            className="text-xs font-semibold bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-slate-700"
          >
            <option value="wheat">Wheat (Grain)</option>
            <option value="rice">Rice (Paddy)</option>
            <option value="maize">Maize (Corn)</option>
            <option value="cotton">Cotton</option>
            <option value="chickpea">Chickpea (Gram)</option>
            <option value="potato">Potato</option>
            <option value="tomato">Tomato</option>
            <option value="sugarcane">Sugarcane</option>
          </select>

          <select
            value={strategy}
            onChange={(e) => setStrategy(e.target.value)}
            className="text-xs font-semibold bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-slate-700"
          >
            <option value="dap_urea_mop">DAP + Urea + MOP</option>
            <option value="straight_ssp_mop">SSP + Urea + MOP</option>
          </select>
        </div>
      </div>

      {schedule && (
        <div className="space-y-6">
          {/* Summary Banner */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <Card>
              <CardContent className="p-4 text-center">
                <span className="text-[10px] text-slate-400 uppercase font-bold">Total Fertilizer Cost / Hectare</span>
                <p className="text-2xl font-black text-slate-900 mt-1">
                  ${schedule.total_estimated_fertilizer_cost_usd_ha}
                </p>
                <p className="text-[11px] text-slate-500 mt-0.5">
                  (${schedule.total_estimated_fertilizer_cost_usd_acre} / acre)
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 text-center">
                <span className="text-[10px] text-slate-400 uppercase font-bold">Elemental N-P-K Demand</span>
                <p className="text-xl font-black text-slate-900 mt-1">
                  {schedule.balance_sheet.total_demand_n_kg} - {schedule.balance_sheet.total_demand_p2o5_kg} - {schedule.balance_sheet.total_demand_k2o_kg}
                </p>
                <p className="text-[11px] text-slate-500 mt-0.5">kg pure nutrients for {targetYield} t/ha yield</p>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 text-center">
                <span className="text-[10px] text-slate-400 uppercase font-bold">Indigenous Soil Supply Deduction</span>
                <p className="text-xl font-black text-emerald-600 mt-1">
                  -{schedule.balance_sheet.indigenous_supply_n_kg} N / -{schedule.balance_sheet.indigenous_supply_p2o5_kg} P kg
                </p>
                <p className="text-[11px] text-slate-500 mt-0.5">Saved from indigenous soil reserves</p>
              </CardContent>
            </Card>
          </div>

          {/* Doses Split Application Table */}
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold flex items-center gap-2">
                <PackageCheck size={18} className="text-agro-600" />
                <span>Commercial Bag Dosage & Growth-Stage Splits</span>
              </CardTitle>
            </CardHeader>
            <CardContent className="p-0">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-50 text-slate-600 uppercase tracking-wider border-b border-slate-100">
                  <tr>
                    <th className="py-3 px-4">Fertilizer Product</th>
                    <th className="py-3 px-4">Application Stage</th>
                    <th className="py-3 px-4">Rate (kg/ha)</th>
                    <th className="py-3 px-4">Bags (50kg / ha)</th>
                    <th className="py-3 px-4">Bags (50kg / acre)</th>
                    <th className="py-3 px-4">Method</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {schedule.doses.map((d, i) => (
                    <tr key={i} className="hover:bg-slate-50">
                      <td className="py-3.5 px-4 font-bold text-slate-900">{d.product_name}</td>
                      <td className="py-3.5 px-4 font-semibold text-agro-700">{d.timing_stage}</td>
                      <td className="py-3.5 px-4 font-bold text-slate-800">{d.rate_kg_ha} kg</td>
                      <td className="py-3.5 px-4 font-bold text-slate-900">{d.bags_50kg_ha} bags</td>
                      <td className="py-3.5 px-4 text-slate-600">{d.bags_50kg_acre} bags</td>
                      <td className="py-3.5 px-4 text-slate-500 max-w-xs">{d.application_method}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  );
};
