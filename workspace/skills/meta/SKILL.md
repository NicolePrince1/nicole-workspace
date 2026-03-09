---
name: meta
description: "Manage Oviond's Meta presence — Facebook Page, Instagram, Facebook/Instagram Ads, and Pixel. Post content, read insights, manage ad campaigns, analyze performance."
metadata:
  {
    "openclaw":
      {
        "emoji": "📱",
      },
  }
---

# Meta Skill — Oviond

Manage Oviond's Facebook Page, Instagram, and Ad Account via the Meta Graph API v21.0.

## Account Details

- **Business Manager ID:** 287659180931920
- **System User:** Nicole Prince (ID: 61584969418636)
- **Facebook Page:** OVIOND (ID: 1700329636926546) — 798 followers, Software category
- **Instagram:** @ovionddigital (ID: 17841415739993320) — 85 followers, 3 posts
- **Ad Account:** act_286631686227626 (Oviond, currency: ZAR)
- **Pixel:** Oviond 2024
- **Dataset:** Oviond 2024
- **Domain:** oviond.com

## Authentication

```bash
TOKEN=$(cat /data/.openclaw/secrets/meta-token.txt)
# System user token — does not expire
```

All API calls use: `https://graph.facebook.com/v21.0/`

## Facebook Page Operations

### Post to Page
```bash
curl -X POST "https://graph.facebook.com/v21.0/1700329636926546/feed" \
  -d "message=Your post text here" \
  -d "access_token=$TOKEN"
```

### Post with Link
```bash
curl -X POST "https://graph.facebook.com/v21.0/1700329636926546/feed" \
  -d "message=Check this out" \
  -d "link=https://oviond.com/blog/article" \
  -d "access_token=$TOKEN"
```

### Post with Image
```bash
curl -X POST "https://graph.facebook.com/v21.0/1700329636926546/photos" \
  -F "message=Caption here" \
  -F "source=@/path/to/image.jpg" \
  -F "access_token=$TOKEN"
```

### Get Recent Posts
```bash
curl -s "https://graph.facebook.com/v21.0/1700329636926546/posts?fields=message,created_time,shares,likes.summary(true),comments.summary(true)&limit=10&access_token=$TOKEN"
```

### Page Insights
```bash
# Page-level metrics (last 28 days)
curl -s "https://graph.facebook.com/v21.0/1700329636926546/insights?metric=page_impressions,page_engaged_users,page_fan_adds,page_views_total&period=day&since=$(date -d '28 days ago' +%Y-%m-%d)&until=$(date +%Y-%m-%d)&access_token=$TOKEN"
```

## Instagram Operations

### Post to Instagram (Image)
```bash
# Step 1: Create media container
curl -X POST "https://graph.facebook.com/v21.0/17841415739993320/media" \
  -d "image_url=https://example.com/image.jpg" \
  -d "caption=Your caption #hashtag" \
  -d "access_token=$TOKEN"

# Step 2: Publish (use creation_id from step 1)
curl -X POST "https://graph.facebook.com/v21.0/17841415739993320/media_publish" \
  -d "creation_id={CREATION_ID}" \
  -d "access_token=$TOKEN"
```

### Post to Instagram (Carousel)
```bash
# Step 1: Create each media item
curl -X POST "https://graph.facebook.com/v21.0/17841415739993320/media" \
  -d "image_url=https://example.com/image1.jpg" \
  -d "is_carousel_item=true" \
  -d "access_token=$TOKEN"
# Repeat for each image...

# Step 2: Create carousel container
curl -X POST "https://graph.facebook.com/v21.0/17841415739993320/media" \
  -d "media_type=CAROUSEL" \
  -d "children={ID1},{ID2},{ID3}" \
  -d "caption=Carousel caption" \
  -d "access_token=$TOKEN"

# Step 3: Publish
curl -X POST "https://graph.facebook.com/v21.0/17841415739993320/media_publish" \
  -d "creation_id={CAROUSEL_CONTAINER_ID}" \
  -d "access_token=$TOKEN"
```

### Instagram Insights
```bash
# Account insights
curl -s "https://graph.facebook.com/v21.0/17841415739993320/insights?metric=impressions,reach,profile_views,follower_count&period=day&since=$(date -d '28 days ago' +%Y-%m-%d)&until=$(date +%Y-%m-%d)&access_token=$TOKEN"

# Media insights (per post)
curl -s "https://graph.facebook.com/v21.0/{MEDIA_ID}/insights?metric=impressions,reach,engagement,saved&access_token=$TOKEN"
```

