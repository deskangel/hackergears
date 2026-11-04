# HackerGear ⚙️

<p align="left">
  <b>中文</b> | <a href="./README.md">English</a>
</p>

> **Hacker News 硬件口碑榜** —— 基于真实社区讨论挖掘与情绪分析的开发者生产力硬件指南。
> Mined and sentiment-ranked hardware recommendations from Hacker News discussions.

---

## 📖 项目简介 (Overview)

**HackerGear** 是一个面向程序员与开发者的开源硬件榜单与选购指南。它通过全自动数据挖掘与情感分析算法，对 Hacker News (HN) 社区海量讨论中的硬件设备进行提取、去重、情感极性判定与置信度加权，真实还原开发者群体的实际使用体验与长期口碑。

### 为什么需要 HackerGear？
在传统的硬件评测与电商榜单中，充斥着商业赞助、返利营销与刷单水军；而在社区讨论中，单一的提及次数又容易陷入“争议陷阱”（即一款充满缺陷或极具争议的产品因为被吐槽而拥有虚高的讨论量）。

HackerGear 致力于解决这些问题：
- **抵御争议陷阱**：按独立发帖/评论作者（Unique Authors）进行统计与加权，单纯的盖楼与争吵不会虚增得分。
- **正反双向情绪判定**：深入识别开发者的正向力荐（如缓解 RSI 手腕酸痛、提高工效）与负向警告（如质量品控问题、退货避坑）。
- **历年趋势洞察**：对比 2025 与 2026 年度讨论趋势，直观掌握硬件在极客圈的口碑演变。

---

## ✨ 核心特性 (Features)

- ⌨️ **九大核心极客硬件分类 (40+ 款生产力装备)**
  - **Keyboards（机械/分体人体工学键盘）**：Kinesis Advantage 360、ZSA Moonlander、Ergodox EZ、HHKB Professional、Corne、Keychron Q/V 系列等。
  - **Mice & Trackballs（鼠标/人体工学轨迹球）**：Logitech MX Master 3S、Magic Trackpad、Kensington SlimBlade、Logitech MX Ergo、Elecom Deft Pro 等。
  - **Monitors（编程显示器）**：Dell UltraSharp 40 5K2K、Apple Studio Display、LG DualUp、LG C3/C4 OLED、ASUS ProArt 等。
  - **Chairs（人体工学椅）**：Herman Miller Aeron / Embody、Steelcase Gesture / Leap V2、Haworth Fern 等。
  - **Laptops（主力开发笔记本）**：MacBook Pro (M-Series)、Framework Laptop 13/16、ThinkPad X1 Carbon、ThinkPad T14、ROG Zephyrus G14 等。
  - **Audio & ANC（降噪耳机与音频）**：Sony WH-1000XM4/XM5、Apple AirPods Pro 2 / Max、Bose QuietComfort 45、Sennheiser HD 600/650、Shure SM7B/MV7 等。
  - **Desk Accessories（桌面配件与工效周边）**：CalDigit TS4 雷电扩展坞、BenQ ScreenBar 屏幕挂灯、Ergotron LX 机械悬臂支架、Uplift V2 / Fully Jarvis 电动升降桌等。
  - **Mini PCs & Homelab（小主机与迷你服务器）**：Apple Mac mini (M系列)、Raspberry Pi 5/4 单板机、Intel NUC、Minisforum/Beelink AMD 迷你主机等。
  - **Network & NAS（网络与私有云存储）**：Ubiquiti UniFi Cloud Gateway & AP、Synology DiskStation (DS920+/DS923+) 等。

- 🧠 **透明且严谨的 Hacker Score 评分算法**
  - 主公式：
    $$\text{Score} = \text{Net Positive} \times (1 + \text{Satisfaction Rate}) \times (1 + \text{Confidence})$$
  - **Net Positive**：正向推荐作者数减去负向批评作者数。
  - **Satisfaction Rate**：好评满意度占比（正向 / (正向 + 负向)）。
  - **Confidence**：样本量置信度平滑加权，既鼓励优质小众神器，又防止单一样本偶然性偏差。

- 💬 **真实社区原声精选 (HN Quotes)**
  - 精选每款硬件在 HN 讨论中的真实引用，高亮赞同观点与吐槽警示，提供原汁原味的极客反馈与原帖直达链接。

