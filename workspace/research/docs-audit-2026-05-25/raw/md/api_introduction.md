> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Explore the Oviond REST API. Authenticate with a Bearer token, manage reports, integrations, automations, and access public shared report data.

The Oviond REST API lets you programmatically manage your agency's reports, clients, integrations, and automations. All requests are made over HTTPS to `https://api.oviond.com`.

## Base URL

```
https://api.oviond.com
```

## Authentication

All API requests (except public endpoints) require a Bearer token in the `Authorization` header:

```bash theme={null}
Authorization: Bearer YOUR_API_KEY
```

Generate an API key from **Settings → API Keys** in the Oviond app. See [Authentication](/authentication) for full details.

## Request format

* Send JSON bodies with `Content-Type: application/json`
* All responses are JSON
* Timestamps use ISO 8601 format

## HTTP status codes

| Code  | Meaning                                   |
| ----- | ----------------------------------------- |
| `200` | Success                                   |
| `201` | Created                                   |
| `204` | No content (successful delete)            |
| `400` | Bad request — check your request body     |
| `401` | Unauthorized — missing or invalid API key |
| `403` | Forbidden — insufficient permissions      |
| `404` | Not found                                 |
| `422` | Validation error                          |
| `500` | Server error                              |

## Rate limiting

API requests are rate-limited per account. If you exceed the limit, you'll receive a `429 Too Many Requests` response. Wait before retrying.
