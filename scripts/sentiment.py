"""
sentiment.py
Hardware-specific sentiment polarity classifier and quote extractor for HackerGear.
Distinguishes glowing endorsements from heated complaints and ergonomic warnings.
"""

import re
import html

# Endorsement & positive sentiment markers in hardware context
POSITIVE_MARKERS = [
    r"\blove\s+(it|them|this|the\b)",
    r"\bbest\s+(keyboard|mouse|monitor|chair|laptop|investment|purchase|hardware)\b",
    r"\bgreat\s+(keyboard|mouse|monitor|chair|laptop|experience|build|tool)\b",
    r"\bgame\s*changer\b",
    r"\bcured\s+(my\s+)?(rsi|pain|wrist|back|carpal)\b",
    r"\bsaved\s+(my\s+)?(wrists|wrist|back|life|hands)\b",
    r"\bhelped\s+(tremendously|so\s+much|greatly|a\s+lot|with\s+(my\s+)?(rsi|pain))\b",
    r"\bhighly\s+recommend\b",
    r"\bwould\s+recommend\b",
    r"\bcan('?t|not)\s+(go\s+back|live\s+without)\b",
    r"\bswitched\s+(to|from\s+\w+\s+to)\b",
    r"\bnever\s+looked\s+back\b",
    r"\bdaily\s+driver\b",
    r"\bworth\s+every\s+(penny|cent|dollar)\b",
    r"\bbuilt\s+like\s+a\s+tank\b",
    r"\bfantastic\b",
    r"\bincredible\b",
    r"\bamazing\b",
    r"\bflawless\b",
    r"\bholy\s+grail\b",
    r"\bpleasure\s+to\s+use\b",
    r"\bmuch\s+better\s+than\b",
    r"\bprefer\s+it\s+over\b",
    r"\bmy\s+favorite\b"
]

# Negative & warning markers (cautionary / complaint / return)
NEGATIVE_MARKERS = [
    r"\bhated\s+(it|them|this)\b",
    r"\breturned\s+(it|them|mine)\b",
    r"\bregret\s+(buying|it|purchasing)\b",
    r"\bcaused\s+(me\s+)?(pain|wrist|rsi|strain|injury|discomfort)\b",
    r"\buncomfortable\b",
    r"\boverpriced\b",
    r"\boverrated\b",
    r"\bterrible\b",
    r"\bhorrible\b",
    r"\bawful\b",
    r"\bjunk\b",
    r"\bbroke\s+(after|within|down|in\s+\d+)\b",
    r"\bbreaking\b",
    r"\bfailure\s+rate\b",
    r"\bdouble[- ]click(ing)?\s+issue\b",
    r"\bpoor\s+build\b",
    r"\bdon'?t\s+buy\b",
    r"\bwouldn'?t\s+recommend\b",
    r"\bdo\s+not\s+recommend\b",
    r"\bdisappointed\b",
    r"\bdisappointing\b",
    r"\bdriver\s+issues?\b",
    r"\bsoftware\s+is\s+garbage\b",
    r"\bgarbage\b",
    r"\bclunky\b",
    r"\bbloatware\b"
]

RE_POS = [re.compile(p, re.IGNORECASE) for p in POSITIVE_MARKERS]
RE_NEG = [re.compile(p, re.IGNORECASE) for p in NEGATIVE_MARKERS]

def clean_hn_html(text: str) -> str:
    """Cleans Hacker News HTML markup into clean markdown/text."""
    if not text:
        return ""
    # Unescape HTML entities (&x27; &gt; &lt; etc.)
    t = html.unescape(text)
    # Replace <p> with double newline
    t = re.sub(r"<\s*p\s*>", "\n\n", t, flags=re.IGNORECASE)
    t = re.sub(r"<\s*/\s*p\s*>", "", t, flags=re.IGNORECASE)
    # Replace <a href="...">text</a> with [text](url) or clean text
    t = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', t, flags=re.IGNORECASE)
    # Strip any remaining tags
    t = re.sub(r"<[^>]+>", "", t)
    return t.strip()

def extract_mention_context(full_text: str, match_start: int, match_end: int, window_chars: int = 240) -> str:
    """Extracts a readable context snippet around a hardware mention."""
    start = max(0, match_start - window_chars)
    end = min(len(full_text), match_end + window_chars)
    
    # Try snapping to sentence or clause boundaries
    snippet = full_text[start:end].strip()
    
    # Add ellipsis if truncated
    prefix = "... " if start > 0 else ""
    suffix = " ..." if end < len(full_text) else ""
    return f"{prefix}{snippet}{suffix}"

def analyze_sentiment_clause(clause_text: str):
    """
    Analyzes sentiment of a specific text window surrounding a mention.
    Returns:
        polarity: 1 (positive/endorsement), -1 (negative/complaint), 0 (neutral/informational)
        pos_matches: list of matched positive phrases
        neg_matches: list of matched negative phrases
    """
    pos_hits = []
    neg_hits = []

    for pattern in RE_POS:
        m = pattern.search(clause_text)
        if m:
            pos_hits.append(m.group(0))

    for pattern in RE_NEG:
        m = pattern.search(clause_text)
        if m:
            neg_hits.append(m.group(0))

    # Weighting: Negative signals take precedence if strongly formulated,
    # but balance if mixed.
    if len(neg_hits) > 0 and len(pos_hits) == 0:
        return -1, pos_hits, neg_hits
    elif len(pos_hits) > 0 and len(neg_hits) == 0:
        return 1, pos_hits, neg_hits
    elif len(pos_hits) > 0 and len(neg_hits) > 0:
        # Mixed: if negative has strong return/hated/broke signals, treat as caution (-1)
        if any(w in " ".join(neg_hits).lower() for w in ["hated", "returned", "broke", "regret", "don't buy"]):
            return -1, pos_hits, neg_hits
        elif len(pos_hits) > len(neg_hits):
            return 1, pos_hits, neg_hits
        else:
            return 0, pos_hits, neg_hits
    else:
        # Default neutral mention (neither strong praise nor condemnation)
        return 0, [], []
