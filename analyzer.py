"""Core phishing email analyzer."""

from typing import Dict, Any, List
from .header_parser import parse_headers
from .url_checker import extract_and_score_urls


class PhishingAnalyzer:
    def __init__(self, virustotal_api_key: str = None):
        self.vt_key = virustotal_api_key

    def analyze_email(self, raw_email: str) -> Dict[str, Any]:
        """Analyze a raw email (string or .eml content)."""
        headers = parse_headers(raw_email)
        urls = extract_and_score_urls(raw_email)
        
        # Placeholder scoring
        risk_score = min(100, len(urls) * 15 + (20 if headers.get("spf") == "fail" else 0))
        
        return {
            "risk_score": risk_score,
            "severity": "HIGH" if risk_score >= 70 else "MEDIUM" if risk_score >= 40 else "LOW",
            "headers": headers,
            "urls": urls,
            "attachments": [],  # TODO: extract
            "recommendations": self._generate_recommendations(risk_score),
        }

    def _generate_recommendations(self, score: int) -> List[str]:
        recs = []
        if score >= 70:
            recs.append("Quarantine the email and block sender.")
            recs.append("Check all extracted URLs in VirusTotal.")
        elif score >= 40:
            recs.append("Review headers and links carefully.")
        else:
            recs.append("Low risk — standard review sufficient.")
        return recs
