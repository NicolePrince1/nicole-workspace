# Keyword clustering research for Oviond SEO

Date: 2026-05-12

## Executive view

Keyword clustering for the new Oviond website should be **SERP-first, NLP-second**.

For page-level decisions, use live Google SERP overlap to decide whether keywords belong on one page or need separate pages. For hub/spoke architecture, use semantic/NLP grouping on top of those SERP clusters to create topical clusters, pillar pages, and internal-linking plans.

This mirrors the strongest public pattern from KeywordInsights.ai: SERP clustering for keyword/page groups, then NLP/semantic grouping for topical clusters.

## What Keyword Insights appears to do

### Page-level keyword clustering

Keyword Insights describes clustering as grouping keywords that share the same or similar ranking URLs in live, country/language-specific Google SERPs.

Key mechanics:

- Use live, country-specific SERP data.
- Compare ranking URLs, not just keyword text.
- Match full ranking URLs rather than only root domains.
- Current docs emphasize the top 7 organic results because modern SERPs often include AI Overviews, featured snippets, PAA, and other SERP features that reduce clean traditional organic listings.
- Keywords are clustered when they share enough ranking URLs.
- Public docs show slight default inconsistency:
  - Main docs mention 40% URL overlap in top 7.
  - API/advanced docs mention `grouping_accuracy` default 4 shared URLs from top 7.
  - Older docs mention 3 shared URLs from top 10.
- Practical takeaway: use top 7 organic URLs, default to 4 shared full URLs for stricter content decisions, and test 3 vs 4 depending on SERP volatility.

### Algorithms

Keyword Insights documents two main clustering approaches:

1. **Centroid / volume clustering**
   - Pick the highest-volume keyword as the centroid.
   - Group other keywords that share the threshold number of URLs with that centroid.
   - Faster and produces larger clusters.
   - Useful for broad exploration and high-volume topic discovery.
   - Risk: less nuanced because all keywords overlap with the centroid, but not necessarily with each other.

2. **Agglomerative clustering**
   - Compare keywords against each other.
   - Group when pairwise SERP overlap passes the threshold.
   - Slower, tighter, more accurate.
   - Better for deciding the actual page map.

Recommended for Oviond: use agglomerative clustering for final page decisions. Use centroid only for broad exploratory passes if keyword lists become very large.

### Topical clusters / hubs

Keyword Insights separates:

- **Keyword cluster:** keywords that usually belong on the same page.
- **Topical cluster / supercluster:** related keyword clusters that belong in the same hub/spoke content area.

Their topical clustering uses NLP/semantic similarity over clusters, not SERP overlap. Public docs describe three topical grouping strengths:

- Soft: broad grouping, around 70% similarity.
- Medium: balanced grouping, around 88% similarity; recommended starting point.
- Hard: stricter grouping, around 93% similarity.

Important limitation: topical clusters are not a finished information architecture. They need manual cleanup, especially in technical niches, with acronyms, and where commercial/informational intent diverges.

### Search intent / “context”

Keyword Insights frames intent as SERP context rather than only query-text intent.

Pattern:

- Inspect top Google results.
- Classify visible page types as informational, commercial, transactional, or other.
- Aggregate dominant context at keyword and cluster level.
- Use fragmented intent as a signal. If one cluster has mixed SERPs, e.g. mostly informational but with some commercial pages, decide whether Oviond needs one page, two supporting pages, or a hybrid commercial guide.

For Oviond, this matters because SaaS keywords often split between:

- informational “how to/reporting/dashboard” guides,
- commercial “best/reporting software/tools” comparisons,
- transactional/product pages,
- competitor-alternative pages.

### Cannibalization detection

Keyword Insights uses clustering plus rank tracking to spot cannibalization.

Pattern:

- If multiple own URLs rank inside the same SERP cluster, there may be cannibalization.
- Merge/redirect/reposition pages when they target the same intent.
- Keep separate pages where SERP overlap is low or intent genuinely differs.

For Oviond, this should be used during the current-site audit before new page planning.

## Recommended Oviond workflow once DataForSEO is live

### Phase 1: Current site audit

1. Crawl/index current `oviond.com` marketing URLs.
2. Pull GSC queries by URL where available.
3. Pull current ranking keywords for Oviond via DataForSEO Labs Ranked Keywords.
4. Map:
   - URL
   - current title/H1/meta
   - primary ranking keywords
   - impressions/clicks if GSC data exists
   - current rank and ranking URL
   - intent/context
5. Flag:
   - pages with overlapping clusters,
   - pages ranking for the wrong intent,
   - URLs with impressions but weak CTR,
   - important keywords with no ranking URL.

### Phase 2: Keyword universe build

Sources:

- DataForSEO keyword ideas from seed terms.
- Related keywords and keyword suggestions.
- Competitor ranked keywords from AgencyAnalytics, Whatagraph, Databox, Looker Studio, Swydo, Reportz, DashThis, Supermetrics, Power My Analytics, etc.
- Current GSC queries.
- Existing site terms/pages.
- Product/integration/category terms.
- Competitor alternative terms.

Normalize and dedupe:

