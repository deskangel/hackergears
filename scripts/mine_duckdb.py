"""
mine_duckdb.py
Enriches HackerGear dataset by running DuckDB remote SQL over Hugging Face Parquet files
for 2025 and 2026.
"""

import duckdb
from hardware_catalog import CATALOG
from sentiment import clean_hn_html

def get_hardware_sql_filter():
    terms = [
        "kinesis", "advantage 360", "moonlander", "hhkb", "happy hacking", "keychron",
        "ergodox", "glove80", "corne", "voyager",
        "mx master", "magic trackpad", "trackball", "slimblade", "mx ergo", "vertical mouse",
        "ultrasharp", "studio display", "oled c3", "oled c4", "ultrafine", "proart",
        "aeron", "embody", "steelcase leap", "gesture", "haworth fern", "ergonomic chair",
        "macbook pro", "framework laptop", "framework 13", "framework 16", "thinkpad x1",
        "thinkpad t14", "zephyrus g14"
    ]
    clauses = [f"text ILIKE '%{term}%'" for term in terms]
    return " OR ".join(clauses)

def mine_parquet_months(parquet_urls):
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs;")
    
    comments = []
    sql_filter = get_hardware_sql_filter()
    
    for url in parquet_urls:
        print(f"Scanning remote Parquet: {url} ...")
        query = f"""
            SELECT id, "by", time, text, parent
            FROM '{url}'
            WHERE type = 2 AND text IS NOT NULL AND ({sql_filter})
            LIMIT 600
        """
        try:
            rows = con.execute(query).fetchall()
            print(f"  -> Extracted {len(rows)} candidate comments.")
            for r in rows:
                cid = str(r[0])
                author = r[1] or "anonymous"
                time_val = str(r[2])
                text = r[3]
                comments.append({
                    "id": cid,
                    "author": author,
                    "created_at": time_val,
                    "text": text,
                    "story_title": "Hacker News Discussion",
                    "source": "huggingface_parquet"
                })
        except Exception as e:
            print(f"Error querying {url}: {e}")
            
    return comments
