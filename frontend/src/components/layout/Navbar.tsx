import React from 'react';
import { Sprout, Bell, CloudSun, User, RefreshCw } from 'lucide-react';
import { useAppStore } from '../../stores/useAppStore';

export const Navbar: React.FC = () => {
  const { activeTab, setActiveTab } = useAppStore();

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-xs">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => setActiveTab('dashboard')}>
            <div className="w-10 h-10 rounded-xl bg-linear-to-br from-agro-500 to-agro-700 flex items-center justify-center text-white shadow-sm shadow-agro-500/20">
              <Sprout size={24} className="stroke-[2.5]" />
            </div>
            <div>
              <span className="text-xl font-extrabold tracking-tight bg-linear-to-r from-agro-800 to-agro-600 bg-clip-text text-transparent">
                AgroPulse
              </span>
              <span className="hidden sm:inline-block ml-2 text-[10px] font-bold tracking-wider uppercase px-1.5 py-0.5 rounded bg-agro-100 text-agro-800">
                Precision Intelligence v1.0
              </span>
            </div>
          </div>

          {/* Quick Metrics & Actions */}
          <div className="flex items-center gap-4">
            {/* Live Weather Widget preview */}
            <div
              onClick={() => setActiveTab('weather')}
              className="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 border border-slate-200 text-xs font-medium text-slate-700 cursor-pointer transition-colors"
            >
              <CloudSun size={16} className="text-amber-500" />
              <span>28.5°C</span>
              <span className="text-slate-300">|</span>
              <span>ET₀: 4.8 mm/d</span>
            </div>

            {/* Notification Bell */}
            <button
              onClick={() => setActiveTab('pest')}
              className="relative p-2 rounded-lg text-slate-500 hover:text-slate-700 hover:bg-slate-100 transition-colors"
              title="Agricultural Alerts"
            >
              <Bell size={20} />
              <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-rose-500 ring-2 ring-white animate-pulse" />
            </button>

            {/* User Profile avatar */}
            <div className="flex items-center gap-2 pl-2 border-l border-slate-200">
              <div className="w-8 h-8 rounded-full bg-agro-100 text-agro-700 flex items-center justify-center font-bold text-xs border border-agro-200">
                <User size={16} />
              </div>
              <div className="hidden lg:block text-left">
                <p className="text-xs font-bold text-slate-800 leading-none">Central Farm Parcel A</p>
                <p className="text-[10px] text-slate-500 leading-none mt-0.5">Lead Agronomist</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
