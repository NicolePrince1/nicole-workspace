#!/usr/bin/env python3
import os, re, csv, json, time, base64, hashlib, html, math
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from collections import Counter, defaultdict

BASE=Path('/data/.openclaw/workspace/research/seo/full-audit-2026-05-12')
RAW=BASE/'raw'
OV=BASE/'oviond'
KW=BASE/'keyword-research'
CL=BASE/'clusters'
COMP=BASE/'competitors'
for p in [RAW,OV,KW,CL,COMP]: p.mkdir(parents=True, exist_ok=True)

UA='NicoleSEOAudit/1.0 (+https://www.oviond.com)'
DFS=os.environ.get('DATA_FOR_SEO','').strip()
if not DFS:
    raise SystemExit('DATA_FOR_SEO missing')
TOKEN=base64.b64encode(DFS.encode()).decode() if ':' in DFS else DFS

def http_get(url, timeout=25):
    try:
        return urlopen(Request(url, headers={'User-Agent':UA}), timeout=timeout).read().decode('utf-8','replace')
    except Exception as e:
        return ''

def dfs_post(path, payload, timeout=90, cache=True):
    key=hashlib.sha1((path+'\n'+json.dumps(payload, sort_keys=True)).encode()).hexdigest()
    cp=RAW/(key+'.json')
    if cache and cp.exists():
        return json.loads(cp.read_text())
    req=Request('https://api.dataforseo.com'+path, data=json.dumps(payload).encode(), method='POST', headers={
        'Authorization':'Basic '+TOKEN,
        'Content-Type':'application/json',
        'User-Agent':UA,
    })
    with urlopen(req, timeout=timeout) as r:
        data=json.loads(r.read().decode('utf-8','replace'))
    cp.write_text(json.dumps(data, indent=2))
    return data

def urls_from_sitemap(url, seen=None, max_urls=20000):
    seen=seen or set()
    if url in seen: return []
    seen.add(url)
    txt=http_get(url)
    locs=re.findall(r'<loc>(.*?)</loc>', txt, re.I)
    out=[]
    for loc in locs:
        loc=html.unescape(loc.strip())
        if loc.endswith('.xml'):
            out.extend(urls_from_sitemap(loc, seen, max_urls))
        else:
            out.append(loc)
        if len(out)>=max_urls: break
    return out[:max_urls]

def clean(s):
    return re.sub(r'\s+',' ', re.sub('<[^>]+>',' ', html.unescape(s or ''))).strip()

def page_meta(url):
    s=http_get(url, timeout=15)
    def rx(pattern):
        m=re.search(pattern, s, re.I|re.S)
        return clean(m.group(1)) if m else ''
    title=rx(r'<title[^>]*>(.*?)</title>')
    desc=''
    m=re.search(r'<meta[^>]+(?:name|property)=["\'](?:description|og:description)["\'][^>]+content=["\'](.*?)["\']', s, re.I|re.S)
    if m: desc=clean(m.group(1))
    h1=rx(r'<h1[^>]*>(.*?)</h1>')
    return {'title':title,'description':desc,'h1':h1,'bytes':len(s)}

def classify_url(u):
    p=urlparse(u).path.strip('/').lower()
    if not p: return 'home'
    if 'alternative' in p or 'vs-' in p or '-vs-' in p or 'compare' in p or 'stacking-up' in p: return 'alternatives/comparisons'
    if 'template' in p: return 'templates'
    if p.startswith('data-sources') or 'integration' in p or 'connector' in p or p.startswith('integrations'): return 'integrations/data-sources'
    if 'reporting-software' in p or 'dashboard' in p or 'client-report' in p or 'white-label' in p or 'automated' in p or 'reporting-tool' in p or 'reports-for' in p: return 'solution/keyword pages'
    if p.startswith('blog') or len(p.split('/'))==1: return 'blog/other'
    return p.split('/')[0]

def safe_slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')[:80]

# 1) Oviond crawl
ov_urls=urls_from_sitemap('https://www.oviond.com/sitemap.xml')
ov_rows=[]
strategic=[]
for u in ov_urls:
    cat=classify_url(u)
    row={'url':u,'path':urlparse(u).path,'cluster':cat}
    ov_rows.append(row)
    if cat in {'home','solution/keyword pages','templates','integrations/data-sources','alternatives/comparisons'} or any(x in u.lower() for x in ['marketing-report','client-report','agency','dashboard','seo','ppc','google-ads','facebook']):
        strategic.append(u)
with (OV/'oviond-url-inventory.csv').open('w', newline='') as f:
    w=csv.DictWriter(f, fieldnames=['url','path','cluster']); w.writeheader(); w.writerows(ov_rows)
