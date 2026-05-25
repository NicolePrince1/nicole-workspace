# Real product screenshot correction — 2026-05-25

Chris correctly called out that the first screenshot samples were not real product captures. This folder corrects that.

## What was captured

Logged into `https://app.oviond.com` as `nicole@oviond.com` using the magic-link flow, completed onboarding far enough to access the app, and captured the real Clients screen and Add Client drawer.

## Real product outputs

Raw captures:

- `raw/real-clients-home.png`
- `raw/real-add-client-modal.png`

Annotated corrected outputs:

- `annotated/real-clients-home-panel-v2.png`
- `annotated/real-add-client-panel-v2.png`

## Product finding encountered

Onboarding still hit `Template not found` after the first-client step in this run. Despite that, the account/client state existed afterward and the app home loaded, which allowed the real Clients and Add Client screenshots to be captured.

## Lesson

For help-center production, screenshots must come from `app.oviond.com` or an approved staging/demo product environment. Mockups are acceptable only for marketing concepting and must be labelled as mockups.
