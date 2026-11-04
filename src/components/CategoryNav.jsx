import React, { useRef } from 'react';
import { 
  LayoutGrid, 
  Keyboard, 
  Laptop, 
  Smartphone,
  Monitor, 
  Armchair, 
  Headphones, 
  HardDrive,
  ChevronLeft,
  ChevronRight
} from 'lucide-react';

export default function CategoryNav({ selectedCategory, onSelectCategory, counts, selectedYear = '2026' }) {
  const scrollRef = useRef(null);

  const categories = [
    { id: 'all', label: 'All Gear', icon: LayoutGrid },
    { id: 'input', label: 'Keyboards & Mice', icon: Keyboard },
    { id: 'computer', label: 'Computers & Laptops', icon: Laptop },
    { id: 'mobile', label: 'Mobile & Tablets', icon: Smartphone },
    { id: 'monitor', label: 'Monitors', icon: Monitor },
    { id: 'furniture', label: 'Desks & Chairs', icon: Armchair },
    { id: 'audio', label: 'Audio & ANC', icon: Headphones },
    { id: 'network', label: 'Network & NAS', icon: HardDrive },
  ];

  const yearLabel = selectedYear === 'All' ? '2-Year Combined' : `${selectedYear} Leaderboard`;

  const scrollNav = (offset) => {
    if (scrollRef.current) {
      scrollRef.current.scrollBy({ left: offset, behavior: 'smooth' });
    }
  };

  return (
    <div className="space-y-2.5">
      {/* Category Nav Header with Active Year Indicator and Scroll Controls */}
      <div className="flex items-center justify-between px-1 text-xs">
        <div className="flex items-center gap-2">
          <span className="font-mono uppercase font-bold text-gray-400 text-[11px] tracking-wider">
            Categories ({categories.length - 1})
          </span>
          <span className="text-[11px] font-mono font-medium text-[#ff8533] bg-[#ff6600]/10 border border-[#ff6600]/25 px-2.5 py-0.5 rounded-full flex items-center gap-1.5 transition-all">
            <span className="w-1.5 h-1.5 rounded-full bg-[#ff6600] animate-pulse" />
            <span>{yearLabel}</span>
            <span className="text-gray-500">•</span>
            <span className="font-bold text-white">{counts ? counts.all : 0} items active</span>
          </span>
        </div>

        {/* Scroll Helper Buttons */}
        <div className="hidden sm:flex items-center gap-1 text-gray-400">
          <button
            onClick={() => scrollNav(-240)}
            className="p-1 hover:text-white hover:bg-gray-800/80 rounded-lg transition-colors cursor-pointer border border-gray-800"
            title="Scroll categories left"
          >
            <ChevronLeft className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => scrollNav(240)}
            className="p-1 hover:text-white hover:bg-gray-800/80 rounded-lg transition-colors cursor-pointer border border-gray-800"
            title="Scroll categories right"
          >
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* Category Buttons Bar - Single-row horizontal scroll, zero layout shifts */}
      <div
        ref={scrollRef}
        className="flex items-center gap-2 overflow-x-auto pb-1.5 scroll-smooth scrollbar-none no-scrollbar"
      >
        {categories.map((cat) => {
          const Icon = cat.icon;
          const isActive = selectedCategory === cat.id;
          const count = counts ? counts[cat.id] : 0;

          return (
            <button
              key={cat.id}
              onClick={() => onSelectCategory(cat.id)}
              className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all cursor-pointer border shrink-0 ${
                isActive
                  ? 'bg-[#ff6600] text-white border-[#ff6600] shadow-md shadow-[#ff6600]/25'
                  : 'bg-[#151924] hover:bg-[#1f2537] text-gray-300 hover:text-white border-gray-800/80 hover:border-gray-700'
              }`}
            >
              <Icon className="w-3.5 h-3.5 shrink-0" />
              <span>{cat.label}</span>
              {count !== undefined && count !== null && (
                <span
                  key={`${selectedYear}-${cat.id}-${count}`}
                  className={`text-[10px] px-1.5 py-0.5 rounded-md font-mono font-bold transition-all ${
                    isActive ? 'bg-black/30 text-white' : 'bg-gray-800 text-gray-300'
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