meta_rows=[]
for u in strategic[:220]:
    mm=page_meta(u); mm.update({'url':u,'cluster':classify_url(u)})
    meta_rows.append(mm)
with (OV/'oviond-strategic-meta.csv').open('w', newline='') as f:
    w=csv.DictWriter(f, fieldnames=['url','cluster','title','h1','description','bytes']); w.writeheader(); w.writerows(meta_rows)
(OV/'oviond-crawl-summary.json').write_text(json.dumps({'total_urls':len(ov_rows),'clusters':Counter(r['cluster'] for r in ov_rows)}, indent=2))

# 2) Keyword universe
sources=['google ads','facebook ads','meta ads','instagram insights','linkedin ads','linkedin pages','tiktok ads','pinterest ads','reddit ads','microsoft ads','bing ads','amazon ads','shopify','woocommerce','ga4','google analytics 4','google search console','google business profile','google my business','youtube analytics','mailchimp','klaviyo','hubspot']
base_terms=[
'marketing reporting software','client reporting software','agency reporting software','digital marketing reporting software','marketing dashboard software','agency dashboard software','client dashboard software','white label reporting software','white label dashboard software','automated marketing reports','automated client reporting','marketing report automation','marketing reporting tool','client reporting tool','agency reporting tool','seo reporting software','ppc reporting software','social media reporting software','ecommerce reporting software','looker studio alternative','google data studio alternative','agencyanalytics alternative','dashthis alternative','whatagraph alternative','swydo alternative','databox alternative','tapclicks alternative','reportgarden alternative','reporting ninja alternative','supermetrics alternative','power my analytics alternative','funnel.io alternative','coupler.io alternative','2 minute reports alternative','two minute reports alternative','marketing report template','client report template','seo report template','ppc report template','social media report template','monthly marketing report template','agency report template','white label report template','marketing kpi dashboard','marketing analytics dashboard','client reporting dashboard','ai marketing reporting','ai client reporting','ai report generator','ai marketing report generator','ai reporting software','chatgpt marketing reporting','claude marketing reporting','mcp marketing reporting','connect marketing data to chatgpt','connect marketing data to claude']
kwset=set(base_terms)
for s in sources:
    kwset.update([
        f'{s} reporting tool', f'{s} reporting software', f'{s} dashboard', f'{s} dashboard template', f'{s} report template', f'{s} client report', f'{s} automated report', f'{s} to looker studio', f'{s} to google sheets', f'{s} connector', f'{s} integration', f'{s} metrics and dimensions', f'connect {s} to chatgpt', f'connect {s} to claude'
    ])
modifiers=['for agencies','for marketing agencies','for clients','white label','automated','best','software','tool','template']
for term in list(base_terms):
    if not term.startswith(('best ','automated ','white label ')):
        kwset.add('best '+term)
    if 'agency' not in term and 'client' not in term:
        kwset.add(term+' for agencies')
kwlist=sorted(kwset)
with (KW/'seed-keywords.csv').open('w', newline='') as f:
    w=csv.writer(f); w.writerow(['keyword']); w.writerows([[k] for k in kwlist])

# 3) Volume / trends via Google Ads search volume live (USA)
vol_rows=[]
for i in range(0,len(kwlist),700):
    chunk=kwlist[i:i+700]
    data=dfs_post('/v3/keywords_data/google_ads/search_volume/live', [{
        'location_code':2840,'language_code':'en','keywords':chunk,'sort_by':'relevance'
    }], timeout=120)
    task=(data.get('tasks') or [{}])[0]
    for item in task.get('result') or []:
        ms=item.get('monthly_searches') or []
        trend=''
        if len(ms)>=2:
            vals=[m.get('search_volume') or 0 for m in ms]
            recent=sum(vals[:3])/max(1,min(3,len(vals)))
            older=sum(vals[-3:])/max(1,min(3,len(vals)))
            trend=round((recent-older)/older,3) if older else ''
        vol_rows.append({
            'keyword':item.get('keyword',''),
            'search_volume':item.get('search_volume') or 0,
            'competition':item.get('competition') or '',
            'competition_index':item.get('competition_index') or '',
            'low_top_of_page_bid':item.get('low_top_of_page_bid') or '',
            'high_top_of_page_bid':item.get('high_top_of_page_bid') or '',
            'trend_recent_vs_oldest_q':trend,
            'monthly_searches_json':json.dumps(ms),
        })
# Ensure zero/no return rows preserved
seen={r['keyword'].lower() for r in vol_rows}
for k in kwlist:
    if k.lower() not in seen:
        vol_rows.append({'keyword':k,'search_volume':0,'competition':'','competition_index':'','low_top_of_page_bid':'','high_top_of_page_bid':'','trend_recent_vs_oldest_q':'','monthly_searches_json':'[]'})
