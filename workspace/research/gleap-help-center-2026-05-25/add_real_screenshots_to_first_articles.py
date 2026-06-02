#!/usr/bin/env python3
import json, os, sys, copy
from pathlib import Path
sys.path.insert(0, '/data/.openclaw/workspace/skills/use-gleap/scripts')
from gleap_api import gleap_request

API_KEY=os.environ['GLEAP_API_KEY']
PROJECT_ID=os.environ['GLEAP_PROJECT_ID']
BASE=os.getenv('GLEAP_BASE_URL','https://api.gleap.io/v3')
OUT=Path('/data/.openclaw/workspace/research/gleap-help-center-2026-05-25')

RAW_BASE='https://raw.githubusercontent.com/NicolePrince1/nicole-workspace/df845eb/workspace/tools/oviond-screenshot-studio/outputs/app-real-product-correction/annotated'
IMG_CLIENTS=f'{RAW_BASE}/real-clients-home-panel-v2.png'
IMG_ADD_CLIENT=f'{RAW_BASE}/real-add-client-panel-v2.png'

TARGETS=[
  {
    'collection':'Getting Started',
    'article':'Quick start checklist',
    'intro':'Use this screenshot to find the Clients area and start the setup flow.',
    'images':[(IMG_CLIENTS,'Real Oviond Clients screen showing the Add Client action')],
    'extra_steps':[]
  },
  {
    'collection':'Getting Started',
    'article':'Create your first client report',
    'intro':'Start by adding the client from the Clients screen. After the client exists, connect data and build the report under that client.',
    'images':[(IMG_CLIENTS,'Real Oviond Clients screen used as the first step in report setup')],
    'extra_steps':[]
  },
  {
    'collection':'Clients',
    'article':'Add a client',
    'intro':'The screenshots below show the live Add Client flow inside Oviond.',
    'images':[
      (IMG_CLIENTS,'Real Oviond Clients screen with the Add Client action'),
      (IMG_ADD_CLIENT,'Real Oviond Add Client drawer with required fields')
    ],
    'extra_steps':['From Clients, click Add Client in the top-right corner.','Fill in Client Name and Client Website.','Check currency, timezone, and manager if your account uses those fields.','Click Create Client when the required details are correct.']
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
    return {'type':'paragraph','content':[text_node(text)]}

def heading(text, level=2):
    return {'type':'heading','attrs':{'level':level},'content':[text_node(text)]}

def bullet(items):
    return {'type':'bulletList','content':[{'type':'listItem','content':[paragraph(x)]} for x in items]}

def image_node(src, alt):
    return {'type':'image','attrs':{'src':src,'alt':alt,'title':alt}}

def link_paragraph(src):
    return {'type':'paragraph','content':[text_node('Open screenshot', [{'type':'link','attrs':{'href':src,'target':'_blank','rel':'noopener noreferrer'}}])]}

def plain_from_doc(doc):
    out=[]
    def walk(n):
        if isinstance(n,dict):
            if n.get('type')=='text' and n.get('text'): out.append(n['text'])
            elif n.get('type')=='image': out.append('[Screenshot: '+(n.get('attrs',{}).get('alt') or n.get('attrs',{}).get('src',''))+']')
            for c in n.get('content') or []: walk(c)
            if n.get('type') in ('paragraph','heading','listItem'): out.append('\n')
        elif isinstance(n,list):
            for x in n: walk(x)
    walk(doc)
    return '\n'.join([x.strip() for x in ''.join(out).split('\n') if x.strip()])

collections=arr(gleap_request('GET','/helpcenter/collections/all',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
updated=[]
for target in TARGETS:
    col=next((c for c in collections if title_en(c)==target['collection']), None)
    if not col: raise SystemExit(f"Collection not found: {target['collection']}")
    cid=col.get('id') or col.get('_id')
    articles=arr(gleap_request('GET',f'/helpcenter/collections/{cid}/articles',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
    art=next((a for a in articles if title_en(a)==target['article']), None)
    if not art: raise SystemExit(f"Article not found: {target['collection']} / {target['article']}")
    aid=art.get('id') or art.get('_id')
    doc=copy.deepcopy((art.get('content') or {}).get('en') or {'type':'doc','content':[]})
    original=[n for n in doc.get('content',[]) if not (isinstance(n,dict) and n.get('attrs',{}).get('dataSource')=='nicole-real-screenshot-pass')]
    insert=[
        {'type':'heading','attrs':{'level':2,'dataSource':'nicole-real-screenshot-pass'},'content':[text_node('Screenshots')]},
        {'type':'paragraph','attrs':{'dataSource':'nicole-real-screenshot-pass'},'content':[text_node(target['intro'])]},
    ]
    for src, alt in target['images']:
        n=image_node(src, alt); n['attrs']['dataSource']='nicole-real-screenshot-pass'; insert.append(n)
        lp=link_paragraph(src); lp['attrs']={'dataSource':'nicole-real-screenshot-pass'}; insert.append(lp)
    if target['extra_steps']:
        insert.append({'type':'heading','attrs':{'level':2,'dataSource':'nicole-real-screenshot-pass'},'content':[text_node('Step-by-step')]})
        bl=bullet(target['extra_steps']); bl['attrs']={'dataSource':'nicole-real-screenshot-pass'}; insert.append(bl)
    doc['content']=original+insert
    payload={
      'title':art['title'],
      'description':art['description'],
      'content':{'en':doc},
      'plainContent':{'en':plain_from_doc(doc)},
      'isDraft':False,
      'targetAudience':art.get('targetAudience','all'),
      'tags':sorted(set((art.get('tags') or [])+['real-product-screenshots']))
    }
    before=OUT/f'article-before-{aid}.json'
    before.write_text(json.dumps(art, indent=2, ensure_ascii=False), encoding='utf-8')
    result=gleap_request('PUT',f'/helpcenter/collections/{cid}/articles/{aid}',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE,data=payload)
    updated.append({'collection':target['collection'],'article':target['article'],'collectionId':cid,'articleId':aid,'images':len(target['images']),'resultTitle':title_en(result) if isinstance(result,dict) else None})

(OUT/'gleap-real-screenshot-article-updates.json').write_text(json.dumps(updated, indent=2), encoding='utf-8')
print(json.dumps({'updated':updated}, indent=2))
