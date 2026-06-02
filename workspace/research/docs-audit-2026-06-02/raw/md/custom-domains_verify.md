> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify Domain

> Confirm DNS records are live so your custom domain activates.

After you [add a domain](/custom-domains/add), Oviond watches DNS for the required records. Once they resolve correctly, the domain moves to **Active** and shared links start rendering under it.

## Statuses

| Status        | Meaning                                                       |
| ------------- | ------------------------------------------------------------- |
| **Pending**   | Just added. DNS records haven't propagated yet.               |
| **Verifying** | Records are visible but SSL is still provisioning.            |
| **Active**    | Records and SSL are live — the domain is fully functional.    |
| **Failed**    | Verification timed out. Records are missing or misconfigured. |

## Trigger a re-check

<Steps>
  <Step title="Open Custom Domains">
    From **Account → Custom Domains**.
  </Step>

  <Step title="Click the domain">
    Opens the detail panel with the current DNS record status.
  </Step>

  <Step title="Click Verify">
    Oviond re-queries DNS and Vercel (the SSL provider) and updates the status immediately.
  </Step>
</Steps>

## Typical DNS propagation times

* **Cloudflare / Vercel DNS** — under 1 minute
* **Route 53** — 1–5 minutes
* **GoDaddy, Namecheap** — 5–30 minutes
* **Older registrars** — up to 24 hours

If the domain stays in **Pending** after a few hours, double-check the CNAME and TXT records match exactly what Oviond showed when you added the domain.
