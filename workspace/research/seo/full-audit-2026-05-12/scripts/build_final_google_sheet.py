#!/usr/bin/env python3
import csv, json, os, re, subprocess, urllib.request, urllib.parse, urllib.error, math, time
from pathlib import Path
from collections import defaultdict, Counter
BASE=Path('/data/.openclaw/workspace/research/seo/full-audit-2026-05-12')
DEL=BASE/'deliverables'; DEL.mkdir(parents=True, exist_ok=True)

def read_csv(path):
    if not Path(path).exists(): return []
    with open(path, newline='', encoding='utf-8') as f: return list(csv.DictReader(f))
def write_csv(name, rows, fields=None):
    path=DEL/(name+'.csv')
    if fields is None:
        fields=[]
        for r in rows:
            for k in r.keys():
                if k not in fields: fields.append(k)
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
    return path

def n(v):
    try: return float(v or 0)
    except: return 0.0


def is_relevant_keyword(k):
    s=(k or '').lower().strip()
    if not s: return False
    # Hard exclusions from competitor keyword exports that are not buyer/reporting intent.
    if re.search(r'\b(log ?in|login|sign ?in|salary|jobs?|careers?|discrete vs continuous|continuous and discrete|continuous versus discrete)\b', s): return False
    if s in {'windsor','funnel','powerbi','constant contact','looker studio','google sheets','shopify','hubspot','mailchimp','klaviyo','databox','supermetrics','whatagraph','dashthis','swydo'}:
        return False
    phrases=[
        'report','reporting','dashboard','template','agency','client','marketing','ads','ppc','seo','social media','analytics','ga4','google analytics','search console','looker studio','data studio','google sheets','white label','white-label','connector','integration','data source','kpi','metrics','dimensions','roas','cpa','cpc','ctr','alternative','alternatives','compare','comparison','chatgpt','claude','mcp','ai ','ai-','oviond','agencyanalytics','dashthis','whatagraph','swydo','two minute reports','twominutereports','tapclicks','reportgarden','reporting ninja','supermetrics','power my analytics','funnel.io','coupler','porter metrics','portermetrics'
    ]
    return any(p in s for p in phrases)

def cluster_for(k):
    s=(k or '').lower()
    if any(x in s for x in ['alternative','alternatives','vs ',' vs','competitor','comparison','compare']): return 'Competitor alternatives / comparison'
    if any(x in s for x in ['chatgpt','claude','mcp','ai report','ai reporting','ai marketing','report generator','connect marketing data to ai']): return 'AI-assisted reporting'
    if 'template' in s: return 'Templates'
    if any(x in s for x in ['google sheets','looker studio','data studio','to sheets','to looker']): return 'Destination workflows: Sheets / Looker Studio'
    if any(x in s for x in ['white label','white-label','branded report']): return 'White-label reporting'
    if any(x in s for x in ['client reporting','agency reporting','marketing agency reporting','for clients','for agencies']): return 'Agency/client reporting'
    if any(x in s for x in ['seo report','seo reporting','search console','gsc','rank tracking','keyword report']): return 'SEO reporting'
    if any(x in s for x in ['ppc','google ads','facebook ads','meta ads','paid ads','linkedin ads','tiktok ads','microsoft ads','bing ads','amazon ads','pinterest ads','reddit ads']): return 'Paid ads reporting'
    if any(x in s for x in ['social media','instagram','facebook insights','linkedin pages','youtube analytics']): return 'Social reporting'
    if any(x in s for x in ['dashboard','kpi','metrics','dimension','analytics dashboard']): return 'Dashboards / KPI reporting'
    if any(x in s for x in ['connector','integration','data source','shopify','woocommerce','hubspot','klaviyo','mailchimp','ga4','google analytics']): return 'Connector / source reporting'
    if any(x in s for x in ['marketing reporting','marketing report','reporting software','reporting tool','report automation','automated report']): return 'Core marketing reporting'
    return 'Long-tail / support content'

def page_type(cluster):
    return {
        'Competitor alternatives / comparison':'Comparison page',
        'AI-assisted reporting':'AI solution page',
        'Templates':'Template page',
        'Destination workflows: Sheets / Looker Studio':'Workflow/destination page',
        'White-label reporting':'Solution page',
        'Agency/client reporting':'Core category page',
        'SEO reporting':'Solution + template cluster',
        'Paid ads reporting':'Solution + connector cluster',
        'Social reporting':'Solution + template cluster',
        'Dashboards / KPI reporting':'Solution/glossary page',
        'Connector / source reporting':'Connector page',
        'Core marketing reporting':'Core category page',
    }.get(cluster,'Support content')

