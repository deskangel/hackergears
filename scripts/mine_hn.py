"""
mine_hn.py
Full Hybrid Mining Pipeline: Algolia Search + DuckDB Remote Hugging Face Parquet.
Mines 2025 and 2026 Hacker News discussions.
"""

import os
import re
import json
import time
import math
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from hardware_catalog import CATALOG
from sentiment import clean_hn_html, extract_mention_context, analyze_sentiment_clause
from mine_duckdb import mine_parquet_months

USER_AGENT = "HackerGear-DataMiner/1.0"

def fetch_algolia_json(url: str, retries: int = 3) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=15) as res:
                return json.loads(res.read().decode("utf-8"))
        except Exception as e:
            if attempt == retries - 1:
                return {}
            time.sleep(0.5)
    return {}

def mine_algolia_threads():
    """Mines comments from major hardware recommendation Ask HN threads."""
    print(">>> [1/3] Mining Ask HN hardware threads via Algolia...")
    queries = [
        "Ask HN What keyboard do you use",
        "Ask HN Favorite ergonomic chair",
        "Ask HN Best monitor for programming",
        "Ask HN Best mouse or trackball",
        "Ask HN laptop for development",
        "Ask HN ergonomic equipment RSI",
        "Ask HN hardware recommendations",
        "Ask HN mechanical keyboard"
    ]
    
    threads = []
    for q in queries:
        encoded = urllib.parse.quote(q)
        url = f"https://hn.algolia.com/api/v1/search?query={encoded}&tags=story&hitsPerPage=5"
        data = fetch_algolia_json(url)
        for hit in data.get("hits", []):
            story_id = hit.get("objectID")
            title = hit.get("title", "")
            if story_id and any(w in title.lower() for w in ["keyboard", "chair", "monitor", "mouse", "laptop", "hardware", "ergonomic", "desk"]):
                threads.append((story_id, title))
        time.sleep(0.2)
    
    comments = []
    seen_ids = set()
    
    for story_id, title in threads[:15]:
        url = f"https://hn.algolia.com/api/v1/search?tags=comment,story_{story_id}&hitsPerPage=50"
        data = fetch_algolia_json(url)
        for hit in data.get("hits", []):
            cid = hit.get("objectID")
            if cid and cid not in seen_ids:
                seen_ids.add(cid)
                comments.append({
                    "id": cid,
                    "author": hit.get("author") or "anonymous",
                    "created_at": hit.get("created_at"),
                    "created_at_i": hit.get("created_at_i", 0),
                    "text": hit.get("comment_text", ""),
                    "story_title": title,
                    "story_id": story_id
                })
        time.sleep(0.2)
    
    print(f"Collected {len(comments)} comments from Ask HN threads.")
    return comments

def mine_algolia_item_keywords(timestamp_cutoff: int):
    """Mines targeted recent comments for each catalog item."""
    print(">>> [2/3] Mining targeted hardware comments from 2025-2026...")
    comments = []
    seen_ids = set()
    
    for item in CATALOG:
        keyword = item["primary_keyword"]
        encoded = urllib.parse.quote(f'"{keyword}"')
        url = f"https://hn.algolia.com/api/v1/search_by_date?query={encoded}&tags=comment&numericFilters=created_at_i>{timestamp_cutoff}&hitsPerPage=25"
        data = fetch_algolia_json(url)
        for hit in data.get("hits", []):
            cid = hit.get("objectID")
            if cid and cid not in seen_ids:
                seen_ids.add(cid)
                comments.append({
                    "id": cid,
                    "author": hit.get("author") or "anonymous",
                    "created_at": hit.get("created_at"),
                    "created_at_i": hit.get("created_at_i", 0),
                    "text": hit.get("comment_text", ""),
                    "story_title": hit.get("story_title") or "Hacker News Comment",
                    "story_id": hit.get("story_id")
                })
        time.sleep(0.1)
        
    print(f"Collected {len(comments)} targeted comments for catalog items.")
    return comments

def mine_duckdb_parquet():
    """Queries Hugging Face Parquet files for 2025 & 2026."""
    print(">>> [3/3] Querying Hugging Face Parquet (2025 & 2026) via DuckDB...")
    parquet_urls = [
        "https://huggingface.co/datasets/open-index/hacker-news/resolve/main/data/2025/2025-01.parquet",
        "https://huggingface.co/datasets/open-index/hacker-news/resolve/main/data/2025/2025-06.parquet",
        "https://huggingface.co/datasets/open-index/hacker-news/resolve/main/data/2025/2025-11.parquet",
        "https://huggingface.co/datasets/open-index/hacker-news/resolve/main/data/2026/2026-01.parquet",
        "https://huggingface.co/datasets/open-index/hacker-news/resolve/main/data/2026/2026-06.parquet"
    ]
    return mine_parquet_months(parquet_urls)

