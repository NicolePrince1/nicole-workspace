#!/usr/bin/env python3
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE = os.environ.get('POSTIZ_API_URL', 'https://api.postiz.com').rstrip('/')
KEY = os.environ.get('POSTIZ_API_KEY', '')
HEADERS = {
    'Authorization': KEY,
    'User-Agent': 'OpenClaw-Nicole/1.0',
    'Accept': 'application/json',
}
RESULTS_PATH = Path('/data/.openclaw/workspace/projects/postiz-dummy-week-2026-04-27/results.json')
MARKER = 'DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH'


def request(method, url):
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8', 'replace'))


def list_remaining():
    params = urllib.parse.urlencode({
        'startDate': '2026-04-27T00:00:00.000Z',
        'endDate': '2026-05-02T23:59:59.000Z',
    })
    status, body = request('GET', f'{BASE}/public/v1/posts?{params}')
    remaining = []
    for post in body.get('posts', []):
        content = (post.get('content') or '')
        if MARKER in content:
            remaining.append({
                'id': post.get('id'),
                'state': post.get('state'),
                'publishDate': post.get('publishDate'),
                'provider': (post.get('integration') or {}).get('providerIdentifier'),
                'content': content[:160],
            })
    return status, remaining


def main():
    if not KEY:
        print(json.dumps({'ok': False, 'error': 'Missing POSTIZ_API_KEY'}, indent=2))
        return 1

    status, remaining = list_remaining()
    deleted = []
    for item in remaining:
        d_status, d_body = request('DELETE', f"{BASE}/public/v1/posts/{item['id']}")
        deleted.append({'requestedId': item['id'], 'provider': item['provider'], 'status': d_status, 'response': d_body})

    verify_status, verify_remaining = list_remaining()

    data = json.loads(RESULTS_PATH.read_text(encoding='utf-8'))
    data.setdefault('cleanup', {})['secondPass'] = {
        'deletedPosts': deleted,
        'verificationStatus': verify_status,
        'remainingDummyPosts': verify_remaining,
    }
    RESULTS_PATH.write_text(json.dumps(data, indent=2), encoding='utf-8')

    print(json.dumps({
        'ok': len(verify_remaining) == 0,
        'initialRemainingCount': len(remaining),
        'deletedPosts': deleted,
        'verificationStatus': verify_status,
        'remainingDummyPosts': verify_remaining,
    }, indent=2))
    return 0 if len(verify_remaining) == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
