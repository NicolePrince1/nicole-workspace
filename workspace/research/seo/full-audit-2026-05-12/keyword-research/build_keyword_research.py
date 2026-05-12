#!/usr/bin/env python3
"""Build USA keyword research dataset for Oviond using DataForSEO.

Reads DATA_FOR_SEO from environment; does not print credentials.
"""
import base64, csv, json, os, re, time, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

OUT = Path('/data/.openclaw/workspace/research/seo/full-audit-2026-05-12/keyword-research')
RAW = OUT / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
LOCATION_CODE = 2840  # United States
LANGUAGE_CODE = 'en'

SEEDS = [
    'marketing reporting software','client reporting software','agency reporting software','white label reporting software',
    'marketing dashboard software','agency dashboard software','automated marketing reports','SEO reporting software',
    'PPC reporting software','social media reporting software','Google Ads reporting tool','Facebook Ads reporting tool',
    'GA4 reporting tool','Looker Studio alternative','AgencyAnalytics alternative','DashThis alternative',
    'Whatagraph alternative','Swydo alternative','2-Minute Reports alternative','Supermetrics alternative',
    'Google Sheets reporting automation','AI marketing reporting','AI report generator for agencies','ChatGPT marketing reporting',
    'Claude marketing data','MCP marketing reporting'
]

# Extra deterministic long-tail coverage around the brief; DataForSEO expansion misses many low-volume SaaS/B2B terms.
MODIFIERS = ['software','tool','platform','dashboard','template','automation','reports','reporting tool','reporting software']
BASES = [
    'marketing reporting','client reporting','agency reporting','white label reporting','white label dashboard',
    'digital marketing reporting','seo reporting','ppc reporting','paid ads reporting','social media reporting',
    'google ads reporting','facebook ads reporting','meta ads reporting','ga4 reporting','google analytics reporting',
    'looker studio alternative','agencyanalytics alternative','dashthis alternative','whatagraph alternative','swydo alternative',
    'supermetrics alternative','2 minute reports alternative','google sheets reporting automation',
    'ai marketing reporting','ai client reporting','ai report generator','chatgpt marketing reports','claude marketing analytics',
    'mcp marketing reporting'
]
AUDIENCE = ['for agencies','for marketing agencies','for clients','for small agencies','for digital agencies']

INCLUDE_RE = re.compile(r'\b(report|reporting|reports|dashboard|dashboards|agency|agencies|client|clients|white label|marketing|seo|ppc|ads|advertising|analytics|ga4|google analytics|looker|agencyanalytics|dashthis|whatagraph|swydo|supermetrics|sheets|ai|chatgpt|claude|mcp|data connector|connector)\b', re.I)
EXCLUDE_RE = re.compile(r'\b(job|salary|course|training|certification|free download crack|login|careers|definition|meaning|stock|share price|invoice|accounting|medical|patient|school|real estate|weather|sports|crystal reports?|court reporting|client management software|compliance reporting|data looker studio)\b', re.I)
COMPETITOR_RE = re.compile(r'\b(agencyanalytics|agency analytics|dashthis|whatagraph|swydo|supermetrics|looker studio|2[- ]?minute reports|two minute reports|databox|klipfolio|tapclicks|ninjacat|reportgarden|porter metrics|funnel.io|funnel io|windsor.ai|windsor ai|coupler.io|coupler io|power my analytics)\b', re.I)

cred = os.getenv('DATA_FOR_SEO')
if not cred:
    raise SystemExit('DATA_FOR_SEO env var missing')
token = base64.b64encode(cred.encode()).decode() if ':' in cred else cred

api_cost = 0.0
calls = []

def post(path, body, name):
    global api_cost
    url = 'https://api.dataforseo.com/v3/' + path
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers={'Authorization':'Basic '+token, 'Content-Type':'application/json'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                obj = json.load(resp)
            cost = float(obj.get('cost') or sum((t.get('cost') or 0) for t in obj.get('tasks', [])))
            api_cost += cost
            calls.append({'name': name, 'path': path, 'status': obj.get('status_code'), 'cost': cost})
            return obj
        except urllib.error.HTTPError as e:
            txt = e.read().decode(errors='replace')[:500]
            if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 * (attempt + 1)); continue
            raise RuntimeError(f'{name} HTTP {e.code}: {txt}')
        except Exception:
            if attempt < 3:
                time.sleep(2 * (attempt + 1)); continue
            raise

