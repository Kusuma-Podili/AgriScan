import React, { useState } from 'react';
import { ShieldAlert, Bug, Activity, AlertCircle, CheckCircle, ChevronDown } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Badge } from '../ui/Badge';
import { Button } from '../ui/Button';

interface ThreatItem {
  id: string;
  name: string;
  type: string;
  target: string;
  riskPct: number;
  status: 'Critical' | 'Warning' | 'Moderate' | 'Low';
  symptoms: string;
  biological: string;
  chemical: string;
}

export const PestDiagnosticCenter: React.FC = () => {
  const [threats] = useState<ThreatItem[]>([
    {
      id: 'wheat_rust',
      name: 'Wheat Stripe / Yellow Rust (Puccinia striiformis)',
      type: 'Fungus',
      target: 'Wheat, Barley',
      riskPct: 68.0,
      status: 'Warning',
      symptoms: 'Parallel rows of bright yellow pustules along leaf veins.',
      biological: 'Plant resistant multi-line cultivars with stacked Yr genes.',
      chemical: 'Propiconazole 25% EC @ 1.0 ml/L or Tebuconazole 25.9% EC @ 1.0 ml/L.',
    },
    {
      id: 'rice_blast',
      name: 'Rice Blast (Magnaporthe oryzae)',
      type: 'Fungus',
      target: 'Rice, Finger Millet',
      riskPct: 78.5,
      status: 'Critical',
      symptoms: 'Spindle-shaped lesions with ash-grey centers; black neck rot.',
      biological: 'Pseudomonas fluorescens seed treatment (10g/kg) and foliar spray.',
      chemical: 'Tricyclazole 75% WP @ 0.6 g/L or Nativo (Trifloxystrobin + Tebuconazole) @ 0.8 g/L.',
    },
    {
      id: 'pink_bollworm',
      name: 'Pink Bollworm (Pectinophora gossypiella)',
      type: 'Insect',
      target: 'Cotton',
      riskPct: 45.0,
      status: 'Moderate',
      symptoms: 'Rosette flowers, internal feeding in developing bolls.',
      biological: 'Trichogramma bactrae egg parasitoid @ 150,000/ha; gossyplure traps.',
      chemical: 'Profenofos 50% EC @ 2 ml/L or Spinosad 45% SC @ 0.35 ml/L.',
    },
    {
      id: 'fall_armyworm',
      name: 'Fall Armyworm (Spodoptera frugiperda)',
      type: 'Insect',
      target: 'Maize, Sorghum, Sugarcane',
      riskPct: 32.0,
      status: 'Moderate',
      symptoms: 'Window pane leaf damage with coarse sawdust-like frass in whorl.',
      biological: 'Metarhizium anisopliae or Nomuraea rileyi bio-fungus.',
      chemical: 'Chlorantraniliprole 18.5% SC @ 0.4 ml/L or Emamectin Benzoate 5% SG @ 0.45 g/L.',
    },
  ]);

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <ShieldAlert size={22} className="text-rose-600" />
            <span>Plant Pathology & Epidemiological Early Warning Radar</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            Microclimatic temperature-humidity infection indices and Integrated Pest Management (IPM) chemical rosters.
          </p>
        </div>

        <Badge variant="danger" size="md">
          2 Active Pathogen Alerts
        </Badge>
      </div>

      {/* Threats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
        {threats.map((t) => (
          <Card key={t.id} hoverEffect className={t.status === 'Critical' ? 'border-rose-300 ring-1 ring-rose-200' : ''}>
            <CardHeader className="pb-2">
              <div>
                <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">{t.type} Threat</span>
                <h3 className="text-base font-bold text-slate-900">{t.name}</h3>
                <p className="text-xs text-slate-500 mt-0.5">Target: {t.target}</p>
              </div>

              <div className="text-right">
                <span className={`text-xl font-black ${t.riskPct >= 70 ? 'text-rose-600' : (t.riskPct >= 40 ? 'text-amber-600' : 'text-slate-700')}`}>
                  {t.riskPct}%
                </span>
                <p className="text-[10px] text-slate-400 uppercase font-semibold">Infection Risk</p>
              </div>
            </CardHeader>

            <CardContent className="space-y-3 text-xs pt-2">
              <div className="p-2.5 bg-slate-50 rounded-lg">
                <span className="text-slate-500 font-bold block mb-0.5">Visible Diagnostics:</span>
                <span className="text-slate-700 leading-relaxed">{t.symptoms}</span>
              </div>

              <div className="p-2.5 bg-emerald-50 rounded-lg text-emerald-900">
                <span className="font-bold block mb-0.5">Biological / Cultural Action:</span>
                <span>{t.biological}</span>
              </div>

              <div className="p-2.5 bg-rose-50 rounded-lg text-rose-900">
                <span className="font-bold block mb-0.5">Chemical Intervention (ETL reached):</span>
                <span>{t.chemical}</span>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};
