> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Data Sources

> Every marketing platform connected to your Oviond account.

Integrations are OAuth connections between Oviond and your clients' marketing platforms. Once connected, Oviond pulls live data from those platforms into your reports and dashboards — no manual exports or copy-pasting required. Each integration is connected on a per-client basis, so the data you see in a report always belongs to the client that report is built for.

## Supported integrations

Oviond supports 30+ marketing platforms across six categories.

| Category             | Platforms                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| **Paid Search**      | Google Ads, Microsoft Ads (Bing Ads)                                                              |
| **Paid Social**      | Facebook Ads, Instagram Ads, LinkedIn Ads, TikTok Ads, Pinterest Ads, Snapchat Ads, Twitter/X Ads |
| **Analytics**        | Google Analytics 4, Google Analytics (Universal), Adobe Analytics                                 |
| **SEO**              | Google Search Console, Semrush, Moz, Ahrefs                                                       |
| **Email Marketing**  | Mailchimp, Klaviyo, Campaign Monitor, ActiveCampaign                                              |
| **E-commerce & CRM** | Shopify, HubSpot, Salesforce                                                                      |

<Note>
  The full list of available integrations is visible inside Oviond under **Integrations** in the left sidebar. New platforms are added regularly.
</Note>

## How integrations work

When you connect an integration, Oviond guides you through an OAuth flow — you log in to the marketing platform and grant Oviond permission to read your data. Oviond stores the resulting authorization as an **auth profile**.

After authorization, you link a specific account or data source (for example, a particular Google Ads account or Facebook Ads campaign) to a client. That linked data source then becomes available in widgets when you build reports for that client.

### Auth profiles

An auth profile represents one authorized connection to a platform — typically tied to one login. If you manage multiple clients' accounts through a single agency login (such as a Google Ads manager account), one auth profile can cover all of those sub-accounts.

You can reuse the same auth profile across multiple clients. For example, if your agency has a single Google Ads manager account that contains sub-accounts for 10 clients, you authorize Google Ads once and then link each client to their respective sub-account — all without re-authenticating.

## Listing your connected integrations

To see all integrations connected across your workspace:

1. Click **Integrations** in the left sidebar.
2. The integrations list shows every platform you have authorized, along with the auth profiles and their connection status.

To see integrations for a specific client:

1. Navigate to the client from the **Clients** screen.
2. Open the client's **Integrations** tab. This lists only the data sources linked to that client.

## Testing an integration connection

If you want to verify that a connected integration is returning data correctly:

1. Go to **Integrations** and locate the integration you want to test.
2. Click the three-dot menu next to the integration.
3. Select **Test Connection**.

Oviond will attempt to fetch data from the platform and confirm whether the connection is active. If the test fails, see [Connect a Data Source to a Client](/data-sources/connect) for troubleshooting steps.

## Unlinking and deleting integrations

**Unlinking** removes the data source from a specific client but keeps the auth profile available for reuse. **Deleting** an auth profile removes it from your workspace entirely and disconnects all clients that relied on it.

### Unlink a data source from a client

1. Open the client and go to the **Integrations** tab.
2. Find the data source you want to remove.
3. Click the three-dot menu and select **Unlink**.

The auth profile remains available and can be relinked to the same or a different client at any time.

### Delete an auth profile

<Warning>
  Deleting an auth profile removes it permanently and disconnects every client and widget that used it. Any widgets in reports that relied on that connection will stop displaying data. This cannot be undone.
</Warning>

1. Click **Integrations** in the left sidebar.
2. Find the auth profile you want to delete.
3. Click the three-dot menu and select **Delete**.
4. Confirm the deletion in the dialog.

## Next steps

<CardGroup cols={2}>
  <Card title="Connect a data source" icon="plug" href="/data-sources/connect">
    Step-by-step guide to authorizing a platform and linking it to a client.
  </Card>

  <Card title="Custom metrics and data" icon="sliders" href="/data-sources/metrics">
    Create calculated metrics, save metric presets, and upload custom CSV data.
  </Card>
</CardGroup>
