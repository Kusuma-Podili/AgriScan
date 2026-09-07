import React from 'react';

interface SliderProps {
  label: string;
  value: number;
  min: number;
  max: number;
  step?: number;
  unit?: string;
  onChange: (val: number) => void;
  helperText?: string;
  className?: string;
}

export const Slider: React.FC<SliderProps> = ({
  label,
  value,
  min,
  max,
  step = 1,
  unit = '',
  onChange,
  helperText,
  className = '',
}) => {
  return (
    <div className={`space-y-1.5 ${className}`}>
      <div className="flex justify-between items-center text-sm">
        <label className="font-medium text-slate-700">{label}</label>
        <span className="font-semibold text-slate-900 bg-slate-100 px-2 py-0.5 rounded text-xs">
          {value} {unit}
        </span>
      </div>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
        className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-agro-600 focus:outline-none focus:ring-2 focus:ring-agro-500/30"
      />
      {helperText && <p className="text-[11px] text-slate-500">{helperText}</p>}
    </div>
  );
};
