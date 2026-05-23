> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Domains

> Every custom domain registered to your Oviond account.

By default, shared report links use an `oviond.com` subdomain. A custom domain replaces that with a URL you own — for example, `reports.youragency.com`. Clients see only your domain, reinforcing your agency brand at every touchpoint.

## Before you start

To add a custom domain, you need:

* **A domain you own** — this can be a subdomain of your main domain (recommended) or a standalone domain.
* **Access to your domain's DNS settings** — you'll need to add a CNAME record. This is done through your domain registrar or DNS provider (for example, Cloudflare, GoDaddy, or Namecheap).

<Note>
  DNS changes can take up to 48 hours to propagate globally, though most providers update within a few hours. Plan ahead if you have a deadline for switching clients to the new domain.
</Note>

## Add a custom domain

<Steps>
  <Step title="Open White Label settings">
    Go to **Account Settings** > **White Label**, then scroll to the **Custom Domain** section.
  </Step>

  <Step title="Enter your domain">
    In the **Custom domain** field, type the domain or subdomain you want to use — for example, `reports.youragency.com`. Do not include `https://`.
  </Step>

  <Step title="Save to generate your CNAME record">
    Click **Save** (or **Add domain**). Oviond generates a CNAME record specific to your account. The target value is displayed on screen — copy it before leaving this page.
  </Step>
</Steps>

## Add the CNAME record to your DNS provider

Once Oviond gives you the CNAME target, you need to add it to your DNS provider. How you do this depends on which provider you use.

### Cloudflare and GoDaddy (automated setup)

Oviond offers automated DNS setup for Cloudflare and GoDaddy. If you use either of these providers:

<Steps>
  <Step title="Select your DNS provider">
    In the **Custom Domain** section, choose **Cloudflare** or **GoDaddy** from the provider selector.
  </Step>

  <Step title="Authenticate with your provider">
    Follow the prompts to connect your Cloudflare or GoDaddy account. Oviond requests permission to add the DNS record on your behalf.
  </Step>

  <Step title="Confirm the record">
    Review the CNAME record Oviond will add, then confirm. Oviond adds the record automatically and begins verification.
  </Step>
</Steps>

### Other DNS providers (manual setup)

For all other providers, add the CNAME record manually through your DNS provider's control panel:

<Steps>
  <Step title="Log in to your DNS provider">
    Open your domain registrar or DNS provider and navigate to the DNS management panel for your domain.
  </Step>

  <Step title="Add a new CNAME record">
    Create a new record with the following values:

    | Field              | Value                                                                                                           |
    | ------------------ | --------------------------------------------------------------------------------------------------------------- |
    | **Type**           | CNAME                                                                                                           |
    | **Name / Host**    | The subdomain portion of your custom domain (for example, `reports` if your domain is `reports.youragency.com`) |
    | **Value / Target** | The CNAME target provided by Oviond                                                                             |
    | **TTL**            | 3600 (or your provider's default)                                                                               |
  </Step>

  <Step title="Save the record">
    Save the DNS record in your provider's panel. Changes begin propagating immediately but may take time to fully resolve.
  </Step>
</Steps>

## Verify DNS propagation

After adding the CNAME record, return to Oviond and wait for verification.

<Steps>
  <Step title="Return to White Label settings">
    Go back to **Account Settings** > **White Label** > **Custom Domain**.
  </Step>

  <Step title="Check the verification status">
    Oviond automatically checks whether the CNAME record resolves correctly. The status indicator shows one of:

    * **Pending** — the record hasn't propagated yet. Check back later.
    * **Verified** — DNS is configured correctly. Your custom domain is active.
    * **Error** — the record wasn't found or doesn't match. Double-check the CNAME target you entered.
  </Step>

  <Step title="Wait if needed">
    If the status is **Pending**, wait a few hours and check again. Full global propagation can take up to 48 hours. You can use a tool like [dnschecker.org](https://dnschecker.org) to monitor propagation status independently.
  </Step>
</Steps>

## After verification

Once Oviond verifies your domain:

* All new shared report links use your custom domain automatically.
* Existing report links on `oviond.com` continue to work during a transition period, but new links will use your domain.
* Clients who open a shared link see your domain in the browser address bar.

<Note>
  SSL is provisioned automatically for your custom domain. You don't need to set up a certificate manually.
</Note>

## Remove a custom domain

<Warning>
  Removing your custom domain immediately breaks any existing shared report links that use it. Clients who have bookmarked or saved those links will no longer be able to open them. Before removing a domain, notify affected clients or update the links you've shared with them.
</Warning>

<Steps>
  <Step title="Open White Label settings">
    Go to **Account Settings** > **White Label** > **Custom Domain**.
  </Step>

  <Step title="Remove the domain">
    Click **Remove** next to your custom domain. Confirm when prompted.
  </Step>

  <Step title="Clean up your DNS records">
    Log in to your DNS provider and delete the CNAME record you added. Leaving an unused CNAME record in your DNS is harmless but unnecessary.
  </Step>
</Steps>

After removal, Oviond falls back to the default `oviond.com` domain for all shared report links.
