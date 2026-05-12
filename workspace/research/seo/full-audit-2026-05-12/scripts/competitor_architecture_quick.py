#!/usr/bin/env python3
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import re, html, csv, json, os, time
from pathlib import Path
from collections import Counter
OUT=Path('/data/.openclaw/workspace/research/seo/full-audit-2026-05-12/competitor-architecture')
OUT.mkdir(parents=True, exist_ok=True)
UA='NicoleSEOAudit/1.0'
DOMAINS=['twominutereports.com','agencyanalytics.com','dashthis.com','whatagraph.com','swydo.com','databox.com','tapclicks.com','reportgarden.com','reportingninja.com','supermetrics.com','powermyanalytics.com','funnel.io','windsor.ai','portermetrics.com','coupler.io']
SITEMAPS={d:[f'https://{d}/sitemap.xml',f'https://www.{d}/sitemap.xml'] for d in DOMAINS}
SITEMAPS['dashthis.com']=['https://dashthis.com/sitemap_index.xml','https://dashthis.com/sitemap.xml']
SITEMAPS['supermetrics.com']=['https://supermetrics.com/sitemap.xml','https://supermetrics.com/post-sitemap.xml','https://supermetrics.com/page-sitemap.xml']
SITEMAPS['funnel.io']=['https://funnel.io/sitemap.xml']
SITEMAPS['coupler.io']=['https://www.coupler.io/sitemap.xml','https://blog.coupler.io/sitemap.xml']

def fetch(url,timeout=15):
 try:
  return urlopen(Request(url,headers={'User-Agent':UA}),timeout=timeout).read().decode('utf-8','replace')
 except Exception:
  return ''

def urls_from_sitemap(url, seen=None, depth=0):
 seen=seen or set()
 if url in seen or depth>4: return []
 seen.add(url); txt=fetch(url)
 locs=re.findall(r'<loc>(.*?)</loc>',txt,re.I)
 out=[]
 for loc in locs:
  loc=html.unescape(loc.strip())
  if loc.endswith('.xml') or 'sitemap' in loc.lower() and not re.search(r'\.(html?|php)$',loc):
   out.extend(urls_from_sitemap(loc,seen,depth+1))
  else:
   out.append(loc)
 return out

def classify(u):
 p=urlparse(u).path.strip('/').lower()
 if not p: return 'home'
 if any(x in p for x in ['alternative','alternatives','vs-','-vs-','compare','comparison']): return 'alternatives/comparisons'
 if 'template' in p or 'templates' in p: return 'templates'
 if any(x in p for x in ['integration','connector','data-source','data-sources','source/']): return 'integrations/connectors'
 if any(x in p for x in ['chatgpt','claude','mcp','ai-report','ai-reporting','ai-insight']): return 'ai/agent pages'
 if any(x in p for x in ['metric','kpi','dimension','glossary']): return 'metrics/kpi/glossary'
 if any(x in p for x in ['reporting-software','reporting-tool','dashboard','client-report','white-label','automated-report','agency-report','marketing-report','seo-report','ppc-report','social-media-report']): return 'solution/keyword pages'
 if p.startswith(('blog','resources','learn','guides','articles')) or '/blog/' in p: return 'blog/resources'
 if any(x in p for x in ['pricing','customers','case-studies','case-study','reviews']): return 'commercial/proof'
 return p.split('/')[0]

def clean(s): return re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',html.unescape(s or ''))).strip()
def meta(u):
 s=fetch(u,timeout=12)
 def m(rx):
  x=re.search(rx,s,re.I|re.S); return clean(x.group(1)) if x else ''
 title=m(r'<title[^>]*>(.*?)</title>')
 h1=m(r'<h1[^>]*>(.*?)</h1>')
 d=''; x=re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',s,re.I|re.S)
 if x: d=clean(x.group(1))
 return title,h1,d,len(s)
summary=[]
for d in DOMAINS:
 urls=[]
 for sm in SITEMAPS.get(d,[]):
  urls=urls_from_sitemap(sm)
  if len(urls)>5: break
 urls=sorted(set(urls))
 rows=[{'domain':d,'url':u,'path':urlparse(u).path,'cluster':classify(u)} for u in urls]
 with (OUT/(d.replace('.','_')+'-urls.csv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['domain','url','path','cluster']); w.writeheader(); w.writerows(rows)
 c=Counter(r['cluster'] for r in rows)
 summary.append({'domain':d,'total_urls':len(rows),**{k:v for k,v in c.most_common(12)}})
 strategic=[r['url'] for r in rows if r['cluster'] in ['alternatives/comparisons','templates','integrations/connectors','ai/agent pages','metrics/kpi/glossary','solution/keyword pages']][:80]
 mrows=[]
 for u in strategic:
  title,h1,desc,bytes_=meta(u); mrows.append({'domain':d,'url':u,'cluster':classify(u),'title':title,'h1':h1,'description':desc,'bytes':bytes_})
 with (OUT/(d.replace('.','_')+'-strategic-meta.csv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['domain','url','cluster','title','h1','description','bytes']); w.writeheader(); w.writerows(mrows)
with (OUT/'competitor-architecture-summary.csv').open('w',newline='') as f:
 fields=['domain','total_urls','blog/resources','solution/keyword pages','templates','integrations/connectors','alternatives/comparisons','ai/agent pages','metrics/kpi/glossary','commercial/proof','home']
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader(); w.writerows(summary)
Path(OUT/'competitor-architecture-summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2)[:6000])