def kw_norm(k):
    k = re.sub(r'\s+', ' ', (k or '').strip().lower())
    # Clean generator artifacts like "reporting reporting software" while preserving natural phrases.
    k = re.sub(r'\breporting reporting\b', 'reporting', k)
    k = re.sub(r'\bdashboard dashboard\b', 'dashboard', k)
    k = re.sub(r'\bsoftware software\b', 'software', k)
    k = re.sub(r'\btool tool\b', 'tool', k)
    return k

def item_fields(item):
    # Labs endpoints return either direct item or {keyword_data:{...}} with keyword_info.
    # Google Ads search_volume returns metrics directly on the item.
    if 'keyword_data' in item:
        item = item['keyword_data']
    direct = 'keyword_info' not in item
    ki = item if direct else (item.get('keyword_info') or {})
    props = item.get('keyword_properties') or {}
    intent = item.get('search_intent_info') or {}
    trend = ki.get('search_volume_trend') or {}
    months = ki.get('monthly_searches') or []
    recent_3 = [m.get('search_volume') for m in months[:3] if isinstance(m.get('search_volume'), int)]
    prior_3 = [m.get('search_volume') for m in months[3:6] if isinstance(m.get('search_volume'), int)]
    yoy_month = None
    if len(months) >= 12 and months[0].get('search_volume') not in (None,0) and months[11].get('search_volume') is not None:
        yoy_month = round((months[0]['search_volume'] - months[11]['search_volume']) / max(months[11]['search_volume'],1) * 100, 1)
    qoq = None
    if recent_3 and prior_3 and mean(prior_3):
        qoq = round((mean(recent_3)-mean(prior_3))/mean(prior_3)*100, 1)
    return {
        'keyword': kw_norm(item.get('keyword')),
        'search_volume': ki.get('search_volume'),
        'cpc': ki.get('cpc'),
        'competition': ki.get('competition_index') if direct else ki.get('competition'),
        'competition_level': ki.get('competition') if direct else ki.get('competition_level'),
        'low_top_of_page_bid': ki.get('low_top_of_page_bid'),
        'high_top_of_page_bid': ki.get('high_top_of_page_bid'),
        'monthly_trend_pct': trend.get('monthly'),
        'quarterly_trend_pct': trend.get('quarterly'),
        'yearly_trend_pct': trend.get('yearly'),
        'recent_3mo_vs_prior_3mo_pct': qoq,
        'latest_month_yoy_pct': yoy_month,
        'keyword_difficulty': props.get('keyword_difficulty'),
        'main_intent': intent.get('main_intent'),
        'words_count': props.get('words_count'),
        'monthly_searches_json': json.dumps(months, separators=(',',':')),
        'last_updated_time': ki.get('last_updated_time'),
    }

def classify(k):
    kl = k.lower()
    if 'alternative' in kl or COMPETITOR_RE.search(kl): return 'competitor_alternative'
    if any(x in kl for x in ['ai ', 'chatgpt', 'claude', 'mcp']): return 'ai_reporting'
    if 'white label' in kl: return 'white_label_reporting'
    if 'seo' in kl: return 'seo_reporting'
    if 'ppc' in kl or 'google ads' in kl or 'facebook ads' in kl or 'meta ads' in kl or 'paid ads' in kl: return 'paid_ads_reporting'
    if 'social' in kl: return 'social_reporting'
    if 'ga4' in kl or 'google analytics' in kl: return 'analytics_reporting'
    if 'sheet' in kl or 'connector' in kl or 'supermetrics' in kl: return 'connector_automation'
    if 'dashboard' in kl: return 'dashboard_software'
    if 'client' in kl: return 'client_reporting'
    if 'agency' in kl: return 'agency_reporting'
    return 'marketing_reporting'

def relevance(k):
    kl = k.lower(); score = 0
    for term, pts in [
        ('reporting',5),('report',4),('dashboard',4),('agency',4),('client',3),('white label',5),('marketing',3),
        ('seo',3),('ppc',3),('google ads',4),('facebook ads',4),('ga4',4),('looker studio',5),('alternative',5),
        ('supermetrics',4),('agencyanalytics',4),('dashthis',4),('whatagraph',4),('swydo',4),('ai',2),('chatgpt',3),('claude',2),('mcp',2),('automation',3),('software',2),('tool',2)
    ]:
        if term in kl: score += pts
    if EXCLUDE_RE.search(kl): score -= 10
    if not INCLUDE_RE.search(kl): score -= 5
    wc = len(kl.split())
    if wc >= 3: score += 2
    if wc >= 6: score -= 1
    return score

