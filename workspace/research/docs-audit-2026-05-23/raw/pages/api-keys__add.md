> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add API Key

> Generate a new API key to authenticate REST API calls.

API keys let external scripts and integrations call the Oviond REST API on behalf of your account. A key inherits the permissions of the user who created it — invite a dedicated read-only user for key-issuing if you want to scope-limit.

<Steps>
  <Step title="Open API Keys">
    From **Account → API Keys**.
  </Step>

  <Step title="Click + New Key">
    Opens the create dialog.
  </Step>

  <Step title="Name the key">
    Use a descriptive name — e.g. *Zapier — Marketing Workflows* — so you know what depends on it.
  </Step>

  <Step title="Create">
    Oviond shows the key **once** — copy it immediately. We hash the key after this screen; there's no way to retrieve it later.
  </Step>

  <Step title="Paste into your tool">
    Use the key as a Bearer token: `Authorization: Bearer <key>`.
  </Step>
</Steps>

<Warning>
  The full key is only visible at creation. If you lose it, you'll need to [revoke](/api-keys/revoke) the key and generate a new one.
</Warning>
