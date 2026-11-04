import React from 'react';
import { LayoutGrid, Keyboard, Mouse, Monitor, Armchair, Laptop } from 'lucide-react';

export default function CategoryNav({ selectedCategory, onSelectCategory, counts, selectedYear = '2026' }) {
  const categories = [
    { id: 'all', label: 'All Gear', icon: LayoutGrid },
    { id: 'keyboard', label: 'Keyboards', icon: Keyboard },
    { id: 'mouse', label: 'Mice & Trackballs', icon: Mouse },
    { id: 'monitor', label: 'Monitors', icon: Monitor },
    { id: 'chair', label: 'Ergonomic Chairs', icon: Armchair },
    { id: 'laptop', label: 'Laptops', icon: Laptop },
  ];

  const yearLabel = selectedYear === 'All' ? '2-Year Combined' : `${selectedYear} Leaderboard`;

  return (
    <div className="space-y-2.5">
      {/* Category Nav Header with Active Year Indicator */}
      <div className="flex items-center justify-between px-1 text-xs">
        <div className="flex items-center gap-2">
          <span className="font-mono uppercase font-bold text-gray-400 text-[11px] tracking-wider">
            Categories
          </span>
          <span className="text-[11px] font-mono font-medium text-[#ff8533] bg-[#ff6600]/10 border border-[#ff6600]/25 px-2.5 py-0.5 rounded-full flex items-center gap-1.5 transition-all">
            <span className="w-1.5 h-1.5 rounded-full bg-[#ff6600] animate-pulse" />
            <span>{yearLabel}</span>
            <span className="text-gray-500">•</span>
            <span className="font-bold text-white">{counts ? counts.all : 0} items active</span>
          </span>
        </div>
      </div>

      {/* Category Buttons Bar */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none no-scrollbar">
        {categories.map((cat) => {
          const Icon = cat.icon;
          const isActive = selectedCategory === cat.id;
          const count = counts ? counts[cat.id] : 0;

          return (
            <button
              key={cat.id}
              onClick={() => onSelectCategory(cat.id)}
              className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all cursor-pointer ${
                isActive
                  ? 'bg-[#ff6600] text-white shadow-md shadow-[#ff6600]/25'
                  : 'bg-[#151924] hover:bg-[#1f2537] text-gray-300 hover:text-white border border-gray-800'
              }`}
            >
              <Icon className="w-3.5 h-3.5" />
              <span>{cat.label}</span>
              {count !== undefined && count !== null && (
                <span
                  key={`${selectedYear}-${cat.id}-${count}`}
                  className={`text-[10px] px-1.5 py-0.2 rounded-md font-mono transition-all animate-in fade-in duration-200 ${
                    isActive ? 'bg-black/25 text-white' : 'bg-gray-800 text-gray-300 font-bold'
                  }`}
                >
                  {count}
                </span>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
