> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Domain

> Register a custom domain so shared reports load under your agency's URL.

Custom domains replace `app.oviond.com` with your own URL on shared report links — e.g. `reports.youragency.com`. Oviond detects the DNS provider and tells you exactly which records to add.

<Steps>
  <Step title="Open Custom Domains">
    From **Account → Custom Domains**.
  </Step>

  <Step title="Click + Add Domain">
    Enter the subdomain you want to use — e.g. `reports.youragency.com`.
  </Step>

  <Step title="Detect DNS provider">
    Oviond auto-detects the domain's DNS host (Cloudflare, GoDaddy, Route 53, etc).
  </Step>

  <Step title="Copy the DNS records">
    Oviond shows a CNAME (and verification TXT) record. Add them exactly as shown in your DNS provider's admin.
  </Step>

  <Step title="Start verification">
    Click **Verify**. Oviond polls DNS until the records propagate.
  </Step>
</Steps>

## Supported providers with auto-setup

If your domain is on **Cloudflare** or **GoDaddy**, Oviond can configure the DNS records for you via OAuth — you grant permission once and Oviond writes the records automatically. For other providers, add the records manually as shown in the UI.

See [Verify Domain](/custom-domains/verify) for the verification flow.
