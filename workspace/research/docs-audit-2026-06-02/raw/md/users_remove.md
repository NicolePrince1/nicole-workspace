> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove User

> Revoke a team member's access to your Oviond account.

Removing a user immediately revokes their access. They can no longer sign in, and any API keys they issued stop working.

<Steps>
  <Step title="Open Users">
    Under **Account → Users**.
  </Step>

  <Step title="Open the user's menu">
    Click the three-dot menu.
  </Step>

  <Step title="Choose Remove">
    Confirm when prompted.
  </Step>
</Steps>

## What happens to their work

* **Reports and dashboards they created** stay in the account — they belong to the client, not the user.
* **Integrations they connected** keep working — the OAuth tokens are stored on the account, not the user.
* **API keys they issued** are revoked immediately. If any automations depend on them, regenerate the keys under a different user or the owner.
* **Activity log entries** remain intact with their name attached for audit purposes.

<Warning>
  Removing the only account **Owner** requires transferring ownership first. See [Update User](/users/update).
</Warning>