def url_for(cluster, keyword):
    slug=re.sub(r'[^a-z0-9]+','-',keyword.lower()).strip('-')
    if cluster=='Competitor alternatives / comparison': return f'/alternatives/{slug}/'
    if cluster=='Templates': return f'/templates/{slug}/'
    if cluster=='Connector / source reporting': return f'/data-sources/{slug}/'
    return f'/solutions/{slug}/'

ideas=read_csv(BASE/'keyword-research/keyword_ideas.csv')
vols=read_csv(BASE/'keyword-research/keyword-volumes-usa.csv')
volmap={r['keyword'].lower():r for r in vols}
serps=read_csv(BASE/'keyword-research/serp-top20-usa.csv') + read_csv(BASE/'keyword-research/serp_samples.csv')
ranked=read_csv(BASE/'competitor-keywords/competitor-ranked-keywords-usa.csv')
domain_summary=read_csv(BASE/'competitor-keywords/competitor-domain-seo-summary-usa.csv')
arch=read_csv(BASE/'competitor-architecture/competitor-architecture-summary.csv')
ov_pages=read_csv(BASE/'oviond/oviond-strategic-meta.csv')
# Master keyword table
bykw={}
for r in ideas:
    kw=r.get('keyword','').strip().lower()
    if not kw: continue
    bykw.setdefault(kw, {'keyword':kw,'source':'seed/dataforseo ideas','competitor_domains':'','best_competitor_rank':'','best_competitor_url':'','oviond_rank':'','oviond_url':''})
    bykw[kw].update({'search_volume':r.get('search_volume') or 0,'cpc':r.get('cpc') or '', 'competition_level':r.get('competition_level') or r.get('competition') or '', 'trend_recent':r.get('recent_3mo_vs_prior_3mo_pct') or r.get('monthly_trend_pct') or '', 'intent':r.get('main_intent') or '', 'seed_cluster':r.get('cluster') or ''})
for r in vols:
    kw=r.get('keyword','').strip().lower()
    if not kw: continue
    bykw.setdefault(kw, {'keyword':kw,'source':'seed volume expansion','competitor_domains':'','best_competitor_rank':'','best_competitor_url':'','oviond_rank':'','oviond_url':''})
    if not bykw[kw].get('search_volume'): bykw[kw]['search_volume']=r.get('search_volume') or 0
    bykw[kw].setdefault('cpc', r.get('high_top_of_page_bid') or '')
    bykw[kw].setdefault('competition_level', r.get('competition') or '')
    bykw[kw].setdefault('trend_recent', r.get('trend_recent_vs_oldest_q') or '')
competitors_by_kw=defaultdict(list); oviond_by_kw={}
for r in ranked:
    kw=(r.get('keyword') or '').lower().strip(); dom=r.get('domain') or ''
    if not kw: continue
    sv=n(r.get('search_volume'))
    # Retain only buyer/reporting/agency/connector/template/comparison/AI keywords. Competitor exports include noisy brand/login/math terms.
    if not is_relevant_keyword(kw):
        continue
    if sv < 10 and not any(x in kw for x in ['oviond','agencyanalytics','dashthis','whatagraph','swydo','supermetrics','two minute reports','twominutereports','alternative']):
        continue
    bykw.setdefault(kw, {'keyword':kw,'source':'competitor ranked keywords','competitor_domains':'','best_competitor_rank':'','best_competitor_url':'','oviond_rank':'','oviond_url':''})
    if not bykw[kw].get('search_volume'): bykw[kw]['search_volume']=r.get('search_volume') or 0
    if not bykw[kw].get('cpc'): bykw[kw]['cpc']=r.get('cpc') or ''
    if dom in ['oviond.com','www.oviond.com']:
        if kw not in oviond_by_kw or n(r.get('rank_group')) < n(oviond_by_kw[kw].get('rank_group')):
            oviond_by_kw[kw]=r
    else:
        competitors_by_kw[kw].append(r)
for kw, rows in competitors_by_kw.items():
    rows=sorted(rows, key=lambda r:n(r.get('rank_group')) or 999)
    top=rows[0]
    bykw[kw]['competitor_domains']=' | '.join(dict.fromkeys([r.get('domain','') for r in rows[:6]]))
    bykw[kw]['best_competitor_rank']=top.get('rank_group') or ''
    bykw[kw]['best_competitor_url']=top.get('ranking_url') or ''
