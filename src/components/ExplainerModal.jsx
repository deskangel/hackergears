import React from 'react';
import { X, Calculator, ShieldCheck, UserCheck, Flame, Scale, CheckCircle2, TrendingUp, Activity } from 'lucide-react';

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
            <div className="w-8 h-8 rounded-lg bg-[#ff6600]/20 text-[#ff6600] flex items-center justify-center border border-[#ff6600]/30">
              <Calculator className="w-4 h-4" />
            </div>
            <div>
              <h2 className="text-base font-extrabold text-white">
                Ranking Algorithm & Methodology
              </h2>
              <p className="text-xs text-gray-400">
                How HackerGear calculates Hacker Score, sentiment weighting, and rankings
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
          
          {/* Master Formula Banner */}
          <div className="bg-[#0e121b] border border-orange-500/30 rounded-xl p-4">
            <div className="flex items-center gap-2 text-[#ff6600] font-bold mb-2 text-sm">
              <Scale className="w-4 h-4" />
              <span>Hacker Score Master Formula</span>
            </div>
            <div className="bg-[#151926] p-3 rounded-lg font-mono text-[13px] text-white border border-gray-800 text-center font-bold tracking-wide">
              Score = Net Positive × (1 + Satisfaction%) × (1 + Confidence)
            </div>
            <p className="text-[11px] text-gray-400 mt-2">
              Every hardware score balances real developer sentiment, community consensus percentage, and sample size confidence.
            </p>
          </div>

          {/* Section 1: Detailed Breakdown */}
          <div className="space-y-3">
            <div className="text-sm font-bold text-white flex items-center gap-2">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span>Algorithm Components</span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {/* Component 1 */}
              <div className="bg-[#161c2b] border border-gray-800 rounded-xl p-3.5 flex flex-col justify-between">
                <div>
                  <div className="font-bold text-emerald-400 flex items-center gap-1.5 mb-1.5 text-xs">
                    <UserCheck className="w-3.5 h-3.5" />
                    1. Unique Author Deduplication
                  </div>
                  <p className="text-[11px] text-gray-400">
                    All mentions are deduplicated by HN username. If a user posts 10 comments in a heated thread, they contribute exactly 1 net stance (Positive, Cautionary, or Neutral).
                  </p>
                </div>
                <div className="mt-2 text-[10px] font-mono text-gray-500 bg-gray-900/60 px-2 py-1 rounded">
                  N = U_pos + U_neg + U_neutral
                </div>
              </div>

              {/* Component 2 */}
              <div className="bg-[#161c2b] border border-gray-800 rounded-xl p-3.5 flex flex-col justify-between">
                <div>
                  <div className="font-bold text-amber-400 flex items-center gap-1.5 mb-1.5 text-xs">
                    <Flame className="w-3.5 h-3.5" />
                    2. 1.5× Caution Penalty
                  </div>
                  <p className="text-[11px] text-gray-400">
                    Negative experiences (e.g. <em>"returned it"</em>, <em>"wrist pain"</em>, <em>"broke"</em>) carry a 1.5× weight penalty to protect developers from notorious hardware flaws.
                  </p>
                </div>
                <div className="mt-2 text-[10px] font-mono text-amber-300/80 bg-gray-900/60 px-2 py-1 rounded">
                  Net Pos = max(0, U_pos - 1.5 × U_neg + 0.15 × U_neu)
                </div>
              </div>

              {/* Component 3 */}
              <div className="bg-[#161c2b] border border-gray-800 rounded-xl p-3.5 flex flex-col justify-between">
                <div>
                  <div className="font-bold text-cyan-400 flex items-center gap-1.5 mb-1.5 text-xs">
                    <TrendingUp className="w-3.5 h-3.5" />
                    3. Satisfaction Multiplier
                  </div>
                  <p className="text-[11px] text-gray-400">
                    Measures approval consensus among engineers who voiced an opinion. High satisfaction amplifies the net positive score by up to 2.0×.
                  </p>
                </div>
                <div className="mt-2 text-[10px] font-mono text-cyan-300/80 bg-gray-900/60 px-2 py-1 rounded">
                  Satisfaction% = U_pos / (U_pos + U_neg)
                </div>
              </div>

              {/* Component 4 */}
              <div className="bg-[#161c2b] border border-gray-800 rounded-xl p-3.5 flex flex-col justify-between">
                <div>
                  <div className="font-bold text-purple-400 flex items-center gap-1.5 mb-1.5 text-xs">
                    <Activity className="w-3.5 h-3.5" />
                    4. Log-Confidence Multiplier
                  </div>
                  <p className="text-[11px] text-gray-400">
                    A logarithmic sample-size confidence factor. Prevents an item with only 1 isolated comment from outranking gear proven across dozens of engineers.
                  </p>
                </div>
                <div className="mt-2 text-[10px] font-mono text-purple-300/80 bg-gray-900/60 px-2 py-1 rounded">
                  C = log10(1 + N) × [N / (N + 2)]
                </div>
              </div>
            </div>
          </div>

          {/* Section 2: Concrete Walkthrough */}
          <div className="bg-[#151a27] border border-gray-800 rounded-xl p-3.5">
            <div className="font-bold text-white mb-2 flex items-center gap-1.5 text-xs">
              <Calculator className="w-3.5 h-3.5 text-[#ff6600]" />
              <span>Step-by-Step Calculation Walkthrough</span>
            </div>
            <div className="bg-[#0f131e] p-3 rounded-lg font-mono text-[11px] space-y-1.5 text-gray-300">
              <div className="text-gray-400 font-semibold text-[10px] uppercase tracking-wider">Example: Ergodox EZ (24 unique authors)</div>
              <div className="flex justify-between border-b border-gray-800 pb-1">
                <span className="text-gray-400">• Developer Feedback:</span>
                <span className="text-white">21 Positive, 2 Cautionary, 1 Neutral</span>
              </div>
              <div className="flex justify-between border-b border-gray-800 pb-1">
                <span className="text-gray-400">• Net Positive:</span>
                <span>21 - (1.5 × 2) + (0.15 × 1) = <strong className="text-emerald-400">18.15</strong></span>
              </div>
              <div className="flex justify-between border-b border-gray-800 pb-1">
                <span className="text-gray-400">• Satisfaction Rate:</span>
                <span>21 / 23 = <strong className="text-cyan-400">91.3%</strong> (Factor: ×1.913)</span>
              </div>
              <div className="flex justify-between border-b border-gray-800 pb-1">
                <span className="text-gray-400">• Sample Confidence (N=24):</span>
                <span>log10(25) × (24/26) = <strong className="text-purple-400">1.29</strong> (Factor: ×2.29)</span>
              </div>
              <div className="flex justify-between pt-0.5 text-xs">
                <span className="text-[#ff6600] font-bold">→ Hacker Score:</span>
                <span className="text-white font-bold">18.15 × 1.913 × 2.29 = <span className="text-[#ff6600]">79.5</span></span>
              </div>
            </div>
          </div>

          {/* Section 3: Controversy & Edition Partitioning */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="bg-[#151a27] border border-gray-800 rounded-xl p-3">
              <div className="font-bold text-rose-400 mb-1 flex items-center gap-1.5 text-xs">
                <Flame className="w-3.5 h-3.5" />
                Controversy Index
              </div>
              <p className="text-[11px] text-gray-400 mb-1.5">
                Measures opinion polarization when hardware attracts both passionate advocates and vocal critics.
              </p>
              <div className="text-[10px] font-mono text-rose-300/80 bg-gray-900/60 p-1.5 rounded">
                Index = [min(U_pos, U_neg) / N] × 100 × ln(1 + N)
              </div>
            </div>

            <div className="bg-[#151a27] border border-gray-800 rounded-xl p-3">
              <div className="font-bold text-sky-400 mb-1 flex items-center gap-1.5 text-xs">
                <CheckCircle2 className="w-3.5 h-3.5" />
                Yearly Partitioning
              </div>
              <p className="text-[11px] text-gray-400">
                Discussions are partitioned into <strong>2026 Edition</strong> and <strong>2025 Annual</strong> to reflect current developer recommendations without obsolete hardware contamination.
              </p>
            </div>
          </div>

        </div>

        {/* Footer */}
        <div className="p-4 border-t border-gray-800 bg-[#161a29] flex justify-end">
          <button
            onClick={onClose}
            className="bg-[#ff6600] hover:bg-[#ff771a] text-white font-semibold px-4 py-1.5 rounded-lg text-xs transition-colors cursor-pointer"
          >
            Got it, close
          </button>
        </div>

      </div>
    </div>
  );
}
