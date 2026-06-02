#!/usr/bin/env python3
import csv, json, re, time, sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, urljoin, urldefrag
from urllib.request import Request, urlopen
from urllib.error import HTTPError

BASE = 'https://docs.oviond.com'
OUT = Path('/data/.openclaw/workspace/research/docs-audit-2026-06-02')
UA = 'Mozilla/5.0 OpenClaw Nicole Docs Launch Audit 2026-06-02'

for p in ['raw/md','raw/json','raw/html']:
    (OUT/p).mkdir(parents=True, exist_ok=True)

class HTMLMeta(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_title=False; self.in_h1=False; self.in_h2=False
        self.title=''; self.h1=[]; self.h2=[]; self.meta={}; self.links=[]; self.anchors=set(); self.scripts=[]; self.styles=[]; self.images=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='title': self.in_title=True
        if tag=='h1': self.in_h1=True
        if tag=='h2': self.in_h2=True
        if tag=='meta':
            k=attrs.get('name') or attrs.get('property')
            if k: self.meta[k]=attrs.get('content','')
        if tag=='a' and attrs.get('href'): self.links.append(attrs['href'])
        if attrs.get('id'): self.anchors.add(attrs['id'])
        if tag=='script' and attrs.get('src'): self.scripts.append(attrs['src'])
        if tag=='link' and attrs.get('href'): self.styles.append(attrs['href'])
        if tag=='img' and attrs.get('src'): self.images.append(attrs['src'])
    def handle_endtag(self, tag):
        if tag=='title': self.in_title=False
        if tag=='h1': self.in_h1=False
        if tag=='h2': self.in_h2=False
    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.in_h1 and data.strip(): self.h1.append(data.strip())
        if self.in_h2 and data.strip(): self.h2.append(data.strip())

def fetch(url, accept='*/*', method='GET', timeout=30):
    req = Request(url, method=method, headers={'User-Agent':UA,'Accept':accept})
    try:
        with urlopen(req, timeout=timeout) as r:
            body = b'' if method == 'HEAD' else r.read()
            return {'url':url,'status':r.status,'content_type':r.headers.get('content-type',''),'location':r.headers.get('location',''),'body':body.decode('utf-8','replace')}
    except HTTPError as e:
        body = b'' if method == 'HEAD' else e.read()
        return {'url':url,'status':e.code,'content_type':e.headers.get('content-type',''),'location':e.headers.get('location',''),'body':body.decode('utf-8','replace'),'error':str(e)}
    except Exception as e:
        return {'url':url,'status':0,'content_type':'','location':'','body':'','error':repr(e)}

def slug_path(url):
    p=urlparse(url).path.strip('/') or 'index'
    return re.sub(r'[^A-Za-z0-9_.-]+','_',p)

def word_count(md):
    txt=re.sub(r'```.*?```',' ',md,flags=re.S)
    txt=re.sub(r'<[^>]+>',' ',txt)
    txt=re.sub(r'https?://\S+',' ',txt)
    txt=re.sub(r'[#>*_`\[\](){}=/:-]',' ',txt)
    return len(re.findall(r"\b[A-Za-z][A-Za-z0-9'’-]*\b",txt))

def md_h1s(md): return re.findall(r'^#\s+(.+)$', md, re.M)
def md_h2s(md): return re.findall(r'^##\s+(.+)$', md, re.M)
def md_links(md): return re.findall(r'(?!!)(?:\[[^\]]*\]\(([^)]+)\)|href=["\']([^"\']+)["\'])', md)
def flat_links(md):
    out=[]
    for a,b in md_links(md): out.append(a or b)
    return out

def norm_internal(src_url, href):
    if not href or href.startswith(('mailto:','tel:','javascript:','#')): return None
    href = href.strip()
    absu = urljoin(src_url, href)
    absu, frag = urldefrag(absu)
    pr = urlparse(absu)
    if pr.netloc != 'docs.oviond.com': return None
    if pr.path.startswith('/cdn-cgi/'):
        return None
    # Mintlify markdown links may include .md in llms
    if absu.endswith('.md'): absu = absu[:-3]
    return absu.rstrip('/') or BASE

leak_terms=['Supabase','S3','SQS','Resend','Vercel','cron scheduler','accounts row','users table','upstream API','raw_data','client_integrations','account.onboarding','user_id','resource_type','resource_id','Stripe','database table','foreign key','row-level','bucket']
placeholder_terms=['TODO','TBD','lorem ipsum','coming soon','sample API','Plant Store','sandbox.mintlify.com','NewPlant','/plants']
destructive_words=['delete','bulk-delete','bulk delete','remove','archive','revoke','cancel','purge','permanent','irreversible']

# Discovery
robots=fetch(BASE+'/robots.txt','text/plain'); (OUT/'raw'/'robots.txt').write_text(robots['body'])
llms=fetch(BASE+'/llms.txt','text/plain'); (OUT/'llms.txt').write_text(llms['body'])
sitemap=fetch(BASE+'/sitemap.xml','text/xml'); (OUT/'sitemap.xml').write_text(sitemap['body'])

llms_urls=[]
for m in re.finditer(r'\((https://docs\.oviond\.com/[^)\s]+)\)', llms['body']):
    u=m.group(1)
    llms_urls.append(u[:-3] if u.endswith('.md') else u)
llms_urls=sorted(set(u.rstrip('/') for u in llms_urls))
site_urls=sorted(set(m.rstrip('/') for m in re.findall(r'<loc>(https://docs\.oviond\.com/[^<]+)</loc>', sitemap['body'])))
all_urls=sorted(set(llms_urls)|set(site_urls))

# Specs
spec_paths=['/api-reference/openapi.json','/api/openapi.json','/openapi.json','/api-reference/openapi.json.md','/api/openapi.json.md']
specs={}
def spec_capture_name(path):
    name = path.strip('/').replace('/','_') or 'root'
    if path.endswith('.json'):
        return name
    return name + '.txt'

for path in spec_paths:
    res=fetch(BASE+path,'application/json,text/plain,*/*')
    specs[path]={'status':res['status'],'content_type':res['content_type'],'location':res.get('location',''),'body_start':res['body'][:800]}
    (OUT/'raw'/'json'/spec_capture_name(path)).write_text(res['body'])

pages=[]; findings=[]; link_refs=defaultdict(list); link_targets=set(); external_links=set(); html_pages=[]

# Page markdown + HTML crawl
for i,u in enumerate(all_urls,1):
    mdurl = u + '.md'
    mres = fetch(mdurl,'text/markdown,text/plain,*/*')
    md = mres['body'] if mres['status']==200 else ''
    (OUT/'raw'/'md'/(slug_path(u)+'.md')).write_text(md)
    hres = fetch(u,'text/html,*/*')
    html = hres['body'] if hres['status']==200 else ''
    (OUT/'raw'/'html'/(slug_path(u)+'.html')).write_text(html[:1200000])
    hp=HTMLMeta(); hp.feed(html[:800000])
    wc=word_count(md)
    hs=md_h1s(md)
    h2=md_h2s(md)
    path=urlparse(u).path.lower()
    is_api='/api/' in path or path.startswith('/api-') or path.startswith('/mcp') or path.startswith('/authentication')
    # Use markdown/source page content for content-quality checks. Rendered Mintlify HTML can embed
    # the full docs index/search data, which creates false positives on every page.
    mentions=sorted({t for t in leak_terms if t.lower() in md.lower()})
    placeholders=sorted({t for t in placeholder_terms if t.lower() in md.lower()})
    page={
        'url':u,'md_url':mdurl,'md_status':mres['status'],'html_status':hres['status'],'content_type_md':mres['content_type'],'content_type_html':hres['content_type'],
        'word_count':wc,'md_h1':hs[0] if hs else '', 'html_title':hp.title.strip(), 'html_h1':' '.join(hp.h1).strip(),
        'meta_description':hp.meta.get('description') or hp.meta.get('og:description') or '',
        'h2_count':len(h2),'is_api':is_api,'has_cardgroup':'<CardGroup' in md,'has_steps':'<Steps' in md,
        'has_warning':'<Warning' in md or '<Warning>' in md,'has_info':'<Info' in md,'has_code_fence':'```' in md,
        'has_tabs':'<Tabs' in md,'has_accordion':'<Accordion' in md,'mentions':mentions,'placeholders':placeholders,
        'html_links_count':len(hp.links),'image_count':len(hp.images),'script_count':len(hp.scripts),'style_count':len(hp.styles)
    }
    pages.append(page)
    if mres['status'] != 200:
        sev = 'P0' if u.endswith('/api/openapi.json') else 'P1'
        findings.append({'severity':sev,'type':'markdown_fetch_failed','url':u,'detail':f'markdown endpoint returned {mres["status"]}'})
    if hres['status'] != 200:
        findings.append({'severity':'P0','type':'html_fetch_failed','url':u,'detail':f'HTML page returned {hres["status"]}'})
    if not hs and not u.endswith('.json'):
        findings.append({'severity':'P1','type':'missing_md_h1','url':u,'detail':'No markdown H1 found'})
    if wc < (100 if is_api else 140):
        findings.append({'severity':'P1' if is_api else 'P2','type':'thin_page','url':u,'detail':f'{wc} words'})
    if mentions:
        findings.append({'severity':'P1','type':'internal_or_vendor_leak','url':u,'detail':', '.join(mentions)})
    if placeholders:
        severity='P0' if any(x in placeholders for x in ['Plant Store','sandbox.mintlify.com','/plants','NewPlant']) else 'P1'
        findings.append({'severity':severity,'type':'placeholder_or_sample_content','url':u,'detail':', '.join(placeholders)})
    if any(w in path or w in (page['md_h1'] or '').lower() for w in destructive_words) and not page['has_warning']:
        findings.append({'severity':'P1','type':'destructive_missing_warning','url':u,'detail':'Destructive/risky page has no Mintlify Warning component'})
    if is_api and wc < 180 and not page['has_code_fence']:
        findings.append({'severity':'P1','type':'api_page_lacks_examples','url':u,'detail':'API page is short and has no fenced example'})
    if len(page['meta_description']) < 80 and not u.endswith('.json'):
        findings.append({'severity':'P2','type':'weak_meta_description','url':u,'detail':f'{len(page["meta_description"])} chars'})
    for href in flat_links(md) + hp.links:
        ni=norm_internal(u, href)
        if ni:
            link_targets.add(ni); link_refs[u].append({'href':href,'target':ni})
        elif href and href.startswith(('http://','https://')):
            external_links.add(href)

known=set(all_urls)
# internal target checks
internal_checks=[]
for target in sorted(link_targets):
    status='known' if target in known else 'unknown'
    if status=='unknown':
        res=fetch(target,'text/html,*/*',method='GET',timeout=20)
        status=res['status']
        internal_checks.append({'target':target,'status':status,'content_type':res['content_type']})
        if status >= 400 or status == 0:
            refs=[src for src,rs in link_refs.items() if any(r['target']==target for r in rs)]
            findings.append({'severity':'P1','type':'broken_internal_link','url':target,'detail':f'status {status}; referenced from {refs[:5]}'})
    else:
        internal_checks.append({'target':target,'status':200,'content_type':'known'})

# limited external checks: important Oviond/app/API links only to avoid noisy third-party scans
external_checks=[]
important_ext=sorted([u for u in external_links if any(host in u for host in ['oviond.com','api.oviond.com','app.oviond.com','mintlify.com'])])[:200]
for u in important_ext:
    res=fetch(u,'*/*',method='HEAD',timeout=20)
    if res['status'] in (405,403,0): res=fetch(u,'*/*',method='GET',timeout=20)
    external_checks.append({'url':u,'status':res['status'],'content_type':res['content_type'],'location':res.get('location','')})
    if res['status'] >= 400 or res['status']==0:
        findings.append({'severity':'P2','type':'broken_or_questionable_external_link','url':u,'detail':f'status {res["status"]}'})

# Spec analysis
spec_analysis={}
try:
    sample=json.loads((OUT/'raw'/'json'/'api-reference_openapi.json').read_text())
    spec_analysis['sample_title']=sample.get('info',{}).get('title')
    spec_analysis['sample_paths']=list((sample.get('paths') or {}).keys())[:20]
    if sample.get('info',{}).get('title')=='OpenAPI Plant Store' or any('/plants' in p for p in (sample.get('paths') or {})):
        findings.insert(0, {'severity':'P0','type':'sample_openapi_live','url':BASE+'/api-reference/openapi.json','detail':'Still serves Mintlify OpenAPI Plant Store sample spec'})
except Exception as e:
    spec_analysis['sample_error']=repr(e)
try:
    real=json.loads((OUT/'raw'/'json'/'api_openapi.json').read_text())
    paths=real.get('paths') or {}
    spec_txt=json.dumps(real)
    colon=[p for p in paths if re.search(r'/:[A-Za-z_]',p)]
    brace=[p for p in paths if '{' in p]
    missing_path_params=[]; invalid_param_names=[]; operations=0; operations_missing_examples=0; operations_missing_errors=0
    for p,ops in paths.items():
        if not isinstance(ops, dict): continue
        declared_common=set()
        for par in ops.get('parameters') or []:
            if par.get('in')=='path': declared_common.add(par.get('name'))
        for op,body in ops.items():
            if op.startswith('x-') or op=='parameters' or not isinstance(body, dict): continue
            operations += 1
            params_in_path=re.findall(r'\{([^}]+)\}',p)
            declared=set(declared_common)
            for par in body.get('parameters') or []:
                if par.get('in')=='path': declared.add(par.get('name'))
            for pp in params_in_path:
                if pp not in declared: missing_path_params.append({'path':p,'operation':op,'param':pp})
            for par in body.get('parameters') or []:
                if par.get('in')=='path' and par.get('name') not in params_in_path and ':' not in p:
                    invalid_param_names.append({'path':p,'operation':op,'param':par.get('name')})
            responses=body.get('responses') or {}
            if not any(str(code).startswith(('4','5')) for code in responses.keys()): operations_missing_errors += 1
            has_example='example' in json.dumps(body).lower() or 'examples' in json.dumps(body).lower()
            if not has_example: operations_missing_examples += 1
    vendor=sorted({t for t in leak_terms if t.lower() in spec_txt.lower()})
    auth=json.dumps(real.get('components',{}).get('securitySchemes',{}))
    spec_analysis.update({
        'real_title':real.get('info',{}).get('title'),'real_version':real.get('info',{}).get('version'),
        'path_count':len(paths),'operation_count':operations,'colon_paths':colon,'colon_paths_count':len(colon),'brace_paths_count':len(brace),
        'vendor_terms':vendor,'missing_path_params':missing_path_params,'invalid_path_param_declarations':invalid_param_names[:100],
        'securitySchemes':real.get('components',{}).get('securitySchemes',{}),
        'bearer_jwt_declared':'JWT' in auth,
        'operations_missing_examples':operations_missing_examples,
        'operations_missing_error_responses':operations_missing_errors,
    })
    if colon:
        findings.append({'severity':'P0','type':'openapi_invalid_colon_paths','url':BASE+'/api/openapi.json','detail':f'{len(colon)} colon-style paths still present'})
    if vendor:
        findings.append({'severity':'P1','type':'openapi_internal_or_vendor_leak','url':BASE+'/api/openapi.json','detail':', '.join(vendor)})
    if 'JWT' in auth:
        findings.append({'severity':'P1','type':'auth_scheme_mismatch_risk','url':BASE+'/api/openapi.json','detail':'BearerAuth still declares bearerFormat JWT; docs also use API key language'})
    if operations_missing_examples:
        findings.append({'severity':'P1','type':'openapi_operations_missing_examples','url':BASE+'/api/openapi.json','detail':f'{operations_missing_examples}/{operations} operations appear to lack examples'})
except Exception as e:
    spec_analysis['real_error']=repr(e)
    findings.append({'severity':'P0','type':'openapi_parse_failed','url':BASE+'/api/openapi.json','detail':repr(e)})

# Introduction focused assessment
intro_md=(OUT/'raw'/'md'/'introduction.md').read_text() if (OUT/'raw'/'md'/'introduction.md').exists() else ''
intro_html=(OUT/'raw'/'html'/'introduction.html').read_text() if (OUT/'raw'/'html'/'introduction.html').exists() else ''
intro_links=link_refs.get(BASE+'/introduction', [])
intro_assessment={
    'word_count':word_count(intro_md),'h1':(md_h1s(intro_md) or [''])[0],'h2s':md_h2s(intro_md),
    'has_cardgroup':'<CardGroup' in intro_md,'has_steps':'<Steps' in intro_md,'has_primary_ctas':any(x in intro_md.lower() for x in ['quickstart','authentication','api','mcp']),
    'internal_links':intro_links,'mentions':sorted({t for t in leak_terms if t.lower() in intro_md.lower()}),
    'placeholders':sorted({t for t in placeholder_terms if t.lower() in intro_md.lower()}),
}
if intro_assessment['word_count'] < 250:
    findings.append({'severity':'P1','type':'introduction_too_light','url':BASE+'/introduction','detail':f'{intro_assessment["word_count"]} words; needs stronger product/use-case framing'})
if not intro_assessment['has_primary_ctas']:
    findings.append({'severity':'P1','type':'introduction_weak_cta','url':BASE+'/introduction','detail':'Intro does not clearly route readers into Quickstart/Auth/API/MCP paths'})

summary={
    'generated_at':time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'all_url_count':len(all_urls),'llms_url_count':len(llms_urls),'sitemap_url_count':len(site_urls),
    'llms_minus_sitemap':sorted(set(llms_urls)-set(site_urls))[:100],
    'sitemap_minus_llms':sorted(set(site_urls)-set(llms_urls))[:100],
    'api_pages':sum(1 for p in pages if p['is_api']),'non_api_pages':sum(1 for p in pages if not p['is_api']),
    'findings_total':len(findings),'findings_by_severity':dict(Counter(f['severity'] for f in findings)),'findings_by_type':dict(Counter(f['type'] for f in findings)),
    'thin_pages_under_120':sum(1 for p in pages if p['word_count']<120),'pages_with_leaks':sum(1 for p in pages if p['mentions']),
    'pages_with_placeholder_or_sample':sum(1 for p in pages if p['placeholders']),
    'destructive_pages_missing_warning':sum(1 for f in findings if f['type']=='destructive_missing_warning'),
    'broken_internal_links':sum(1 for f in findings if f['type']=='broken_internal_link'),
    'questionable_external_links':sum(1 for f in findings if f['type']=='broken_or_questionable_external_link'),
    'specs':specs,'spec_analysis':spec_analysis,'intro_assessment':intro_assessment,
}

(OUT/'pages.json').write_text(json.dumps(pages,indent=2))
(OUT/'findings.json').write_text(json.dumps(findings,indent=2))
(OUT/'summary.json').write_text(json.dumps(summary,indent=2))
(OUT/'internal_links.json').write_text(json.dumps({'target_count':len(link_targets),'checks':internal_checks,'note':'Compact file: full page-level refs are intentionally omitted to keep audit artifacts small.'},indent=2))
(OUT/'external_link_checks.json').write_text(json.dumps(external_checks,indent=2))
with (OUT/'findings.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['severity','type','url','detail']); w.writeheader(); w.writerows(findings)
with (OUT/'pages.csv').open('w',newline='') as f:
    fields=['url','md_status','html_status','word_count','md_h1','html_title','html_h1','meta_description','is_api','has_warning','has_code_fence','mentions','placeholders']
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader();
    for p in pages:
        row={k:p.get(k,'') for k in fields}; row['mentions']='; '.join(p.get('mentions') or []); row['placeholders']='; '.join(p.get('placeholders') or [])
        w.writerow(row)
print(json.dumps(summary,indent=2))
