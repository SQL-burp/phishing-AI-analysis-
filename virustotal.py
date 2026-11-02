"""VirusTotal integration stub."""

# TODO: Implement with vt-py or official API
# Example:
# from virustotal_python import Virustotal
# vt = Virustotal(API_KEY)
# resp = vt.request("url", {"url": target})

def check_url(url: str, api_key: str) -> dict:
    return {"status": "not_implemented", "url": url}

def check_hash(file_hash: str, api_key: str) -> dict:
    return {"status": "not_implemented", "hash": file_hash}