for kw,r in oviond_by_kw.items():
    bykw.setdefault(kw, {'keyword':kw})
    bykw[kw]['oviond_rank']=r.get('rank_group') or ''
    bykw[kw]['oviond_url']=r.get('ranking_url') or ''
master=[]
for kw,r in bykw.items():
    if not is_relevant_keyword(kw):
        continue
    sv=n(r.get('search_volume')); comp_rank=n(r.get('best_competitor_rank')); ov_rank=n(r.get('oviond_rank'))
    cl=cluster_for(kw)
    # Keep the planning dataset commercial/relevant. Raw competitor exports remain in their own tab.
    if cl=='Long-tail / support content':
        continue
    if cl=='Templates' and not any(x in kw for x in ['report','reporting','marketing','ads','seo','social','client','agency','dashboard','looker','analytics']):
        continue
    if cl=='Destination workflows: Sheets / Looker Studio' and not any(x in kw for x in ['report','reporting','marketing','ads','analytics','client','agency','dashboard','looker studio','data studio']):
        continue
    if cl=='Social reporting' and 'monitoring' in kw and not any(x in kw for x in ['report','reporting','dashboard','analytics']):
        continue
    if cl=='Connector / source reporting' and not any(x in kw for x in ['report','reporting','dashboard','analytics','metrics','dimensions','connector','integration','data source']):
        continue
    if ov_rank and ov_rank<=10: gap='Defend / improve CTR'
    elif ov_rank and ov_rank<=30: gap='Quick-win refresh'
    elif comp_rank and comp_rank<=10: gap='High-priority gap'
    elif sv>=100: gap='New/refresh opportunity'
    else: gap='Long-tail support'
    score=sv + (500 if gap=='High-priority gap' else 0) + (300 if cl in ['Agency/client reporting','White-label reporting','Competitor alternatives / comparison','AI-assisted reporting'] else 0) + (200 if n(r.get('cpc'))>=50 else 0)
    master.append({'priority_score':round(score,2),'cluster':cl,'keyword':kw,'search_volume':int(sv),'cpc':r.get('cpc',''),'competition_level':r.get('competition_level',''),'trend_recent':r.get('trend_recent',''),'intent':r.get('intent',''),'gap_status':gap,'oviond_rank':r.get('oviond_rank',''),'oviond_url':r.get('oviond_url',''),'best_competitor_rank':r.get('best_competitor_rank',''),'competitor_domains':r.get('competitor_domains',''),'best_competitor_url':r.get('best_competitor_url',''),'recommended_page_type':page_type(cl),'recommended_url':url_for(cl, kw)})
master=sorted(master, key=lambda r:(n(r['priority_score']),n(r['search_volume'])), reverse=True)
# Cluster map
clusters=[]
for cl,rows in defaultdict(list, {c:[r for r in master if r['cluster']==c] for c in set(r['cluster'] for r in master)}).items():
    rows=sorted(rows,key=lambda r:n(r['priority_score']),reverse=True)
    clusters.append({'cluster':cl,'keyword_count':len(rows),'total_search_volume':sum(n(r['search_volume']) for r in rows),'top_keyword':rows[0]['keyword'] if rows else '','top_keyword_volume':rows[0]['search_volume'] if rows else 0,'page_type':page_type(cl),'recommended_strategy':{
        'Competitor alternatives / comparison':'Build/refresh honest alternative pages for the tools prospects already compare: AgencyAnalytics, DashThis, Whatagraph, Swydo, 2-Minute Reports, Supermetrics, Looker Studio.',
        'AI-assisted reporting':'Own AI-assisted agency reporting before competitors define it: reliable connectors + white-label scheduled reports + editable AI insights + API/MCP future.',
        'Templates':'Turn templates into acquisition assets with screenshots, KPIs, setup steps, FAQs, and links into connector pages.',
        'Destination workflows: Sheets / Looker Studio':'Decide whether to compete directly on Sheets/Looker workflows or position Oviond as the agency-grade alternative to spreadsheet/report-builder patchwork.',
        'White-label reporting':'Make white-label reporting a pillar page with proof, examples, pricing objections, and agency workflow CTAs.',
        'Agency/client reporting':'Core money cluster: client reporting, agency reporting, automated reporting, client dashboards. Build the strongest category hub in the industry.',
        'SEO reporting':'Build a hub plus templates for SEO reports, GSC, rank/keyword reporting, PageSpeed, local SEO.',
        'Paid ads reporting':'Build paid media reporting cluster around Google Ads, Meta Ads, PPC, ROAS, multi-channel paid reporting.',
        'Social reporting':'Build social media reporting/templates cluster around Meta, Instagram, LinkedIn, TikTok, YouTube.',
        'Dashboards / KPI reporting':'Create KPI/dashboard support pages that internally link into solution and template pages.',
        'Connector / source reporting':'Systematize every integration as source reporting tool + dashboard template + metrics page where SERPs justify it.',
        'Core marketing reporting':'Refresh homepage/core pages around simple automated reporting software for agencies.'
    }.get(cl,'Use as support content feeding commercial pages')})
