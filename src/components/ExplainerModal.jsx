import React from 'react';
import { X, AlertTriangle, ShieldCheck, UserCheck, Flame, Scale, CheckCircle2 } from 'lucide-react';

export default function ExplainerModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-black/75 backdrop-blur-sm flex items-center justify-center p-3 sm:p-5">
      <div 
        className="relative bg-[#121622] border border-gray-700 rounded-2xl w-full max-w-2xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="p-5 border-b border-gray-800 bg-[#161a29] flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center border border-amber-500/30">
              <Scale className="w-4 h-4" />
            </div>
            <div>
              <h2 className="text-base font-extrabold text-white">
                The HackerBooks Problem & Our Algorithm
              </h2>
              <p className="text-xs text-gray-400">
                Why HackerGear does not use raw mention counts
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="text-gray-400 hover:text-white bg-gray-800/60 hover:bg-gray-800 p-2 rounded-xl transition-colors cursor-pointer"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-5 overflow-y-auto space-y-4 text-xs text-gray-300 leading-relaxed">
          
          {/* Section 1: The HackerBooks Problem */}
          <div className="bg-rose-950/20 border border-rose-900/40 rounded-xl p-4">
            <div className="flex items-center gap-2 text-rose-400 font-bold mb-1.5 text-sm">
              <AlertTriangle className="w-4 h-4" />
              <span>What went wrong with raw mention counts?</span>
            </div>
            <p className="mb-2">
              Previous projects like <em>HackerBooks</em> ranked items purely by total comment occurrences. This caused major ranking distortions:
            </p>
            <ul className="list-disc pl-5 space-y-1 text-gray-300">
              <li>
                <strong>The Flame-War Anomaly:</strong> Highly controversial or heavily criticized items received hundreds of angry mentions (e.g. <em>"Don't buy X, it caused wrist pain"</em> or <em>"X is terrible"</em>), pushing them to #1.
              </li>
              <li>
                <strong>Sybil & Astroturfing Bias:</strong> A single zealous user or vendor posting 12 times in an argument counted as 12 votes.
              </li>
              <li>
                <strong>Hardware Obsolescence:</strong> Mixing 20 years together meant 2017 Intel MacBook butterfly keyboard complaints dragged down modern Apple Silicon MacBooks.
              </li>
            </ul>
          </div>

          {/* Section 2: How HackerGear Fixes It */}
          <div>
            <div className="text-sm font-bold text-white mb-2 flex items-center gap-2">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span>How HackerGear Solves This</span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-3">
              <div className="bg-[#161c2b] border border-gray-800 rounded-xl p-3">
                <div className="font-bold text-emerald-400 flex items-center gap-1.5 mb-1">
                  <UserCheck className="w-3.5 h-3.5" />
                  1. Unique Author Weighting
                </div>
                <p className="text-[11px] text-gray-400">
                  Multiple mentions by the same user in an argument are deduplicated into at most 1 net vote. Astroturfing has zero amplification.
                </p>
              </div>

              <div className="bg-[#161c2b] border border-gray-800 rounded-xl p-3">
                <div className="font-bold text-amber-400 flex items-center gap-1.5 mb-1">
                  <Flame className="w-3.5 h-3.5" />
                  2. 1.5× Caution Penalty
                </div>
                <p className="text-[11px] text-gray-400">
                  Critical reviews (e.g. <em>"returned it"</em>, <em>"wrist pain"</em>, <em>"broke"</em>) carry a 1.5× penalty to ensure recommendations don't hide notorious flaws.
                </p>
              </div>
            </div>

            <div className="bg-[#0e121b] border border-gray-800 rounded-xl p-3 font-mono text-[11px] space-y-1">
              <div className="text-gray-400 font-bold">Hacker Score Formula:</div>
              <div className="text-[#ff6600]">
                Score = (U_pos - 1.5 * U_neg) × (1 + Satisfaction%) × (1 + log10(1 + N))
              </div>
              <div className="text-gray-500 text-[10px]">
                Where U_pos = unique endorsing authors, U_neg = unique cautionary authors, N = total unique authors.
              </div>
            </div>
          </div>

          {/* Section 3: Yearly Partitioning */}
          <div className="bg-[#151a27] border border-gray-800 rounded-xl p-3.5">
            <div className="font-bold text-sky-400 mb-1 flex items-center gap-1.5">
              <CheckCircle2 className="w-3.5 h-3.5" />
              Yearly Partitioning (2025 & 2026 Editions)
            </div>
            <p className="text-xs text-gray-400">
              By viewing recommendations partitioned by year, users can inspect what Hacker News engineers recommend right now, without 10-year-old obsolete revisions polluting modern rankings.
            </p>
          </div>

        </div>

        {/* Footer */}
        <div className="p-4 border-t border-gray-800 bg-[#161a29] flex justify-end">
          <button
            onClick={onClose}
            className="bg-[#ff6600] hover:bg-[#ff771a] text-white font-semibold px-4 py-1.5 rounded-lg text-xs transition-colors cursor-pointer"
          >
            Got it, take me back
          </button>
        </div>

      </div>
    </div>
  );
}
