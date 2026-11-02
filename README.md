# Phishing AI Analysis (phishly.ly)

AI-assisted phishing email analysis toolkit. Combines header forensics, link/attachment extraction, indicator scoring, and integrations with common threat intel sources.

## Overview

This project helps analysts and security teams quickly triage suspicious emails by:

- Parsing email headers and extracting observables
- Scoring indicators of compromise
- Checking URLs, IPs, and file hashes against VirusTotal
- Providing hooks for automated workflows (mailbox polling, TheHive / Cortex / MISP style pipelines)

Inspired by tools such as PhishTool, ThePhish, Cyware Orchestrate, and VirusTotal.

## Project Structure

```
phishing-ai-analysis/
├── README.md
├── requirements.txt
├── phishly/
│   ├── __init__.py
│   ├── analyzer.py          # Core analysis engine
│   ├── header_parser.py     # Email header forensics
│   ├── url_checker.py       # URL / IP reputation
│   └── virustotal.py        # VirusTotal client (stub)
├── examples/
│   └── sample_email.eml
└── cli.py                   # Command-line interface
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Analyze an email file
python cli.py analyze examples/sample_email.eml

# Check a URL
python cli.py check-url "http://suspicious-link.example"
```

## Features (planned / stubbed)

- [x] Basic project skeleton
- [ ] Full email header parsing (SPF, DKIM, DMARC, Received chains)
- [ ] Link and attachment extraction
- [ ] VirusTotal integration
- [ ] Indicator scoring engine
- [ ] ThePhish / MISP export
- [ ] Mailbox polling automation

## License

MIT