clusters=sorted(clusters,key=lambda r:n(r['total_search_volume']),reverse=True)

# Replace noisy broad competitor-derived cluster map with the retained USA buyer-intent cluster summary from DataForSEO research.
cluster_label_map={
 'seo_reporting':('SEO reporting','Solution + template cluster','Build the category hub for SEO reports, GSC, keyword/rank reporting, PageSpeed, local SEO, and client-ready SEO templates.'),
 'paid_ads_reporting':('Paid ads reporting','Solution + connector cluster','Build paid-media reporting around Google Ads, Meta/Facebook Ads, PPC, ROAS, CPA, and multi-channel paid performance.'),
 'social_reporting':('Social reporting','Solution + template cluster','Build social reporting around social media report templates, Instagram, Facebook Insights, LinkedIn, TikTok, and YouTube.'),
 'marketing_reporting':('Core marketing reporting','Core category page','Refresh the core category around simple automated marketing reporting software for agencies.'),
 'competitor_alternative':('Competitor alternatives / comparison','Comparison page','Build honest alternative pages for AgencyAnalytics, DashThis, Whatagraph, Swydo, 2-Minute Reports, Supermetrics, Looker Studio, and similar tools.'),
 'white_label_reporting':('White-label reporting','Solution page','Make white-label reporting a pillar with brand control, client-ready proof, examples, and agency workflow CTAs.'),
 'dashboard_software':('Dashboards / KPI reporting','Solution/glossary page','Build dashboard and KPI pages that support the commercial reporting clusters.'),
 'analytics_reporting':('Connector / source reporting','Connector page','Use GA4/GSC/source-specific pages to connect integration intent to report templates and solution pages.'),
 'client_reporting':('Agency/client reporting','Core category page','Build the strongest client reporting hub in the market for agency reporting chaos, automation, trust, and delivery.'),
 'agency_reporting':('Agency/client reporting','Core category page','Support the client-reporting hub with agency-specific reporting software/tool intent.'),
 'ai_reporting':('AI-assisted reporting','AI solution page','Own AI-assisted agency reporting: reliable connector truth, white-label delivery, editable insights, API/MCP direction.'),
 'connector_automation':('Destination workflows: Sheets / Looker Studio','Workflow/destination page','Decide where to compete with Sheets/Looker workflows and where to position Oviond as the less-fragile agency-grade alternative.'),
}
notes_rows=read_csv(BASE/'keyword-research/notes.csv')
curated_clusters=[]
for nr in notes_rows:
    if nr.get('section')!='cluster_summary': continue
    item=nr.get('item')
    if item not in cluster_label_map: continue
    label,ptype,strat=cluster_label_map[item]
    detail=nr.get('detail','')
    top_kw=''
    m=re.search(r'top: ([^(;]+)', detail)
    if m: top_kw=m.group(1).strip()
    curated_clusters.append({'cluster':label,'keyword_count':re.search(r'(\d+) keywords',detail).group(1) if re.search(r'(\d+) keywords',detail) else '', 'total_search_volume':nr.get('value','0'),'top_keyword':top_kw,'top_keyword_volume':'','page_type':ptype,'recommended_strategy':strat})
# Merge duplicate agency/client rows.
merged={}
for c in curated_clusters:
    key=c['cluster']
    if key not in merged: merged[key]=c
    else:
        merged[key]['total_search_volume']=str(int(float(merged[key]['total_search_volume'] or 0))+int(float(c['total_search_volume'] or 0)))
        merged[key]['keyword_count']=str(int(merged[key]['keyword_count'] or 0)+int(c['keyword_count'] or 0))
        if not merged[key]['top_keyword']: merged[key]['top_keyword']=c['top_keyword']
