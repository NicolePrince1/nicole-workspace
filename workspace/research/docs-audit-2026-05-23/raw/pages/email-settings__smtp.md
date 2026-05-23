> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMTP

> Route Oviond emails through your own SMTP server.

By default Oviond sends automation emails via our managed provider (Resend). If your agency needs every email to pass through its own SMTP server — for audit, deliverability isolation, or IP warming — configure SMTP under **Account → Email Settings → SMTP**.

## Configure

<Steps>
  <Step title="Enable Use SMTP">
    Toggles Oviond from the managed provider to your SMTP server.
  </Step>

  <Step title="Enter SMTP details">
    Host, port, username, password, and TLS/SSL setting. Most agencies use port 587 with STARTTLS.
  </Step>

  <Step title="Save">
    Oviond stores the credentials encrypted and starts using them for every automation delivery.
  </Step>
</Steps>

## Test

Always test before going live:

<Steps>
  <Step title="Click Send Test Email">
    Under the SMTP config section.
  </Step>

  <Step title="Check delivery">
    Oviond sends a test email to your logged-in address via your configured SMTP. If it arrives, you're good.
  </Step>

  <Step title="Check the error if it fails">
    The error is shown inline — usually auth, TLS, or firewall-related.
  </Step>
</Steps>

## Fall back

Toggle **Use SMTP** off to revert to Oviond's managed provider. No changes to existing automations are needed — they pick up the new route on the next fire.

<Warning>
  A misconfigured SMTP server stops every automation from delivering. Keep **Use SMTP** off until the test passes.
</Warning>
