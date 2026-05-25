#!/usr/bin/env python3
import copy, json, os, sys
from pathlib import Path
sys.path.insert(0, '/data/.openclaw/workspace/skills/use-gleap/scripts')
from gleap_api import gleap_request

API_KEY=os.environ['GLEAP_API_KEY']
PROJECT_ID=os.environ['GLEAP_PROJECT_ID']
BASE=os.getenv('GLEAP_BASE_URL','https://api.gleap.io/v3')
OUT=Path('/data/.openclaw/workspace/research/gleap-help-center-2026-05-25')
SOURCE='nicole-marker-only-screenshot-pass'

TARGETS=[
 ('6a141b8ccdbfc01912816cb7','6a141c3a89bb8170ed69610c'),
 ('6a141b8ccdbfc01912816cb7','6a141c3b28329d0818da1000'),
 ('6a141c3c5365e1840c1441f1','6a141c3ca4aae5893cf54de3'),
]

def text_node(text): return {'type':'text','text':text}
def para(text): return {'type':'paragraph','content':[text_node(text)]}
def ordered(items):
    clean=[]
    for x in items:
        # Remove manually typed leading numbers; orderedList renders them.
        clean.append(__import__('re').sub(r'^\s*\d+\.\s*','',x).strip())
    return {'type':'orderedList','attrs':{'start':1,'dataSource':SOURCE},'content':[{'type':'listItem','content':[para(x)]} for x in clean]}

def plain_from_doc(doc):
    out=[]
    def walk(n):
        if isinstance(n,dict):
            if n.get('type')=='text' and n.get('text'): out.append(n['text'])
            elif n.get('type')=='image': out.append('\n[Screenshot: '+(n.get('attrs',{}).get('alt') or '')+']\n')
            for c in n.get('content') or []: walk(c)
            if n.get('type') in ('paragraph','heading','listItem'): out.append('\n')
        elif isinstance(n,list):
            for x in n: walk(x)
    walk(doc)
    return '\n'.join([x.strip() for x in ''.join(out).split('\n') if x.strip()])

updated=[]
for cid,aid in TARGETS:
    arts=gleap_request('GET',f'/helpcenter/collections/{cid}/articles',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE)
    art=next(a for a in arts if (a.get('id') or a.get('_id'))==aid)
    doc=copy.deepcopy((art.get('content') or {}).get('en'))
    changed=False
    new=[]
    for n in doc.get('content') or []:
        if isinstance(n,dict) and n.get('type')=='bulletList':
            attrs=n.get('attrs') or {}
            # Convert screenshot explanation bullet lists only when items begin with manual numbers.
            texts=[]
            for li in n.get('content') or []:
                txt=''.join(t.get('text','') for p in li.get('content') or [] for t in p.get('content') or [] if isinstance(t,dict))
                texts.append(txt)
            if attrs.get('dataSource')==SOURCE or any(__import__('re').match(r'^\s*\d+\.\s+', t) for t in texts):
                new.append(ordered(texts)); changed=True; continue
        new.append(n)
    doc['content']=new
    if changed:
        payload={
          'title':art['title'],
          'description':art['description'],
          'content':{'en':doc},
          'plainContent':{'en':plain_from_doc(doc)},
          'isDraft':False,
          'targetAudience':art.get('targetAudience','all'),
          'tags':art.get('tags') or []
        }
        (OUT/f'article-before-ordered-list-fix-{aid}.json').write_text(json.dumps(art,indent=2,ensure_ascii=False),encoding='utf-8')
        gleap_request('PUT',f'/helpcenter/collections/{cid}/articles/{aid}',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE,data=payload)
        updated.append({'collectionId':cid,'articleId':aid})
print(json.dumps({'updated':updated},indent=2))
