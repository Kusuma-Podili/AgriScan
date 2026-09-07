import React, { useState, useEffect } from 'react';
import { TrendingUp, ArrowUpRight, ArrowDownRight, DollarSign, Store } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/Card';
import { marketService } from '../../services/marketService';
import { MandiMarketPrice } from '../../types/market';

export const MandiMarketTicker: React.FC = () => {
  const [prices, setPrices] = useState<MandiMarketPrice[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchPrices = async () => {
      try {
        const res = await marketService.getMandiPrices();
        setPrices(res);
      } catch (err) {
        console.error('Failed to load market prices:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchPrices();
  }, []);

  return (
    <div className="space-y-6">
      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <TrendingUp size={22} className="text-emerald-600" />
            <span>Mandi Commodity Telemetry & Market Intelligence</span>
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            Real-time modal mandi prices, weekly price momentum, and commodity arrival volumes.
          </p>
        </div>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-sm font-bold flex items-center gap-2">
            <Store size={18} className="text-slate-500" />
            <span>APMC Regulated Market Rates (Current Arrivals)</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 uppercase tracking-wider border-b border-slate-100">
                <tr>
                  <th className="py-3 px-4">Commodity</th>
                  <th className="py-3 px-4">Market / Mandi</th>
                  <th className="py-3 px-4">State</th>
                  <th className="py-3 px-4">Modal Price ($/ton)</th>
                  <th className="py-3 px-4">Price Range</th>
                  <th className="py-3 px-4">7-Day Trend</th>
                  <th className="py-3 px-4">Daily Arrival</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {prices.map((p) => {
                  const isPositive = p.price_trend_7day_pct >= 0;
                  return (
                    <tr key={p.crop_id} className="hover:bg-slate-50/80 transition-colors">
                      <td className="py-3.5 px-4 font-bold text-slate-900">{p.commodity_name}</td>
                      <td className="py-3.5 px-4 text-slate-700 font-medium">{p.mandi_name}</td>
                      <td className="py-3.5 px-4 text-slate-500">{p.state}</td>
                      <td className="py-3.5 px-4 font-black text-slate-900">${p.modal_price_usd_per_ton}</td>
                      <td className="py-3.5 px-4 text-slate-500">
                        ${p.min_price_usd_per_ton} - ${p.max_price_usd_per_ton}
                      </td>
                      <td className="py-3.5 px-4">
                        <span
                          className={`inline-flex items-center gap-1 font-bold ${
                            isPositive ? 'text-emerald-600' : 'text-rose-600'
                          }`}
                        >
                          {isPositive ? <ArrowUpRight size={14} /> : <ArrowDownRight size={14} />}
                          {p.price_trend_7day_pct > 0 ? `+${p.price_trend_7day_pct}` : p.price_trend_7day_pct}%
                        </span>
                      </td>
                      <td className="py-3.5 px-4 text-slate-600 font-medium">{p.arrival_quantity_ton} Tons</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