vol_rows.sort(key=lambda r: (int(r.get('search_volume') or 0), str(r['keyword'])), reverse=True)
with (KW/'keyword-volumes-usa.csv').open('w', newline='') as f:
    fields=['keyword','search_volume','competition','competition_index','low_top_of_page_bid','high_top_of_page_bid','trend_recent_vs_oldest_q','monthly_searches_json']
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(vol_rows)

# 4) SERP pulls for top priority keywords
priority=[]
include_patterns=['reporting software','client reporting','agency reporting','dashboard software','white label','alternative','report template','dashboard template','ai ','chatgpt','claude','looker studio','google sheets','reporting tool']
for r in vol_rows:
    kw=r['keyword']; sv=int(r.get('search_volume') or 0)
    if sv>0 and any(p in kw for p in include_patterns):
        priority.append(kw)
priority=priority[:120]
# add essentials even if volume missing
for k in base_terms:
    if k not in priority: priority.append(k)
priority=priority[:150]
serp_rows=[]
kw_to_domains={}
kw_to_urls={}
for kwd in priority:
    data=dfs_post('/v3/serp/google/organic/live/advanced', [{
        'keyword':kwd,'location_code':2840,'language_code':'en','device':'desktop','os':'windows','depth':20
    }], timeout=90)
    task=(data.get('tasks') or [{}])[0]
    result=(task.get('result') or [{}])[0]
    domains=[]; urls=[]
    for item in result.get('items') or []:
        if item.get('type')!='organic': continue
        row={'keyword':kwd,'rank_group':item.get('rank_group'),'domain':item.get('domain'),'url':item.get('url'),'title':item.get('title'),'description':item.get('description')}
        serp_rows.append(row)
        if item.get('domain'): domains.append(item.get('domain'))
        if item.get('url'): urls.append(item.get('url'))
    kw_to_domains[kwd]=domains[:10]
    kw_to_urls[kwd]=urls[:10]
with (KW/'serp-top20-usa.csv').open('w', newline='') as f:
    fields=['keyword','rank_group','domain','url','title','description']
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(serp_rows)

# 5) Competitor SERP share
share=Counter()
for r in serp_rows:
    rg=int(r.get('rank_group') or 999)
    if rg<=10 and r.get('domain'):
        share[r['domain']]+=1
with (KW/'serp-domain-share-top10.csv').open('w', newline='') as f:
    w=csv.writer(f); w.writerow(['domain','top10_count']); w.writerows(share.most_common())

# 6) SERP overlap clustering
# Create graph edges if top10 URL overlap >=2 or domain overlap >=4.
keywords=priority
parent={k:k for k in keywords}
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: parent[rb]=ra
for i,a in enumerate(keywords):
    for b in keywords[i+1:]:
        uo=len(set(kw_to_urls.get(a,[])) & set(kw_to_urls.get(b,[])))
        do=len(set(kw_to_domains.get(a,[])) & set(kw_to_domains.get(b,[])))
        if uo>=2 or do>=4:
            union(a,b)
clusters=defaultdict(list)
for k in keywords: clusters[find(k)].append(k)
# name cluster by highest volume keyword
volmap={r['keyword']:int(r.get('search_volume') or 0) for r in vol_rows}
cluster_rows=[]; keyword_cluster_rows=[]
for idx,(root,members) in enumerate(sorted(clusters.items(), key=lambda kv:max(volmap.get(m,0) for m in kv[1]), reverse=True),1):
    members=sorted(members, key=lambda k:volmap.get(k,0), reverse=True)
    name=members[0]
    total=sum(volmap.get(m,0) for m in members)
    intent=''
    low=' '.join(members).lower()
    if 'alternative' in low: intent='Comparison / competitor alternative'
    elif 'template' in low: intent='Template / downloadable asset'
    elif 'ai' in low or 'chatgpt' in low or 'claude' in low or 'mcp' in low: intent='AI-assisted reporting'
    elif 'google sheets' in low or 'looker studio' in low or 'connector' in low or 'integration' in low: intent='Connector / destination workflow'
    elif 'white label' in low: intent='White-label agency reporting'
    elif 'client reporting' in low or 'agency reporting' in low: intent='Agency/client reporting category'
    else: intent='Reporting software category'
    recommended='New page' if not any(name.replace(' ','-') in r['url'].lower() for r in meta_rows) else 'Refresh existing page'
    cluster_rows.append({'cluster_id':idx,'cluster_name':name,'intent':intent,'keyword_count':len(members),'total_search_volume':total,'primary_keyword':name,'recommended_action':recommended,'notes':''})
    for m in members:
        keyword_cluster_rows.append({'cluster_id':idx,'cluster_name':name,'keyword':m,'search_volume':volmap.get(m,0),'top_serp_domains':' | '.join(kw_to_domains.get(m,[])[:5])})
