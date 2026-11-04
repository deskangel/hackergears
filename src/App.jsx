import React, { useState, useMemo } from 'react';
import Header from './components/Header';
import YearSelector from './components/YearSelector';
import CategoryNav from './components/CategoryNav';
import FilterBar from './components/FilterBar';
import HardwareCard from './components/HardwareCard';
import ItemDetailModal from './components/ItemDetailModal';
import ExplainerModal from './components/ExplainerModal';
import rawData from './data/hardware_data.json';

export default function App() {
  const [selectedYear, setSelectedYear] = useState('2026');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [sortOrder, setSortOrder] = useState('hacker_score');
  const [selectedItem, setSelectedItem] = useState(null);
  const [isExplainerOpen, setIsExplainerOpen] = useState(false);
  const [hideZeroMentions, setHideZeroMentions] = useState(true);

  // Raw edition items
  const allEditionItems = useMemo(() => {
    return rawData.editions?.[selectedYear] || [];
  }, [selectedYear]);

  // Count of items with zero mentions in this edition
  const zeroMentionCount = useMemo(() => {
    return allEditionItems.filter((item) => (item.stats?.unique_users || 0) === 0).length;
  }, [allEditionItems]);

  // Current filtered edition items (excluding 0-mention items by default for clean rankings)
  const currentEditionItems = useMemo(() => {
    if (hideZeroMentions) {
      return allEditionItems.filter((item) => (item.stats?.unique_users || 0) > 0);
    }
    return allEditionItems;
  }, [allEditionItems, hideZeroMentions]);

  // Rank Trend comparison between 2026 and 2025
  const rankTrends = useMemo(() => {
    const trends = {};
    const items2025 = (rawData.editions?.['2025'] || []).filter(
      (it) => (it.stats?.unique_users || 0) > 0
    );
    const map2025 = {};
    items2025.forEach((it, idx) => {
      map2025[it.id] = idx + 1;
    });

    const items2026 = (rawData.editions?.['2026'] || []).filter(
      (it) => (it.stats?.unique_users || 0) > 0
    );
    const map2026 = {};
    items2026.forEach((it, idx) => {
      map2026[it.id] = idx + 1;
    });

    if (selectedYear === '2026') {
      currentEditionItems.forEach((it, idx) => {
        const curRank = idx + 1;
        const prevRank = map2025[it.id];
        if (prevRank !== undefined) {
          const diff = prevRank - curRank;
          trends[it.id] = {
            diff,
            prevRank,
            type: diff > 0 ? 'up' : diff < 0 ? 'down' : 'same'
          };
        } else {
          trends[it.id] = { diff: 0, type: 'new' };
        }
      });
    } else if (selectedYear === '2025') {
      currentEditionItems.forEach((it, idx) => {
        const curRank = idx + 1;
        const nextRank = map2026[it.id];
        if (nextRank !== undefined) {
          const diff = curRank - nextRank;
          trends[it.id] = {
            diff,
            nextRank,
            type: diff > 0 ? 'up' : diff < 0 ? 'down' : 'same'
          };
        }
      });
    }

    return trends;
  }, [selectedYear, currentEditionItems]);

  // Compute category counts based on current active edition
  const categoryCounts = useMemo(() => {
    const counts = { all: currentEditionItems.length };
    currentEditionItems.forEach((item) => {
      counts[item.category] = (counts[item.category] || 0) + 1;
    });
    return counts;
  }, [currentEditionItems]);

  // Filter & Sort
  const filteredAndSortedItems = useMemo(() => {
    let items = [...currentEditionItems];

    // Filter by Category
    if (selectedCategory !== 'all') {
      items = items.filter((item) => item.category === selectedCategory);
    }

    // Filter by Search Query
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase().trim();
      items = items.filter((item) => {
        return (
          item.name.toLowerCase().includes(q) ||
          item.brand.toLowerCase().includes(q) ||
          item.category.toLowerCase().includes(q) ||
          (item.specs && item.specs.toLowerCase().includes(q)) ||
          (item.tags && item.tags.some((t) => t.toLowerCase().includes(q)))
        );
      });
    }

    // Sort Order
    items.sort((a, b) => {
      const aStats = a.stats || {};
      const bStats = b.stats || {};

      if (sortOrder === 'hacker_score') {
        return (bStats.hacker_score || 0) - (aStats.hacker_score || 0);
      } else if (sortOrder === 'satisfaction') {
        // Tie-breaker with positive users
        const diff = (bStats.satisfaction_rate || 0) - (aStats.satisfaction_rate || 0);
        if (Math.abs(diff) < 0.1) {
          return (bStats.positive_users || 0) - (aStats.positive_users || 0);
        }
        return diff;
      } else if (sortOrder === 'positive_users') {
        return (bStats.positive_users || 0) - (aStats.positive_users || 0);
      } else if (sortOrder === 'controversy') {
        return (bStats.controversy_index || 0) - (aStats.controversy_index || 0);
      }
      return 0;
    });

    return items;
  }, [currentEditionItems, selectedCategory, searchQuery, sortOrder]);

  return (
    <div className="min-h-screen flex flex-col bg-[#0b0e16] text-[#e2e8f0]">
      {/* Top Header */}
      <Header 
        metadata={rawData.metadata} 
        onOpenExplainer={() => setIsExplainerOpen(true)} 
      />

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        
        {/* Year Edition Selector */}
        <YearSelector
          selectedYear={selectedYear}
          onSelectYear={setSelectedYear}
        />

        {/* Categories Bar */}
        <div className="mb-4">
          <CategoryNav
            selectedCategory={selectedCategory}
            onSelectCategory={setSelectedCategory}
            counts={categoryCounts}
            selectedYear={selectedYear}
          />
        </div>

        {/* Filter & Sort Bar */}
        <FilterBar
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          sortOrder={sortOrder}
          onSortChange={setSortOrder}
          totalResults={filteredAndSortedItems.length}
          selectedYear={selectedYear}
          hideZeroMentions={hideZeroMentions}
          onToggleHideZeroMentions={() => setHideZeroMentions((prev) => !prev)}
          zeroMentionCount={zeroMentionCount}
        />

        {/* Hardware Items Grid */}
        {filteredAndSortedItems.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {filteredAndSortedItems.map((item, index) => (
              <HardwareCard
                key={`${selectedYear}-${item.id}`}
                item={item}
                rank={index + 1}
                selectedYear={selectedYear}
                rankTrend={rankTrends[item.id]}
                onSelect={(it) => setSelectedItem(it)}
              />
            ))}
          </div>
        ) : (
          <div className="text-center py-20 bg-[#121622] rounded-2xl border border-gray-800">
            <p className="text-gray-400 text-sm mb-2">
              No hardware matched your search criteria.
            </p>
            <button
              onClick={() => {
                setSearchQuery('');
                setSelectedCategory('all');
              }}
              className="text-[#ff6600] text-xs font-semibold hover:underline"
            >
              Reset filters
            </button>
          </div>
        )}

      </main>

      {/* Footer */}
      <footer className="border-t border-gray-800/80 bg-[#0d1017] py-6 text-center text-xs text-gray-500 font-mono">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
          <div>
            HackerGear — Powered by Hacker News discussions (2025–2026).
          </div>
          <div className="text-gray-600">
            Deduplicated by unique authors • Anti-controversy weighted
          </div>
        </div>
      </footer>

      {/* Detail Modal */}
      {selectedItem && (
        <ItemDetailModal
          item={selectedItem}
          year={selectedYear}
          onClose={() => setSelectedItem(null)}
        />
      )}

      {/* Explainer Modal */}
      <ExplainerModal
        isOpen={isExplainerOpen}
        onClose={() => setIsExplainerOpen(false)}
      />
    </div>
  );
}
