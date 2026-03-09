# HEARTBEAT.md — Nicole's Periodic Checks

## Rotation (pick 1-2 per heartbeat, track in memory/heartbeat-state.json)

### 1. Trial Health Check
- Check MailerLite group "1.1 Trial Users" for current count
- Compare to last check — trending up or down?
- If a trial is about to expire (day 13-15), flag it

### 2. Revenue Pulse
- Pull last 7 days of Stripe paid invoices
- Compare to prior 7 days — any drops?
- Check past_due count — if >20, alert Chris

### 3. SEO Movement
- Pull GSC top 10 non-brand queries
- Compare positions to last check (stored in memory/seo-weekly/)
- Flag any position drops >3

### 4. Email Health
- Check MailerLite automation delivery rates
- Flag any automation with >5% bounce rate or <15% open rate

### 5. Ad Spend Check
- Pull Meta ads spend for current week
- If CPA is >R200 per landing page view, flag it

## Rules
- Only check items not checked in last 4 hours
- Late night (21:00-07:00 SAST) — skip unless urgent
- If nothing notable, reply HEARTBEAT_OK
- If something needs attention, message Chris with the finding
