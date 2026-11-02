"""URL extraction and basic scoring."""

import re
from typing import List, Dict


URL_PATTERN = re.compile(
    r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\-._~:/?#\[\]@!$&\'()*+,;=%]*'
)


def extract_and_score_urls(text: str) -> List[Dict]:
    """Extract URLs and assign a simple risk score."""
    urls = URL_PATTERN.findall(text)
    results = []
    suspicious_keywords = ["login", "secure", "account", "verify", "update", "bank", "paypal"]

    for url in set(urls):  # dedupe
        score = 10
        lower = url.lower()
        if any(k in lower for k in suspicious_keywords):
            score += 30
        if any(ext in lower for ext in [".exe", ".zip", ".scr", ".js"]):
            score += 40
        if len(url) > 100:
            score += 10  # long URLs often suspicious

        results.append({
            "url": url,
            "score": min(score, 100),
            "flagged": score >= 40,
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)
