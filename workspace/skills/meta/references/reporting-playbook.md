# Meta reporting playbook for Oviond

## 1. Fast account audit

Run:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_doctor.py
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py overview --days 7
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py insights campaign --days 30 --sort spend
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py breakdown campaign publisher_platform --days 30
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py action-types campaign --days 30
```

Use this sequence to answer:
- is access healthy?
- what changed vs the prior period?
- which campaigns are consuming budget?
- is Facebook or Instagram carrying results?
- which action types are actually available?

## 2. LPV-focused performance read

When traffic quality matters more than vanity metrics:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py overview --days 7 --primary-action-type landing_page_view
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py insights adset --days 14 --sort cost_per_primary_action --primary-action-type landing_page_view
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py breakdown ad publisher_platform --days 14 --primary-action-type landing_page_view
```

## 3. Custom-conversion audit

First discover the conversion key:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py action-types campaign --days 30
```

Then rerun reporting with the exact custom action type, for example:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py overview --days 14 --primary-action-type offsite_conversion.custom.936973485167575
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py insights ad --days 14 --sort cost_per_primary_action --primary-action-type offsite_conversion.custom.936973485167575
```

## 4. Creative triage

Use ad-level reporting when you need to separate creative winners from audience or budget effects:

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py insights ad --days 14 --sort spend --primary-action-type landing_page_view
```

Look for:
- high spend + weak LPV or weak primary action volume
- low CTR but strong conversion efficiency after click
- strong creative on one platform but not another

## 5. Social presence check

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py page-overview --limit 5
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_report.py instagram-overview --limit 5
```

Use this when you need the latest post history, audience size, or proof that Page/Instagram access is live.
