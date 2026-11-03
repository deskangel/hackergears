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

  // Current year items
  const currentEditionItems = useMemo(() => {
    return rawData.editions?.[selectedYear] || [];
  }, [selectedYear]);

  // Compute category counts
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
          />
        </div>

        {/* Filter & Sort Bar */}
        <FilterBar
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          sortOrder={sortOrder}
          onSortChange={setSortOrder}
          totalResults={filteredAndSortedItems.length}
        />

        {/* Hardware Items Grid */}
        {filteredAndSortedItems.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {filteredAndSortedItems.map((item, index) => (
              <HardwareCard
                key={item.id}
                item={item}
                rank={index + 1}
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
