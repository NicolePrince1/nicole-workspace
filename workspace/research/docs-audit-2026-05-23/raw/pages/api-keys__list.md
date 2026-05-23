> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List API Keys

> Every API key issued for your Oviond account.

Oviond API keys let you authenticate requests to the Oviond REST API from external tools, scripts, or integrations. Each key is tied to your account and operates within your permission level.

## Create an API key

<Steps>
  <Step title="Open API Keys settings">
    Click your account name in the top-right corner, select **Settings**, and go to the **API Keys** tab.
  </Step>

  <Step title="Click Create API Key">
    Click **Create API Key** and enter a descriptive name — for example, "Zapier workflow" or "Internal dashboard script".
  </Step>

  <Step title="Copy your key">
    Your new API key is displayed once. Copy it and store it somewhere secure.

    <Warning>
      You cannot view the full key again after closing this dialog. If you lose it, revoke the key and create a new one.
    </Warning>
  </Step>
</Steps>

## Use your API key

Include the key in the `Authorization` header on every API request:

```bash theme={null}
curl https://api.oviond.com/v1/users/me \
  -H "Authorization: Bearer YOUR_API_KEY"
```

See [Authentication](/authentication) for more details on how to authenticate API requests.

## Manage existing keys

From **Settings → API Keys** you can:

* **View** all active keys (name and creation date — the full key value is never shown again)
* **Revoke** a key — immediately invalidates it, any requests using it will receive `401 Unauthorized`
* **Delete** a key — permanently removes it from your account

<Note>
  Revoking a key is immediate. Update any integrations or scripts using that key before revoking to avoid downtime.
</Note>

## Security best practices

* Give each key a descriptive name so you can identify and revoke individual integrations
* Never commit API keys to version control
* Rotate keys periodically or immediately if you suspect a key has been exposed
* Use one key per integration so you can revoke a single key without affecting others
