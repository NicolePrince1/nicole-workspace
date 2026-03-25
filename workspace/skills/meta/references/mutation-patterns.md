# Meta mutation patterns for Oviond

Default stance: **preview first, validate second, apply last**.

## Spec format

All writes use a JSON spec file with this shape:

```json
{
  "op": "create_campaign",
  "account_id": "286631686227626",
  "params": {
    "name": "US remarketing - LPV - Mar 2026",
    "objective": "OUTCOME_TRAFFIC",
    "status": "PAUSED",
    "special_ad_categories": []
  }
}
```

Top-level keys:
- `op` — operation name
- `account_id` / `page_id` / `instagram_account_id` / `object_id` — target object when needed
- `params` — exact Meta API payload

## Supported operations

Ads:
- `create_campaign`
- `update_campaign`
- `create_adset`
- `update_adset`
- `create_adcreative`
- `create_ad`
- `update_ad`

Social:
- `create_page_post`
- `create_page_photo` (URL-based)
- `create_instagram_media` (container step)
- `publish_instagram_media`

## Safe workflow

### Preview only

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_mutate.py preview ./spec.json
```

### Server-side validation when supported

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_mutate.py validate ./spec.json
```

### Apply for real

```bash
python3 /data/.openclaw/workspace/skills/meta/scripts/meta_mutate.py apply ./spec.json --yes-apply
```

## Guardrails

- Ads objects requesting `ACTIVE` are automatically forced to `PAUSED` unless `--allow-active` is supplied.
- Do not jump straight to apply mode.
- Keep campaign/ad set/ad launches paused until copy, targeting, creative, budget, and tracking are reviewed.
- For social posts, preview copy and links in natural language before publishing.

## Examples

### Pause a campaign

```json
{
  "op": "update_campaign",
  "object_id": "120234146733660563",
  "params": {
    "status": "PAUSED"
  }
}
```

### Create a campaign shell

```json
{
  "op": "create_campaign",
  "params": {
    "name": "Oviond remarketing - LPV - paused shell",
    "objective": "OUTCOME_TRAFFIC",
    "status": "PAUSED",
    "special_ad_categories": []
  }
}
```

### Create a page post

```json
{
  "op": "create_page_post",
  "params": {
    "message": "Custom Metrics in Oviond just got a major upgrade.",
    "link": "https://v2.oviond.com/"
  }
}
```

### Create an Instagram media container

```json
{
  "op": "create_instagram_media",
  "params": {
    "image_url": "https://example.com/creative.jpg",
    "caption": "Reporting without the mess. #Oviond"
  }
}
```

After creating the container, use the returned `creation_id` in `publish_instagram_media`.