clusters=sorted(merged.values(), key=lambda r:n(r['total_search_volume']), reverse=True)

# Roadmap: curated commercial-first page plan.
commercial_terms = [
('Core marketing reporting','marketing reporting software'),('Agency/client reporting','client reporting software'),('Agency/client reporting','agency reporting software'),('Agency/client reporting','marketing agency reporting software'),('Core marketing reporting','digital marketing reporting software'),('White-label reporting','white label reporting software'),('White-label reporting','white label dashboard software'),('Dashboards / KPI reporting','marketing dashboard software'),('Dashboards / KPI reporting','agency dashboard software'),('Agency/client reporting','client dashboard software'),('Core marketing reporting','automated marketing reports'),('Agency/client reporting','automated client reporting'),
('SEO reporting','seo reporting for clients'),('SEO reporting','seo reporting software'),('SEO reporting','seo reporting tool'),('SEO reporting','seo report template'),('SEO reporting','google search console reporting tool'),('SEO reporting','google search console dashboard'),('SEO reporting','keyword ranking report'),('SEO reporting','local seo report template'),
('Paid ads reporting','ppc reporting tool'),('Paid ads reporting','ppc reporting software'),('Paid ads reporting','ppc report template'),('Paid ads reporting','google ads reporting tool'),('Paid ads reporting','google ads report template'),('Paid ads reporting','facebook ads reporting tool'),('Paid ads reporting','facebook ads report template'),('Paid ads reporting','meta ads reporting'),('Paid ads reporting','paid media reporting dashboard'),
('Social reporting','social media reporting tool'),('Social reporting','social media reporting software'),('Social reporting','social media reporting template'),('Social reporting','instagram analytics report'),('Social reporting','linkedin ads reporting'),('Social reporting','tiktok ads reporting'),('Social reporting','youtube analytics report'),
('Templates','marketing report template'),('Templates','client report template'),('Templates','monthly marketing report template'),('Templates','digital marketing report template'),('Templates','agency report template'),('Templates','white label report template'),('Templates','dashboard report template'),
('Competitor alternatives / comparison','agencyanalytics alternative'),('Competitor alternatives / comparison','alternative to agencyanalytics'),('Competitor alternatives / comparison','dashthis alternative'),('Competitor alternatives / comparison','whatagraph alternative'),('Competitor alternatives / comparison','swydo alternative'),('Competitor alternatives / comparison','looker studio alternative'),('Competitor alternatives / comparison','google data studio alternative'),('Competitor alternatives / comparison','supermetrics alternative'),('Competitor alternatives / comparison','two minute reports alternative'),('Competitor alternatives / comparison','2 minute reports alternative'),('Competitor alternatives / comparison','databox alternative'),('Competitor alternatives / comparison','tapclicks alternative'),('Competitor alternatives / comparison','reportgarden alternative'),('Competitor alternatives / comparison','reporting ninja alternative'),('Competitor alternatives / comparison','coupler.io alternative'),('Competitor alternatives / comparison','porter metrics alternative'),('Competitor alternatives / comparison','power my analytics alternative'),
('Destination workflows: Sheets / Looker Studio','google ads to google sheets'),('Destination workflows: Sheets / Looker Studio','facebook ads to google sheets'),('Destination workflows: Sheets / Looker Studio','ga4 to google sheets'),('Destination workflows: Sheets / Looker Studio','google analytics to google sheets'),('Destination workflows: Sheets / Looker Studio','google search console to google sheets'),('Destination workflows: Sheets / Looker Studio','google ads to looker studio'),('Destination workflows: Sheets / Looker Studio','facebook ads to looker studio'),('Destination workflows: Sheets / Looker Studio','ga4 to looker studio'),
('Connector / source reporting','ga4 reporting tool'),('Connector / source reporting','google analytics reporting tool'),('Connector / source reporting','shopify reporting tool'),('Connector / source reporting','google business profile reporting tool'),('Connector / source reporting','linkedin ads reporting tool'),('Connector / source reporting','tiktok ads reporting tool'),('Connector / source reporting','youtube analytics reporting tool'),('Connector / source reporting','hubspot reporting dashboard'),
('AI-assisted reporting','ai marketing reporting'),('AI-assisted reporting','ai client reporting'),('AI-assisted reporting','ai report generator'),('AI-assisted reporting','ai marketing report generator'),('AI-assisted reporting','ai reporting software'),('AI-assisted reporting','chatgpt marketing reporting'),('AI-assisted reporting','claude marketing reporting'),('AI-assisted reporting','mcp marketing reporting'),('AI-assisted reporting','connect marketing data to chatgpt'),('AI-assisted reporting','connect marketing data to claude')
]
master_by_kw={r['keyword']:r for r in master}
def make_road_row(term_cluster, term, idx):
    r=master_by_kw.get(term)
    if r:
        sv=r['search_volume']; gap=r['gap_status']; score=r['priority_score']; url=r['recommended_url']; ptype=r['recommended_page_type']
    else:
        v=volmap.get(term.lower(),{})
        sv=str(int(n(v.get('search_volume')))); gap='Strategic new build'; score=str(n(sv)+(500 if term_cluster in ['Agency/client reporting','White-label reporting','Competitor alternatives / comparison','AI-assisted reporting'] else 0)); url=url_for(term_cluster,term); ptype=page_type(term_cluster)
    phase='Phase 1' if idx<40 else 'Phase 2' if idx<85 else 'Phase 3'
    return {'phase':phase,'priority_score':score,'cluster':term_cluster,'primary_keyword':term,'search_volume':sv,'gap_status':gap,'recommended_page_type':ptype,'recommended_url':url,'angle':'','internal_links':'','notes':''}
