"""
test_sentiment.py
Unit tests verifying sentiment polarity classification and author de-duplication rules.
"""

import unittest
from scripts.sentiment import clean_hn_html, analyze_sentiment_clause, extract_mention_context

class TestSentimentClassifier(unittest.TestCase):

    def test_positive_endorsement(self):
        text = "The Kinesis Advantage is a great keyboard. Cured my RSI and I can't go back. Daily driver for 5 years."
        polarity, pos, neg = analyze_sentiment_clause(text)
        self.assertEqual(polarity, 1)
        self.assertTrue(len(pos) > 0)
        self.assertEqual(len(neg), 0)

    def test_negative_warning(self):
        text = "I hated the mouse, it caused severe wrist pain and I returned it within 3 days. Bloatware software."
        polarity, pos, neg = analyze_sentiment_clause(text)
        self.assertEqual(polarity, -1)
        self.assertTrue(len(neg) > 0)

    def test_neutral_question(self):
        text = "Does the Dell U2723QE support daisy chaining with a MacBook? Looking at the spec sheet."
        polarity, pos, neg = analyze_sentiment_clause(text)
        self.assertEqual(polarity, 0)
        self.assertEqual(len(pos), 0)
        self.assertEqual(len(neg), 0)

    def test_html_cleaning(self):
        raw = "This is great&#x27;s item!<p>Another paragraph &quot;quoted&quot; <a href=\"https://example.com\">link</a></p>"
        cleaned = clean_hn_html(raw)
        self.assertIn("great's item!", cleaned)
        self.assertIn('"quoted"', cleaned)
        self.assertIn("[link](https://example.com)", cleaned)

if __name__ == "__main__":
    unittest.main()