- 📈 **年份与趋势对比**
  - 支持在 2025 与 2026 年度数据之间平滑切换，提供榜单名次变化指示器（上升/下降/新上榜）。

- ⚡ **现代极致交互体验**
  - 极速响应的纯客户端静态渲染，支持多维度即时搜索、分类过滤、排序切换（Hacker Score / 满意度 / 讨论热度）与详情弹窗。

---

## 🛠️ 技术栈 (Tech Stack)

### 前端 (Frontend)
- **Framework**: [React 18](https://react.dev/)
- **Build Tool**: [Vite 6](https://vitejs.dev/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **Icons**: [Lucide React](https://lucide.dev/)

### 数据挖掘管线 (Data Mining Pipeline)
- **Language**: Python 3.10+
- **Data Mining**:
  - [Algolia HN Search API](https://hn.algolia.com/api)：采集 Ask HN 经典硬件讨论主题
  - [DuckDB](https://duckdb.org/)：远程直接流式查询分析 Hugging Face 上的全量 Hacker News Parquet 数据集
- **NLP / 情绪分析**: 针对硬件评测领域深度定制的分词与极性分类规则库（`sentiment.py`）
- **实体库**: 严密正则匹配与消歧字典（`hardware_catalog.py`）

---

## 📂 项目结构 (Directory Layout)

```text
hackergear/
├── index.html                 # 入口 HTML
├── vite.config.js             # Vite 构建配置
├── package.json               # Node.js 项目依赖与运行脚本
├── public/                    # 静态资源与硬件官方图像
│   └── images/hardware/
├── src/
│   ├── main.jsx               # React 挂载入口
│   ├── App.jsx                # 主页面布局与筛选/排序状态管理
│   ├── index.css              # 全局样式与 Tailwind 引入
│   ├── components/            # React 业务组件
│   │   ├── Header.jsx         # 顶部导航与品牌栏
│   │   ├── YearSelector.jsx   # 年份切换器 (2025 / 2026)
│   │   ├── CategoryNav.jsx    # 硬件五大类别切换胶囊
│   │   ├── FilterBar.jsx      # 搜索、排序与展示开关
│   │   ├── HardwareCard.jsx   # 硬件卡片（评分、满意度、参数、趋势）
│   │   ├── ItemDetailModal.jsx# 详细弹窗（规格、真实原声精选）
│   │   └── ExplainerModal.jsx # 算法与计分机制解析弹窗
│   └── data/
│       └── hardware_data.json # 挖掘生成的结构化榜单数据
├── scripts/                   # Python 数据挖掘管线
│   ├── mine_hn.py             # 混合数据挖掘主入口
│   ├── mine_duckdb.py         # DuckDB 远程 Hugging Face 挖掘脚本
│   ├── hardware_catalog.py    # 硬件实体库与正则定义
│   ├── sentiment.py           # 硬件情感分析与引文提取
│   └── download_hardware_images.py # 硬件配图下载与优化脚本
├── tests/                     # 自动化测试
│   └── test_sentiment.py      # 情绪分析单元测试
└── LICENSE                    # GNU GPL v3 开源协议
```

---

## 🚀 快速上手 (Quick Start)

### 1. 环境准备
确保本地安装了 Node.js（推荐 v18+）与 npm。如需运行数据挖掘，需具备 Python 3.10+。

```bash
node -v
python3 --version
```

### 2. 安装依赖

```bash
npm install
```

### 3. 启动开发服务器

```bash
npm run dev
```
打开浏览器访问控制台提示的地址（通常为 `http://localhost:5173`）。

### 4. 构建生产产物

```bash
npm run build
```
产物将输出至 `dist/` 目录，可直接部署在 GitHub Pages、Vercel、Cloudflare Pages 等静态托管平台。

预览构建后的生产包：
```bash
npm run preview
```

---

## 🧪 运行测试与数据挖掘 (Mining & Tests)

### 运行单元测试
测试情感分析算法的准确性：

```bash
python3 -m unittest discover tests
```

### 重新挖掘与更新数据
重新抓取最新的 Hacker News 讨论并更新 `src/data/hardware_data.json`：

```bash
npm run mine
# 或者直接运行:
python3 scripts/mine_hn.py
```

---

## 📄 开源许可 (License)

本项目基于 [GNU General Public License v3.0 (GPLv3)](file:///root/novel/hackergear/LICENSE) 协议开源。