road=[]; seen=set()
for cl,term in commercial_terms:
    if term in seen: continue
    seen.add(term); road.append(make_road_row(cl,term,len(road)))
# Add strongest remaining commercial opportunities behind curated terms.
for r in master:
    if len(road)>=150: break
    if r['keyword'] in seen: continue
    if r['gap_status'] not in ['High-priority gap','Quick-win refresh','New/refresh opportunity','Defend / improve CTR']: continue
    if n(r['search_volume']) < 70 and r['gap_status']!='High-priority gap': continue
    seen.add(r['keyword'])
    road.append({'phase':'Phase 1' if len(road)<40 else 'Phase 2' if len(road)<95 else 'Phase 3','priority_score':r['priority_score'],'cluster':r['cluster'],'primary_keyword':r['keyword'],'search_volume':r['search_volume'],'gap_status':r['gap_status'],'recommended_page_type':r['recommended_page_type'],'recommended_url':r['recommended_url'],'angle':'', 'internal_links':'', 'notes':''})
for rr in road:
    cl=rr['cluster']
    rr['angle']={
      'Competitor alternatives / comparison':'Conversion page with comparison table, who each tool fits, agency workflow angle, migration CTA, honest limitations.',
      'AI-assisted reporting':'Show AI insights grounded in connector truth, not generic chatbot summaries; tie to scheduled reports and agency review flow.',
      'Templates':'Free template asset plus automated Oviond version; include KPI checklist, screenshots, FAQ, related connectors.',
      'Destination workflows: Sheets / Looker Studio':'Capture workflow pain; position Oviond as easier, branded, less fragile agency reporting.',
      'Agency/client reporting':'Lead with agency pain: reporting chaos, client trust, white-label delivery, fast setup, scheduled reporting.',
      'White-label reporting':'Show brand control, custom domains, client portals/reports, agency credibility.',
      'SEO reporting':'Cover GSC/rank/keyword/PageSpeed/local SEO, template preview, automated delivery.',
      'Paid ads reporting':'Cover spend, ROAS, CPA, campaign performance, cross-channel paid media reporting.',
      'Social reporting':'Cover engagement/reach/follower/content KPIs and monthly client social reporting.',
      'Connector / source reporting':'Show source metrics, automated pulls, templates, report examples, and cross-channel reporting use cases.',
      'Core marketing reporting':'Make this a money page: simple automated reporting software for agencies, proof, templates, integrations, comparisons.'
    }.get(cl,'Build as SEO support page that links into the nearest money page.')
    rr['internal_links']='Homepage | Integrations | Templates | Alternatives | Pricing | Related connector pages'
