# HackerGear ⚙️

<p align="left">
  <a href="./README_CN.md">中文</a> | <b>English</b>
</p>

> **Hacker News Hardware Recommendations** — Mined and sentiment-ranked developer hardware guide powered by authentic community discussions.

---

## 📖 Overview

**HackerGear** is an open-source hardware ranking and purchasing guide crafted for programmers, software engineers, and tech enthusiasts. By executing automated data mining and domain-specific sentiment analysis across hundreds of thousands of Hacker News (HN) comments, HackerGear extracts, deduplicates, and ranks hardware devices to reflect authentic, long-term developer consensus.

### Why HackerGear?
Traditional tech review platforms and affiliate hardware lists are frequently compromised by sponsored placements, kickbacks, and referral bias. Conversely, raw mention counts in community threads fall victim to the **"Controversy Trap"** — where a flawed or polarizing product racks up high mention numbers simply due to heated arguments and complaints.

HackerGear solves this by:
- **Defeating the Controversy Trap**: Scoring is weighted by **Unique Authors** rather than raw comment counts. Endless flame wars between two users will not artificially inflate a score.
- **Bi-directional Sentiment Analysis**: The algorithm distinguishes glowing endorsements (e.g., curing RSI pain, bulletproof durability, daily-driver setups) from caveats and returns (e.g., poor ergonomics, firmware bugs, quality control failures).
- **Year-over-Year Trend Tracking**: Directly compares 2025 and 2026 discussion editions to visualize shifting developer preferences.

---

## ✨ Features

- ⌨️ **Five Core Geek Hardware Categories**
  - **Keyboards**: Kinesis Advantage 360 / 2, ZSA Moonlander, ZSA Voyager, Ergodox EZ, HHKB Professional, Corne, Keychron, etc.
  - **Mice & Trackballs**: Logitech MX Master 3S, Kensington SlimBlade / Expert, Elecom Deft Pro, Apple Magic Trackpad, etc.
  - **Monitors**: Dell UltraSharp 40 5K2K, LG DualUp 28MQ780, Apple Studio Display, ASUS ProArt, etc.
  - **Ergonomic Chairs**: Herman Miller Aeron & Embody, Steelcase Gesture & Leap V2, Haworth Fern, etc.
  - **Laptops**: Apple MacBook Pro (M-Series), Framework Laptop 13/16, Lenovo ThinkPad X1 Carbon / T14, etc.

- 🧠 **Transparent Ranking Algorithm (Hacker Score)**
  - Master formula:
    $$\text{Score} = \text{Net Positive} \times (1 + \text{Satisfaction Rate}) \times (1 + \text{Confidence})$$
  - **Net Positive**: Unique positive recommenders minus unique negative critics.
  - **Satisfaction Rate**: $\frac{\text{Positive}}{\text{Positive} + \text{Negative}}$, assessing community consensus.
  - **Confidence Weighting**: Logarithmic dampening based on author volume, preventing single-comment outliers from topping the charts while still allowing rising gems to surface.

- 💬 **Curated Hacker News Quotes**
  - Read authentic excerpts from HN developers directly on each hardware profile, highlighting both enthusiastic praise and critical caveats with direct permalinks to original HN threads.

- 📈 **Historical Trends (2025 vs 2026)**
  - Toggle between annual editions with visual ranking indicators (rank rises, falls, or newly debuted items).

- ⚡ **Modern & Blazing Fast UI**
  - Fully static, instant client-side rendering with Tailwind CSS v4, dynamic search, multi-factor sorting, category tabs, and accessible modal dialogs.

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: [React 18](https://react.dev/)
- **Build Tool**: [Vite 6](https://vitejs.dev/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **Icons**: [Lucide React](https://lucide.dev/)

### Data Mining Pipeline
- **Language**: Python 3.10+
- **Data Mining**:
  - [Algolia HN Search API](https://hn.algolia.com/api): Captures recurring "Ask HN: What hardware/chair/keyboard do you use?" discussion threads.
  - [DuckDB](https://duckdb.org/): Direct remote streaming queries over full Hacker News Parquet archives on Hugging Face.
- **Sentiment Engine**: Tailored hardware lexicon and clause polarity classification (`sentiment.py`).
- **Catalog Registry**: Multi-pattern regex matching and entity disambiguation (`hardware_catalog.py`).

---

## 📂 Project Structure

```text
hackergear/
├── index.html                 # Main HTML entrypoint
├── vite.config.js             # Vite configuration
├── package.json               # Node.js project scripts & dependencies
├── README.md                  # English documentation (this file)
├── README_CN.md               # Chinese documentation (中文文档)
├── public/                    # Static public assets & hardware images
│   └── images/hardware/
├── src/
│   ├── main.jsx               # React DOM initialization
│   ├── App.jsx                # Core dashboard layout, state & filters
│   ├── index.css              # Global styles & Tailwind CSS imports
│   ├── components/            # UI Components
│   │   ├── Header.jsx         # Header & logo navigation
│   │   ├── YearSelector.jsx   # Edition selector (2025 / 2026)
│   │   ├── CategoryNav.jsx    # Hardware category tabs
│   │   ├── FilterBar.jsx      # Search, sort & zero-mention filters
│   │   ├── HardwareCard.jsx   # Hardware card (score, specs, stats, rank)
│   │   ├── ItemDetailModal.jsx# Detail modal with specs & curated HN quotes
│   │   └── ExplainerModal.jsx # Algorithm breakdown modal
│   └── data/
│       └── hardware_data.json # Mined hardware dataset
├── scripts/                   # Python data pipeline
│   ├── mine_hn.py             # Hybrid data mining runner
│   ├── mine_duckdb.py         # DuckDB remote parquet mining logic
│   ├── hardware_catalog.py    # Hardware definitions & regex patterns
│   ├── sentiment.py           # Hardware sentiment extraction rules
│   └── download_hardware_images.py # Image scraper & downloader
├── tests/                     # Unit test suites
│   └── test_sentiment.py      # Sentiment engine test cases
└── LICENSE                    # GNU GPL v3 License
```

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Node.js (v18+ recommended) and npm installed. Python 3.10+ is required if you wish to run the data mining pipeline.

```bash
node -v
python3 --version
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start Development Server

```bash
npm run dev
```
Open your browser at the local server address (usually `http://localhost:5173`).

### 4. Build for Production

```bash
npm run build
```
Production assets are generated in the `dist/` directory, ready for deployment on GitHub Pages, Vercel, Cloudflare Pages, or Netlify.

To preview the production build locally:
```bash
npm run preview
```

---

## 🧪 Mining & Automated Tests

### Run Unit Tests
Verify sentiment analysis classification accuracy:

```bash
python3 -m unittest discover tests
```

### Refresh Mined Dataset
Re-run the mining pipeline to fetch recent HN discussions and update `src/data/hardware_data.json`:

```bash
npm run mine
# or directly:
python3 scripts/mine_hn.py
```

---

## 📄 License

This project is licensed under the [GNU General Public License v3.0 (GPLv3)](file:///root/novel/hackergear/LICENSE).
