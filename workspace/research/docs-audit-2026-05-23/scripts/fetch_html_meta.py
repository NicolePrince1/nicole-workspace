#!/usr/bin/env python3
from urllib.request import Request, urlopen
from pathlib import Path
import re, html
urls = [
    "https://docs.oviond.com/",
    "https://docs.oviond.com/api/introduction",
    "https://docs.oviond.com/api/clients/create-client",
    "https://docs.oviond.com/mcp/overview",
    "https://docs.oviond.com/billing/plans",
]
out = Path("research/docs-audit-2026-05-23/raw/html")
out.mkdir(parents=True, exist_ok=True)
for u in urls:
    req = Request(u, headers={"User-Agent": "NicoleDocsAudit/1.0", "Accept": "text/html"})
    with urlopen(req, timeout=20) as r:
        text = r.read().decode("utf-8", "replace")
    name = u.replace("https://docs.oviond.com/", "").strip("/") or "root"
    name = name.replace("/", "__") + ".html"
    (out / name).write_text(text, encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", text, re.S)
    desc = re.search(r"<meta[^>]+name=[\"']description[\"'][^>]+content=[\"']([^\"']*)", text, re.I | re.S)
    canon = re.search(r"<link[^>]+rel=[\"']canonical[\"'][^>]+href=[\"']([^\"']*)", text, re.I | re.S)
    print("URL", u, "bytes", len(text))
    print(" title", html.unescape(title.group(1))[:180] if title else None)
    print(" desc", html.unescape(desc.group(1))[:220] if desc else None)
    print(" canon", canon.group(1) if canon else None)
    print(" has_noindex", "noindex" in text.lower(), "plant_store", "Plant Store" in text)
