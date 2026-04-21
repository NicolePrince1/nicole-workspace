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


def request(method, url):
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8', 'replace'))


def main():
    if not KEY:
        print(json.dumps({'ok': False, 'error': 'Missing POSTIZ_API_KEY'}, indent=2))
        return 1

    data = json.loads(RESULTS_PATH.read_text(encoding='utf-8'))
    scheduled = data['scheduledPosts']
    delete_ids = [days[next(iter(days))] for days in scheduled.values()]

    deleted = []
    for post_id in delete_ids:
        status, body = request('DELETE', f'{BASE}/public/v1/posts/{post_id}')
        deleted.append({'requestedId': post_id, 'status': status, 'response': body})

    params = urllib.parse.urlencode({
        'startDate': '2026-04-27T00:00:00.000Z',
        'endDate': '2026-05-02T23:59:59.000Z',
    })
    status, body = request('GET', f'{BASE}/public/v1/posts?{params}')

    remaining = []
    for post in body.get('posts', []):
        content = (post.get('content') or '')
        if 'DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH' in content:
            remaining.append({
                'id': post.get('id'),
                'state': post.get('state'),
                'publishDate': post.get('publishDate'),
                'provider': (post.get('integration') or {}).get('providerIdentifier'),
                'content': content[:160],
            })

    data['cleanup'] = {
        'deletedGroups': deleted,
        'verificationStatus': status,
        'remainingDummyPosts': remaining,
    }
    RESULTS_PATH.write_text(json.dumps(data, indent=2), encoding='utf-8')

    print(json.dumps({
        'ok': len(remaining) == 0,
        'deletedGroups': deleted,
        'verificationStatus': status,
        'remainingDummyPosts': remaining,
    }, indent=2))
    return 0 if len(remaining) == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
