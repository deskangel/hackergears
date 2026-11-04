import React from 'react';
import { 
  Keyboard, 
  Mouse, 
  Monitor, 
  Armchair, 
  Laptop, 
  Headphones,
  LampDesk,
  Cpu,
  HardDrive,
  Sparkles, 
  ShieldCheck, 
  AlertTriangle, 
  MessageSquareQuote, 
  ExternalLink, 
  ChevronRight,
  ThumbsUp,
  ThumbsDown,
  ArrowUp,
  ArrowDown,
  Minus
} from 'lucide-react';

const CATEGORY_ICONS = {
  keyboard: Keyboard,
  mouse: Mouse,
  monitor: Monitor,
  chair: Armchair,
  laptop: Laptop,
  audio: Headphones,
  desk: LampDesk,
  minipc: Cpu,
  network: HardDrive
};

const CATEGORY_COLORS = {
  keyboard: 'text-violet-400 bg-violet-500/10 border-violet-500/20',
  mouse: 'text-cyan-400 bg-cyan-500/10 border-cyan-500/20',
  monitor: 'text-blue-400 bg-blue-500/10 border-blue-500/20',
  chair: 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20',
  laptop: 'text-amber-400 bg-amber-500/10 border-amber-500/20',
  audio: 'text-pink-400 bg-pink-500/10 border-pink-500/20',
  desk: 'text-orange-400 bg-orange-500/10 border-orange-500/20',
  minipc: 'text-teal-400 bg-teal-500/10 border-teal-500/20',
  network: 'text-indigo-400 bg-indigo-500/10 border-indigo-500/20'
};