def process_and_rank_hardware(all_comments):
    print(f">>> Deduplicating and ranking {len(all_comments)} comments across {len(CATALOG)} hardware items...")
    
    compiled_catalog = []
    for item in CATALOG:
        regs = [re.compile(p, re.IGNORECASE) for p in item["patterns"]]
        compiled_catalog.append({
            "meta": item,
            "regexes": regs
        })

    # item_id -> year -> author -> counts
    records = {item["id"]: {"2026": {}, "2025": {}, "All": {}} for item in CATALOG}
    quotes = {item["id"]: {"2026": {"pos": [], "neg": []}, "2025": {"pos": [], "neg": []}, "All": {"pos": [], "neg": []}} for item in CATALOG}

    total_mentions = 0
    unique_authors_global = set()

    for c in all_comments:
        raw_text = c.get("text") or ""
        clean_text = clean_hn_html(raw_text)
        if not clean_text or len(clean_text) < 15:
            continue
        
        author = c.get("author") or "anonymous"
        cid = str(c.get("id"))
        created_at_str = str(c.get("created_at") or "")
        created_year = created_at_str[:4] if len(created_at_str) >= 4 else "2025"
        if created_year not in ["2025", "2026"]:
            created_year = "2025"

        unique_authors_global.add(author)
        permalink = f"https://news.ycombinator.com/item?id={cid}"

        for entry in compiled_catalog:
            item_id = entry["meta"]["id"]
            
            matched = False
            match_span = None
            for r in entry["regexes"]:
                m = r.search(clean_text)
                if m:
                    matched = True
                    match_span = m.span()
                    break
            
            if matched:
                total_mentions += 1
                snippet = extract_mention_context(clean_text, match_span[0], match_span[1])
                polarity, pos_words, neg_words = analyze_sentiment_clause(snippet)

                quote_obj = {
                    "id": cid,
                    "author": author,
                    "date": created_at_str[:10] if created_at_str else "2025",
                    "polarity": polarity,
                    "snippet": snippet,
                    "permalink": permalink,
                    "story_title": c.get("story_title") or "Discussion"
                }

                for target_year in [created_year, "All"]:
                    year_authors = records[item_id][target_year]
                    if author not in year_authors:
                        year_authors[author] = {"pos": 0, "neg": 0, "neu": 0}
                    
                    if polarity == 1:
                        year_authors[author]["pos"] += 1
                        if len(quotes[item_id][target_year]["pos"]) < 12:
                            quotes[item_id][target_year]["pos"].append(quote_obj)
                    elif polarity == -1:
                        year_authors[author]["neg"] += 1
                        if len(quotes[item_id][target_year]["neg"]) < 8:
                            quotes[item_id][target_year]["neg"].append(quote_obj)
                    else:
                        year_authors[author]["neu"] += 1

    editions_output = {}

    for year_label in ["2026", "2025", "All"]:
        item_scores = []
        for item in CATALOG:
            iid = item["id"]
            author_map = records[iid][year_label]
            
            u_pos = 0
            u_neg = 0
            u_neu = 0

            for auth, counts in author_map.items():
                if counts["pos"] > counts["neg"]:
                    u_pos += 1
                elif counts["neg"] > counts["pos"]:
                    u_neg += 1
                else:
                    u_neu += 1

            u_total = u_pos + u_neg + u_neu
            
            # Satisfaction %
            if (u_pos + u_neg) > 0:
                satisfaction_rate = round((u_pos / (u_pos + u_neg)) * 100, 1)
            else:
                satisfaction_rate = 100.0 if u_pos > 0 else 50.0

            # Confidence Multiplier
            confidence = math.log10(1 + u_total) * (u_total / (u_total + 2.0)) if u_total > 0 else 0

            # Hacker Score: (U_pos - 1.5 * U_neg) with floor 0, weighted by satisfaction and log-confidence
            net_positive = max(0.0, float(u_pos - 1.5 * u_neg + 0.15 * u_neu))
            hacker_score = round(net_positive * (1.0 + (satisfaction_rate / 100.0)) * (1.0 + confidence), 1)

            # Controversy Index: High when opinions are mixed and mention volume is high
            if u_total >= 3 and u_pos > 0 and u_neg > 0:
                controversy_index = round((min(u_pos, u_neg) / u_total) * 100 * math.log(1 + u_total), 1)
            else:
                controversy_index = 0.0

            item_scores.append({
                **item,
                "stats": {
                    "hacker_score": hacker_score,
                    "unique_users": u_total,
                    "positive_users": u_pos,
                    "negative_users": u_neg,
                    "neutral_users": u_neu,
                    "satisfaction_rate": satisfaction_rate,
                    "controversy_index": controversy_index
                },
                "quotes": {
                    "positive": quotes[iid][year_label]["pos"],
                    "caution": quotes[iid][year_label]["neg"]
                }
            })

        # Sort by Hacker Score descending, tiebreak on positive users
        item_scores.sort(key=lambda x: (x["stats"]["hacker_score"], x["stats"]["positive_users"]), reverse=True)
        
        for idx, it in enumerate(item_scores):
            it["rank"] = idx + 1
        
        editions_output[year_label] = item_scores

    return {
        "metadata": {
            "title": "HackerGear - Hacker News Hardware Recommendations",
            "description": "Scored by unique-author weighting and sentiment polarity across 2025-2026 discussions.",
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "total_comments_analyzed": len(all_comments),
            "total_mentions_identified": total_mentions,
            "total_unique_authors": len(unique_authors_global),
            "years_covered": ["2026", "2025", "All"]
        },
        "editions": editions_output
    }

def main():
    print("==================================================")
    print("HackerGear: Mining HN Discussions (2025 - 2026)")
    print("==================================================")
    
    timestamp_cutoff = 1735689600 # 2025-01-01
    comments = []
    
    comments.extend(mine_algolia_threads())
    comments.extend(mine_algolia_item_keywords(timestamp_cutoff))
    
    try:
        duck_comments = mine_duckdb_parquet()
        comments.extend(duck_comments)
    except Exception as e:
        print(f"DuckDB step warning: {e}")
        
    # Deduplicate
    unique_dict = {}
    for c in comments:
        cid = str(c.get("id"))
        if cid and cid not in unique_dict:
            unique_dict[cid] = c
            
    deduped = list(unique_dict.values())
    print(f"Total deduplicated comments: {len(deduped)}")
    
    dataset = process_and_rank_hardware(deduped)
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "src", "data")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "hardware_data.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Updated dataset written to: {out_file}")

if __name__ == "__main__":
    main()
