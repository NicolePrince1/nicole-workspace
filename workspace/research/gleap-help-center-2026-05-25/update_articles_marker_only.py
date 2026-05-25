#!/usr/bin/env python3
import copy, json, os, sys
from pathlib import Path
sys.path.insert(0, '/data/.openclaw/workspace/skills/use-gleap/scripts')
from gleap_api import gleap_request

API_KEY=os.environ['GLEAP_API_KEY']
PROJECT_ID=os.environ['GLEAP_PROJECT_ID']
BASE=os.getenv('GLEAP_BASE_URL','https://api.gleap.io/v3')
OUT=Path('/data/.openclaw/workspace/research/gleap-help-center-2026-05-25')
COMMIT='3ad202b'
RAW_BASE=f'https://raw.githubusercontent.com/NicolePrince1/nicole-workspace/{COMMIT}/workspace/tools/oviond-screenshot-studio/outputs/help-center-rollout'
IMG_CLIENTS=f'{RAW_BASE}/clients-home-markers-safe.png'
IMG_ADD_CLIENT=f'{RAW_BASE}/add-client-drawer-markers-safe.png'
SOURCE='nicole-marker-only-screenshot-pass'
OLD_SOURCE='nicole-real-screenshot-pass'

TARGETS=[
  {
    'collection':'Getting Started',
    'article':'Quick start checklist',
    'blocks':[
      {'type':'heading','text':'Screenshot guide'},
      {'type':'paragraph','text':'Use the screenshot below as a quick map for the first setup step.'},
      {'type':'image','src':IMG_CLIENTS,'alt':'Real Oviond Clients screen with numbered markers'},
      {'type':'heading','text':'What the numbers show'},
      {'type':'bullet','items':[
        '1. Use the left sidebar to open Clients, Templates, Automations, or Settings.',
        '2. Click Add Client to start creating a new client workspace.',
        '3. Use the client card to open an existing client and check its website and data-source count.'
      ]}
    ]
  },
  {
    'collection':'Getting Started',
    'article':'Create your first client report',
    'blocks':[
      {'type':'heading','text':'Start from the Clients screen'},
      {'type':'paragraph','text':'Your first report starts by adding or opening the client you want to report on.'},
      {'type':'image','src':IMG_CLIENTS,'alt':'Real Oviond Clients screen showing where to add or open a client'},
      {'type':'heading','text':'What the numbers show'},
      {'type':'bullet','items':[
        '1. Use the sidebar to stay in the main Clients area.',
        '2. Click Add Client if the client does not exist yet.',
        '3. Open the client card once you are ready to connect data sources and create a report.'
      ]}
    ]
  },
  {
    'collection':'Clients',
    'article':'Add a client',
    'blocks':[
      {'type':'heading','text':'From Clients to Add Client'},
      {'type':'paragraph','text':'Start on the Clients screen, then open the Add Client drawer.'},
      {'type':'image','src':IMG_CLIENTS,'alt':'Real Oviond Clients screen showing the Add Client action'},
      {'type':'heading','text':'What the numbers show'},
      {'type':'bullet','items':[
        '1. Use the sidebar to confirm you are in the main Clients area.',
        '2. Click Add Client in the top-right corner.',
        '3. Existing client cards show the client name, website, data-source count, and creation date.'
      ]},
      {'type':'heading','text':'Complete the Add Client drawer'},
      {'type':'image','src':IMG_ADD_CLIENT,'alt':'Real Oviond Add Client drawer with numbered fields'},
      {'type':'heading','text':'What the numbers show'},
      {'type':'bullet','items':[
        '1. Enter the client name as it should appear inside Oviond.',
        '2. Add the client website. The https prefix is already handled by the field.',
        '3. Review optional setup details such as currency, timezone, and manager.',
        '4. Click Create Client when the required details are correct.'
      ]}
    ]
  }
]

def arr(payload):
    if isinstance(payload,list): return payload
    if isinstance(payload,dict):
        for k in ('collections','articles','items','data','results'):
            if isinstance(payload.get(k),list): return payload[k]
    return []

def title_en(obj):
    t=obj.get('title') or {}
    return t.get('en') if isinstance(t,dict) else str(t)

def text_node(text, marks=None):
    node={'type':'text','text':text}
    if marks: node['marks']=marks
    return node

def paragraph(text):
    return {'type':'paragraph','attrs':{'dataSource':SOURCE},'content':[text_node(text)]}

