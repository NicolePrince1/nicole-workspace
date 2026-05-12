#!/usr/bin/env python3
"""Light public sitemap + metadata crawler for Oviond competitor SEO audit.

No secrets. Uses robots.txt + common sitemap locations, recursively parses sitemap indexes,
and fetches only a capped strategic subset of pages for title/description/H1 extraction.
"""
from __future__ import annotations

import csv
import gzip
import html
import io
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

OUT_DIR = Path("research/seo/full-audit-2026-05-12/competitor-crawls")
DOMAINS = [
    "twominutereports.com",
    "agencyanalytics.com",
    "dashthis.com",
    "whatagraph.com",
    "swydo.com",
    "databox.com",
    "tapclicks.com",
    "reportgarden.com",
    "reportingninja.com",
    "supermetrics.com",
    "powermyanalytics.com",
    "funnel.io",
    "windsor.ai",
    "portermetrics.com",
    "coupler.io",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; OviondSEOAudit/1.0; +https://www.oviond.com/)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

COMMON_SITEMAPS = [
    "/sitemap.xml",
    "/sitemap_index.xml",
    "/sitemap-index.xml",
    "/sitemap/sitemap.xml",
    "/post-sitemap.xml",
    "/page-sitemap.xml",
]

STRATEGIC_TERMS = [
    "agency", "client", "white-label", "white_label", "report", "reporting", "dashboard",
    "template", "templates", "integration", "integrations", "connector", "connectors",
    "google", "facebook", "instagram", "linkedin", "tiktok", "seo", "ppc", "ads",
    "looker", "data-studio", "sheets", "excel", "analytics", "marketing", "kpi",
    "alternative", "alternatives", "competitor", "vs", "pricing", "features", "solutions",
    "blog", "guide", "resources", "ai", "chatgpt", "automated", "automation",
]

CATEGORY_PATTERNS = [
    ("integration/connector", re.compile(r"/(integrations?|connectors?|data-sources?|sources?)/", re.I)),
    ("template", re.compile(r"/(templates?|dashboard-templates?|report-templates?)/", re.I)),
    ("alternative/comparison", re.compile(r"/(alternatives?|compare|comparison|vs)/|alternative", re.I)),
    ("blog/resource", re.compile(r"/(blog|resources?|guides?|learn|articles?)/", re.I)),
    ("agency/white-label", re.compile(r"agency|white[-_ ]label|client[-_ ]report", re.I)),
    ("pricing", re.compile(r"/pricing/?$|pricing", re.I)),
    ("product/feature", re.compile(r"/(features?|product|platform|solutions?)/", re.I)),
    ("landing/page", re.compile(r"/(lp|landing|use-cases?)/", re.I)),
]

MAX_SITEMAPS_PER_DOMAIN = 80
MAX_URLS_PER_DOMAIN = 20000
MAX_META_PER_DOMAIN = 100
REQUEST_DELAY = 0.05
TIMEOUT = 8

@dataclass
class UrlRow:
    domain: str
    url: str
    sitemap: str
    lastmod: str = ""
    category: str = "other"
    path_depth: int = 0
    strategic_score: int = 0


def slug(domain: str) -> str:
    return domain.replace(".", "_").replace("-", "_")


def fetch_bytes(url: str, timeout: int = TIMEOUT) -> tuple[int, bytes, str]:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read(8_000_000)
        final_url = resp.geturl()
        code = getattr(resp, "status", 200)
        ctype = resp.headers.get("Content-Type", "")
    if url.endswith(".gz") or data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    return code, data, final_url


def try_fetch(url: str) -> tuple[int, bytes, str] | None:
    try:
        return fetch_bytes(url)
    except Exception:
        return None
    finally:
        time.sleep(REQUEST_DELAY)


def discover_sitemaps(domain: str) -> list[str]:
    found: list[str] = []
    for scheme in ("https", "http"):
        robots_url = f"{scheme}://{domain}/robots.txt"
        res = try_fetch(robots_url)
        if res and res[0] < 400:
            text = res[1].decode("utf-8", "ignore")
            for line in text.splitlines():
                if line.lower().startswith("sitemap:"):
                    sm = line.split(":", 1)[1].strip()
                    if sm and sm not in found:
                        found.append(sm)
            break
    for path in COMMON_SITEMAPS:
        url = f"https://{domain}{path}"
        if url not in found:
            found.append(url)
    return found


def parse_sitemap(url: str, seen: set[str], sitemaps_seen: set[str], domain: str) -> list[UrlRow]:
    if url in sitemaps_seen or len(sitemaps_seen) >= MAX_SITEMAPS_PER_DOMAIN:
        return []
    sitemaps_seen.add(url)
    res = try_fetch(url)
    if not res or res[0] >= 400:
        return []
    text = res[1].decode("utf-8", "ignore").strip().lstrip("\ufeff")
    if not text.startswith("<"):
        return []
    try:
        root = ET.fromstring(text.encode("utf-8"))
    except Exception:
        return []
    rows: list[UrlRow] = []
    tag = root.tag.lower()
    ns_strip = lambda t: t.split("}", 1)[-1].lower()
    if ns_strip(root.tag) == "sitemapindex":
        for sm in root:
            loc = ""
            for child in sm:
                if ns_strip(child.tag) == "loc" and child.text:
                    loc = child.text.strip()
            if loc:
                rows.extend(parse_sitemap(loc, seen, sitemaps_seen, domain))
            if len(rows) >= MAX_URLS_PER_DOMAIN:
                break
    elif ns_strip(root.tag) == "urlset":
        for u in root:
            loc = lastmod = ""
            for child in u:
                key = ns_strip(child.tag)
                if key == "loc" and child.text:
                    loc = child.text.strip()
                elif key == "lastmod" and child.text:
                    lastmod = child.text.strip()
            if not loc or loc in seen:
                continue
            host = urllib.parse.urlparse(loc).netloc.lower().removeprefix("www.")
            if not (host == domain or host.endswith("." + domain)):
                continue
            seen.add(loc)
            rows.append(classify_row(domain, loc, url, lastmod))
            if len(seen) >= MAX_URLS_PER_DOMAIN:
                break
    return rows


def classify_row(domain: str, url: str, sitemap_url: str, lastmod: str = "") -> UrlRow:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path or "/"
    depth = len([p for p in path.split("/") if p])
    lowered = urllib.parse.unquote(path).lower()
    category = "other"
    for name, pat in CATEGORY_PATTERNS:
        if pat.search(lowered):
            category = name
            break
    score = 0
    for term in STRATEGIC_TERMS:
        if term in lowered:
            score += 3 if term in ("agency", "white-label", "reporting", "template", "integration", "connector", "alternative", "looker", "sheets", "dashboard") else 1
    if depth <= 2:
        score += 2
    if category != "other":
        score += 5
    if re.search(r"/(blog|resources?|guides?)/page/|/tag/|/author/|/category/", lowered):
        score -= 4
    return UrlRow(domain, url, sitemap_url, lastmod, category, depth, score)


def extract_meta(url: str) -> dict[str, str]:
    out = {"status": "", "final_url": "", "title": "", "meta_description": "", "h1": "", "canonical": "", "og_title": ""}
    try:
        code, data, final_url = fetch_bytes(url, timeout=TIMEOUT)
        out["status"] = str(code)
        out["final_url"] = final_url
        text = data.decode("utf-8", "ignore")[:900_000]
    except Exception as e:
        out["status"] = "ERR"
        out["final_url"] = url
        out["title"] = type(e).__name__
        time.sleep(REQUEST_DELAY)
        return out
    # crude but robust enough for strategic meta extraction
    def one(pattern: str, flags=re.I | re.S) -> str:
        m = re.search(pattern, text, flags)
        if not m:
            return ""
        return clean(m.group(1))
    out["title"] = one(r"<title[^>]*>(.*?)</title>")
    out["meta_description"] = one(r"<meta[^>]+name=[\"']description[\"'][^>]+content=[\"'](.*?)[\"'][^>]*>") or one(r"<meta[^>]+content=[\"'](.*?)[\"'][^>]+name=[\"']description[\"'][^>]*>")
    out["h1"] = one(r"<h1[^>]*>(.*?)</h1>")
    out["canonical"] = one(r"<link[^>]+rel=[\"']canonical[\"'][^>]+href=[\"'](.*?)[\"'][^>]*>") or one(r"<link[^>]+href=[\"'](.*?)[\"'][^>]+rel=[\"']canonical[\"'][^>]*>")
    out["og_title"] = one(r"<meta[^>]+property=[\"']og:title[\"'][^>]+content=[\"'](.*?)[\"'][^>]*>")
    return out


def clean(s: str) -> str:
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def select_meta_rows(rows: list[UrlRow]) -> list[UrlRow]:
    selected: list[UrlRow] = []
    by_cat: dict[str, list[UrlRow]] = defaultdict(list)
    for r in rows:
        by_cat[r.category].append(r)
    # guarantee category coverage, then fill by score/newness-ish
    for cat, cat_rows in sorted(by_cat.items()):
        cat_rows.sort(key=lambda r: (r.strategic_score, r.lastmod), reverse=True)
        selected.extend(cat_rows[: min(25, len(cat_rows))])
    selected_urls = {r.url for r in selected}
    remainder = sorted([r for r in rows if r.url not in selected_urls], key=lambda r: (r.strategic_score, r.lastmod), reverse=True)
    selected.extend(remainder[: max(0, MAX_META_PER_DOMAIN - len(selected))])
    return selected[:MAX_META_PER_DOMAIN]


def write_csv(path: Path, rows: Iterable[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    all_rows: list[UrlRow] = []
    meta_rows: list[dict[str, str]] = []
    domain_stats: list[dict[str, str | int]] = []
    errors: list[str] = []

    for domain in DOMAINS:
        print(f"== {domain}", flush=True)
        seed_sitemaps = discover_sitemaps(domain)
        seen_urls: set[str] = set()
        seen_sitemaps: set[str] = set()
        rows: list[UrlRow] = []
        for sm in seed_sitemaps:
            rows.extend(parse_sitemap(sm, seen_urls, seen_sitemaps, domain))
            if len(seen_urls) >= MAX_URLS_PER_DOMAIN:
                break
        # dedupe after sitemap overlap
        dedup = {}
        for r in rows:
            dedup[r.url] = r
        rows = sorted(dedup.values(), key=lambda r: r.url)
        all_rows.extend(rows)
        inv_fields = ["domain", "url", "category", "path_depth", "strategic_score", "lastmod", "sitemap"]
        write_csv(
            OUT_DIR / f"{slug(domain)}_url_inventory.csv",
            [r.__dict__ for r in rows],
            inv_fields,
        )
        counts = Counter(r.category for r in rows)
        domain_stats.append({
            "domain": domain,
            "url_count": len(rows),
            "sitemap_count": len(seen_sitemaps),
            **{f"cat_{k}": v for k, v in sorted(counts.items())},
        })
        meta_selection = select_meta_rows(rows)
        for idx, r in enumerate(meta_selection, 1):
            if idx % 50 == 0:
                print(f"  meta {idx}/{len(meta_selection)}", flush=True)
            m = extract_meta(r.url)
            meta_rows.append({
                "domain": r.domain,
                "url": r.url,
                "category": r.category,
                "path_depth": str(r.path_depth),
                "strategic_score": str(r.strategic_score),
                "lastmod": r.lastmod,
                **m,
            })
        print(f"  urls={len(rows)} meta={len(meta_selection)} sitemaps={len(seen_sitemaps)}", flush=True)

    inv_fields = ["domain", "url", "category", "path_depth", "strategic_score", "lastmod", "sitemap"]
    write_csv(OUT_DIR / "all_competitor_url_inventory.csv", [r.__dict__ for r in all_rows], inv_fields)
    meta_fields = ["domain", "url", "category", "path_depth", "strategic_score", "lastmod", "status", "final_url", "title", "meta_description", "h1", "canonical", "og_title"]
    write_csv(OUT_DIR / "all_competitor_strategic_meta.csv", meta_rows, meta_fields)
    # per-domain strategic meta files
    by_domain_meta: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in meta_rows:
        by_domain_meta[row["domain"]].append(row)
    for domain, rows in by_domain_meta.items():
        write_csv(OUT_DIR / f"{slug(domain)}_strategic_meta.csv", rows, meta_fields)

    stat_fields = sorted({k for row in domain_stats for k in row.keys()}, key=lambda x: (x != "domain", x != "url_count", x))
    write_csv(OUT_DIR / "domain_architecture_counts.csv", domain_stats, stat_fields)
    print(f"Wrote {OUT_DIR}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
