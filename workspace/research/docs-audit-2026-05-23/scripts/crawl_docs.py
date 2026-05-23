#!/usr/bin/env python3
"""Crawl docs.oviond.com public documentation for launch QA.
No external deps; stores raw markdown plus JSON/CSV summaries.
"""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import ssl
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

BASE = "https://docs.oviond.com"
OUT = Path("research/docs-audit-2026-05-23")
RAW = OUT / "raw"
PAGES = RAW / "pages"
UA = "NicoleDocsAudit/1.0 (+https://oviond.com; launch QA)"
TIMEOUT = 20
SLEEP = 0.03

OUT.mkdir(parents=True, exist_ok=True)
RAW.mkdir(parents=True, exist_ok=True)
PAGES.mkdir(parents=True, exist_ok=True)

ctx = ssl.create_default_context()


def fetch(url: str) -> dict:
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/markdown,text/plain,text/html,application/json,*/*"})
    started = time.time()
    try:
        with urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            body = r.read()
            charset = r.headers.get_content_charset() or "utf-8"
            try:
                text = body.decode(charset, errors="replace")
            except LookupError:
                text = body.decode("utf-8", errors="replace")
            return {
                "url": url,
                "final_url": r.geturl(),
                "status": r.status,
                "content_type": r.headers.get("content-type", ""),
                "bytes": len(body),
                "text": text,
                "error": None,
                "elapsed_ms": round((time.time()-started)*1000),
            }
    except HTTPError as e:
        try:
            body = e.read()
            text = body.decode("utf-8", errors="replace")
        except Exception:
            text = ""
        return {"url": url, "final_url": getattr(e, "url", url), "status": e.code, "content_type": e.headers.get("content-type", "") if e.headers else "", "bytes": len(text.encode()), "text": text, "error": str(e), "elapsed_ms": round((time.time()-started)*1000)}
    except URLError as e:
        return {"url": url, "final_url": url, "status": None, "content_type": "", "bytes": 0, "text": "", "error": str(e), "elapsed_ms": round((time.time()-started)*1000)}


def save_text(name: str, text: str):
    (RAW / name).write_text(text, encoding="utf-8")


def norm_path(url_or_path: str) -> str | None:
    if not url_or_path:
        return None
    s = html.unescape(url_or_path.strip())
    if s.startswith("#"):
        return None
    if s.startswith("mailto:") or s.startswith("tel:") or s.startswith("javascript:"):
        return None
    if s.startswith("http://") or s.startswith("https://"):
        u = urlparse(s)
        if u.netloc != "docs.oviond.com":
            return None
        path = u.path
    else:
        # keep root-relative and simple relative urls as docs paths
        if s.startswith("/"):
            path = s
        else:
            path = "/" + s
    path = path.split("#", 1)[0].split("?", 1)[0]
    if path.endswith("/") and path != "/":
        path = path[:-1]
    if path.endswith(".md"):
        path = path[:-3]
    if path == "":
        path = "/"
    return path


def md_url_from_path(path: str) -> str:
    if path == "/":
        return BASE + "/introduction.md"
    return BASE + path + ".md"


def safe_file_for_path(path: str) -> str:
    if path == "/":
        return "index.md"
    return path.strip("/").replace("/", "__") + ".md"


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end+4:].lstrip()
    return text


def extract_links(md: str) -> list[tuple[str, str]]:
    out = []
    # markdown links/images
    for m in re.finditer(r"!?\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", md):
        out.append((m.group(1), m.group(2)))
    # MDX/html href props
    for m in re.finditer(r"\bhref=[\"']([^\"']+)[\"']", md):
        out.append(("href", m.group(1)))
    # src can reveal broken images if absolute/root-relative
    for m in re.finditer(r"\bsrc=[\"']([^\"']+)[\"']", md):
        out.append(("src", m.group(1)))
    return out


def headings(md: str):
    hs = []
    for line in md.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            hs.append((len(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2)).strip()))
    return hs


def words(md: str) -> list[str]:
    # remove code blocks, tags, urls, markdown symbols
    t = re.sub(r"```.*?```", " ", md, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"https?://\S+", " ", t)
    return re.findall(r"[A-Za-z][A-Za-z0-9'’-]+", t)


def first_summary(md: str) -> str:
    for line in md.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("<") or s.startswith("---"):
            continue
        if s.startswith(">"):
            return s.lstrip("> ").strip()
        if len(s) > 25:
            return re.sub(r"\s+", " ", s)[:220]
    return ""

# Fetch indices
for name, url in {
    "robots.txt": BASE + "/robots.txt",
    "sitemap.xml": BASE + "/sitemap.xml",
    "llms.txt": BASE + "/llms.txt",
    "llms-full.txt": BASE + "/llms-full.txt",
    "api-reference-openapi.json": BASE + "/api-reference/openapi.json",
}.items():
    res = fetch(url)
    save_text(name, res["text"])
    time.sleep(SLEEP)

# Parse sitemap
sitemap_text = (RAW / "sitemap.xml").read_text(encoding="utf-8")
sitemap_paths = set()
try:
    root = ET.fromstring(sitemap_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for loc in root.findall(".//sm:loc", ns):
        p = norm_path(loc.text or "")
        if p:
            sitemap_paths.add(p)
except Exception as e:
    print("sitemap parse error", e, file=sys.stderr)

# Parse llms index
llms_text = (RAW / "llms.txt").read_text(encoding="utf-8")
llms_items = []
for line in llms_text.splitlines():
    m = re.match(r"- \[([^\]]+)\]\((https://docs\.oviond\.com/[^)]+)\)(?::\s*(.*))?$", line.strip())
    if m:
        title, url, desc = m.groups()
        p = norm_path(url)
        llms_items.append({"title": title, "url": url, "path": p, "desc": desc or ""})

paths = sorted((sitemap_paths | {i["path"] for i in llms_items if i["path"]}), key=lambda p: (p.count('/'), p))
known_paths = set(paths)

# Fetch all markdown pages
page_records = []
for idx, path in enumerate(paths, 1):
    url = md_url_from_path(path)
    res = fetch(url)
    # fallback to non-md if needed
    if res["status"] == 404:
        res2 = fetch(BASE + ("/" if path == "/" else path))
        if res2["status"] and res2["status"] < 400:
            res = res2
    md = res["text"] or ""
    (PAGES / safe_file_for_path(path)).write_text(md, encoding="utf-8")
    hs = headings(md)
    h1s = [h for lvl, h in hs if lvl == 1]
    wc = len(words(md))
    links = extract_links(md)
    internal = []
    external = []
    for label, link in links:
        np = norm_path(link)
        if np is not None:
            internal.append({"label": label, "target": link, "path": np})
        elif link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"):
            external.append({"label": label, "target": link})
    content_hash = hashlib.sha256(re.sub(r"\s+", " ", md).strip().encode()).hexdigest()[:16]
    page_records.append({
        "path": path,
        "url": BASE + ("/" if path == "/" else path),
        "md_url": url,
        "status": res["status"],
        "final_url": res["final_url"],
        "content_type": res["content_type"],
        "bytes": res["bytes"],
        "elapsed_ms": res["elapsed_ms"],
        "title": h1s[0] if h1s else "",
        "h1_count": len(h1s),
        "h2_count": sum(1 for lvl, _ in hs if lvl == 2),
        "word_count": wc,
        "summary": first_summary(md),
        "internal_links": internal,
        "external_links": external,
        "hash": content_hash,
        "raw_file": str(PAGES / safe_file_for_path(path)),
    })
    print(f"[{idx}/{len(paths)}] {res['status']} {path} words={wc}")
    time.sleep(SLEEP)

# Link status checks for internal links (including unknowns)
link_refs = []
unknown_paths = set()
for rec in page_records:
    for l in rec["internal_links"]:
        target_path = l["path"]
        if target_path and not target_path.startswith("/_next") and not target_path.startswith("/cdn-cgi"):
            known = target_path in known_paths or target_path == "/"
            if not known:
                unknown_paths.add(target_path)
            link_refs.append({"source": rec["path"], "label": l["label"], "target": l["target"], "target_path": target_path, "known": known})

checked = {}
for p in sorted(unknown_paths):
    # Prefer md because docs exposes content there; fallback to page route
    res = fetch(md_url_from_path(p))
    if res["status"] == 404:
        res2 = fetch(BASE + p)
        if res2["status"] and res2["status"] < 400:
            res = res2
    checked[p] = {"status": res["status"], "final_url": res["final_url"], "content_type": res["content_type"], "bytes": res["bytes"], "error": res["error"]}
    time.sleep(SLEEP)

# Generate findings
findings = []

def add(sev, category, path, issue, evidence="", recommendation=""):
    findings.append({"severity": sev, "category": category, "path": path, "issue": issue, "evidence": evidence, "recommendation": recommendation})

# Index/openapi blockers
openapi_text = (RAW / "api-reference-openapi.json").read_text(encoding="utf-8")
if "OpenAPI Plant Store" in openapi_text or "sandbox.mintlify.com" in openapi_text or "/plants" in openapi_text:
    add("P0", "API reference", "/api-reference/openapi.json", "Public OpenAPI spec is Mintlify Plant Store sample, not Oviond.", "Found title='OpenAPI Plant Store', server='http://sandbox.mintlify.com', /plants paths.", "Replace with the real Oviond OpenAPI JSON or remove/hide the endpoint before launch.")

# Missing from indices
if not any(p in known_paths for p in ["/quickstart", "/authentication"]):
    add("P0", "Navigation", "/", "Homepage cards link to Quick Start and Authentication, but these pages are not in sitemap/llms index.", "/quickstart and /authentication referenced from introduction; absent from sitemap/llms.", "Create these pages or change the cards to existing onboarding/API auth pages.")

# Broken unknown internal links
for ref in link_refs:
    if not ref["known"]:
        st = checked.get(ref["target_path"], {}).get("status")
        if st is None or st >= 400:
            add("P0" if st == 404 else "P1", "Broken internal link", ref["source"], f"Broken internal link to {ref['target_path']}", f"Label='{ref['label']}', target='{ref['target']}', status={st}", "Create the target page or update the link to an existing route.")
        else:
            add("P2", "Index coverage", ref["source"], f"Internal link target {ref['target_path']} resolves but is missing from sitemap/llms index.", f"status={st}", "Add the page to navigation/indexing if it should be discoverable.")

# Page-level quality
for rec in page_records:
    if rec["status"] is None or rec["status"] >= 400:
        add("P0", "Availability", rec["path"], "Indexed page does not return a successful status.", f"status={rec['status']}; url={rec['md_url']}", "Fix route or remove from sitemap/llms.")
    if rec["h1_count"] == 0:
        add("P1", "Content structure", rec["path"], "Missing H1 title.", f"word_count={rec['word_count']}", "Add exactly one H1 that matches the page intent.")
    elif rec["h1_count"] > 1:
        add("P2", "Content structure", rec["path"], "Multiple H1 headings.", f"h1_count={rec['h1_count']}", "Keep one H1; demote others to H2/H3.")
    if rec["word_count"] < 120:
        add("P1", "Thin content", rec["path"], "Very thin page content.", f"{rec['word_count']} words; title='{rec['title']}'", "Expand with purpose, prerequisites, steps, expected outcome, and related links.")
    elif rec["word_count"] < 220 and not rec["path"].startswith("/api/"):
        add("P2", "Thin content", rec["path"], "Short non-API guide page.", f"{rec['word_count']} words; title='{rec['title']}'", "Add stronger task context, edge cases, screenshots/GIFs, and next-step links.")
    if not rec["summary"]:
        add("P2", "Metadata/content", rec["path"], "Missing opening summary/description.", "No first meaningful summary line detected.", "Add a concise description below the H1.")

# Duplicate titles and summaries
by_title = defaultdict(list)
by_summary = defaultdict(list)
by_hash = defaultdict(list)
for rec in page_records:
    if rec["title"]:
        by_title[rec["title"].strip().lower()].append(rec)
    if rec["summary"]:
        by_summary[rec["summary"].strip().lower()].append(rec)
    by_hash[rec["hash"]].append(rec)

for title, recs in by_title.items():
    if len(recs) > 1:
        paths2 = [r["path"] for r in recs]
        # duplicate API/UI titles can still be confusing in search/nav
        add("P2", "Title clarity", ", ".join(paths2[:5]), f"Duplicate H1 title '{recs[0]['title']}' across {len(recs)} pages.", ", ".join(paths2), "Disambiguate API vs UI pages, e.g. 'Delete Account API' vs 'Delete your account'.")

for h, recs in by_hash.items():
    if len(recs) > 1:
        add("P1", "Duplicate content", ", ".join(r["path"] for r in recs[:5]), f"Exact duplicate page body across {len(recs)} pages.", ", ".join(r["path"] for r in recs), "Merge duplicates or rewrite one page for its distinct task intent.")

# Placeholder and risky copy search
patterns = {
    "Plant Store / Mintlify sample copy": re.compile(r"OpenAPI Plant Store|sandbox\.mintlify|/plants\b|Plant response", re.I),
    "TODO/TBD placeholder": re.compile(r"\b(TODO|TBD|coming soon|lorem ipsum|placeholder)\b", re.I),
    "Uncertain UI language": re.compile(r"\b(sometimes listed|may send|where applicable|if needed)\b", re.I),
    "Old billing plan framing": re.compile(r"\b(plan tiers|Starter|Professional|Enterprise|plan limit|plan's limits|upgrade your plan|subscription plan)\b", re.I),
    "Supabase/internal implementation leak": re.compile(r"\bSupabase|S3|cron scheduler|users table|accounts row|Stripe customer|Resend|SQS|Vercel\b", re.I),
}
for rec in page_records:
    md = Path(rec["raw_file"]).read_text(encoding="utf-8")
    for label, pat in patterns.items():
        matches = pat.findall(md)
        if matches:
            sev = "P0" if "Plant" in label else ("P1" if "internal implementation" in label or "Old billing" in label else "P2")
            sample_lines = []
            for line in md.splitlines():
                if pat.search(line):
                    sample_lines.append(line.strip()[:220])
                    if len(sample_lines) >= 3:
                        break
            add(sev, "Copy consistency", rec["path"], label, " | ".join(sample_lines), "Rewrite for customer-facing clarity; remove internal implementation details and uncertain wording.")

# API endpoint doc completeness heuristic
api_pages = [r for r in page_records if r["path"].startswith("/api/") and r["path"] != "/api/introduction"]
for rec in api_pages:
    md = Path(rec["raw_file"]).read_text(encoding="utf-8")
    required_signals = {
        "method": re.search(r"\b(GET|POST|PUT|PATCH|DELETE)\b|<Endpoint|api=", md),
        "path": re.search(r"`/(api/)?[A-Za-z0-9_/{}/.-]+`|url=\"/", md),
        "request": re.search(r"Request|Body|Parameters|Query|Path parameter", md, re.I),
        "response": re.search(r"Response|Returns|200|201|204", md, re.I),
        "example": re.search(r"```|curl|Example", md, re.I),
    }
    missing = [k for k, v in required_signals.items() if not v]
    if missing:
        sev = "P1" if len(missing) >= 3 else "P2"
        add(sev, "API completeness", rec["path"], "API endpoint doc is missing standard reference elements.", f"Missing: {', '.join(missing)}; words={rec['word_count']}", "Use a consistent endpoint template: method/path, auth, params, body schema, response schema, errors, curl/JS example.")

# Navigation taxonomy counts
top_counts = Counter(p.strip('/').split('/')[0] if p.strip('/') else 'root' for p in paths)

# Write outputs
(OUT / "pages.json").write_text(json.dumps(page_records, indent=2, ensure_ascii=False), encoding="utf-8")
(OUT / "internal_links.json").write_text(json.dumps({"refs": link_refs, "unknown_checks": checked}, indent=2, ensure_ascii=False), encoding="utf-8")
(OUT / "findings.json").write_text(json.dumps(findings, indent=2, ensure_ascii=False), encoding="utf-8")
(OUT / "taxonomy.json").write_text(json.dumps({"page_count": len(paths), "top_level_counts": top_counts, "sitemap_count": len(sitemap_paths), "llms_count": len(llms_items)}, indent=2, ensure_ascii=False), encoding="utf-8")

with (OUT / "pages.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path", "status", "title", "word_count", "h1_count", "h2_count", "summary", "bytes", "elapsed_ms"])
    w.writeheader()
    for r in page_records:
        w.writerow({k: r.get(k) for k in w.fieldnames})
with (OUT / "findings.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["severity", "category", "path", "issue", "evidence", "recommendation"])
    w.writeheader()
    for r in findings:
        w.writerow(r)

print(json.dumps({
    "pages": len(page_records),
    "sitemap_paths": len(sitemap_paths),
    "llms_items": len(llms_items),
    "unknown_internal_targets": len(unknown_paths),
    "findings": Counter(f["severity"] for f in findings),
    "top_level_counts": top_counts,
}, indent=2, default=lambda x: dict(x)))
