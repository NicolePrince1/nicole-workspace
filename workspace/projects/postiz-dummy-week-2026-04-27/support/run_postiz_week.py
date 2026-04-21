#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

week_dir = Path('/data/.openclaw/workspace/tmp/postiz-week-2026-04-27')
script = '/data/.openclaw/workspace/skills/oviond-content-engine/scripts/postiz_create_post.py'
mode = sys.argv[1] if len(sys.argv) > 1 else 'validate'
if mode not in {'validate', 'apply'}:
    raise SystemExit('usage: run_postiz_week.py [validate|apply]')

results = []
for path in sorted(week_dir.glob('*.json')):
    cmd = ['python3', script, str(path)]
    if mode == 'apply':
        cmd.append('--apply')
    proc = subprocess.run(cmd, capture_output=True, text=True)
    payload = None
    if proc.stdout.strip():
        try:
            payload = json.loads(proc.stdout)
        except Exception:
            payload = {'raw': proc.stdout}
    results.append({'file': path.name, 'returncode': proc.returncode, 'result': payload, 'stderr': proc.stderr})
    if proc.returncode != 0:
        print(json.dumps({'ok': False, 'mode': mode, 'results': results}, indent=2))
        raise SystemExit(proc.returncode)

print(json.dumps({'ok': True, 'mode': mode, 'results': results}, indent=2))