def heading(text, level=2):
    return {'type':'heading','attrs':{'level':level,'dataSource':SOURCE},'content':[text_node(text)]}

def bullet(items):
    return {'type':'orderedList','attrs':{'start':1,'dataSource':SOURCE},'content':[{'type':'listItem','content':[{'type':'paragraph','content':[text_node(__import__('re').sub(r'^\s*\d+\.\s*','',x).strip())]}]} for x in items]}

def image(src, alt):
    return {'type':'image','attrs':{'src':src,'alt':alt,'title':alt,'dataSource':SOURCE}}

def render(block):
    if block['type']=='heading': return heading(block['text'])
    if block['type']=='paragraph': return paragraph(block['text'])
    if block['type']=='bullet': return bullet(block['items'])
    if block['type']=='image': return image(block['src'], block['alt'])
    raise ValueError(block)

def node_text(n):
    if not isinstance(n, dict): return ''
    return ''.join(c.get('text','') for c in n.get('content') or [] if isinstance(c,dict))

def remove_old(nodes):
    clean=[]
    screenshot_section_heads={
      'Screenshot guide', 'What the numbers show', 'Start from the Clients screen',
      'From Clients to Add Client', 'Complete the Add Client drawer'
    }
    skip_rest=False
    for n in nodes:
        if not isinstance(n, dict):
            if not skip_rest: clean.append(n)
            continue
        attrs=n.get('attrs') or {}
        txt=node_text(n).strip()
        if n.get('type')=='heading' and txt in screenshot_section_heads:
            skip_rest=True
            continue
        if skip_rest:
            continue
        if attrs.get('dataSource') in (SOURCE, OLD_SOURCE):
            continue
        # remove old image/link insertions by URL even if attrs were dropped by Gleap
        if n.get('type')=='image':
            src=(attrs.get('src') or '')
            if 'real-clients-home-panel' in src or 'real-add-client-panel' in src or 'real-clients-home-markers' in src or 'real-add-client-drawer-crop-markers' in src or 'help-center-rollout' in src:
                continue
        if n.get('type')=='paragraph' and txt.lower()=='open screenshot':
            continue
        clean.append(n)
    return clean

def plain_from_doc(doc):
    out=[]
    def walk(n):
        if isinstance(n,dict):
            if n.get('type')=='text' and n.get('text'):
                out.append(n['text'])
            elif n.get('type')=='image':
                out.append('\n[Screenshot: '+(n.get('attrs',{}).get('alt') or '')+']\n')
            for c in n.get('content') or []: walk(c)
            if n.get('type') in ('paragraph','heading','listItem'):
                out.append('\n')
        elif isinstance(n,list):
            for x in n: walk(x)
    walk(doc)
    return '\n'.join([x.strip() for x in ''.join(out).split('\n') if x.strip()])

collections=arr(gleap_request('GET','/helpcenter/collections/all',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
updated=[]
for target in TARGETS:
    col=next(c for c in collections if title_en(c)==target['collection'])
    cid=col.get('id') or col.get('_id')
    arts=arr(gleap_request('GET',f'/helpcenter/collections/{cid}/articles',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
    art=next(a for a in arts if title_en(a)==target['article'])
    aid=art.get('id') or art.get('_id')
    doc=copy.deepcopy((art.get('content') or {}).get('en') or {'type':'doc','content':[]})
    doc['content']=remove_old(doc.get('content') or []) + [render(b) for b in target['blocks']]
    payload={
        'title':art['title'],
        'description':art['description'],
        'content':{'en':doc},
        'plainContent':{'en':plain_from_doc(doc)},
        'isDraft':False,
        'targetAudience':art.get('targetAudience','all'),
        'tags':sorted(set((art.get('tags') or [])+['real-product-screenshots','marker-only-screenshots']))
    }
    (OUT/f'article-before-marker-only-{aid}.json').write_text(json.dumps(art,indent=2,ensure_ascii=False),encoding='utf-8')
    res=gleap_request('PUT',f'/helpcenter/collections/{cid}/articles/{aid}',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE,data=payload)
    updated.append({'collection':target['collection'],'article':target['article'],'collectionId':cid,'articleId':aid,'images':sum(1 for b in target['blocks'] if b['type']=='image')})

(OUT/'gleap-marker-only-article-updates.json').write_text(json.dumps(updated,indent=2),encoding='utf-8')
print(json.dumps({'updated':updated},indent=2))
