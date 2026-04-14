# GTM Audit Checklist

Use this checklist when auditing Oviond's GTM setup.

## 1) Account and container structure

Confirm:
- which GTM account is the production account
- which container is live for Oviond web properties
- whether app and marketing site share one container
- whether multiple domains are intentionally tracked through the same tags

## 2) Workspace hygiene

Check:
- how many workspaces exist
- whether the default workspace contains risky unpublished drift
- whether naming is disciplined enough to understand recent changes

## 3) Tag inventory

List:
- GA4 config or Google tag entries
- GA4 event tags
- Google Ads conversion and remarketing tags
- Meta/custom HTML tags
- duplicate or legacy tags
- paused tags that still create confusion

Important questions:
- which tags are firing on `www.oviond.com`
- which tags are firing on `v2.oviond.com`
- whether hostname restrictions exist at all

## 4) Trigger logic

Look for:
- broad `All Pages` triggers
- hostname filters using `Page Hostname`
- path filters that are too loose
- custom event triggers that might duplicate measurement
- exceptions that are missing where they should exist

## 5) Variable quality

Check:
- whether GA4 measurement IDs are hard-coded or variable-driven
- whether environment/domain variables exist
- whether variables make hostname-specific firing easy or impossible

## 6) Publishing discipline

Check:
- recent version history
- whether version names and notes are meaningful
- whether there is a safe rollback path
- whether publishing is happening directly from messy default workspaces

## 7) Data quality implications

Translate GTM findings into business consequences:
- polluted GA4 host mix
- duplicate conversions
- noisy remarketing audiences
- bad attribution
- hidden product-vs-marketing behavior inside one property

## 8) Output standard

End the audit with:
- current state
- key risks
- exact tags/triggers causing the issue
- safest change path
- what should be verified after publish