# Candidate generation
candidates = {kw_norm(s): {'keyword':kw_norm(s), 'source':'seed', 'seed':'self'} for s in SEEDS}
for base in BASES:
    for mod in MODIFIERS:
        k = kw_norm(base if base.endswith(mod) else f'{base} {mod}')
        candidates.setdefault(k, {'keyword':k,'source':'generated','seed':base})
    for aud in AUDIENCE:
        k = kw_norm(f'{base} {aud}')
        candidates.setdefault(k, {'keyword':k,'source':'generated','seed':base})

# Labs keyword suggestions: tight, seed-led expansion.
for i, seed in enumerate(SEEDS, 1):
    body = [{'location_code': LOCATION_CODE, 'language_code': LANGUAGE_CODE, 'keyword': seed, 'limit': 35}]
    obj = post('dataforseo_labs/google/keyword_suggestions/live', body, f'suggestions:{seed}')
    (RAW / f'suggestions_{i:02d}.json').write_text(json.dumps(obj, indent=2))
    items = (((obj.get('tasks') or [{}])[0].get('result') or [{}])[0].get('items') or [])
    for item in items:
        f = item_fields(item)
        k = f['keyword']
        if k and relevance(k) >= 3:
            candidates.setdefault(k, {'keyword':k,'source':'dataforseo_suggestion','seed':seed})
    time.sleep(0.15)

# A few broader idea pulls, capped and filtered hard.
idea_groups = [
    ['marketing reporting software','agency reporting software','client reporting software'],
    ['white label reporting software','marketing dashboard software','agency dashboard software'],
    ['SEO reporting software','PPC reporting software','social media reporting software'],
    ['Google Ads reporting tool','Facebook Ads reporting tool','GA4 reporting tool'],
    ['Looker Studio alternative','AgencyAnalytics alternative','DashThis alternative','Whatagraph alternative'],
    ['AI marketing reporting','AI report generator for agencies','ChatGPT marketing reporting']
]
for i, group in enumerate(idea_groups, 1):
    body = [{'location_code': LOCATION_CODE, 'language_code': LANGUAGE_CODE, 'keywords': group, 'limit': 80}]
    obj = post('dataforseo_labs/google/keyword_ideas/live', body, f'ideas:{i}')
    (RAW / f'ideas_{i:02d}.json').write_text(json.dumps(obj, indent=2))
    results = ((obj.get('tasks') or [{}])[0].get('result') or [])
    for result in results:
        for item in result.get('items') or []:
            f = item_fields(item); k=f['keyword']
            if k and relevance(k) >= 7:
                candidates.setdefault(k, {'keyword':k,'source':'dataforseo_idea','seed':'|'.join(group)})
    time.sleep(0.15)

# Enrich all candidates via Google Ads Search Volume in chunks.
keywords = sorted(candidates)
volume_rows = {}
for chunk_i in range(0, len(keywords), 700):
    chunk = keywords[chunk_i:chunk_i+700]
    body = [{'location_code': LOCATION_CODE, 'language_code': LANGUAGE_CODE, 'keywords': chunk}]
    obj = post('keywords_data/google_ads/search_volume/live', body, f'search_volume:{chunk_i//700+1}')
    (RAW / f'volumes_{chunk_i//700+1:02d}.json').write_text(json.dumps(obj, indent=2))
    results = ((obj.get('tasks') or [{}])[0].get('result') or [])
    for item in results:
        f = item_fields(item); k=f['keyword']
        if k:
            volume_rows[k] = f
    time.sleep(0.15)

# Merge, final filter. Keep all seeds even if low/no volume; otherwise require relevance and some signal.
idea_rows = []
for k, meta in candidates.items():
    v = volume_rows.get(k, {'keyword':k})
    sv = v.get('search_volume')
    row = {
        'keyword': k,
        'cluster': classify(k),
        'source': meta['source'],
        'seed': meta['seed'],
        'relevance_score': relevance(k),
        **{kk:v.get(kk) for kk in ['search_volume','cpc','competition','competition_level','low_top_of_page_bid','high_top_of_page_bid','monthly_trend_pct','quarterly_trend_pct','yearly_trend_pct','recent_3mo_vs_prior_3mo_pct','latest_month_yoy_pct','keyword_difficulty','main_intent','words_count','last_updated_time']}
    }
    keep = meta['source']=='seed' or (relevance(k) >= 6 and (sv is None or sv >= 10)) or (relevance(k) >= 11)
    if keep and not EXCLUDE_RE.search(k):
        idea_rows.append(row)

# Deduplicate sorted by cluster, volume desc, relevance desc.
def sv_num(r):
    return r.get('search_volume') if isinstance(r.get('search_volume'), int) else -1
