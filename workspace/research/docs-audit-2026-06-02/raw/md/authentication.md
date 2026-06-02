> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> Oviond authenticates API requests with Bearer tokens. Learn how to generate an API key, set the Authorization header, and handle auth errors.

Oviond's REST API uses Bearer token authentication. Every request must include your API key in the `Authorization` header. This page explains how to generate an API key from your account settings and how to pass it correctly in your requests.

## Generate an API key

<Steps>
  <Step title="Open API key settings">
    In the Oviond app, click your account name in the top-right corner and select **Settings**. Navigate to the **API Keys** tab.
  </Step>

  <Step title="Create a new key">
    Click **Create API Key**. Give it a descriptive name (for example, "Zapier integration" or "Custom dashboard") so you can identify it later.
  </Step>

  <Step title="Copy and store the key">
    Your key is shown once. Copy it and store it securely — you won't be able to see the full key again after you close this dialog.

    <Warning>
      Treat your API key like a password. Do not commit it to version control or expose it in client-side code.
    </Warning>
  </Step>
</Steps>

## Make authenticated requests

Include your API key in the `Authorization` header as a Bearer token on every request:

```bash theme={null}
curl -X GET https://api.oviond.com/v1/users/me \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with the key you generated above.

## Example: Fetch your account

```bash theme={null}
curl https://api.oviond.com/v1/users/me \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A successful response returns your user profile:

```json theme={null}
{
  "id": "usr_abc123",
  "email": "you@youragency.com",
  "name": "Your Name",
  "accountId": "acc_xyz789"
}
```

## Authentication errors

| Status             | Meaning                                                          |
| ------------------ | ---------------------------------------------------------------- |
| `401 Unauthorized` | The `Authorization` header is missing or the key is invalid.     |
| `403 Forbidden`    | Your key is valid but doesn't have permission for this resource. |

If you receive a `401`, double-check that you've included the `Authorization: Bearer <key>` header and that the key hasn't been revoked.

## Manage your API keys

You can list, create, and revoke API keys at any time from **Settings → API Keys** in the app, or via the [API Keys API](/api-keys/list).

<Note>
  Each API key is scoped to your account. Keys created by team members operate within their permission level.
</Note>
