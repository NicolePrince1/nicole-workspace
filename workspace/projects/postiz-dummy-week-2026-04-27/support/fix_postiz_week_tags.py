#!/usr/bin/env python3
import json
from pathlib import Path

week_dir = Path('/data/.openclaw/workspace/tmp/postiz-week-2026-04-27')
for path in week_dir.glob('*.json'):
    data = json.loads(path.read_text(encoding='utf-8'))
    data['tags'] = []
    path.write_text(json.dumps(data, indent=2), encoding='utf-8')
print('fixed', len(list(week_dir.glob('*.json'))), 'files')
