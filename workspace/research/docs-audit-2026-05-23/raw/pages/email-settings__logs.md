> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Logs

> Every automation email Oviond has sent — status, events, and any errors.

The **Email Logs** view shows every individual email Oviond has sent — automation deliveries, test sends that hit recipients, and transactional emails (invites, password resets).

## Columns

| Column         | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| **Recipient**  | The to-address that received the email.                       |
| **Subject**    | The subject line as rendered.                                 |
| **Sender**     | The from-address / sender name.                               |
| **Sent at**    | Timestamp of send.                                            |
| **Status**     | Delivered / Bounced / Deferred / Opened / Clicked.            |
| **Last event** | Most recent status change (via the provider's webhook).       |
| **Error**      | Present only for failed sends — the provider's error message. |

## Events

Provider webhook events update each log row in near-real-time:

* **Delivered** — accepted by the recipient's provider.
* **Bounced** — the recipient address rejected the message (hard bounce = invalid address).
* **Deferred** — temporary failure (mailbox full, greylisting) — usually retries.
* **Opened** / **Clicked** — tracked via pixel and link rewrites.

## Filters

* **Recipient search** — find every email sent to a specific address.
* **Date range** — narrow to a specific window.
* **Status** — show only bounced, deferred, or opened.

## Retention

Email logs are retained for 12 months.
