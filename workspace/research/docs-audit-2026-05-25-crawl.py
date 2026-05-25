import json, re, ssl, sys, time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from html.parser import HTMLParser
from collections import Counter, defaultdict

BASE='https://docs.oviond.com'
OUT=Path('/data/.openclaw/workspace/research/docs-audit-2026-05-25')
(OUT/'raw'/'md').mkdir(parents=True, exist_ok=True)
(OUT/'raw'/'json').mkdir(parents=True, exist_ok=True)
UA='Mozilla/5.0 OpenClaw Docs Audit 2026-05-25'

class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_title=False; self.title=''; self.meta={}; self.h1=[]; self.in_h1=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='title': self.in_title=True
        if tag=='meta' and attrs.get('name'): self.meta[attrs.get('name')]=attrs.get('content','')
        if tag=='meta' and attrs.get('property'): self.meta[attrs.get('property')]=attrs.get('content','')
        if tag=='h1': self.in_h1=True
    def handle_endtag(self, tag):
        if tag=='title': self.in_title=False
        if tag=='h1': self.in_h1=False
    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.in_h1: self.h1.append(data.strip())

def fetch(url, accept='*/*'):
    req=Request(url, headers={'User-Agent':UA,'Accept':accept})
    try:
        with urlopen(req, timeout=30) as r:
            body=r.read()
            return {'url':url,'status':r.status,'content_type':r.headers.get('content-type',''),'body':body.decode('utf-8','replace')}
    except HTTPError as e:
        return {'url':url,'status':e.code,'content_type':e.headers.get('content-type',''),'body':e.read().decode('utf-8','replace'),'error':str(e)}
    except Exception as e:
        return {'url':url,'status':0,'content_type':'','body':'','error':repr(e)}

def slug_path(url):
    p=urlparse(url).path.strip('/') or 'index'
    return re.sub(r'[^A-Za-z0-9_.-]+','_',p)

def word_count(md):
    txt=re.sub(r'```.*?```',' ',md,flags=re.S)
    txt=re.sub(r'<[^>]+>',' ',txt)
    txt=re.sub(r'[#>*_`\[\](){}=/:-]',' ',txt)
    return len(re.findall(r"\b[A-Za-z][A-Za-z0-9'’-]*\b",txt))

def h1s(md):
    return re.findall(r'^#\s+(.+)$', md, re.M)

def links(md):
    return re.findall(r'\[[^\]]+\]\(([^)]+)\)', md)

llms=fetch(BASE+'/llms.txt','text/plain')
(OUT/'llms.txt').write_text(llms['body'])
urls=[]
for m in re.finditer(r'\((https://docs\.oviond\.com/[^)\s]+)\)', llms['body']):
    u=m.group(1)
    if u.endswith('.md'):
        urls.append(u[:-3])
    else:
        urls.append(u)
urls=sorted(set(urls))

sitemap=fetch(BASE+'/sitemap.xml','text/xml')
(OUT/'sitemap.xml').write_text(sitemap['body'])
site_urls=sorted(set(re.findall(r'<loc>(https://docs\.oviond\.com/[^<]+)</loc>', sitemap['body'])))
all_urls=sorted(set(urls)|set(site_urls))

specs={}
for path in ['/api-reference/openapi.json','/api/openapi.json','/openapi.json']:
    res=fetch(BASE+path,'application/json')
    specs[path]= {'status':res['status'],'content_type':res['content_type'],'body_start':res['body'][:500]}
    (OUT/'raw'/'json'/(path.strip('/').replace('/','_')+'.json')).write_text(res['body'])

pages=[]; findings=[]; internal_links=defaultdict(list); link_targets=set()
leak_terms=['Supabase','S3','SQS','Resend','Vercel','cron scheduler','accounts row','users table','upstream API','raw_data','client_integrations','account.onboarding','user_id','resource_type','resource_id','Stripe']
destructive_words=['delete','bulk delete','remove','archive','revoke','cancel','purge','permanent','irreversible']

