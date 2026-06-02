> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke API Key

> Immediately disable an API key without deleting its audit record.

Revoking a key stops it from authenticating new requests — every future call returns `401 Unauthorized`. The key's metadata (name, created-at, created-by) stays in the list for audit.

Use revoke when:

* The key was accidentally shared or committed to a public repo
* A team member leaves the agency
* An integration is being decommissioned

<Steps>
  <Step title="Open API Keys">
    From **Account → API Keys**.
  </Step>

  <Step title="Open the key's menu">
    Click the three-dot menu on the key row.
  </Step>

  <Step title="Choose Revoke">
    Confirm when prompted.
  </Step>
</Steps>

## Revoked vs deleted

| State       | Still in list? | Can still authenticate? | Can be restored?      |
| ----------- | -------------- | ----------------------- | --------------------- |
| **Revoked** | Yes            | No                      | No — create a new key |
| **Deleted** | No             | No                      | No                    |

Revoke first — deleting is irreversible and drops the audit record. See [Delete API Key](/api-keys/delete).