# Competitor win/loss pages
# Competitor win/loss pages from ranked keywords
# SERP share condensed
serp_share=read_csv(BASE/'keyword-research/serp-domain-share-top10.csv')
# Executive summary
exec_rows=[
 {'section':'Status','finding':'USA keyword research, Oviond crawl, competitor ranked keyword pull, SERP samples, and architecture crawl are complete. Sheet generated from local CSV deliverables.'},
 {'section':'Biggest SEO opportunity','finding':'Build the strongest agency/client reporting hub in the industry, then surround it with white-label, templates, paid ads, SEO reporting, social reporting, alternatives, and AI-assisted reporting clusters.'},
 {'section':'Competitor threat','finding':'2-Minute Reports is the most structurally aggressive newer SEO competitor: connector + destination + template + alternatives + AI/MCP pages. DashThis/Whatagraph/AgencyAnalytics remain strong on classic agency reporting/template SERPs.'},
 {'section':'USA demand signal','finding':'Highest demand pools found: SEO reporting, paid ads reporting, social reporting, marketing reporting, competitor alternatives, templates, and destination workflows.'},
 {'section':'SERP reality','finding':'Reddit appears heavily across sampled SERPs, which means prospects are asking for tool recommendations; Oviond can win with better comparison and workflow pages.'},
 {'section':'Execution rule','finding':'Do not publish thin pages. Every page should include use-case proof, screenshots/templates, integration depth, FAQs/schema, and strong internal links.'},
]
# Content briefs for top roadmap
briefs=[]
for rr in road[:60]:
    briefs.append({'recommended_url':rr['recommended_url'],'page_type':rr['recommended_page_type'],'cluster':rr['cluster'],'primary_keyword':rr['primary_keyword'],'target_secondary_keywords':'See Keyword Master filtered by cluster','h1_draft':rr['primary_keyword'].title() + ' for Agencies','title_tag_draft':rr['primary_keyword'].title() + ' | Oviond','brief':rr['angle'],'must_include_sections':'Pain/problem | What to track | How Oviond automates it | Example/template | Integrations | FAQs | CTA','conversion_cta':'Start free trial / Book demo / View template','internal_links':rr['internal_links']})
