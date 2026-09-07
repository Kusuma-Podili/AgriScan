import React from 'react';
import {
  LayoutDashboard,
  FlaskConical,
  Sprout,
  Sliders,
  Map,
  Beaker,
  CloudSun,
  ShieldAlert,
  TrendingUp,
  FileSpreadsheet,
} from 'lucide-react';
import { useAppStore, ActiveTab } from '../../stores/useAppStore';

interface NavItem {
  id: ActiveTab;
  label: string;
  icon: React.ReactNode;
  badge?: string;
}

export const Sidebar: React.FC = () => {
  const { activeTab, setActiveTab } = useAppStore();

  const navItems: NavItem[] = [
    { id: 'dashboard', label: 'Overview Dashboard', icon: <LayoutDashboard size={18} /> },
    { id: 'recommendation', label: 'Crop Recommendation', icon: <Sprout size={18} />, badge: 'AI ML' },
    { id: 'soil', label: 'Soil Health & Tests', icon: <FlaskConical size={18} /> },
    { id: 'simulator', label: 'What-If Simulator', icon: <Sliders size={18} /> },
    { id: 'fertilizer', label: 'SSNM Fertilizer Balancer', icon: <Beaker size={18} /> },
    { id: 'weather', label: 'Agro-Meteorology & ET₀', icon: <CloudSun size={18} /> },
    { id: 'map', label: 'GIS Field Mapping', icon: <Map size={18} /> },
    { id: 'pest', label: 'Pest & Disease Radar', icon: <ShieldAlert size={18} />, badge: 'Alerts' },
    { id: 'market', label: 'Mandi Market Trends', icon: <TrendingUp size={18} /> },
    { id: 'reports', label: 'Advisory Dossier Export', icon: <FileSpreadsheet size={18} /> },
  ];

  return (
    <aside className="w-64 bg-white border-r border-slate-200 shrink-0 hidden md:flex flex-col min-h-[calc(100vh-4rem)]">
      <div className="p-4 space-y-1">
        <p className="px-3 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">
          Agronomic Intelligence
        </p>

        {navItems.map((item) => {
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium transition-all ${
                isActive
                  ? 'bg-agro-50 text-agro-800 font-semibold border-l-4 border-agro-600 rounded-l-none'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
              }`}
            >
              <div className="flex items-center gap-3">
                <span className={isActive ? 'text-agro-600' : 'text-slate-400'}>{item.icon}</span>
                <span>{item.label}</span>
              </div>
              {item.badge && (
                <span
                  className={`px-1.5 py-0.5 text-[10px] font-bold rounded ${
                    isActive ? 'bg-agro-200 text-agro-900' : 'bg-slate-100 text-slate-600'
                  }`}
                >
                  {item.badge}
                </span>
              )}
            </button>
          );
        })}
      </div>

      <div className="mt-auto p-4 border-t border-slate-100">
        <div className="p-3 bg-slate-50 rounded-xl border border-slate-200/80">
          <p className="text-xs font-bold text-slate-800">120+ Crops Catalog</p>
          <p className="text-[11px] text-slate-500 mt-0.5">
            FAO-56 & EcoCrop models with multi-model ML ensemble.
          </p>
        </div>
      </div>
    </aside>
  );
};
