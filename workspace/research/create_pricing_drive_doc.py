#!/usr/bin/env python3
import html
import json
import re
import subprocess
import urllib.request
from pathlib import Path

md_path = Path('/data/.openclaw/workspace/research/oviond-pricing-slider-agent-instructions-2026-05-26.md')
text = md_path.read_text()

def md_to_html(md):
    out = ['<!doctype html><html><head><meta charset="utf-8"><title>Oviond Pricing Slider Agent Instructions</title>',
           '<style>body{font-family:Arial,sans-serif;line-height:1.45;max-width:860px;margin:40px auto;color:#111}h1{font-size:30px}h2{font-size:22px;margin-top:30px;border-top:1px solid #ddd;padding-top:18px}h3{font-size:17px;margin-top:20px}blockquote{border-left:4px solid #1a73e8;padding:8px 16px;background:#f6f9ff;margin:12px 0}code{background:#f3f4f6;padding:2px 4px;border-radius:3px}ul{margin-top:6px}strong{font-weight:700}</style></head><body>']
    in_ul = False
    in_quote = False
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith('> '):
            if in_ul:
                out.append('</ul>'); in_ul=False
            if not in_quote:
                out.append('<blockquote>'); in_quote=True
            content = html.escape(line[2:])
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            out.append(f'<p>{content}</p>')
            continue
        else:
            if in_quote:
                out.append('</blockquote>'); in_quote=False
        if not line:
            if in_ul:
                out.append('</ul>'); in_ul=False
            continue
        if line.startswith('# '):
            if in_ul: out.append('</ul>'); in_ul=False
            out.append(f'<h1>{html.escape(line[2:])}</h1>')
        elif line.startswith('## '):
            if in_ul: out.append('</ul>'); in_ul=False
            out.append(f'<h2>{html.escape(line[3:])}</h2>')
        elif line.startswith('### '):
            if in_ul: out.append('</ul>'); in_ul=False
            out.append(f'<h3>{html.escape(line[4:])}</h3>')
        elif line.startswith('- '):
            if not in_ul:
                out.append('<ul>'); in_ul=True
            content = html.escape(line[2:])
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            out.append(f'<li>{content}</li>')
        elif re.match(r'^\d+\. ', line):
            if in_ul: out.append('</ul>'); in_ul=False
            content = html.escape(re.sub(r'^\d+\. ', '', line))
            out.append(f'<p>{content}</p>')
        else:
            if in_ul: out.append('</ul>'); in_ul=False
            content = html.escape(line)
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
            out.append(f'<p>{content}</p>')
    if in_ul: out.append('</ul>')
    if in_quote: out.append('</blockquote>')
    out.append('</body></html>')
    return '\n'.join(out)

token = subprocess.check_output(['node','/data/.openclaw/secrets/gws-token.js','drive,documents'], text=True).strip()
metadata = {
    'name': 'Oviond Pricing Slider Agent Instructions — 2026-05-26',
    'mimeType': 'application/vnd.google-apps.document'
}
html_body = md_to_html(text).encode('utf-8')
boundary = '----openclawpricingdocboundary'
body = (
    f'--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n' + json.dumps(metadata) +
    f'\r\n--{boundary}\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
).encode('utf-8') + html_body + f'\r\n--{boundary}--\r\n'.encode('utf-8')
req = urllib.request.Request('https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name,webViewLink', data=body, method='POST', headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': f'multipart/related; boundary={boundary}',
})
with urllib.request.urlopen(req) as resp:
    created = json.loads(resp.read())
file_id = created['id']
# Share with Chris directly, no notification email.
perm = {'type':'user','role':'writer','emailAddress':'chris@oviond.com'}
req = urllib.request.Request(f'https://www.googleapis.com/drive/v3/files/{file_id}/permissions?sendNotificationEmail=false', data=json.dumps(perm).encode(), method='POST', headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
})
try:
    with urllib.request.urlopen(req) as resp:
        permission = json.loads(resp.read())
except urllib.error.HTTPError as e:
    print(e.read().decode(), flush=True)
    raise
# Fetch link after permission.
req = urllib.request.Request(f'https://www.googleapis.com/drive/v3/files/{file_id}?fields=id,name,webViewLink', headers={'Authorization': f'Bearer {token}'})
with urllib.request.urlopen(req) as resp:
    info = json.loads(resp.read())
print(json.dumps(info, indent=2))