### Get Recent Instagram Posts
```bash
curl -s "https://graph.facebook.com/v21.0/17841415739993320/media?fields=id,caption,timestamp,like_count,comments_count,media_type,permalink&limit=10&access_token=$TOKEN"
```

## Facebook/Instagram Ads

### List Campaigns
```bash
curl -s "https://graph.facebook.com/v21.0/act_286631686227626/campaigns?fields=name,status,objective,daily_budget,lifetime_budget,start_time,stop_time&limit=25&access_token=$TOKEN"
```

### Campaign Performance (Last 30 Days)
```bash
curl -s "https://graph.facebook.com/v21.0/act_286631686227626/insights?fields=campaign_name,impressions,clicks,spend,cpc,cpm,ctr,actions,cost_per_action_type&time_range={\"since\":\"$(date -d '30 days ago' +%Y-%m-%d)\",\"until\":\"$(date +%Y-%m-%d)\"}&level=campaign&access_token=$TOKEN"
```

### Ad Set Performance
```bash
curl -s "https://graph.facebook.com/v21.0/act_286631686227626/insights?fields=adset_name,campaign_name,impressions,clicks,spend,cpc,actions,cost_per_action_type&time_range={\"since\":\"$(date -d '30 days ago' +%Y-%m-%d)\",\"until\":\"$(date +%Y-%m-%d)\"}&level=adset&access_token=$TOKEN"
```

### Ad Performance
```bash
curl -s "https://graph.facebook.com/v21.0/act_286631686227626/insights?fields=ad_name,adset_name,campaign_name,impressions,clicks,spend,cpc,actions&time_range={\"since\":\"$(date -d '30 days ago' +%Y-%m-%d)\",\"until\":\"$(date +%Y-%m-%d)\"}&level=ad&access_token=$TOKEN"
```

### Pause/Enable a Campaign
```bash
# Pause
curl -X POST "https://graph.facebook.com/v21.0/{CAMPAIGN_ID}" \
  -d "status=PAUSED" \
  -d "access_token=$TOKEN"

# Enable
curl -X POST "https://graph.facebook.com/v21.0/{CAMPAIGN_ID}" \
  -d "status=ACTIVE" \
  -d "access_token=$TOKEN"
```

### Audience Breakdown
```bash
curl -s "https://graph.facebook.com/v21.0/act_286631686227626/insights?fields=impressions,clicks,spend,actions&breakdowns=age,gender&time_range={\"since\":\"$(date -d '30 days ago' +%Y-%m-%d)\",\"until\":\"$(date +%Y-%m-%d)\"}&access_token=$TOKEN"
```

### Platform Breakdown (Facebook vs Instagram)
```bash
curl -s "https://graph.facebook.com/v21.0/act_286631686227626/insights?fields=impressions,clicks,spend,actions&breakdowns=publisher_platform&time_range={\"since\":\"$(date -d '30 days ago' +%Y-%m-%d)\",\"until\":\"$(date +%Y-%m-%d)\"}&access_token=$TOKEN"
```

## Current Campaigns

| Campaign | Status | Objective | Budget |
|----------|--------|-----------|--------|
| Remarketing USA | ACTIVE | Traffic | R350/day |
| Remarketing Top Countries | PAUSED | Sales | — |
| United States - Free Trial Remarketing | PAUSED | Leads | R300/day |

Note: Currency is ZAR (South African Rand). daily_budget is in cents (35000 = R350).

## Output Formatting (Slack)

```
*Facebook Ads Performance (Last 30 Days)*

• *Remarketing USA* — R2,450 spend, 12,300 impressions, 450 clicks, 3.6% CTR
• *Free Trial Remarketing* — PAUSED

*Page Stats:*
• *Followers:* 798
• *Recent reach:* X impressions
• *Engagement:* X interactions
```

## Safety Rules

- **Always confirm before posting** to Facebook or Instagram
- **Always confirm before changing** ad campaign status or budgets
- **Draft posts first** — show the user what will be posted before publishing
- Page token is embedded in the API response — use it for page-level operations
- System user token does not expire — no refresh needed
