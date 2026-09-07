import React from 'react';
import {
  Sprout,
  FlaskConical,
  CloudSun,
  ShieldAlert,
  ArrowUpRight,
  Droplets,
  TrendingUp,
  MapPin,
  CheckCircle2,
} from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Button } from '../ui/Button';
import { Badge } from '../ui/Badge';
import { useAppStore } from '../../stores/useAppStore';
import { useSoilStore } from '../../stores/useSoilStore';
import { useRecommendationStore } from '../../stores/useRecommendationStore';

export const DashboardOverview: React.FC = () => {
  const { setActiveTab } = useAppStore();
  const { currentSample } = useSoilStore();
  const { results } = useRecommendationStore();

  return (
    <div className="space-y-6">
      {/* Top Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-linear-to-r from-agro-900 via-agro-800 to-slate-900 text-white p-6 sm:p-8 shadow-md">
        <div className="relative z-10 max-w-2xl">
          <Badge variant="primary" className="bg-agro-500/20 text-agro-300 border-agro-400/30 mb-3">
            Agro-Climatic Zone: Central Semi-Arid Vertisol
          </Badge>
          <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
            Precision Crop & Soil Advisory Intelligence
          </h1>
          <p className="mt-2 text-sm text-slate-300 leading-relaxed">
            Multi-model Machine Learning blended with deterministic FAO EcoCrop & Penman-Monteith algorithms.
            Simulate climate shifts, balance NPK deficits, and maximize seasonal net returns.
          </p>

          <div className="mt-5 flex flex-wrap gap-3">
            <Button
              variant="primary"
              className="bg-agro-500 hover:bg-agro-400 text-slate-950 font-bold"
              onClick={() => setActiveTab('recommendation')}
              icon={<Sprout size={16} />}
            >
              Run Crop Recommendation
            </Button>
            <Button
              variant="secondary"
              className="bg-white/10 hover:bg-white/20 text-white border-transparent"
              onClick={() => setActiveTab('simulator')}
              icon={<ArrowUpRight size={16} />}
            >
              Launch What-If Simulator
            </Button>
          </div>
        </div>

        {/* Decorative background circle */}
        <div className="absolute -right-12 -bottom-12 w-80 h-80 rounded-full bg-agro-500/10 blur-3xl pointer-events-none" />
      </div>

      {/* 4 Stat Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card hoverEffect>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Top Recommended Crop</p>
              <h4 className="text-xl font-bold text-slate-900 mt-1">
                {results?.crop_rankings[0]?.crop_name || 'Wheat (Triticum)'}
              </h4>
              <p className="text-xs text-emerald-600 font-medium flex items-center gap-1 mt-1">
                <CheckCircle2 size={12} />
                Suitability: {results?.crop_rankings[0]?.composite_suitability_score || '92.4'}%
              </p>
            </div>
            <div className="w-12 h-12 rounded-xl bg-agro-50 text-agro-600 flex items-center justify-center">
              <Sprout size={24} />
            </div>
          </CardContent>
        </Card>

        <Card hoverEffect>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Soil Health Status</p>
              <h4 className="text-xl font-bold text-slate-900 mt-1">pH {currentSample.ph}</h4>
              <p className="text-xs text-slate-500 font-medium mt-1">
                NPK: {currentSample.nitrogen_kg_ha} / {currentSample.phosphorus_kg_ha} / {currentSample.potassium_kg_ha} kg/ha
              </p>
            </div>
            <div className="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center">
              <FlaskConical size={24} />
            </div>
          </CardContent>
        </Card>

        <Card hoverEffect>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Reference ET₀</p>
              <h4 className="text-xl font-bold text-slate-900 mt-1">4.82 mm/day</h4>
              <p className="text-xs text-slate-500 font-medium mt-1">FAO-56 Penman-Monteith</p>
            </div>
            <div className="w-12 h-12 rounded-xl bg-sky-50 text-sky-600 flex items-center justify-center">
              <Droplets size={24} />
            </div>
          </CardContent>
        </Card>

        <Card hoverEffect>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Microclimatic Risk</p>
              <h4 className="text-xl font-bold text-slate-900 mt-1">Moderate Risk</h4>
              <p className="text-xs text-rose-500 font-medium mt-1">Wheat Rust & Aphid alerts</p>
            </div>
            <div className="w-12 h-12 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center">
              <ShieldAlert size={24} />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Main Grid: Recommended Crops preview & Quick Actions */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Column: Top Recommended Crops Table */}
        <div className="lg:col-span-2">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Sprout size={18} className="text-agro-600" />
                <span>Crop Recommendation Engine (Top 5 Suitable)</span>
              </CardTitle>
              <Button variant="ghost" size="sm" onClick={() => setActiveTab('recommendation')}>
                View All Ranked Crops →
              </Button>
            </CardHeader>
            <CardContent className="p-0">
              <div className="overflow-x-auto">
                <table className="w-full text-left text-sm">
                  <thead className="bg-slate-50 text-slate-600 text-[11px] uppercase tracking-wider border-b border-slate-100">
                    <tr>
                      <th className="py-3 px-4">Rank</th>
                      <th className="py-3 px-4">Crop</th>
                      <th className="py-3 px-4">Category</th>
                      <th className="py-3 px-4">Suitability</th>
                      <th className="py-3 px-4">Est. Yield</th>
                      <th className="py-3 px-4">Net Margin</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {(results?.crop_rankings?.slice(0, 5) || [
                      { rank: 1, crop_name: 'Wheat (Sharbati)', category: 'Cereals', composite_suitability_score: 92.4, estimated_yield_ton_ha: 4.8, estimated_net_profit_usd_ha: 728.0 },
                      { rank: 2, crop_name: 'Chickpea (Gram)', category: 'Pulses', composite_suitability_score: 88.5, estimated_yield_ton_ha: 2.2, estimated_net_profit_usd_ha: 1016.0 },
                      { rank: 3, crop_name: 'Mustard & Rapeseed', category: 'Oilseeds', composite_suitability_score: 84.1, estimated_yield_ton_ha: 2.1, estimated_net_profit_usd_ha: 985.0 },
                      { rank: 4, crop_name: 'Potato (Jyoti)', category: 'Vegetables', composite_suitability_score: 79.8, estimated_yield_ton_ha: 28.5, estimated_net_profit_usd_ha: 4165.0 },
                      { rank: 5, crop_name: 'Barley', category: 'Cereals', composite_suitability_score: 76.2, estimated_yield_ton_ha: 3.8, estimated_net_profit_usd_ha: 416.0 },
                    ]).map((c: any) => (
                      <tr key={c.rank} className="hover:bg-slate-50/80 transition-colors">
                        <td className="py-3.5 px-4 font-bold text-slate-700">#{c.rank}</td>
                        <td className="py-3.5 px-4 font-semibold text-slate-900">{c.crop_name}</td>
                        <td className="py-3.5 px-4">
                          <span className="text-xs px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 font-medium">
                            {c.category}
                          </span>
                        </td>
                        <td className="py-3.5 px-4 font-bold text-agro-700">{c.composite_suitability_score}%</td>
                        <td className="py-3.5 px-4 text-slate-700">{c.estimated_yield_ton_ha} t/ha</td>
                        <td className="py-3.5 px-4 font-bold text-emerald-600">+${c.estimated_net_profit_usd_ha}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Right Column: Agronomic Action Center */}
        <div className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold flex items-center gap-2">
                <FlaskConical size={16} className="text-agro-600" />
                <span>Active Soil Sample ({currentSample.sample_code})</span>
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <div className="grid grid-cols-3 gap-2 text-center">
                <div className="p-2.5 rounded-lg bg-slate-50 border border-slate-100">
                  <p className="text-[10px] text-slate-400 font-bold uppercase">Nitrogen (N)</p>
                  <p className="text-base font-extrabold text-slate-800 mt-0.5">{currentSample.nitrogen_kg_ha}</p>
                  <p className="text-[10px] text-amber-600 font-medium">kg/ha (Medium)</p>
                </div>
                <div className="p-2.5 rounded-lg bg-slate-50 border border-slate-100">
                  <p className="text-[10px] text-slate-400 font-bold uppercase">Phosphorus (P)</p>
                  <p className="text-base font-extrabold text-slate-800 mt-0.5">{currentSample.phosphorus_kg_ha}</p>
                  <p className="text-[10px] text-emerald-600 font-medium">kg/ha (Adequate)</p>
                </div>
                <div className="p-2.5 rounded-lg bg-slate-50 border border-slate-100">
                  <p className="text-[10px] text-slate-400 font-bold uppercase">Potassium (K)</p>
                  <p className="text-base font-extrabold text-slate-800 mt-0.5">{currentSample.potassium_kg_ha}</p>
                  <p className="text-[10px] text-emerald-600 font-medium">kg/ha (Adequate)</p>
                </div>
              </div>

              <Button
                variant="outline"
                size="sm"
                className="w-full text-xs"
                onClick={() => setActiveTab('soil')}
              >
                Modify Soil Parameters & Test Wizard →
              </Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold flex items-center gap-2">
                <ShieldAlert size={16} className="text-rose-500" />
                <span>Epidemiological Alert</span>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-xs text-slate-600 leading-relaxed">
                Cool humid conditions (68% RH, night temp &lt;16°C) favor early yellow rust spore germination on wheat flag leaves.
              </p>
              <div className="mt-3 flex gap-2">
                <Button variant="danger" size="sm" className="text-xs" onClick={() => setActiveTab('pest')}>
                  View IPM Spray Roster
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};