export default function HardwareCard({ 
  item, 
  rank, 
  selectedYear = '2026',
  rankTrend,
  onSelect 
}) {
  const [imgError, setImgError] = React.useState(false);
  const Icon = CATEGORY_ICONS[item.category] || Sparkles;
  const colorClass = CATEGORY_COLORS[item.category] || 'text-gray-400 bg-gray-500/10 border-gray-500/20';

  const stats = item.stats || {};
  const hackerScore = stats.hacker_score || 0;
  const satisfactionRate = stats.satisfaction_rate || 100;
  const posUsers = stats.positive_users || 0;
  const negUsers = stats.negative_users || 0;
  const neuUsers = stats.neutral_users || 0;
  const totalUsers = stats.unique_users || (posUsers + negUsers + neuUsers);

  // Top positive quote
  const topQuote = item.quotes?.positive?.[0] || item.quotes?.caution?.[0];

  // Polarity bar percentages
  const posWidth = totalUsers > 0 ? (posUsers / totalUsers) * 100 : 0;
  const negWidth = totalUsers > 0 ? (negUsers / totalUsers) * 100 : 0;
  const neuWidth = totalUsers > 0 ? (neuUsers / totalUsers) * 100 : 0;

  return (
    <div 
      onClick={() => onSelect(item)}
      className="group relative bg-[#131722] hover:bg-[#181d2c] border border-gray-800/90 hover:border-gray-700/80 rounded-2xl p-5 transition-all duration-200 flex flex-col justify-between shadow-lg hover:shadow-2xl hover:shadow-[#ff6600]/5 cursor-pointer animate-in fade-in duration-200"
    >
      {/* Top Bar: Rank & Category & Price */}
      <div>
        <div className="flex items-center justify-between gap-2 mb-3">
          <div className="flex items-center gap-2 flex-wrap">
            <span className={`w-7 h-7 rounded-lg flex items-center justify-center font-mono font-bold text-xs ${
              rank === 1 ? 'bg-amber-400/20 text-amber-300 ring-1 ring-amber-400/40' :
              rank === 2 ? 'bg-slate-300/20 text-slate-200 ring-1 ring-slate-300/40' :
              rank === 3 ? 'bg-amber-700/20 text-amber-500 ring-1 ring-amber-700/40' :
              'bg-gray-800/80 text-gray-400 border border-gray-700/60'
            }`}>
              #{rank}
            </span>

            {/* Rank Movement Trend Badge */}
            {rankTrend && (
              <>
                {rankTrend.type === 'up' && (
                  <span 
                    className="flex items-center gap-0.5 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold text-emerald-400 bg-emerald-500/10 border border-emerald-500/25"
                    title={`Up ${rankTrend.diff} spots vs 2025 (#${rankTrend.prevRank})`}
                  >
                    <ArrowUp className="w-2.5 h-2.5" />+{rankTrend.diff}
                  </span>
                )}
                {rankTrend.type === 'down' && (
                  <span 
                    className="flex items-center gap-0.5 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold text-rose-400 bg-rose-500/10 border border-rose-500/25"
                    title={`Down ${Math.abs(rankTrend.diff)} spots vs 2025 (#${rankTrend.prevRank})`}
                  >
                    <ArrowDown className="w-2.5 h-2.5" />{rankTrend.diff}
                  </span>
                )}
                {rankTrend.type === 'same' && rank === 1 && (
                  <span className="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold text-amber-400 bg-amber-500/10 border border-amber-500/25">
                    ★ #1 Leader
                  </span>
                )}
                {rankTrend.type === 'new' && (
                  <span className="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold text-cyan-400 bg-cyan-500/10 border border-cyan-500/25">
                    NEW
                  </span>
                )}
              </>
            )}

            <span className={`flex items-center gap-1.2 px-2.5 py-0.5 rounded-full text-[11px] font-medium border ${colorClass}`}>
              <Icon className="w-3 h-3" />
              <span className="capitalize">{item.category}</span>
            </span>
          </div>

          <div className="flex items-center gap-1.5 font-mono text-[11px]">
            <span className="text-gray-400 bg-gray-900/80 px-2 py-0.5 rounded border border-gray-800">
              {item.price_tier || '$$$'}
            </span>
          </div>
        </div>

        {/* Hardware Real Photo Showcase */}
        <div className="relative w-full h-40 mb-3.5 rounded-xl bg-[#090c14] border border-gray-800/80 overflow-hidden flex items-center justify-center group-hover:border-gray-700 transition-colors">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(255,102,0,0.03)_0%,transparent_70%)] pointer-events-none" />
          {item.image && !imgError ? (
            <img 
              src={item.image} 
              alt={item.name}
              loading="lazy"
              onError={() => setImgError(true)}
              className="max-h-full max-w-full object-contain p-2.5 group-hover:scale-105 transition-transform duration-300 drop-shadow-[0_6px_12px_rgba(0,0,0,0.6)]"
            />
          ) : (
            <div className="flex flex-col items-center justify-center text-gray-600 gap-1.5 py-6">
              <Icon className="w-10 h-10 stroke-[1.2] opacity-40 text-gray-500" />
              <span className="text-[10px] font-mono uppercase tracking-wider text-gray-500">Hardware Preview</span>
            </div>
          )}
        </div>

        {/* Item Brand & Name */}
        <div className="mb-3">
          <div className="text-[11px] font-mono text-gray-400 font-semibold tracking-wider uppercase mb-0.5">
            {item.brand}
          </div>
          <h3 className="text-base font-bold text-white group-hover:text-[#ff8533] transition-colors leading-snug">
            {item.name}
          </h3>
        </div>

        {/* Score & Satisfaction Banner */}
        <div className="bg-[#0b0e16] border border-gray-800/80 rounded-xl p-3 mb-4">
          <div className="flex items-center justify-between mb-2">
            <div>
              <div className="text-[10px] font-mono uppercase text-gray-400">
                {selectedYear === 'All' ? 'Combined Score' : `${selectedYear} Score`}
              </div>
              <div className="flex items-baseline gap-1.5">
                <span className="text-xl font-extrabold text-[#ff6600] font-mono">
                  {hackerScore}
                </span>
                <span className="text-[10px] text-gray-500">pts</span>
              </div>
            </div>

            <div className="text-right">
              <div className="text-[10px] font-mono uppercase text-gray-400">
                Satisfaction
              </div>
              <div className="flex items-center gap-1 justify-end font-mono">
                <ShieldCheck className={`w-3.5 h-3.5 ${satisfactionRate >= 80 ? 'text-emerald-400' : 'text-amber-400'}`} />
                <span className={`text-sm font-bold ${satisfactionRate >= 80 ? 'text-emerald-400' : 'text-amber-400'}`}>
                  {satisfactionRate}%
                </span>
              </div>
            </div>
          </div>

          {/* Sentiment Polarity Distribution Bar */}
          <div>
            <div className="h-1.5 w-full bg-gray-800/80 rounded-full overflow-hidden flex mb-1.5">
              <div style={{ width: `${posWidth}%` }} className="bg-emerald-500 h-full" title={`Positive: ${posUsers} unique authors`} />
              <div style={{ width: `${neuWidth}%` }} className="bg-gray-600 h-full" title={`Neutral: ${neuUsers} unique authors`} />
              <div style={{ width: `${negWidth}%` }} className="bg-rose-500 h-full" title={`Caution: ${negUsers} unique authors`} />
            </div>

            <div className="flex items-center justify-between text-[10px] font-mono text-gray-400">
              <span className="flex items-center gap-1 text-emerald-400">
                <ThumbsUp className="w-2.5 h-2.5" /> {posUsers} endorsed
              </span>
              <span className={`flex items-center gap-1 ${neuUsers > 0 ? 'text-gray-300' : 'text-gray-500'}`}>
                <Minus className="w-2.5 h-2.5 text-gray-500" /> {neuUsers} neutral
              </span>
              {negUsers > 0 ? (
                <span className="flex items-center gap-1 text-rose-400">
                  <ThumbsDown className="w-2.5 h-2.5" /> {negUsers} cautions
                </span>
              ) : (
                <span className="text-gray-500">0 warnings</span>
              )}
            </div>
          </div>
        </div>

        {/* Tags */}
        {item.tags && item.tags.length > 0 && (
          <div className="flex flex-wrap gap-1.5 mb-4">
            {item.tags.slice(0, 3).map((tag, idx) => (
              <span 
                key={idx} 
                className="text-[10px] bg-gray-800/60 text-gray-300 px-2 py-0.5 rounded-md border border-gray-700/50"
              >
                {tag}
              </span>
            ))}
          </div>
        )}
      </div>

      {/* Featured HN Quote Snippet */}
      <div>
        {topQuote ? (
          <div className="bg-[#10141f] border border-gray-800/70 rounded-xl p-3 mb-3 relative group/quote">
            <div className="flex items-center justify-between text-[11px] text-gray-400 mb-1.5 font-mono">
              <span className="flex items-center gap-1 text-[#ff8533]">
                <MessageSquareQuote className="w-3.5 h-3.5" />
                <span>@{topQuote.author}</span>
              </span>
              <span className="text-gray-500">{topQuote.date}</span>
            </div>
            <p className="text-xs text-gray-300 italic line-clamp-2 leading-relaxed">
              "{topQuote.snippet}"
            </p>
          </div>
        ) : (
          <div className="text-xs text-gray-400 italic mb-3">
            Referenced in discussions without extracted single-sentence quotes.
          </div>
        )}

        {/* Footer Action */}
        <div className="pt-2 border-t border-gray-800/60 flex items-center justify-between text-xs font-medium text-gray-400 group-hover:text-white transition-colors">
          <span>Inspect {totalUsers} HN {selectedYear === 'All' ? '' : `${selectedYear} `}reviews</span>
          <ChevronRight className="w-4 h-4 text-gray-500 group-hover:text-[#ff6600] group-hover:translate-x-0.5 transition-all" />
        </div>
      </div>
    </div>
  );
}