for i,u in enumerate(all_urls,1):
    mdurl=u+'.md'
    res=fetch(mdurl,'text/markdown')
    md=res['body'] if res['status']==200 else ''
    (OUT/'raw'/'md'/(slug_path(u)+'.md')).write_text(md)
    wc=word_count(md)
    hs=h1s(md)
    is_api='/api/' in urlparse(u).path
    page={
        'url':u,'md_url':mdurl,'status':res['status'],'content_type':res['content_type'],'word_count':wc,'h1':hs[0] if hs else '',
        'is_api':is_api,
        'has_cardgroup':'<CardGroup' in md,
        'has_steps':'<Steps' in md,
        'has_warning':'<Warning' in md or '<Warning>' in md,
        'has_code_fence':'```' in md,
        'mentions': [t for t in leak_terms if t.lower() in md.lower()]
    }
    pages.append(page)
    sev=None
    if res['status']!=200:
        findings.append({'severity':'P0','type':'fetch_failed','url':u,'detail':f'markdown endpoint returned {res["status"]}'})
    if not hs:
        findings.append({'severity':'P1','type':'missing_h1','url':u,'detail':'No markdown H1 found'})
    if wc < (80 if is_api else 120):
        findings.append({'severity':'P1' if is_api else 'P2','type':'thin_page','url':u,'detail':f'{wc} words'})
    if page['mentions']:
        findings.append({'severity':'P1','type':'internal_or_vendor_leak','url':u,'detail':', '.join(page['mentions'])})
    path=urlparse(u).path.lower()
    if any(w in path or w in (page['h1'] or '').lower() for w in destructive_words) and not page['has_warning']:
        findings.append({'severity':'P1','type':'destructive_missing_warning','url':u,'detail':'Destructive/risky page has no Mintlify Warning component'})
    if is_api and wc < 160 and not page['has_code_fence']:
        findings.append({'severity':'P1','type':'api_page_lacks_examples','url':u,'detail':'API page is short and has no fenced example'})
    for l in links(md):
        if l.startswith('/'):
            link_targets.add(BASE+l.split('#')[0].rstrip('/'))
            internal_links[u].append(l)

# rendered/html samples
html_samples=[]
for u in [BASE+'/introduction', BASE+'/authentication', BASE+'/api/introduction', BASE+'/quickstart', BASE+'/api/account/delete-account']:
    res=fetch(u,'text/html')
    hp=TitleParser(); hp.feed(res['body'][:500000])
    html_samples.append({'url':u,'status':res['status'],'content_type':res['content_type'],'title':hp.title.strip(),'h1':' '.join(hp.h1).strip(),'description':hp.meta.get('description') or hp.meta.get('og:description') or '', 'body_len':len(res['body'])})

# spec analysis
spec_analysis={}
try:
    real=json.loads((OUT/'raw'/'json'/'api_openapi.json.json').read_text())
    paths=real.get('paths',{})
    colon=[p for p in paths if re.search(r'/:[A-Za-z_]',p)]
    brace=[p for p in paths if '{' in p]
    vendor=[]
    spec_txt=json.dumps(real)
    for t in leak_terms:
        if t.lower() in spec_txt.lower(): vendor.append(t)
    missing_path_params=[]
    for p,ops in paths.items():
        params_in_path=re.findall(r'\{([^}]+)\}',p)
        if params_in_path:
            declared=set()
            for op,body in (ops or {}).items():
                if not isinstance(body,dict): continue
                for par in body.get('parameters') or []:
                    if par.get('in')=='path': declared.add(par.get('name'))
            for pp in params_in_path:
                if pp not in declared: missing_path_params.append({'path':p,'param':pp})
    spec_analysis={'title':real.get('info',{}).get('title'),'path_count':len(paths),'colon_paths':colon,'brace_paths_count':len(brace),'vendor_terms':vendor,'missing_path_params':missing_path_params[:50], 'securitySchemes':real.get('components',{}).get('securitySchemes',{})}
except Exception as e:
    spec_analysis={'error':repr(e)}

# sample spec analysis
try:
    sample=json.loads((OUT/'raw'/'json'/'api-reference_openapi.json.json').read_text())
    if sample.get('info',{}).get('title')=='OpenAPI Plant Store':
        findings.insert(0, {'severity':'P0','type':'sample_openapi_live','url':BASE+'/api-reference/openapi.json','detail':'Still serves Mintlify OpenAPI Plant Store sample spec'})
except Exception as e: pass

summary={
    'generated_at':time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'all_url_count':len(all_urls),'llms_url_count':len(urls),'sitemap_url_count':len(site_urls),
    'api_pages':sum(1 for p in pages if p['is_api']),'non_api_pages':sum(1 for p in pages if not p['is_api']),
    'findings_total':len(findings),'findings_by_severity':dict(Counter(f['severity'] for f in findings)),'findings_by_type':dict(Counter(f['type'] for f in findings)),
    'specs':specs,'spec_analysis':spec_analysis,'html_samples':html_samples,
    'thin_pages_under_120':sum(1 for p in pages if p['word_count']<120),
    'pages_with_leaks':sum(1 for p in pages if p['mentions']),
}
(OUT/'pages.json').write_text(json.dumps(pages,indent=2))
(OUT/'findings.json').write_text(json.dumps(findings,indent=2))
(OUT/'summary.json').write_text(json.dumps(summary,indent=2))
# CSV lite
(OUT/'findings.csv').write_text('severity,type,url,detail\n'+'\n'.join(','.join('"'+str(x.get(k,'')).replace('"','""')+'"' for k in ['severity','type','url','detail']) for x in findings))
print(json.dumps(summary,indent=2))
