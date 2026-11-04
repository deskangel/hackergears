import React from 'react';
import { Calendar, Flame, Trophy, Layers } from 'lucide-react';

export default function YearSelector({ selectedYear, onSelectYear }) {
  const options = [
    {
      id: '2026',
      label: '2026 Edition',
      subtitle: 'Latest discussions & trending hardware',
      icon: Flame,
      badge: 'Trending Now',
      badgeColor: 'bg-rose-500/10 text-rose-400 border-rose-500/20',
      itemCount: '24 Ranked'
    },
    {
      id: '2025',
      label: '2025 Annual',
      subtitle: 'Full year verified developer favorites',
      icon: Trophy,
      badge: 'Annual Benchmark',
      badgeColor: 'bg-amber-500/10 text-amber-400 border-amber-500/20',
      itemCount: '26 Ranked'
    },
    {
      id: 'All',
      label: 'Combined (2-Year)',
      subtitle: 'Aggregated unique author rankings',
      icon: Layers,
      badge: '2025 - 2026',
      badgeColor: 'bg-sky-500/10 text-sky-400 border-sky-500/20',
      itemCount: '26 Ranked'
    }
  ];

  return (
    <div className="bg-[#151924] border border-gray-800/90 rounded-2xl p-3.5 mb-6 shadow-xl">
      <div className="flex items-center justify-between mb-3 px-1">
        <div className="flex items-center gap-2">
          <Calendar className="w-4 h-4 text-[#ff6600]" />
          <span className="text-xs font-bold uppercase tracking-wider text-gray-400 font-mono">
            Edition / Time Window
          </span>
        </div>
        <span className="text-[11px] text-gray-400 hidden sm:inline">
          Partitioned by year to eliminate obsolete hardware contamination
        </span>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
        {options.map((opt) => {
          const Icon = opt.icon;
          const isActive = selectedYear === opt.id;
          return (
            <button
              key={opt.id}
              onClick={() => onSelectYear(opt.id)}
              className={`text-left p-3 rounded-xl border transition-all cursor-pointer flex flex-col justify-between ${
                isActive
                  ? 'bg-gradient-to-b from-[#1e2538] to-[#171d2b] border-[#ff6600]/60 ring-1 ring-[#ff6600]/40 shadow-lg shadow-[#ff6600]/5'
                  : 'bg-[#10131d]/60 border-gray-800/80 hover:bg-[#1a202f] hover:border-gray-700 text-gray-400'
              }`}
            >
              <div className="flex items-center justify-between mb-1.5">
                <div className="flex items-center gap-2">
                  <Icon className={`w-4 h-4 ${isActive ? 'text-[#ff6600]' : 'text-gray-500'}`} />
                  <span className={`font-bold text-sm ${isActive ? 'text-white' : 'text-gray-300'}`}>
                    {opt.label}
                  </span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className={`text-[10px] font-mono px-1.5 py-0.5 rounded font-bold ${
                    isActive ? 'bg-[#ff6600]/20 text-[#ff8533] border border-[#ff6600]/30' : 'bg-gray-800/80 text-gray-400'
                  }`}>
                    {opt.itemCount}
                  </span>
                  <span className={`text-[10px] font-mono px-2 py-0.5 rounded-full border ${opt.badgeColor}`}>
                    {opt.badge}
                  </span>
                </div>
              </div>
              <p className="text-xs text-gray-400">
                {opt.subtitle}
              </p>
            </button>
          );
        })}
      </div>
    </div>
  );
}