- lowercase,
- remove weird punctuation variants,
- preserve original keyword,
- keep country/language/device metadata,
- tag modifiers: best, software, tool, alternative, pricing, dashboard, report, template, integration, white label, agency, client, automated, PPC, SEO, social media, ecommerce.

### Phase 3: Volume and enrichment

For each keyword, enrich with:

- search volume,
- CPC,
- competition,
- monthly trend,
- intent/context,
- SERP features,
- current Oviond rank/ranking URL,
- competitor visibility,
- likely funnel stage.

### Phase 4: SERP clustering

Use DataForSEO SERP API to fetch top organic URLs per keyword.

Default Oviond clustering settings:

- Market: start United States, English.
- Device: desktop first; mobile validation for key commercial clusters.
- SERP depth: top 7 organic full URLs.
- URL matching: full canonical-ish URL, stripped of tracking parameters and fragments.
- Default overlap threshold: 4 shared URLs out of 7 for final page map.
- Exploratory threshold: 3 shared URLs out of 7 when building broad early ideas.
- Recheck volatile/high-value clusters manually.

Graph method:

- Each keyword is a node.
- Add edge if SERP overlap >= threshold.
- Use connected components/agglomerative grouping for final clusters.
- Name each cluster by highest volume keyword, but allow manual override where the highest-volume keyword is not the best page title.

### Phase 5: Intent split / merge decisions

For each cluster:

- If SERP overlap is high and intent is consistent: one page.
- If SERP overlap is moderate but intent is split: review manually.
- If commercial and informational intent both appear but URLs differ materially: consider separate spoke pages with different jobs.
- If competitor/product pages dominate: product/commercial page, not a blog post.
- If guides dominate: educational spoke or pillar section.

### Phase 6: Hub/spoke mapping

After SERP clusters are created:

1. Generate semantic embeddings for cluster labels, representative keywords, and SERP titles.
2. Group keyword clusters into topical superclusters.
3. Start with medium strength; manually split/merge based on Oviond product architecture and commercial value.
4. For each hub, define:
   - hub/pillar page,
   - spoke pages,
   - product/integration pages,
   - comparison/alternative pages,
   - internal links,
   - primary conversion path.

Potential Oviond hubs:

- Agency reporting software
- White-label reporting
- Marketing dashboards
- Automated client reporting
- Integrations/connectors
- PPC reporting
- SEO reporting
- Social media reporting
- Client reporting templates/examples
- Competitor alternatives
- Looker Studio / spreadsheet replacement
- AI reporting / automated insights

### Phase 7: Prioritization model

Score each cluster using:

- search volume,
- CPC/commercial value,
- intent closeness to signup,
- keyword difficulty/competition proxy,
- Oviond current ranking gap,
- competitor visibility,
- product readiness,
- strategic importance to new website IA,
- content production effort,
- internal-link value.

Recommended priority formula:

`priority = (commercial_fit * 3) + (intent_fit * 2) + (opportunity_volume * 2) + (strategic_fit * 2) - difficulty - production_effort`

### Phase 8: Brief generation

For each selected page:

- choose representative keyword,
- fetch live SERP competitors,
- extract headings/title/meta from top pages,
- collect PAA/related searches where available,
- identify content type that Google rewards,
- produce brief:
  - page type,
  - target cluster,
  - title/H1 options,
  - search intent,
  - audience/job-to-be-done,
  - outline,
  - internal links in/out,
  - CTA,
  - schema suggestions,
  - pages to consolidate/redirect if relevant.

## Skill requirements

The future `dataforseo` or `oviond-seo-research` skill should include scripts for:

- `discover_keywords.py` — seed expansion via DataForSEO Labs.
- `enrich_keywords.py` — search volume, CPC, competition, trend.
- `fetch_serps.py` — top organic full URLs per keyword.
- `cluster_serp_overlap.py` — graph/agglomerative SERP clustering.
- `cluster_topics.py` — embedding/NLP superclusters.
- `audit_current_site.py` — URL/query/rank mapping.
- `detect_cannibalization.py` — multiple Oviond URLs in same cluster.
- `prioritize_clusters.py` — opportunity scoring.
- `build_page_map.py` — hub/spoke recommendations.
- `brief_cluster.py` — SERP-led content brief.

## Sources reviewed

- https://www.keywordinsights.ai/features/keyword-clustering/
- https://docs.keywordinsights.ai/learning-center/the-features/keyword-clustering/README
- https://docs.keywordinsights.ai/learning-center/the-features/keyword-clustering/the-advanced-settings/clustering-types
- https://docs.keywordinsights.ai/learning-center/the-features/keyword-clustering/the-advanced-settings/keyword-grouping-accuracy
- https://docs.keywordinsights.ai/learning-center/the-features/keyword-clustering/the-advanced-settings/topical-cluster-creation-method
- https://docs.keywordinsights.ai/learning-center/the-features/search-intent-context.md
- https://docs.keywordinsights.ai/api/api-use-cases/public-api-clustering.md
- https://www.keywordinsights.ai/blog/keyword-clustering-guide/
- https://www.keywordinsights.ai/features/content-briefs/
- https://www.keywordinsights.ai/blog/how-we-increased-traffic-by-fixing-content-cannibalization/
