import React, { useState } from 'react';
import {
  Sprout,
  Filter,
  CheckCircle2,
  TrendingUp,
  AlertTriangle,
  FileText,
  DollarSign,
  ChevronRight,
  Info,
} from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Button } from '../ui/Button';
import { Badge } from '../ui/Badge';
import { Modal } from '../ui/Modal';
import { useRecommendationStore } from '../../stores/useRecommendationStore';
import { useSoilStore } from '../../stores/useSoilStore';
import { recommendationService } from '../../services/recommendationService';
import { CompositeRecommendation } from '../../types/recommendation';

export const RecommendationStudio: React.FC = () => {
  const { queryParams, setQueryParams, results, setResults, selectedCrop, setSelectedCrop, isGenerating, setIsGenerating } =
    useRecommendationStore();
  const { currentSample } = useSoilStore();

  const [filterCategory, setFilterCategory] = useState<string>('');
  const [detailModalOpen, setDetailModalOpen] = useState<boolean>(false);

  const handleRunRecommendation = async () => {
    setIsGenerating(true);
    try {
      const response = await recommendationService.runRecommendation({
        ...queryParams,
        n_kg_ha: currentSample.nitrogen_kg_ha,
        p_kg_ha: currentSample.phosphorus_kg_ha,
        k_kg_ha: currentSample.potassium_kg_ha,
        ph: currentSample.ph,
        organic_carbon_pct: currentSample.organic_carbon_pct,
        ec_ds_m: currentSample.electrical_conductivity_ds_m,
        category_filter: filterCategory || undefined,
      });
      setResults(response);
    } catch (err) {
      console.error('Failed to run recommendation:', err);
    } finally {
      setIsGenerating(false);
    }
  };

  const handleOpenCropDetail = (crop: CompositeRecommendation) => {
    setSelectedCrop(crop);
    setDetailModalOpen(true);
  };

  const categories = [
    'All Categories',
    'Cereals',
    'Pulses',
    'Oilseeds',
    'Commercial',
    'Spices',
    'Vegetables',
    'Fruits',
    'Plantation',
    'Fodder',
  ];

  return (
    <div className="space-y-6">
      {/* Header bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Sprout size={22} className="text-agro-600" />
            <span>Multi-Model Crop Recommendation Studio</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            Hybrid soft-voting ensemble (Random Forest, Gradient Boosting, Deep MLP) & FAO EcoCrop laws.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={filterCategory}
            onChange={(e) => setFilterCategory(e.target.value === 'All Categories' ? '' : e.target.value)}
            className="text-xs font-medium bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-slate-700 focus:outline-none focus:ring-2 focus:ring-agro-500"
          >
            {categories.map((c) => (
              <option key={c} value={c === 'All Categories' ? '' : c}>
                {c}
              </option>
            ))}
          </select>

          <Button
            variant="primary"
            onClick={handleRunRecommendation}
            isLoading={isGenerating}
            icon={<Sprout size={16} />}
          >
            Generate Advisory
          </Button>
        </div>
      </div>

      {/* Recommended Crops Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {(results?.crop_rankings || []).map((crop) => {
          const isTop = crop.rank === 1;

          return (
            <Card
              key={crop.crop_id}
              hoverEffect
              className={`relative flex flex-col justify-between ${
                isTop ? 'ring-2 ring-agro-600 border-agro-300' : ''
              }`}
            >
              {isTop && (
                <div className="absolute -top-3 left-4 bg-agro-600 text-white text-[10px] font-bold px-2.5 py-0.5 rounded-full shadow-sm flex items-center gap-1">
                  <CheckCircle2 size={12} />
                  <span>Optimal Fit (#1)</span>
                </div>
              )}

              <CardContent className="p-5 space-y-4">
                {/* Header info */}
                <div className="flex items-start justify-between">
                  <div>
                    <span className="text-[11px] font-bold text-slate-400">Rank #{crop.rank}</span>
                    <h3 className="text-lg font-bold text-slate-900 mt-0.5">{crop.crop_name}</h3>
                    <Badge variant="neutral" size="sm" className="mt-1">
                      {crop.category}
                    </Badge>
                  </div>

                  <div className="text-right">
                    <span className="text-2xl font-black text-agro-700">
                      {crop.composite_suitability_score}%
                    </span>
                    <p className="text-[10px] text-slate-400 uppercase font-semibold">Suitability</p>
                  </div>
                </div>

                {/* Metrics Breakdown */}
                <div className="grid grid-cols-2 gap-2 pt-2 border-t border-slate-100 text-xs">
                  <div className="bg-slate-50 p-2.5 rounded-lg">
                    <span className="text-slate-400 text-[10px] font-medium block">Projected Yield</span>
                    <span className="font-bold text-slate-800 text-sm mt-0.5 block">
                      {crop.estimated_yield_ton_ha} t/ha
                    </span>
                  </div>
                  <div className="bg-emerald-50 p-2.5 rounded-lg">
                    <span className="text-emerald-600 text-[10px] font-medium block">Net Margin</span>
                    <span className="font-bold text-emerald-800 text-sm mt-0.5 block">
                      +${crop.estimated_net_profit_usd_ha}/ha
                    </span>
                  </div>
                </div>

                {/* Limiting Constraint */}
                <div className="text-xs flex items-center gap-2 p-2 bg-slate-50/80 rounded-lg text-slate-600">
                  <Info size={14} className="shrink-0 text-slate-400" />
                  <span className="truncate">Limit: {crop.primary_limiting_factor}</span>
                </div>
              </CardContent>

              {/* Action footer */}
              <div className="p-4 pt-0 border-t border-slate-100 flex items-center justify-between">
                <span className="text-[11px] font-semibold text-slate-500">
                  ROI: {crop.economic_roi_pct}%
                </span>
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => handleOpenCropDetail(crop)}
                  icon={<ChevronRight size={14} />}
                >
                  View Agronomic Dossier
                </Button>
              </div>
            </Card>
          );
        })}
      </div>

      {/* Modal: Full Agronomic Crop Detail */}
      {selectedCrop && (
        <Modal
          isOpen={detailModalOpen}
          onClose={() => setDetailModalOpen(false)}
          title={`Agronomic Dossier: ${selectedCrop.crop_name}`}
          maxWidth="2xl"
        >
          <div className="space-y-5 text-sm">
            <div className="flex items-center justify-between p-4 bg-agro-50 rounded-xl border border-agro-100">
              <div>
                <p className="text-xs font-semibold text-agro-800">Suitability Classification</p>
                <p className="text-lg font-bold text-agro-900 mt-0.5">{selectedCrop.fao_suitability_class}</p>
              </div>
              <div className="text-right">
                <p className="text-xs font-semibold text-agro-800">ML Confidence</p>
                <p className="text-lg font-bold text-agro-900 mt-0.5">{selectedCrop.ml_confidence_pct}%</p>
              </div>
            </div>

            <div>
              <h4 className="font-bold text-slate-800 mb-2">Economics & Revenue Potential</h4>
              <div className="grid grid-cols-3 gap-3 text-center">
                <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                  <p className="text-[11px] text-slate-500 font-medium">Cultivation Cost</p>
                  <p className="text-base font-bold text-slate-800 mt-1">${selectedCrop.estimated_cultivation_cost_usd_ha}</p>
                </div>
                <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                  <p className="text-[11px] text-slate-500 font-medium">Gross Revenue</p>
                  <p className="text-base font-bold text-slate-800 mt-1">${selectedCrop.estimated_gross_revenue_usd_ha}</p>
                </div>
                <div className="p-3 bg-emerald-50 rounded-lg border border-emerald-200">
                  <p className="text-[11px] text-emerald-700 font-medium">Estimated Net Return</p>
                  <p className="text-base font-bold text-emerald-800 mt-1">+${selectedCrop.estimated_net_profit_usd_ha}</p>
                </div>
              </div>
            </div>

            <div>
              <h4 className="font-bold text-slate-800 mb-1">Agronomic Cultivation Guidance</h4>
              <p className="text-xs text-slate-600 leading-relaxed p-3.5 bg-slate-50 rounded-xl border border-slate-200">
                {selectedCrop.agronomic_advisory}
              </p>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
};
