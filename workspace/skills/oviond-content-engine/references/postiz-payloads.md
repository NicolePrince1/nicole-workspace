# Postiz Payloads

## Purpose

Use this file when preparing JSON payloads for the Postiz Public API or for the local helper script.

## Safe default

Default to `draft`.

Only use:
- `schedule` when timing is approved
- `now` when Chris explicitly wants immediate posting or has clearly delegated live autonomy

## Core payload shape

```json
{
  "type": "draft",
  "date": "2026-04-22T08:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-integration-id"
      },
      "value": [
        {
          "content": "Your post content here",
          "image": []
        }
      ],
      "settings": {
        "__type": "linkedin-page"
      }
    }
  ]
}
```

## Oviond channel templates

### LinkedIn Page text post

```json
{
  "type": "draft",
  "date": "2026-04-22T08:00:00.000Z",
  "shortLink": false,
  "tags": ["oviond", "linkedin"],
  "posts": [
    {
      "integration": {
        "id": "cmo8gmcii05bin50ytakd9ehj"
      },
      "value": [
        {
          "content": "Most agency reporting pain is not caused by a lack of dashboards. It's caused by messy setup, weak trust, and too much manual work.",
          "image": []
        }
      ],
      "settings": {
        "__type": "linkedin-page",
        "post_as_images_carousel": false
      }
    }
  ]
}
```

### Facebook Page post with optional link

```json
{
  "type": "draft",
  "date": "2026-04-22T08:15:00.000Z",
  "shortLink": false,
  "tags": ["oviond", "facebook"],
  "posts": [
    {
      "integration": {
        "id": "cmo8gnucn05r3ld0yciyxbdpw"
      },
      "value": [
        {
          "content": "New on the Oviond blog: why reporting complexity kills trust faster than most agencies realise.",
          "image": []
        }
      ],
      "settings": {
        "__type": "facebook",
        "url": "https://www.oviond.com/"
      }
    }
  ]
}
```

### X post

```json
{
  "type": "draft",
  "date": "2026-04-22T08:30:00.000Z",
  "shortLink": false,
  "tags": ["oviond", "x"],
  "posts": [
    {
      "integration": {
        "id": "cmo8gp7wo05rald0y4xqwghcq"
      },
      "value": [
        {
          "content": "A lot of agency reporting pain isn't a reporting problem. It's a trust problem dressed up as a dashboard problem.",
          "image": []
        }
      ],
      "settings": {
        "__type": "x",
        "who_can_reply_post": "everyone",
        "made_with_ai": false,
        "paid_partnership": false
      }
    }
  ]
}
```

## Multi-post thread example for X

Use multiple `value` items under one post object.

```json
{
  "type": "draft",
  "date": "2026-04-22T09:00:00.000Z",
  "shortLink": false,
  "tags": ["oviond", "x-thread"],
  "posts": [
    {
      "integration": {
        "id": "cmo8gp7wo05rald0y4xqwghcq"
      },
      "value": [
        {
          "content": "1/ Agencies do not need more reporting clutter.",
          "image": []
        },
        {
          "content": "2/ They need reporting that feels invisible, dependable, and done.",
          "image": []
        }
      ],
      "settings": {
        "__type": "x",
        "who_can_reply_post": "everyone"
      }
    }
  ]
}
```

## Helper script usage

Validate only:

```bash
python3 /data/.openclaw/workspace/skills/oviond-content-engine/scripts/postiz_create_post.py ./payload.json --pretty
```

Force draft during validation:

```bash
python3 /data/.openclaw/workspace/skills/oviond-content-engine/scripts/postiz_create_post.py ./payload.json --force-draft --pretty
```

Actually create the post in Postiz:

```bash
python3 /data/.openclaw/workspace/skills/oviond-content-engine/scripts/postiz_create_post.py ./payload.json --apply
```

## Safety rules

- Validate before apply.
- Prefer exact live integration IDs.
- Keep one primary message per post.
- Do not use `now` casually.
- Do not assume platform settings are interchangeable.
- Do not create live content against the wrong destination just because two channels are both named OVIOND.
