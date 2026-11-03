import React from 'react';
import { LayoutGrid, Keyboard, Mouse, Monitor, Armchair, Laptop } from 'lucide-react';

export default function CategoryNav({ selectedCategory, onSelectCategory, counts }) {
  const categories = [
    { id: 'all', label: 'All Gear', icon: LayoutGrid },
    { id: 'keyboard', label: 'Keyboards', icon: Keyboard },
    { id: 'mouse', label: 'Mice & Trackballs', icon: Mouse },
    { id: 'monitor', label: 'Monitors', icon: Monitor },
    { id: 'chair', label: 'Ergonomic Chairs', icon: Armchair },
    { id: 'laptop', label: 'Laptops', icon: Laptop },
  ];

  return (
    <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none no-scrollbar">
      {categories.map((cat) => {
        const Icon = cat.icon;
        const isActive = selectedCategory === cat.id;
        const count = counts ? counts[cat.id] : null;

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
                className={`text-[10px] px-1.5 py-0.2 rounded-md font-mono ${
                  isActive ? 'bg-black/25 text-white' : 'bg-gray-800 text-gray-400'
                }`}
              >
                {count}
              </span>
            )}
          </button>
        );
      })}
    </div>
  );
}
