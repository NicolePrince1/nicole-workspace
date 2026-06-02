> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Domain

> Remove a custom domain from your account.

Deleting a domain stops it from serving reports and removes it from Vercel on Oviond's side. Shared links that used the custom domain will fall back to `app.oviond.com`.

<Steps>
  <Step title="Open Custom Domains">
    From **Account → Custom Domains**.
  </Step>

  <Step title="Open the domain's menu">
    Click the three-dot menu.
  </Step>

  <Step title="Choose Delete">
    Confirm when prompted.
  </Step>

  <Step title="Remove DNS records">
    Optionally clean up the CNAME/TXT records in your DNS provider — Oviond doesn't touch your DNS admin.
  </Step>
</Steps>

<Note>
  Existing shared links keep working — they transparently redirect from `yourdomain.com` to `app.oviond.com`. If you want a hard cut-off, also remove the DNS records so the domain no longer resolves.
</Note>