idea_rows.sort(key=lambda r: (r['cluster'], -sv_num(r), -r['relevance_score'], r['keyword']))

# volumes/trends are same universe with monthly JSON included.
volume_full = []
for r in idea_rows:
    k = r['keyword']; v = volume_rows.get(k, {'keyword':k})
    volume_full.append({
        'keyword': k,
        'cluster': r['cluster'],
        'search_volume': v.get('search_volume'),
        'cpc': v.get('cpc'),
        'competition': v.get('competition'),
        'competition_level': v.get('competition_level'),
        'low_top_of_page_bid': v.get('low_top_of_page_bid'),
        'high_top_of_page_bid': v.get('high_top_of_page_bid'),
        'monthly_trend_pct': v.get('monthly_trend_pct'),
        'quarterly_trend_pct': v.get('quarterly_trend_pct'),
        'yearly_trend_pct': v.get('yearly_trend_pct'),
        'recent_3mo_vs_prior_3mo_pct': v.get('recent_3mo_vs_prior_3mo_pct'),
        'latest_month_yoy_pct': v.get('latest_month_yoy_pct'),
        'keyword_difficulty': v.get('keyword_difficulty'),
        'main_intent': v.get('main_intent'),
        'monthly_searches_json': v.get('monthly_searches_json'),
        'last_updated_time': v.get('last_updated_time'),
    })

# SERP samples for top strategic terms: top by volume per cluster + all important seeds with volume.
selected = []
seen = set()
seed_set = {kw_norm(s) for s in SEEDS}
# choose 4 per cluster by volume/relevance
clusters = sorted(set(r['cluster'] for r in idea_rows))
for cl in clusters:
    rows = [r for r in idea_rows if r['cluster']==cl and isinstance(r.get('search_volume'), int) and r['search_volume'] >= 10]
    rows.sort(key=lambda r: (-r['search_volume'], -r['relevance_score']))
    for r in rows[:4]:
        if r['keyword'] not in seen:
            selected.append(r['keyword']); seen.add(r['keyword'])
# add exact strategic seeds where available
for k in sorted(seed_set):
    if k in volume_rows and k not in seen:
        selected.append(k); seen.add(k)
# cap for cost
selected = selected[:55]

serp_rows = []
for i, k in enumerate(selected, 1):
    body = [{'keyword': k, 'location_code': LOCATION_CODE, 'language_code': LANGUAGE_CODE, 'device':'desktop', 'os':'windows', 'depth': 10}]
    obj = post('serp/google/organic/live/advanced', body, f'serp:{k}')
    (RAW / f'serp_{i:02d}.json').write_text(json.dumps(obj, indent=2))
    task = (obj.get('tasks') or [{}])[0]
    result = (task.get('result') or [{}])[0]
    for item in result.get('items') or []:
        if item.get('type') != 'organic':
            continue
        serp_rows.append({
            'keyword': k,
            'cluster': classify(k),
            'rank_group': item.get('rank_group'),
            'rank_absolute': item.get('rank_absolute'),
            'domain': item.get('domain'),
            'url': item.get('url'),
            'title': item.get('title'),
            'description': item.get('description'),
            'breadcrumb': item.get('breadcrumb'),
        })
    time.sleep(0.2)

# Write CSVs.
def write_csv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

idea_fields = ['keyword','cluster','source','seed','relevance_score','search_volume','cpc','competition','competition_level','low_top_of_page_bid','high_top_of_page_bid','monthly_trend_pct','quarterly_trend_pct','yearly_trend_pct','recent_3mo_vs_prior_3mo_pct','latest_month_yoy_pct','keyword_difficulty','main_intent','words_count','last_updated_time']
vol_fields = ['keyword','cluster','search_volume','cpc','competition','competition_level','low_top_of_page_bid','high_top_of_page_bid','monthly_trend_pct','quarterly_trend_pct','yearly_trend_pct','recent_3mo_vs_prior_3mo_pct','latest_month_yoy_pct','keyword_difficulty','main_intent','monthly_searches_json','last_updated_time']
serp_fields = ['keyword','cluster','rank_group','rank_absolute','domain','url','title','description','breadcrumb']
write_csv(OUT / 'keyword_ideas.csv', idea_rows, idea_fields)
write_csv(OUT / 'keyword_volumes_trends.csv', volume_full, vol_fields)
write_csv(OUT / 'serp_samples.csv', serp_rows, serp_fields)

