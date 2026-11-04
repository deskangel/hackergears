# HackerGear Agent Development Rules & Guidelines

This document specifies mandatory rules and quality baselines for developing, data-mining, and maintaining **HackerGear**. These rules are derived from real regressions and edge-case fixes in prior development sessions and MUST be strictly enforced.

---

## 1. Hardware Catalog & Regex Matching (Anti-False-Positive Rules)

1. **No Overly Generic Single-Word Patterns**:
   - **FORBIDDEN**: Generic dictionary words or programming terms matching alone.
     - ❌ `r"\bembody\b"` (matches "this project embodies the open source spirit")
     - ❌ `r"\bframework\b"` (matches web frameworks like React, Django, Rails)
     - ❌ `r"\bhappy\s+hacking\b"` (matches colloquial phrase "happy hacking!")
     - ❌ `r"\bvoyager\b"` (matches Star Trek, Voyager spacecraft, or unrelated software)
     - ❌ `r"\bcorne\b"` (matches French words or non-English typos without keyboard context)
     - ❌ `r"\bfern\b"` (matches plants or non-furniture references)
   - **REQUIRED**: Always require brand names, category context, or model-specific tokens:
     - ✅ `r"\bherman\s+miller\s+embody\b"`, `r"\bembody\s+(chair|seat|gaming)\b"`, `r"\bhm\s+embody\b"`
     - ✅ `r"\bframework\s+laptop\b"`, `r"\bframework\s+(12|13|16)\b"`
     - ✅ `r"\bhhkb\b"`, `r"\bhappy\s+hacking\s+keyboard\b"`
     - ✅ `r"\bzsa\s+voyager\b"`, `r"\bvoyager\s+keyboard\b"`
     - ✅ `r"\bhaworth\s+fern\b"`, `r"\bfern\s+chair\b"`

2. **Boundary Anchoring**:
   - Always use word boundary delimiters `\b...\b`.
   - Use case-insensitive matching (`re.IGNORECASE`).

3. **Entity Uniqueness & Disambiguation**:
   - Every hardware entity must have a unique `id`, clear `brand`, designated `category`, accurate `specs`, `price_tier`, and informative `tags`.

---

## 2. HN Quotes & Sentiment Integrity Rules

1. **Authentic Hacker News Attribution**:
   - All quotes displayed in HackerGear must originate from actual Hacker News items or comments.
   - `permalink` MUST be a valid `https://news.ycombinator.com/item?id=<ID>` link.
   - `author` must be the real HN username (never synthetic or hallucinated names).
   - `date` must correspond to the actual post timestamp (YYYY-MM-DD).

2. **Strict Sentiment Polarity (`polarity`) Classification**:
   - **Positive (`1`)**: Explicit user endorsement, daily driving with satisfaction, pain relief (e.g. RSI mitigation, comfort, durability), or strong recommendation.
   - **Negative (`-1`)**: Definite warnings, build quality defects, firmware glitches, returning/regretting the purchase, or ergonomic pain caused by the device.
   - **Neutral (`0`)**: Factual discussion, spec comparison without emotional preference, setup questions, or balanced pros & cons.
   - **Disambiguation Guard**: Do NOT attribute criticism of an operating system or software (e.g., Linux sleep issues, macOS window management) as a hardware flaw unless directly related to hardware drivers or firmware.

3. **Context Snippet Quality**:
   - Snippets must be concise, readable sentences directly discussing the hardware in question.
   - Strip raw HTML tags (`<p>`, `<code>`, `<a>`, `<i>`, etc.) and HTML entities (`&#x27;`, `&quot;`, `&amp;`).

---

## 3. Product Imagery Rules

1. **Authentic Official Imagery Only**:
   - Never use random unsorted placeholders or generic stock photos that depict a different model.
   - Every image must accurately portray the exact product model (e.g., Logitech MX Ergo must show the trackball mouse, not a normal MX Master mouse; Herman Miller Embody must depict the distinctive spine backrest).
   - Images should be stored locally in `public/images/hardware/` in clean `.webp`, `.png`, or `.jpg` formats.
   - Web cards and modal views should provide smooth image fallbacks (e.g., elegant icon/badge placeholder) in case network or assets fail to load.

---

## 4. Multi-Edition & Scoring Consistency Rules

1. **Editions Synchrony**:
   - Data must maintain three synchronized views: `2026`, `2025`, and `All`.
   - Every catalog item should exist across all three editions in `src/data/hardware_data.json`. Items with zero mentions in a given year should record `unique_users: 0` and `hacker_score: 0`.

2. **Mathematical Consistency**:
   - `unique_users` = `positive_users` + `negative_users` + `neutral_users`
   - `satisfaction_rate` = $\frac{\text{positive\_users}}{\text{positive\_users} + \text{negative\_users}} \times 100\%$ (when positive + negative > 0, else 0%)
   - `hacker_score` must follow the formula:
     $$\text{Score} = \max(0, \text{Net Positive}) \times (1 + \text{Satisfaction Rate}) \times (1 + \text{Confidence})$$
   - Ranks must be dynamically computed based on descending `hacker_score`.

---

## 5. UI & Responsive Layout Rules

1. **Category Navigation Scalability**:
   - When new hardware categories are added, `CategoryNav` must remain aesthetically balanced across mobile (narrow screen) and desktop (wide screen).
   - Use flexible wrapping (`flex-wrap`) or modern horizontal scroll with subtle scrollbars to prevent awkward wrapping or horizontal page-breaking overflow.
   - Dynamic item counts per category must update immediately when switching between `2026`, `2025`, and `All`.

2. **Zero-Mention Handling**:
   - By default, items with zero mentions in the active year are filtered out from the leaderboard to keep rankings clean and high-signal, while keeping the toggle available for users who want to explore all catalog items.