with (CL/'keyword-clusters-serp-overlap.csv').open('w', newline='') as f:
    fields=['cluster_id','cluster_name','intent','keyword_count','total_search_volume','primary_keyword','recommended_action','notes']
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(cluster_rows)
with (CL/'keyword-cluster-members.csv').open('w', newline='') as f:
    fields=['cluster_id','cluster_name','keyword','search_volume','top_serp_domains']
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(keyword_cluster_rows)

# 7) Strategic page roadmap
road=[]
for c in cluster_rows[:80]:
    name=c['cluster_name']
    slug=safe_slug(name)
    if c['intent']=='Comparison / competitor alternative':
        page_type='Comparison page'; url=f'/alternatives/{slug}/'
    elif c['intent']=='Template / downloadable asset':
        page_type='Template page'; url=f'/templates/{slug}/'
    elif c['intent']=='AI-assisted reporting':
        page_type='AI solution page'; url=f'/solutions/{slug}/'
    elif c['intent']=='Connector / destination workflow':
        page_type='Connector/workflow page'; url=f'/data-sources/{slug}/'
    else:
        page_type='Core solution page'; url=f'/solutions/{slug}/'
    priority_score=(int(c['total_search_volume']) if c['total_search_volume'] else 0) + (500 if 'agency' in name or 'client' in name else 0) + (300 if 'white label' in name else 0) + (250 if 'alternative' in name else 0)
    road.append({'priority_score':priority_score,'cluster_id':c['cluster_id'],'page_type':page_type,'recommended_url':url,'primary_keyword':c['primary_keyword'],'cluster_volume':c['total_search_volume'],'intent':c['intent'],'brief_angle':brief_angle(c['intent'], name) if False else ''})

def angle(intent,name):
    if intent=='Comparison / competitor alternative': return 'Honest alternative page: best fit, pricing/workflow differences, white-label agency reporting angle, migration CTA.'
    if intent=='Template / downloadable asset': return 'Free template + automated Oviond version; include KPI list, screenshots, setup steps, related connectors.'
    if intent=='AI-assisted reporting': return 'AI-assisted agency reporting built on reliable connector truth, scheduled delivery, white-label outputs, and human-editable insights.'
    if intent=='Connector / destination workflow': return 'Show the source-to-report workflow, metrics available, automation, templates, and agency/client use cases.'
    return 'Category page for agencies: pain, use cases, feature proof, integrations, templates, FAQs, comparison links.'
for r in road: r['brief_angle']=angle(r['intent'], r['primary_keyword'])
road=sorted(road, key=lambda r:r['priority_score'], reverse=True)
with (CL/'oviond-seo-roadmap.csv').open('w', newline='') as f:
    fields=['priority_score','cluster_id','page_type','recommended_url','primary_keyword','cluster_volume','intent','brief_angle']
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(road)

# 8) summary markdown
summary=f'''# Oviond USA SEO full audit pipeline summary

Generated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}

## Dataset

- Oviond sitemap URLs crawled: {len(ov_rows)}
- Strategic Oviond pages meta-extracted: {len(meta_rows)}
- Keyword seeds tested in USA Google Ads volume endpoint: {len(kwlist)}
- USA SERPs pulled: {len(priority)} keywords, top 20 desktop organic
- SERP-overlap clusters created: {len(cluster_rows)}

## Top SERP domains across sampled priority queries

''' + '\n'.join([f'- {d}: {n} top-10 appearances' for d,n in share.most_common(25)]) + '''

## Highest-volume / highest-priority clusters

''' + '\n'.join([f"- Cluster {c['cluster_id']}: {c['cluster_name']} — {c['intent']} — volume {c['total_search_volume']}" for c in cluster_rows[:25]]) + '''

## Immediate strategic read

Oviond already appears in some core category SERPs, but the industry SEO game is being won by systematic page matrices: category pages, connector/workflow pages, templates, competitor alternatives, AI-intent pages, and metric/dimension glossaries. The roadmap CSV ranks the first wave of pages to build or refresh.
'''
(BASE/'pipeline-summary.md').write_text(summary)

print(json.dumps({'ok':True,'base':str(BASE),'oviond_urls':len(ov_rows),'keywords':len(kwlist),'serps':len(priority),'clusters':len(cluster_rows),'top_domains':share.most_common(10)}, indent=2))