# Summary tables for notes.
by_cluster = {}
for r in idea_rows:
    cl = r['cluster']; by_cluster.setdefault(cl, {'count':0,'known_volume_keywords':0,'total_volume':0,'top':[]})
    by_cluster[cl]['count'] += 1
    if isinstance(r.get('search_volume'), int):
        by_cluster[cl]['known_volume_keywords'] += 1
        by_cluster[cl]['total_volume'] += r['search_volume']
        by_cluster[cl]['top'].append((r['keyword'], r['search_volume'], r.get('cpc')))
for cl in by_cluster:
    by_cluster[cl]['top'] = sorted(by_cluster[cl]['top'], key=lambda x: -x[1])[:8]

# SERP domain frequency.
domains = {}
for s in serp_rows:
    d = s.get('domain')
    if d: domains[d] = domains.get(d,0)+1

top_keywords = sorted([r for r in idea_rows if isinstance(r.get('search_volume'), int)], key=lambda r: -r['search_volume'])[:25]
high_cpc = sorted([r for r in idea_rows if isinstance(r.get('cpc'), (int,float))], key=lambda r: -r['cpc'])[:20]

notes_rows = []
for cl, data in sorted(by_cluster.items(), key=lambda kv: -kv[1]['total_volume']):
    notes_rows.append({'section':'cluster_summary','item':cl,'value':data['total_volume'],'detail':f"{data['count']} keywords; top: " + '; '.join([f'{k} ({v})' for k,v,c in data['top'][:5]])})
for d,c in sorted(domains.items(), key=lambda kv: -kv[1])[:20]:
    notes_rows.append({'section':'serp_domain_frequency','item':d,'value':c,'detail':'top-10 organic appearances across sampled keywords'})
write_csv(OUT / 'notes.csv', notes_rows, ['section','item','value','detail'])

notes_md = []
notes_md.append('# USA keyword research notes — Oviond SEO full audit')
notes_md.append('')
notes_md.append(f'Generated: {datetime.now(timezone.utc).isoformat()}')
notes_md.append('Market: United States, English (`location_code=2840`, `language_code=en`).')
notes_md.append(f'DataForSEO estimated API cost observed: ${api_cost:.4f}.')
notes_md.append(f'Keyword universe retained: {len(idea_rows)} keywords. SERP samples: {len(selected)} keywords / {len(serp_rows)} organic results.')
notes_md.append('')
notes_md.append('## Cluster demand summary')
for cl, data in sorted(by_cluster.items(), key=lambda kv: -kv[1]['total_volume']):
    notes_md.append(f"- **{cl}** — {data['count']} retained keywords, {data['total_volume']} total reported monthly searches. Top: " + '; '.join([f'{k} ({v}/mo, CPC {c})' for k,v,c in data['top'][:5]]))
notes_md.append('')
notes_md.append('## Highest-volume retained keywords')
for r in top_keywords:
    notes_md.append(f"- {r['keyword']} — {r['search_volume']}/mo, CPC {r.get('cpc')}, cluster {r['cluster']}")
notes_md.append('')
notes_md.append('## Highest-CPC retained keywords')
for r in high_cpc[:12]:
    notes_md.append(f"- {r['keyword']} — CPC ${r.get('cpc')}, volume {r.get('search_volume')}, competition {r.get('competition_level')}")
notes_md.append('')
notes_md.append('## Top sampled SERP domains')
for d,c in sorted(domains.items(), key=lambda kv: -kv[1])[:15]:
    notes_md.append(f'- {d} — {c} top-10 appearances')
notes_md.append('')
notes_md.append('## Operator notes')
notes_md.append('- `keyword_ideas.csv` is the prioritization-friendly universe: source, seed, cluster, relevance score, volume/CPC/competition.')
notes_md.append('- `keyword_volumes_trends.csv` keeps monthly trend JSON for seasonality and trend analysis.')
notes_md.append('- `serp_samples.csv` contains top organic URLs for selected high-value/strategic terms; use for SERP-overlap clustering and content brief validation.')
notes_md.append('- Raw DataForSEO responses are retained under `raw/` for auditability; no credentials are written.')
(OUT / 'notes.md').write_text('\n'.join(notes_md) + '\n')

(RAW / 'api_calls.json').write_text(json.dumps({'total_cost': api_cost, 'calls': calls}, indent=2))
print(json.dumps({
    'retained_keywords': len(idea_rows),
    'serp_keywords': len(selected),
    'serp_rows': len(serp_rows),
    'api_cost': round(api_cost, 4),
    'out': str(OUT),
    'top_clusters': sorted([(cl,d['total_volume'],d['count']) for cl,d in by_cluster.items()], key=lambda x:-x[1])[:8]
}, indent=2))
