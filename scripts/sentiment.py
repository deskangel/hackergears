"""
sentiment.py
Hardware-specific sentiment polarity classifier and quote extractor for HackerGear.
Accurately distinguishes genuine endorsements, cautionary reviews, and handles
comparative statements, negations, and multi-device mentions.
"""

import re
import html

# Endorsement & positive sentiment markers in hardware context
POSITIVE_MARKERS = [
    r"\blove\s+(it|them|this|the\b)",
    r"\bbest\s+(keyboard|mouse|monitor|chair|laptop|investment|purchase|hardware)\b",
    r"\bgreat\s+(keyboard|mouse|monitor|chair|laptop|experience|build|tool|concept)\b",
    r"\bgame\s*changer\b",
    r"\bcured\s+(my\s+)?(rsi|pain|wrist|back|carpal)\b",
    r"\bsaved\s+(my\s+)?(wrists|wrist|back|life|hands)\b",
    r"\bhelped\s+(tremendously|so\s+much|greatly|a\s+lot|with\s+(my\s+)?(rsi|pain))\b",
    r"\bhighly\s+recommend\b",
    r"\bwould\s+recommend\b",
    r"\bcan('?t|not)\s+(go\s+back|live\s+without)\b",
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
    r"\bmy\s+favorite\b",
    r"\bno\s+complaints\b",
    r"\bzero\s+(regrets?|issues?|problems?)\b",
    r"\b(won'?t|wouldn'?t|never|no|not)\s+(have\s+)?(any\s+)?regrets?\b",
    r"\bnever\s+uncomfortable\b",
    r"\bnot\s+uncomfortable\b"
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
    r"\bbloatware\b",
    r"\bbuyer'?s\s+remorse\b",
    r"\b(terrible|awful|horrific|useless)\s+(keyboard|trackpad|screen|display|battery|performance)\b"
]

# Specific negation patterns that cancel negative markers
NEGATION_CANCEL_PATTERNS = [
    (re.compile(r"\b(won'?t|wouldn'?t|never|no|zero|don'?t|not)\s+(?:have\s+)?(?:any\s+)?regret", re.IGNORECASE), "regret"),
    (re.compile(r"\b(never|not|hardly)\s+(?:feel\s+|felt\s+)?uncomfortable", re.IGNORECASE), "uncomfortable"),
    (re.compile(r"\b(not|hardly|far\s+from)\s+(?:that\s+)?(?:awful|terrible|horrible|junk|garbage)", re.IGNORECASE), "awful|terrible|horrible|junk|garbage"),
    (re.compile(r"\b(no|zero|without)\s+(?:issues?|problems?|failures?)", re.IGNORECASE), "issue|problem|failure"),
]

RE_POS = [re.compile(p, re.IGNORECASE) for p in POSITIVE_MARKERS]
RE_NEG = [re.compile(p, re.IGNORECASE) for p in NEGATIVE_MARKERS]

def clean_hn_html(text: str) -> str:
    """Cleans Hacker News HTML markup into clean markdown/text."""
    if not text:
        return ""
    # Unescape HTML entities (&x27; &gt; &lt; etc.)
    t = html.unescape(text)
    # Normalize typography quotes
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
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
    
    # Try snapping backward to sentence start
    prev_boundary = -1
    for sep in ["\n\n", "\n", ". ", "? ", "! "]:
        idx = full_text.rfind(sep, start, match_start)
        if idx != -1:
            prev_boundary = max(prev_boundary, idx + len(sep))
    if prev_boundary != -1 and prev_boundary >= start:
        start = prev_boundary

    # Try snapping forward to sentence end
    next_boundary = len(full_text)
    for sep in ["\n\n", "\n", ". ", "? ", "! "]:
        idx = full_text.find(sep, match_end, end)
        if idx != -1:
            next_boundary = min(next_boundary, idx + (1 if sep == "\n" else 0))
    if next_boundary <= end:
        end = next_boundary

    snippet = full_text[start:end].strip()
    prefix = "... " if start > 0 and not full_text[start:start+4].startswith((">", "#")) else ""
    suffix = " ..." if end < len(full_text) else ""
    return f"{prefix}{snippet}{suffix}"

def strip_blockquotes(text: str) -> str:
    """Strips out blockquotes (lines starting with >)."""
    lines = text.split("\n")
    kept = [line for line in lines if not line.strip().startswith(">")]
    return "\n".join(kept)

def analyze_sentiment_clause(clause_text: str, target_name: str = None):
    """
    Analyzes sentiment of text surrounding a hardware mention.
    Properly handles comparative phrasing, negations, and cross-entity sentiments.
    """
    clean_text = clean_hn_html(clause_text)
    unquoted = strip_blockquotes(clean_text)

    # Check for conditional praise ("would love ... if ... wasn't crap")
    conditional_praise = re.search(r"\b(?:would|could)\s+love\b.*?\b(?:if|unless)\b", unquoted, re.IGNORECASE)

    pos_hits = []
    neg_hits = []

    for pattern in RE_POS:
        m = pattern.search(unquoted)
        if m:
            if conditional_praise and "love" in m.group(0).lower():
                continue
            pos_hits.append(m.group(0))

    # Match negative patterns unless negated
    for pattern in RE_NEG:
        m = pattern.search(unquoted)
        if m:
            hit = m.group(0)
            # Check if this hit is cancelled by a negation pattern
            cancelled = False
            for cancel_re, cancel_word in NEGATION_CANCEL_PATTERNS:
                if cancel_re.search(unquoted) and re.search(cancel_word, hit, re.IGNORECASE):
                    cancelled = True
                    break
            if not cancelled:
                neg_hits.append(hit)

    # Comparative / Remedy disambiguation:
    # "hated X ... bought [target] instead"
    remedy_patterns = [
        r"(?:hated|terrible|horrible|awful|broken|failed|garbage)\b.*?\b(?:bought|got|switched to|use)\b.*?(?:instead|replace)",
        r"(?:bought|got|use)\b.*?(?:instead|replace).*?\b(?:because|since)\b.*?(?:terrible|awful|hated|horrible)",
        r"(?:what\s+actually\s+helped\s+was|solved\s+by)\b.*?(?:tried\b.*?\bhated|uncomfortable)",
    ]
    for repat in remedy_patterns:
        if re.search(repat, unquoted, re.IGNORECASE):
            neg_hits = []
            if not pos_hits:
                pos_hits.append("remedy replacement")

    if conditional_praise and len(pos_hits) == 0:
        return -1, [], ["conditional dissatisfaction"]

    if len(neg_hits) > 0 and len(pos_hits) == 0:
        return -1, pos_hits, neg_hits
    elif len(pos_hits) > 0 and len(neg_hits) == 0:
        return 1, pos_hits, neg_hits
    elif len(pos_hits) > 0 and len(neg_hits) > 0:
        if any(w in " ".join(neg_hits).lower() for w in ["hated", "returned", "broke", "regret", "don't buy"]):
            return -1, pos_hits, neg_hits
        elif len(pos_hits) > len(neg_hits):
            return 1, pos_hits, neg_hits
        else:
            return 0, pos_hits, neg_hits
    else:
        return 0, [], []
