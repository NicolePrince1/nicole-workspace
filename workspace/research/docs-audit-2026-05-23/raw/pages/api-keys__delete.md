> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete API Key

> Permanently remove an API key from the list.

Deleting a key removes it entirely from your API Keys list — the audit entry is gone. If you just want to stop the key from working while keeping the audit trail, [Revoke](/api-keys/revoke) instead.

<Steps>
  <Step title="Open API Keys">
    From **Account → API Keys**.
  </Step>

  <Step title="Open the key's menu">
    Click the three-dot menu.
  </Step>

  <Step title="Choose Delete">
    Confirm when prompted.
  </Step>
</Steps>

<Warning>
  Deletion is irreversible and the key's metadata (name, created-at, created-by) is lost. Revoke first and delete later if you want to preserve the audit record.
</Warning>
