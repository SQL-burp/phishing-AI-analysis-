"""Email header parsing utilities."""

import re
from typing import Dict, Any
from email import message_from_string


def parse_headers(raw_email: str) -> Dict[str, Any]:
    """Extract key authentication and routing headers."""
    msg = message_from_string(raw_email)
    headers = {
        "from": msg.get("From"),
        "to": msg.get("To"),
        "subject": msg.get("Subject"),
        "date": msg.get("Date"),
        "message_id": msg.get("Message-ID"),
        "spf": "unknown",
        "dkim": "unknown",
        "dmarc": "unknown",
        "received_count": 0,
    }

    # Simple SPF/DKIM/DMARC extraction (expand as needed)
    auth_results = msg.get("Authentication-Results", "")
    if "spf=pass" in auth_results.lower():
        headers["spf"] = "pass"
    elif "spf=fail" in auth_results.lower():
        headers["spf"] = "fail"

    if "dkim=pass" in auth_results.lower():
        headers["dkim"] = "pass"
    if "dmarc=pass" in auth_results.lower():
        headers["dmarc"] = "pass"

    # Count Received headers
    headers["received_count"] = len(msg.get_all("Received") or [])

    return headers