# Write deliverables
write_csv('00_Executive_Summary',exec_rows,['section','finding'])
write_csv('01_Cluster_Map',clusters,['cluster','keyword_count','total_search_volume','top_keyword','top_keyword_volume','page_type','recommended_strategy'])
write_csv('02_Priority_Roadmap',road,['phase','priority_score','cluster','primary_keyword','search_volume','gap_status','recommended_page_type','recommended_url','angle','internal_links','notes'])
write_csv('03_Keyword_Master_USA',master[:5000],['priority_score','cluster','keyword','search_volume','cpc','competition_level','trend_recent','intent','gap_status','oviond_rank','oviond_url','best_competitor_rank','competitor_domains','best_competitor_url','recommended_page_type','recommended_url'])
write_csv('04_Content_Briefs',briefs,['recommended_url','page_type','cluster','primary_keyword','target_secondary_keywords','h1_draft','title_tag_draft','brief','must_include_sections','conversion_cta','internal_links'])
write_csv('05_Competitor_Domain_Summary',domain_summary,['domain','total_count','items_count','pos_1','pos_2_3','pos_4_10','pos_11_20','etv','estimated_paid_traffic_cost','is_new','is_up','is_down'])
write_csv('06_Competitor_Architecture',arch)
write_csv('07_Competitor_Ranked_Keywords',ranked[:11000])
write_csv('08_Oviond_Current_Pages',ov_pages)
write_csv('09_USA_SERP_Samples',serps[:12000])
# markdown strategy brief
md=f'''# Oviond USA SEO full-audit strategy brief

Generated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}

## Strategic verdict

Oviond can become the most SEO-optimized agency reporting website in the category, but only if the new site is built as an intentional SEO product architecture — not as a normal SaaS brochure site.

The winning structure is:

1. Core category hub: client reporting software / agency reporting software / marketing reporting software.
2. Agency proof pillars: white-label reports, client dashboards, automated reports, scheduled reporting, templates.
3. Channel clusters: SEO reporting, PPC/paid ads reporting, social media reporting, ecommerce reporting.
4. Source pages: Google Ads, Meta/Facebook Ads, GA4, GSC, LinkedIn Ads, TikTok Ads, Shopify, GBP, YouTube, etc.
5. Template pages: every report type becomes a conversion asset.
6. Alternative pages: capture users actively comparing AgencyAnalytics, DashThis, Whatagraph, Swydo, 2-Minute Reports, Supermetrics, Looker Studio.
7. AI-first cluster: AI client reporting, AI marketing report generator, ChatGPT/Claude/MCP marketing reporting.
8. Metric/dimension glossary: use as long-tail topical authority and internal-link fuel.

## Top clusters by aggregate search volume

'''
for c in clusters[:15]: md += f"- {c['cluster']}: {int(c['total_search_volume'])} monthly volume across {c['keyword_count']} tracked terms. Top term: {c['top_keyword']} ({c['top_keyword_volume']}).\n"
md+='''
## First 10 build priorities

'''
for r in road[:10]: md += f"- {r['recommended_url']} — {r['primary_keyword']} — {r['gap_status']} — {r['search_volume']}/mo.\n"
md+='''
## Operating rule

Every page must earn its place: search intent match, real product proof, useful examples/templates, internal links, FAQ/schema, and a clear conversion path. Thin programmatic pages will lose; systematic, useful pages will win.
'''
(DEL/'SEO_Strategy_Brief.md').write_text(md)
# Create Google Sheet via API
sheet_title='Oviond USA SEO Keyword Clustering + Competitor Audit — 2026-05-12'
tabs=[p for p in sorted(DEL.glob('*.csv')) if re.match(r'\d\d_',p.name)]
tab_titles=[p.stem[:90] for p in tabs]
# token
token=subprocess.check_output(['node','/data/.openclaw/secrets/gws-token.js','spreadsheets,drive'], text=True).strip()
def api(method,url,body=None):
    data=json.dumps(body).encode() if body is not None else None
    req=urllib.request.Request(url,data=data,method=method,headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
    
    try:
        with urllib.request.urlopen(req,timeout=120) as r: return json.loads(r.read().decode() or '{}')
    except urllib.error.HTTPError as e:
        body=e.read().decode('utf-8','replace')
        print('API_ERROR', method, url, e.code, body[:1200])
        raise

def rows_from_csv(p):
    with p.open(newline='',encoding='utf-8') as f:
        return list(csv.reader(f))

# Pre-compute sheet sizes so large tabs do not exceed default 1000-row grid.
sheet_specs=[]
for p,t in zip(tabs,tab_titles):
    rows_preview=rows_from_csv(p)
    max_cols=max((len(r) for r in rows_preview), default=10)
    sheet_specs.append({'title':t,'rowCount':max(1000,len(rows_preview)+50),'columnCount':max(26,max_cols+3)})
create_body={'properties':{'title':sheet_title},'sheets':[{'properties':{'title':spec['title'],'gridProperties':{'rowCount':spec['rowCount'],'columnCount':spec['columnCount']}}} for spec in sheet_specs]}
ss=api('POST','https://sheets.googleapis.com/v4/spreadsheets',create_body)
sid=ss['spreadsheetId']
# helper values update in chunks
for p,title in zip(tabs,tab_titles):
    rows=rows_from_csv(p)
    # truncate massive cells and sheet-safe dimensions
    safe=[]
    for row in rows:
        safe.append([str(c)[:45000] for c in row])
    chunk=800
    for start in range(0,len(safe),chunk):
        vals=safe[start:start+chunk]
        rng=f"'{title}'!A{start+1}"
        url='https://sheets.googleapis.com/v4/spreadsheets/%s/values/%s?valueInputOption=USER_ENTERED' % (sid, urllib.parse.quote(rng,safe="'!:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"))
        api('PUT',url,{'majorDimension':'ROWS','values':vals})
# format freeze/filter widths
requests=[]
meta=api('GET',f'https://sheets.googleapis.com/v4/spreadsheets/{sid}?fields=sheets.properties')
for sh in meta['sheets']:
    props=sh['properties']; gid=props['sheetId']; title=props['title']
    requests.append({'updateSheetProperties':{'properties':{'sheetId':gid,'gridProperties':{'frozenRowCount':1}},'fields':'gridProperties.frozenRowCount'}})
    requests.append({'setBasicFilter':{'filter':{'range':{'sheetId':gid}}}})
    requests.append({'autoResizeDimensions':{'dimensions':{'sheetId':gid,'dimension':'COLUMNS','startIndex':0,'endIndex':12}}})
api('POST',f'https://sheets.googleapis.com/v4/spreadsheets/{sid}:batchUpdate',{'requests':requests})
# Share with Chris
try:
    api('POST',f'https://www.googleapis.com/drive/v3/files/{sid}/permissions?sendNotificationEmail=false',{'type':'user','role':'writer','emailAddress':'chris@oviond.com'})
except Exception as e:
    (DEL/'share-warning.txt').write_text(str(e))
url=f'https://docs.google.com/spreadsheets/d/{sid}/edit'
(DEL/'google-sheet-url.txt').write_text(url+'\n')
print(json.dumps({'spreadsheetId':sid,'url':url,'tabs':tab_titles,'rows':{p.stem:sum(1 for _ in open(p,encoding='utf-8')) for p in tabs}},indent=2))
