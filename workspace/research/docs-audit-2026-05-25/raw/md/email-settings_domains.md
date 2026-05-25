> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Domains

> Verify domains so Oviond can send mail on their behalf.

An **email domain** is a domain authorized to send mail through Oviond. Verification involves adding DNS records (SPF, DKIM, DMARC) so recipient providers trust messages coming from your domain.

## Add a domain

<Steps>
  <Step title="Open Email Settings → Domains">
    Under **Account**.
  </Step>

  <Step title="Click + Add Domain">
    Enter the domain — e.g. `youragency.com`.
  </Step>

  <Step title="Copy the DNS records">
    Oviond shows SPF, DKIM, and (optionally) DMARC records. Add them exactly as shown in your DNS provider.
  </Step>

  <Step title="Click Verify">
    Oviond queries DNS and marks the domain **Active** once records resolve.
  </Step>
</Steps>

## Status

| Status      | Meaning                                                             |
| ----------- | ------------------------------------------------------------------- |
| **Pending** | DNS records not visible yet.                                        |
| **Active**  | All required records verified — senders under this domain can send. |
| **Failed**  | Verification timed out. Re-check records and click Verify again.    |

## Remove a domain

Deleting a domain immediately invalidates every [sender](/email-settings/senders) under it. Automations configured with those senders will fail on next fire — switch them to a different verified sender first.
