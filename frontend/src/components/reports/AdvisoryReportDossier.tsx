import React from 'react';
import { FileSpreadsheet, Printer, Download, CheckCircle, Sprout, FlaskConical, Beaker } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Button } from '../ui/Button';
import { useSoilStore } from '../../stores/useSoilStore';
import { useRecommendationStore } from '../../stores/useRecommendationStore';

export const AdvisoryReportDossier: React.FC = () => {
  const { currentSample, healthCard } = useSoilStore();
  const { results } = useRecommendationStore();

  const handlePrint = () => {
    window.print();
  };

  const handleExportJson = () => {
    const data = {
      sample: currentSample,
      health_card: healthCard,
      recommendation: results,
      exported_at: new Date().toISOString(),
    };
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `AgroPulse_Advisory_${currentSample.sample_code}.json`;
    a.click();
  };

  const topCrop = results?.crop_rankings[0];

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4 print:hidden">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <FileSpreadsheet size={22} className="text-agro-600" />
            <span>Comprehensive Agronomic Advisory Dossier</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            Exportable report combining Soil Health diagnostics, SSNM fertilizer schedules, and ML recommendations.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <Button variant="outline" size="sm" onClick={handleExportJson} icon={<Download size={16} />}>
            Export JSON Data
          </Button>
          <Button variant="primary" size="sm" onClick={handlePrint} icon={<Printer size={16} />}>
            Print / Save as PDF
          </Button>
        </div>
      </div>

      {/* Printable Report Document Card */}
      <Card className="p-8 space-y-8 bg-white print:border-none print:shadow-none">
        {/* Document Header */}
        <div className="border-b border-slate-200 pb-6 flex items-start justify-between">
          <div>
            <span className="text-xs font-bold uppercase tracking-widest text-agro-700">Official Advisory Document</span>
            <h1 className="text-2xl font-black text-slate-900 mt-1">AgroPulse Farm Advisory Dossier</h1>
            <p className="text-xs text-slate-500 mt-1">
              Sample Code: {currentSample.sample_code} | Date: {new Date().toLocaleDateString()}
            </p>
          </div>

          <div className="text-right">
            <div className="text-xs font-bold text-slate-800">Precision Agronomy Directorate</div>
            <div className="text-[11px] text-slate-400 mt-0.5">ICAR-FAO Compliant Architecture</div>
          </div>
        </div>

        {/* Section 1: Soil Test & Health Card */}
        <div className="space-y-3">
          <h3 className="text-sm font-bold uppercase tracking-wider text-slate-800 flex items-center gap-2">
            <FlaskConical size={16} className="text-amber-600" />
            <span>1. Soil Chemical & Physical Diagnosis</span>
          </h3>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span className="text-slate-500 block">Reaction (pH):</span>
              <span className="text-base font-bold text-slate-800 mt-0.5 block">{currentSample.ph} (Optimal)</span>
            </div>
            <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span className="text-slate-500 block">Available N:</span>
              <span className="text-base font-bold text-slate-800 mt-0.5 block">{currentSample.nitrogen_kg_ha} kg/ha</span>
            </div>
            <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span className="text-slate-500 block">Available P2O5:</span>
              <span className="text-base font-bold text-slate-800 mt-0.5 block">{currentSample.phosphorus_kg_ha} kg/ha</span>
            </div>
            <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span className="text-slate-500 block">Available K2O:</span>
              <span className="text-base font-bold text-slate-800 mt-0.5 block">{currentSample.potassium_kg_ha} kg/ha</span>
            </div>
          </div>
        </div>

        {/* Section 2: Top Recommended Crop Advisory */}
        {topCrop && (
          <div className="space-y-3">
            <h3 className="text-sm font-bold uppercase tracking-wider text-slate-800 flex items-center gap-2">
              <Sprout size={16} className="text-agro-600" />
              <span>2. Primary Crop Recommendation</span>
            </h3>

            <div className="p-5 bg-agro-50/50 rounded-xl border border-agro-200 space-y-4">
              <div className="flex flex-col sm:flex-row justify-between sm:items-center gap-2">
                <div>
                  <h4 className="text-xl font-black text-agro-950">{topCrop.crop_name}</h4>
                  <span className="text-xs font-semibold text-agro-800">{topCrop.category} | {topCrop.fao_suitability_class}</span>
                </div>
                <div className="text-right">
                  <span className="text-2xl font-black text-agro-700">{topCrop.composite_suitability_score}%</span>
                  <p className="text-[10px] text-agro-600 font-bold uppercase">Suitability Score</p>
                </div>
              </div>

              <div className="grid grid-cols-3 gap-3 text-center text-xs">
                <div className="p-3 bg-white rounded-lg border border-agro-100">
                  <span className="text-slate-500 block">Expected Yield</span>
                  <span className="font-bold text-slate-800 text-sm mt-0.5 block">{topCrop.estimated_yield_ton_ha} t/ha</span>
                </div>
                <div className="p-3 bg-white rounded-lg border border-agro-100">
                  <span className="text-slate-500 block">Estimated Cost</span>
                  <span className="font-bold text-slate-800 text-sm mt-0.5 block">${topCrop.estimated_cultivation_cost_usd_ha}</span>
                </div>
                <div className="p-3 bg-white rounded-lg border border-agro-100">
                  <span className="text-emerald-600 block font-semibold">Net Profit / Ha</span>
                  <span className="font-black text-emerald-800 text-sm mt-0.5 block">+${topCrop.estimated_net_profit_usd_ha}</span>
                </div>
              </div>

              <p className="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-lg border border-agro-100">
                <span className="font-bold block mb-1">Agronomic Sowing & Field Advisory:</span>
                {topCrop.agronomic_advisory}
              </p>
            </div>
          </div>
        )}
      </Card>
    </div>
  );
};
