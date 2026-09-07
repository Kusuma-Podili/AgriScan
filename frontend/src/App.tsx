import React, { useEffect } from 'react';
import { Navbar } from './components/layout/Navbar';
import { Sidebar } from './components/layout/Sidebar';
import { DashboardOverview } from './components/dashboard/DashboardOverview';
import { RecommendationStudio } from './components/recommendation/RecommendationStudio';
import { SoilInputWizard } from './components/soil/SoilInputWizard';
import { WhatIfClimateSimulator } from './components/simulator/WhatIfClimateSimulator';
import { SSNMFormulationCalculator } from './components/fertilizer/SSNMFormulationCalculator';
import { MeteorologyDashboard } from './components/weather/MeteorologyDashboard';
import { FieldParcelGISMap } from './components/map/FieldParcelGISMap';
import { PestDiagnosticCenter } from './components/pest/PestDiagnosticCenter';
import { MandiMarketTicker } from './components/market/MandiMarketTicker';
import { AdvisoryReportDossier } from './components/reports/AdvisoryReportDossier';
import { useAppStore } from './stores/useAppStore';
import { useRecommendationStore } from './stores/useRecommendationStore';
import { recommendationService } from './services/recommendationService';

export const App: React.FC = () => {
  const { activeTab } = useAppStore();
  const { results, setResults, queryParams } = useRecommendationStore();

  // Initial recommendation hydration on boot
  useEffect(() => {
    if (!results) {
      recommendationService
        .runRecommendation(queryParams)
        .then((data) => setResults(data))
        .catch((err) => console.log('Initial recommendation load:', err));
    }
  }, []);

  const renderActiveView = () => {
    switch (activeTab) {
      case 'dashboard':
        return <DashboardOverview />;
      case 'recommendation':
        return <RecommendationStudio />;
      case 'soil':
        return <SoilInputWizard />;
      case 'simulator':
        return <WhatIfClimateSimulator />;
      case 'fertilizer':
        return <SSNMFormulationCalculator />;
      case 'weather':
        return <MeteorologyDashboard />;
      case 'map':
        return <FieldParcelGISMap />;
      case 'pest':
        return <PestDiagnosticCenter />;
      case 'market':
        return <MandiMarketTicker />;
      case 'reports':
        return <AdvisoryReportDossier />;
      default:
        return <DashboardOverview />;
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col">
      <Navbar />

      <div className="flex-1 flex max-w-7xl w-full mx-auto">
        <Sidebar />

        <main className="flex-1 p-4 sm:p-6 lg:p-8 max-w-full overflow-x-hidden">
          {renderActiveView()}
        </main>
      </div>

      <footer className="bg-white border-t border-slate-200 py-6 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <p>© 2026 AgroPulse Precision Agriculture Platform. Built with FAO-56 and Multi-Model ML Ensemble.</p>
          <div className="flex gap-4">
            <span className="hover:text-slate-800 cursor-pointer">Agronomic Monograph</span>
            <span className="hover:text-slate-800 cursor-pointer">API OpenAPI Docs</span>
            <span className="hover:text-slate-800 cursor-pointer">Security & RBAC</span>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default App;
