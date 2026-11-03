import React, { useState } from 'react';
import { 
  X, 
  ExternalLink, 
  ThumbsUp, 
  ThumbsDown, 
  MessageSquareQuote, 
  ShieldCheck, 
  Sparkles, 
  AlertTriangle,
  Layers,
  Cpu,
  Calendar
} from 'lucide-react';

export default function ItemDetailModal({ item, year, onClose }) {
  if (!item) return null;

  const [activeTab, setActiveTab] = useState('quotes'); // 'quotes' or 'cautions' or 'specs'

  const stats = item.stats || {};
  const positiveQuotes = item.quotes?.positive || [];
  const cautionQuotes = item.quotes?.caution || [];

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-black/70 backdrop-blur-sm flex items-center justify-center p-3 sm:p-5">
      <div 
        className="relative bg-[#121622] border border-gray-700/80 rounded-2xl w-full max-w-3xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="p-5 border-b border-gray-800 bg-[#161a29] flex items-start justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <span className="font-mono text-xs font-bold text-[#ff6600] bg-[#ff6600]/15 px-2.5 py-0.5 rounded-full border border-[#ff6600]/30">
                Rank #{item.rank}
              </span>
              <span className="text-xs font-mono uppercase text-gray-400">
                {item.brand}
              </span>
              <span className="text-gray-600">•</span>
              <span className="text-xs font-mono text-gray-400 capitalize">
                {item.category}
              </span>
              <span className="text-gray-600">•</span>
              <span className="text-xs font-mono text-gray-400">
                Edition: <strong className="text-gray-200">{year}</strong>
              </span>
            </div>
            <h2 className="text-xl sm:text-2xl font-extrabold text-white">
              {item.name}
            </h2>
          </div>

          <button
            onClick={onClose}
            className="text-gray-400 hover:text-white bg-gray-800/60 hover:bg-gray-800 p-2 rounded-xl transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-5 overflow-y-auto space-y-5">
          
          {/* Key Metrics Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="bg-[#0b0e16] border border-gray-800 rounded-xl p-3">
              <div className="text-[10px] font-mono uppercase text-gray-400 mb-1">
                Hacker Score
              </div>
              <div className="text-xl font-extrabold text-[#ff6600] font-mono">
                {stats.hacker_score || 0}
              </div>
              <div className="text-[10px] text-gray-400">
                Sentiment-weighted
              </div>
            </div>

            <div className="bg-[#0b0e16] border border-gray-800 rounded-xl p-3">
              <div className="text-[10px] font-mono uppercase text-gray-400 mb-1">
                Satisfaction
              </div>
              <div className="text-xl font-extrabold text-emerald-400 font-mono">
                {stats.satisfaction_rate || 100}%
              </div>
              <div className="text-[10px] text-gray-400">
                Positive author ratio
              </div>
            </div>

            <div className="bg-[#0b0e16] border border-gray-800 rounded-xl p-3">
              <div className="text-[10px] font-mono uppercase text-gray-400 mb-1">
                Endorsements
              </div>
              <div className="text-xl font-extrabold text-emerald-400 font-mono flex items-center gap-1.5">
                <ThumbsUp className="w-4 h-4" />
                {stats.positive_users || 0}
              </div>
              <div className="text-[10px] text-gray-400">
                Unique authors
              </div>
            </div>

            <div className="bg-[#0b0e16] border border-gray-800 rounded-xl p-3">
              <div className="text-[10px] font-mono uppercase text-gray-400 mb-1">
                Cautions
              </div>
              <div className={`text-xl font-extrabold font-mono flex items-center gap-1.5 ${
                (stats.negative_users || 0) > 0 ? 'text-rose-400' : 'text-gray-500'
              }`}>
                <ThumbsDown className="w-4 h-4" />
                {stats.negative_users || 0}
              </div>
              <div className="text-[10px] text-gray-400">
                Unique critics
              </div>
            </div>
          </div>

          {/* Specs & Hardware Overview */}
          <div className="bg-[#171c2b] border border-gray-800 rounded-xl p-3.5">
            <div className="text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5 font-mono flex items-center gap-1.5">
              <Cpu className="w-3.5 h-3.5 text-[#ff8533]" />
              Hardware Profile & Specs
            </div>
            <p className="text-xs text-gray-300 leading-relaxed mb-2.5">
              {item.specs}
            </p>
            {item.tags && (
              <div className="flex flex-wrap gap-1.5">
                {item.tags.map((t, idx) => (
                  <span key={idx} className="text-[10px] bg-gray-900/90 text-gray-300 px-2 py-0.5 rounded border border-gray-700/60 font-mono">
                    {t}
                  </span>
                ))}
              </div>
            )}
          </div>

          {/* Tab Navigation for Quotes */}
          <div>
            <div className="flex items-center gap-2 border-b border-gray-800 pb-2 mb-4">
              <button
                onClick={() => setActiveTab('quotes')}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
                  activeTab === 'quotes'
                    ? 'bg-emerald-500/15 text-emerald-300 border border-emerald-500/30'
                    : 'text-gray-400 hover:text-gray-200'
                }`}
              >
                <ThumbsUp className="w-3.5 h-3.5" />
                <span>Why HN Recommends It ({positiveQuotes.length})</span>
              </button>

              <button
                onClick={() => setActiveTab('cautions')}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
                  activeTab === 'cautions'
                    ? 'bg-rose-500/15 text-rose-300 border border-rose-500/30'
                    : 'text-gray-400 hover:text-gray-200'
                }`}
              >
                <AlertTriangle className="w-3.5 h-3.5" />
                <span>What HN Warns About ({cautionQuotes.length})</span>
              </button>
            </div>

            {/* Positive Quotes List */}
            {activeTab === 'quotes' && (
              <div className="space-y-3">
                {positiveQuotes.length > 0 ? (
                  positiveQuotes.map((q, idx) => (
                    <div key={idx} className="bg-[#0e121b] border border-gray-800/80 rounded-xl p-3.5 relative">
                      <div className="flex items-center justify-between text-xs text-gray-400 mb-2 font-mono">
                        <span className="font-semibold text-[#ff8533] flex items-center gap-1.5">
                          <MessageSquareQuote className="w-3.5 h-3.5 text-emerald-400" />
                          user: {q.author}
                        </span>
                        <div className="flex items-center gap-3">
                          <span className="text-gray-500">{q.date}</span>
                          <a
                            href={q.permalink}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="flex items-center gap-1 text-emerald-400 hover:text-emerald-300 hover:underline text-[11px]"
                          >
                            <span>view on HN</span>
                            <ExternalLink className="w-3 h-3" />
                          </a>
                        </div>
                      </div>
                      <p className="text-xs text-gray-200 leading-relaxed italic">
                        "{q.snippet}"
                      </p>
                    </div>
                  ))
                ) : (
                  <div className="p-8 text-center text-xs text-gray-500 italic bg-[#0e121b] rounded-xl border border-gray-800">
                    No positive quote snippets extracted for this year edition.
                  </div>
                )}
              </div>
            )}

            {/* Cautionary Quotes List */}
            {activeTab === 'cautions' && (
              <div className="space-y-3">
                {cautionQuotes.length > 0 ? (
                  cautionQuotes.map((q, idx) => (
                    <div key={idx} className="bg-[#160e12] border border-rose-900/30 rounded-xl p-3.5 relative">
                      <div className="flex items-center justify-between text-xs text-gray-400 mb-2 font-mono">
                        <span className="font-semibold text-rose-400 flex items-center gap-1.5">
                          <AlertTriangle className="w-3.5 h-3.5 text-rose-400" />
                          user: {q.author}
                        </span>
                        <div className="flex items-center gap-3">
                          <span className="text-gray-500">{q.date}</span>
                          <a
                            href={q.permalink}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="flex items-center gap-1 text-rose-400 hover:text-rose-300 hover:underline text-[11px]"
                          >
                            <span>view on HN</span>
                            <ExternalLink className="w-3 h-3" />
                          </a>
                        </div>
                      </div>
                      <p className="text-xs text-rose-200/90 leading-relaxed italic">
                        "{q.snippet}"
                      </p>
                    </div>
                  ))
                ) : (
                  <div className="p-8 text-center text-xs text-emerald-400/80 bg-[#0c1314] rounded-xl border border-emerald-900/30">
                    ✨ No significant complaints, returns, or ergonomics warnings detected in this dataset.
                  </div>
                )}
              </div>
            )}

          </div>

        </div>

        {/* Modal Footer */}
        <div className="p-4 border-t border-gray-800 bg-[#161a29] flex items-center justify-between text-xs text-gray-400">
          <span>Click any HN link to read the full context on Hacker News</span>
          <button
            onClick={onClose}
            className="bg-gray-800 hover:bg-gray-700 text-white px-4 py-1.5 rounded-lg font-medium transition-colors cursor-pointer"
          >
            Close
          </button>
        </div>

      </div>
    </div>
  );
}
