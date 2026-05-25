> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Delivery

> Configure subject, sender, and body of automation emails.

By default, Oviond sends automated report emails from an Oviond address. You can change this to send from your own agency domain (e.g., `reports@youragency.com`) for a fully branded experience. Oviond supports two custom sending options: custom domain email and SMTP.

## Custom email domain

Send emails from your own domain using Oviond's email infrastructure. You'll need to add DNS records to verify ownership.

<Steps>
  <Step title="Open Email Settings">
    Go to **Settings → Email** and click **Add Sending Domain**.
  </Step>

  <Step title="Enter your domain">
    Type the domain you want to send from (e.g., `youragency.com`). Oviond will generate SPF and DKIM DNS records for you.
  </Step>

  <Step title="Add DNS records">
    Log in to your DNS provider and add the SPF and DKIM records that Oviond provides. The exact steps depend on your provider.

    <Note>
      DNS changes can take up to 24–48 hours to propagate. Oviond checks verification status automatically.
    </Note>
  </Step>

  <Step title="Verify your domain">
    Return to **Settings → Email** and click **Check Verification**. Once verified, you can set the sender name and email address (e.g., `Reports <reports@youragency.com>`).
  </Step>
</Steps>

## SMTP configuration

If you prefer to route emails through your own email provider (e.g., SendGrid, Mailgun, AWS SES), configure SMTP.

<Steps>
  <Step title="Open SMTP settings">
    Go to **Settings → Email → SMTP** and toggle on **Use Custom SMTP**.
  </Step>

  <Step title="Enter SMTP credentials">
    Fill in the host, port, username, and password from your email provider. Common ports are `587` (TLS) and `465` (SSL).
  </Step>

  <Step title="Test the connection">
    Click **Test SMTP** to send a test message. Oviond confirms whether the connection succeeded.

    <Warning>
      If SMTP credentials are incorrect, automated report emails will fail to send. Always test before saving.
    </Warning>
  </Step>

  <Step title="Save">
    Click **Save**. All subsequent report emails will route through your SMTP server.
  </Step>
</Steps>

## Send a test email

At any time, go to **Settings → Email** and click **Send Test Email** to verify your current configuration sends correctly to an address you specify.
