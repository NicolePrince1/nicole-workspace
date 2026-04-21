---
name: oviond-content-engine
description: Own Oviond's organic content strategy, editorial planning, blog production, social post creation, channel adaptation, publishing workflow, and performance feedback loop. Use when the work involves deciding what Oviond should say, turning ideas into blogs or social posts, building a content calendar, repurposing long-form content into multi-channel posts, preparing visuals with the design system, or operating Postiz as the publishing rail for LinkedIn, X, Facebook, and adjacent channels.
---

# Oviond Content Engine

Run content like an operating system, not a pile of posts.

You own the thinking, the editorial judgment, the production workflow, and the learning loop. Postiz is the default distribution layer, not the strategy brain.

## Default operating model

Use this division of responsibility:
- **Nicole / current agent:** strategy, topic selection, message hierarchy, editorial judgment, copy direction, calendar decisions, QA, performance interpretation
- **This skill:** reusable workflow, channel rules, content standards, Postiz operating guidance
- **`oviond-design-director` skill:** visual direction, creative briefs, image prompts, asset QA
- **Postiz Cloud:** channel connections, media upload, drafts, scheduling, publishing, analytics collection

## Default stack

Prefer this stack unless Chris explicitly wants another route:
- **Canonical source asset:** Oviond blog or strong LinkedIn-native post
- **Primary social channel:** LinkedIn
- **Secondary social channel:** X
- **Selective support channel:** Facebook Page
- **Optional later channels:** Threads, Instagram, YouTube, Medium
- **Publishing platform:** Postiz Cloud, not self-hosted, unless there is a clear reason to absorb infra overhead

## Core workflow

1. **Classify the content job**
   - strategy / calendar
   - blog article
   - product or feature announcement
   - thought-leadership post
   - repurposing / cross-channel adaptation
   - campaign burst
   - performance review

2. **Load the right references**
   - Read `references/editorial-system.md` for audience, pillars, source-mining, and content priorities.
   - Read `references/channel-playbooks.md` for format and tone by channel.
   - Read `references/production-workflows.md` for end-to-end creation, review, and repurposing flows.
   - Read `references/postiz-cloud.md` when the task touches setup, drafts, scheduling, API use, or analytics pulls in Postiz.
   - Read `references/postiz-production.md` when the task touches live auth, integrations, env setup, MCP, production readiness, or operational debugging.
   - Read `references/measurement-loop.md` when evaluating what worked or deciding what to repeat.

3. **Find the real input**
   Mine from actual business truth first:
   - product changes
   - support friction
   - onboarding failures
   - retention issues
   - search demand
   - ad learnings
   - customer objections
   - integrations and feature gaps
   - category opinions worth saying out loud

4. **Define the content thesis**
   For each asset, lock:
   - audience
   - funnel stage
   - single core point
   - supporting proof
   - intended action
   - best source format

5. **Create the source asset first**
   Build one strong primary asset before multiplying derivatives.
   Default preference:
   1. blog article
   2. LinkedIn post
   3. X thread

6. **Adapt by channel, do not lazily duplicate**
   Each channel gets its own packaging, hook, and CTA. Same idea, different expression.

7. **Request visuals deliberately**
   If the content needs images, carousels, or blog covers, hand the brief to `oviond-design-director`. Do not improvise generic SaaS art.

8. **Verify Postiz health when the work is live**
   Before trusting live Postiz automation, run:

   ```bash
   python3 /data/.openclaw/workspace/skills/oviond-content-engine/scripts/postiz_healthcheck.py
   ```

   Confirm API connectivity, visible integrations, and MCP endpoint reachability.

9. **Publish through Postiz**
   Prefer draft or schedule mode by default. Publish immediately only when Chris explicitly wants live posting in the current task or has clearly delegated that decision.

10. **Measure and feed the loop**
   Track what earned attention, what drove clicks, and what topics should be reused, expanded, or killed.

## Output standards

For any substantial content task, produce these sections in your working output:
- **Content objective**
- **Audience and angle**
- **Core message**
- **Primary asset**
- **Channel adaptations**
- **Visual brief** (if needed)
- **Publishing plan**
- **What to measure**

## Rules that matter

- Start from business truth, not generic social filler.
- Prefer strong opinions and useful specifics over soft motivational sludge.
- Keep Oviond positioned around simple, credible, agency-focused reporting.
- Default to the positioning lens: **invisible, dependable, and done**.
- Blog is the depth engine. Social is distribution and demand capture.
- LinkedIn is the main organic B2B lane.
- X is for sharp takes, faster iteration, and reach beyond the existing network.
- Facebook is supportive, not the center of gravity.
- One clear point per post beats crowded multi-message sludge.
- Do not trust automatic cross-posting without channel-level edits.
- Do not let AI invent product claims, customer numbers, or case studies.
- Unless explicitly approved, public posting should default to **drafts/scheduled items for review**, not instant live publishing.

## Escalation logic

If content starts feeling generic or weak:
1. go back to a sharper business truth
2. narrow to one argument
3. add proof, specificity, or a real example
4. cut the filler
5. rewrite the hook
6. change the format instead of polishing a dead post

## Assets and future extension

## Scripts

- `scripts/postiz_healthcheck.py` — verify Postiz API auth, list visible integrations, and probe MCP reachability from the current runtime

## Assets and future extension

If reusable templates, calendars, prompts, or helper scripts are added later, store them under `assets/` or `scripts/` and reference them from this file. Keep secrets and API keys out of the skill folder.