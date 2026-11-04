import React from 'react';
import { Search, ArrowUpDown, X, Sparkles, AlertTriangle, ThumbsUp, Percent } from 'lucide-react';

export default function FilterBar({
  searchQuery,
  onSearchChange,
  sortOrder,
  onSortChange,
  totalResults,
  selectedYear = '2026',
  hideZeroMentions = true,
  onToggleHideZeroMentions,
  zeroMentionCount = 0
}) {
  const sortOptions = [
    { id: 'hacker_score', label: 'Hacker Score', desc: 'Weighted Net Sentiment', icon: Sparkles },
    { id: 'satisfaction', label: 'Satisfaction %', desc: 'Highest Pos/Neg Ratio', icon: Percent },
    { id: 'positive_users', label: 'Most Endorsed', desc: 'Raw Unique Users', icon: ThumbsUp },
    { id: 'controversy', label: 'Controversy Index', desc: 'Polarizing Opinions', icon: AlertTriangle }
  ];

  return (
    <div className="bg-[#121622] border border-gray-800/80 rounded-xl p-3 mb-6 flex flex-col md:flex-row md:items-center justify-between gap-3 shadow-md">
      
      {/* Search Input */}
      <div className="relative flex-1">
        <Search className="w-4 h-4 text-gray-500 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
          placeholder="Search by hardware name, brand, tag (e.g. 'split', 'aeron', 'trackball', 'm3', 'oled')..."
          className="w-full bg-[#0d1018] border border-gray-800 rounded-lg pl-9 pr-8 py-2 text-xs text-gray-200 placeholder-gray-500 focus:outline-none focus:border-[#ff6600]/60 focus:ring-1 focus:ring-[#ff6600]/40 transition-all"
        />
        {searchQuery && (
          <button
            onClick={() => onSearchChange('')}
            className="absolute right-2.5 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"
          >
            <X className="w-3.5 h-3.5" />
          </button>
        )}
      </div>

      {/* Sort Options & Counter */}
      <div className="flex items-center gap-2 flex-wrap">
        <span className="text-[11px] font-mono text-gray-500 flex items-center gap-1 uppercase tracking-wider">
          <ArrowUpDown className="w-3 h-3 text-[#ff6600]" />
          Sort:
        </span>

        <div className="flex items-center bg-[#0d1018] border border-gray-800 rounded-lg p-0.5">
          {sortOptions.map((opt) => {
            const Icon = opt.icon;
            const isSelected = sortOrder === opt.id;
            return (
              <button
                key={opt.id}
                onClick={() => onSortChange(opt.id)}
                className={`flex items-center gap-1.5 px-2.5 py-1.5 rounded-md text-[11px] font-medium transition-all cursor-pointer ${
                  isSelected
                    ? 'bg-[#1e2538] text-white shadow-sm border border-gray-700/60'
                    : 'text-gray-400 hover:text-gray-200'
                }`}
                title={opt.desc}
              >
                <Icon className={`w-3 h-3 ${isSelected ? 'text-[#ff6600]' : 'text-gray-500'}`} />
                <span className="hidden sm:inline">{opt.label}</span>
                <span className="sm:hidden">{opt.label.split(' ')[0]}</span>
              </button>
            );
          })}
        </div>

        {/* Results Counter & Year Filter */}
        <div className="flex items-center gap-1.5">
          <div className="text-[11px] font-mono text-gray-400 bg-gray-900/60 px-2.5 py-1 rounded-md border border-gray-800 flex items-center gap-1.5">
            <span className="text-[#ff6600] font-bold">{totalResults}</span>
            <span>items in</span>
            <span className="font-semibold text-gray-200">{selectedYear === 'All' ? 'Combined' : selectedYear}</span>
          </div>

          {zeroMentionCount > 0 && onToggleHideZeroMentions && (
            <button
              onClick={onToggleHideZeroMentions}
              className={`text-[10px] font-mono px-2 py-1 rounded-md border transition-all cursor-pointer ${
                hideZeroMentions 
                  ? 'bg-gray-800/80 text-gray-400 border-gray-700/60 hover:text-white hover:border-gray-600' 
                  : 'bg-[#ff6600]/15 text-[#ff8533] border-[#ff6600]/40 shadow-sm'
              }`}
              title="Toggle hardware with 0 mentions in this edition"
            >
              {hideZeroMentions ? `+${zeroMentionCount} unranked hidden` : 'Showing all items'}
            </button>
          )}
        </div>

      </div>

    </div>
  );
}
