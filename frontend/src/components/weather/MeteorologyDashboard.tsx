import React, { useState, useEffect } from 'react';
import { CloudSun, Wind, Droplets, Sun, AlertTriangle, Clock } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { Badge } from '../ui/Badge';
import { weatherService } from '../../services/weatherService';
import { WeatherCurrentResponse, IrrigationAdvisoryResponse } from '../../types/weather';

export const MeteorologyDashboard: React.FC = () => {
  const [weather, setWeather] = useState<WeatherCurrentResponse | null>(null);
  const [irrigation, setIrrigation] = useState<IrrigationAdvisoryResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [wRes, iRes] = await Promise.all([
          weatherService.getCurrentWeather(21.1458, 79.0882),
          weatherService.getIrrigationAdvisory('wheat', 'mid', 22.0),
        ]);
        setWeather(wRes);
        setIrrigation(iRes);
      } catch (err) {
        console.error('Weather load error:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <CloudSun size={22} className="text-amber-500" />
            <span>Agro-Meteorology & Evapotranspiration Station</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            FAO-56 Penman-Monteith daily reference ET₀ and stage-wise crop water requirement (ETc).
          </p>
        </div>

        {weather && (
          <div className="flex items-center gap-2 text-xs font-semibold bg-agro-50 text-agro-800 px-3 py-1.5 rounded-lg border border-agro-200">
            <Clock size={14} />
            <span>Updated: {new Date(weather.observed_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
          </div>
        )}
      </div>

      {weather && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Current Microclimate */}
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-bold">Ambient Atmospheric State</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="text-center p-4 bg-slate-50 rounded-xl">
                <span className="text-4xl font-extrabold text-slate-900">{weather.temperature_c}°C</span>
                <p className="text-xs text-slate-500 mt-1 font-medium">{weather.condition}</p>
                <div className="flex justify-center gap-4 mt-3 text-xs text-slate-600">
                  <span>Max: {weather.temp_max_c}°C</span>
                  <span>Min: {weather.temp_min_c}°C</span>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3 text-xs">
                <div className="p-3 bg-slate-50 rounded-lg flex items-center gap-2.5">
                  <Droplets size={16} className="text-sky-500" />
                  <div>
                    <span className="text-slate-400 block text-[10px]">Humidity</span>
                    <span className="font-bold text-slate-800">{weather.humidity_pct}%</span>
                  </div>
                </div>

                <div className="p-3 bg-slate-50 rounded-lg flex items-center gap-2.5">
                  <Wind size={16} className="text-slate-400" />
                  <div>
                    <span className="text-slate-400 block text-[10px]">Wind Speed</span>
                    <span className="font-bold text-slate-800">{weather.wind_speed_m_s} m/s</span>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Irrigation & Water Deficit */}
          {irrigation && (
            <Card>
              <CardHeader>
                <CardTitle className="text-sm font-bold">Crop Evapotranspiration (ETc)</CardTitle>
                <Badge variant={irrigation.irrigation_urgency === 'Critical' ? 'danger' : 'warning'} size="sm">
                  {irrigation.irrigation_urgency}
                </Badge>
              </CardHeader>
              <CardContent className="space-y-4 text-xs">
                <div className="p-3.5 bg-sky-50 rounded-xl border border-sky-100 space-y-2">
                  <div className="flex justify-between">
                    <span className="text-slate-600">Reference ET₀:</span>
                    <span className="font-bold text-slate-900">{irrigation.current_et0_mm_day} mm/day</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-600">Crop Coefficient (Kc):</span>
                    <span className="font-bold text-slate-900">{irrigation.crop_coefficient_kc}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-600">Actual Crop ETc:</span>
                    <span className="font-bold text-sky-800">{irrigation.crop_evapotranspiration_etc_mm_day} mm/day</span>
                  </div>
                  <div className="flex justify-between pt-1 border-t border-sky-200 font-bold text-sky-950">
                    <span>Net Irrigation Deficit:</span>
                    <span>{irrigation.net_irrigation_depth_mm} mm</span>
                  </div>
                </div>

                <div className="p-3 bg-slate-50 rounded-lg text-center">
                  <span className="text-slate-500 block text-[11px]">Recommended Drip Runtime</span>
                  <span className="text-xl font-black text-slate-900 mt-1 block">
                    {irrigation.recommended_drip_runtime_hours} Hours
                  </span>
                  <span className="text-[10px] text-slate-400">at 2.5 mm/hr dripper discharge</span>
                </div>
              </CardContent>
            </Card>
          )}

          {/* 7-Day Forecast */}
          <Card className="lg:col-span-1">
            <CardHeader>
              <CardTitle className="text-sm font-bold">7-Day Meteorological Trajectory</CardTitle>
            </CardHeader>
            <CardContent className="p-0">
              <div className="divide-y divide-slate-100 text-xs max-h-72 overflow-y-auto">
                {weather.forecast_7day.map((d, i) => (
                  <div key={i} className="p-3 px-4 flex items-center justify-between hover:bg-slate-50">
                    <div>
                      <span className="font-semibold text-slate-800 block">{d.forecast_date}</span>
                      <span className="text-[11px] text-slate-400">{d.condition_summary}</span>
                    </div>
                    <div className="text-right">
                      <span className="font-bold text-slate-900">{d.temp_max_c}° / {d.temp_min_c}°</span>
                      <span className="text-[10px] text-sky-600 block">{d.expected_rainfall_mm} mm rain</span>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  );
};
