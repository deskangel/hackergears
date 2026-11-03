import React from 'react';
import { Cpu, HelpCircle, Database, Sparkles, ExternalLink } from 'lucide-react';

export default function Header({ metadata, onOpenExplainer }) {
  return (
    <header className="border-b border-gray-800/80 bg-[#12151f]/80 backdrop-blur-md sticky top-0 z-30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        
        {/* Brand & Logo */}
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-[#ff6600] to-[#ff8533] flex items-center justify-center shadow-lg shadow-[#ff6600]/20 ring-1 ring-white/20">
            <Cpu className="w-5 h-5 text-white" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-xl tracking-tight text-white flex items-center gap-1.5">
                Hacker<span className="text-[#ff6600]">Gear</span>
              </span>
              <span className="text-[10px] font-mono font-bold uppercase tracking-wider bg-[#ff6600]/15 text-[#ff6600] px-2 py-0.5 rounded-full border border-[#ff6600]/30">
                HN Hardware Index
              </span>
            </div>
            <p className="text-xs text-gray-400">
              Mined & sentiment-weighted developer hardware recommendations
            </p>
          </div>
        </div>

        {/* Live Stats & Explainer Trigger */}
        <div className="flex items-center flex-wrap gap-2.5 sm:gap-3 text-xs">
          
          {/* Comments & Authors stats pill */}
          <div className="flex items-center space-x-3 bg-gray-900/80 border border-gray-800 px-3 py-1.5 rounded-lg text-gray-300 font-mono">
            <div className="flex items-center gap-1.5">
              <Database className="w-3.5 h-3.5 text-emerald-400" />
              <span>
                <strong className="text-white">{metadata?.total_comments_analyzed || '1,000+'}</strong> comments
              </span>
            </div>
            <span className="text-gray-700">|</span>
            <div className="flex items-center gap-1.5">
              <span>
                <strong className="text-white">{metadata?.total_unique_authors || '800+'}</strong> unique authors
              </span>
            </div>
          </div>

          {/* Explainer Button */}
          <button
            onClick={onOpenExplainer}
            className="flex items-center gap-1.5 bg-[#1a2130] hover:bg-[#222c40] text-amber-300 hover:text-amber-200 border border-amber-500/30 px-3 py-1.5 rounded-lg transition-colors font-medium shadow-sm cursor-pointer"
            title="Read about the HackerBooks mention trap and our algorithm"
          >
            <HelpCircle className="w-3.5 h-3.5 text-amber-400" />
            <span>Why not raw mentions?</span>
          </button>

          {/* Hacker News Link */}
          <a
            href="https://news.ycombinator.com"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1 text-gray-400 hover:text-white transition-colors bg-gray-900/60 hover:bg-gray-800 border border-gray-800 px-2.5 py-1.5 rounded-lg"
          >
            <span>news.yc</span>
            <ExternalLink className="w-3 h-3 text-gray-500" />
          </a>

        </div>

      </div>
    </header>
  );
}
