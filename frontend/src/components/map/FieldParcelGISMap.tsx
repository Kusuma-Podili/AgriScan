import React, { useState } from 'react';
import { Map, Layers, Plus, Info, Check, MapPin } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Button } from '../ui/Button';
import { Badge } from '../ui/Badge';

interface MockParcel {
  id: string;
  name: string;
  area_ha: number;
  crop: string;
  soil_ph: number;
  npk_status: string;
  color: string;
}

export const FieldParcelGISMap: React.FC = () => {
  const [parcels] = useState<MockParcel[]>([
    { id: 'p1', name: 'North Field Block A', area_ha: 4.2, crop: 'Wheat (Sharbati)', soil_ph: 6.8, npk_status: 'Adequate', color: '#4e9f40' },
    { id: 'p2', name: 'East Terraced Plot B', area_ha: 2.8, crop: 'Chickpea (Desi)', soil_ph: 7.1, npk_status: 'Low Nitrogen', color: '#b48d64' },
    { id: 'p3', name: 'South Lowland Basin C', area_ha: 5.5, crop: 'Mustard', soil_ph: 7.4, npk_status: 'High Potash', color: '#eab308' },
    { id: 'p4', name: 'Riverbed Alluvial Plot D', area_ha: 3.1, crop: 'Potato (Jyoti)', soil_ph: 6.2, npk_status: 'Optimum', color: '#0284c7' },
  ]);

  const [selectedParcel, setSelectedParcel] = useState<MockParcel>(parcels[0]);
  const [activeLayer, setActiveLayer] = useState<'satellite' | 'soil_ph' | 'moisture'>('satellite');

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Map size={22} className="text-agro-600" />
            <span>GIS Field Boundary & Soil Spatial Mapper</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            GeoJSON polygon boundaries with NDVI satellite overlays and parcel-level crop tracking.
          </p>
        </div>

        <div className="flex items-center gap-2">
          <div className="bg-slate-100 p-1 rounded-lg flex text-xs font-semibold text-slate-600">
            <button
              onClick={() => setActiveLayer('satellite')}
              className={`px-3 py-1 rounded-md transition-colors ${activeLayer === 'satellite' ? 'bg-white shadow-xs text-slate-900' : ''}`}
            >
              Satellite
            </button>
            <button
              onClick={() => setActiveLayer('soil_ph')}
              className={`px-3 py-1 rounded-md transition-colors ${activeLayer === 'soil_ph' ? 'bg-white shadow-xs text-slate-900' : ''}`}
            >
              Soil pH Heatmap
            </button>
            <button
              onClick={() => setActiveLayer('moisture')}
              className={`px-3 py-1 rounded-md transition-colors ${activeLayer === 'moisture' ? 'bg-white shadow-xs text-slate-900' : ''}`}
            >
              Soil Moisture
            </button>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Interactive Map Visualizer (SVG-based vector GIS canvas) */}
        <div className="lg:col-span-2">
          <Card className="overflow-hidden">
            <div className="relative w-full h-96 bg-slate-900 flex items-center justify-center">
              {/* GIS Vector Map Simulation */}
              <svg className="w-full h-full p-8" viewBox="0 0 600 400">
                {/* Background terrain grid lines */}
                <defs>
                  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" strokeWidth="0.5" strokeOpacity="0.4" />
                  </pattern>
                </defs>
                <rect width="100%" height="100%" fill="url(#grid)" />

                {/* Parcel 1 */}
                <polygon
                  points="60,60 260,80 230,220 70,190"
                  fill={activeLayer === 'soil_ph' ? '#72ba65' : '#306627'}
                  fillOpacity={selectedParcel.id === 'p1' ? '0.85' : '0.55'}
                  stroke="#ffffff"
                  strokeWidth={selectedParcel.id === 'p1' ? '3' : '1.5'}
                  className="cursor-pointer transition-all hover:fill-opacity-80"
                  onClick={() => setSelectedParcel(parcels[0])}
                />
                <text x="130" y="140" fill="#ffffff" fontSize="13" fontWeight="bold">Block A (4.2 ha)</text>

                {/* Parcel 2 */}
                <polygon
                  points="270,90 480,70 450,210 240,230"
                  fill={activeLayer === 'soil_ph' ? '#a37754' : '#885f44'}
                  fillOpacity={selectedParcel.id === 'p2' ? '0.85' : '0.55'}
                  stroke="#ffffff"
                  strokeWidth={selectedParcel.id === 'p2' ? '3' : '1.5'}
                  className="cursor-pointer transition-all hover:fill-opacity-80"
                  onClick={() => setSelectedParcel(parcels[1])}
                />
                <text x="330" y="150" fill="#ffffff" fontSize="13" fontWeight="bold">Plot B (2.8 ha)</text>

                {/* Parcel 3 */}
                <polygon
                  points="80,210 240,240 210,350 90,340"
                  fill={activeLayer === 'soil_ph' ? '#eab308' : '#ca8a04'}
                  fillOpacity={selectedParcel.id === 'p3' ? '0.85' : '0.55'}
                  stroke="#ffffff"
                  strokeWidth={selectedParcel.id === 'p3' ? '3' : '1.5'}
                  className="cursor-pointer transition-all hover:fill-opacity-80"
                  onClick={() => setSelectedParcel(parcels[2])}
                />
                <text x="120" y="280" fill="#ffffff" fontSize="13" fontWeight="bold">Plot C (5.5 ha)</text>

                {/* Parcel 4 */}
                <polygon
                  points="250,250 510,230 480,360 220,370"
                  fill={activeLayer === 'soil_ph' ? '#0284c7' : '#0369a1'}
                  fillOpacity={selectedParcel.id === 'p4' ? '0.85' : '0.55'}
                  stroke="#ffffff"
                  strokeWidth={selectedParcel.id === 'p4' ? '3' : '1.5'}
                  className="cursor-pointer transition-all hover:fill-opacity-80"
                  onClick={() => setSelectedParcel(parcels[3])}
                />
                <text x="340" y="310" fill="#ffffff" fontSize="13" fontWeight="bold">Plot D (3.1 ha)</text>
              </svg>

              {/* Map overlay controls */}
              <div className="absolute bottom-4 left-4 bg-slate-900/80 backdrop-blur-md px-3 py-2 rounded-lg border border-slate-700 text-white text-xs space-y-1">
                <p className="font-semibold flex items-center gap-1.5">
                  <MapPin size={12} className="text-agro-400" />
                  <span>Coordinates: 21°08'44.8"N 79°05'17.5"E</span>
                </p>
                <p className="text-[10px] text-slate-400">Total Holding Area: 15.6 Hectares (38.5 Acres)</p>
              </div>
            </div>
          </Card>
        </div>

        {/* Parcel Inspector Side Panel */}
        <div>
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold">Parcel Attributes Inspector</CardTitle>
              <Badge variant="primary">{selectedParcel.name}</Badge>
            </CardHeader>
            <CardContent className="space-y-4 text-xs">
              <div className="space-y-2.5">
                <div className="flex justify-between p-2.5 bg-slate-50 rounded-lg">
                  <span className="text-slate-500">Surface Area:</span>
                  <span className="font-bold text-slate-800">{selectedParcel.area_ha} Hectares</span>
                </div>

                <div className="flex justify-between p-2.5 bg-slate-50 rounded-lg">
                  <span className="text-slate-500">Current Crop:</span>
                  <span className="font-bold text-agro-800">{selectedParcel.crop}</span>
                </div>

                <div className="flex justify-between p-2.5 bg-slate-50 rounded-lg">
                  <span className="text-slate-500">Soil Reaction (pH):</span>
                  <span className="font-bold text-slate-800">{selectedParcel.soil_ph}</span>
                </div>

                <div className="flex justify-between p-2.5 bg-slate-50 rounded-lg">
                  <span className="text-slate-500">Nutrient Status:</span>
                  <span className="font-bold text-slate-800">{selectedParcel.npk_status}</span>
                </div>
              </div>

              <div className="pt-2">
                <Button variant="outline" size="sm" className="w-full text-xs">
                  Export Parcel GeoJSON Boundary
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};
