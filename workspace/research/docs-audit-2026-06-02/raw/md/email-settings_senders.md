> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Senders

> Add verified from-addresses for automation emails.

A **sender** is a specific from-address (e.g. `reports@youragency.com`) that Oviond can send automation emails from. Before a sender is usable, the domain it belongs to must be verified under [Email Domains](/email-settings/domains).

## Add a sender

<Steps>
  <Step title="Open Email Settings → Senders">
    Under **Account**.
  </Step>

  <Step title="Click + Add Sender">
    Opens the create dialog.
  </Step>

  <Step title="Enter the address">
    Must belong to a verified domain. Unverified domains are blocked.
  </Step>

  <Step title="Enter a display name">
    The name recipients see as the sender (e.g. *Acme Reports Team*).
  </Step>

  <Step title="Save">
    The sender is now selectable on any automation or email default.
  </Step>
</Steps>

## Who sees what

Emails from a verified sender display with your agency name in the recipient's inbox — no "sent via Oviond" footer, no mismatched from-address warnings, and SPF/DKIM pass cleanly because the domain is set up correctly.

See [Email Domains](/email-settings/domains) for the domain verification flow.
