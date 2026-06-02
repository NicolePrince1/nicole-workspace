> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect

> Authorize Oviond to pull data from Google Ads, Facebook, and 30+ other platforms.

Connecting a marketing platform to a client is a two-step process. First, you authorize the platform through OAuth — this creates an **auth profile** in your Oviond workspace. Second, you link a specific account or data source from that platform to the client. Once linked, that data source is available in widgets when you build reports for that client.

<Note>
  Oviond requests read-only access to all connected platforms. Oviond cannot make changes to your campaigns, budgets, or account settings.
</Note>

## Step 1: Authorize the platform

<Steps>
  <Step title="Open Integrations">
    Click **Integrations** in the left sidebar. This shows all platforms available to connect.
  </Step>

  <Step title="Find the platform">
    Browse the list or use the search bar to find the platform you want to connect (for example, Google Ads or Facebook Ads).
  </Step>

  <Step title="Click Connect">
    Click **Connect** next to the platform name. Oviond opens an OAuth authorization window.
  </Step>

  <Step title="Log in and grant permissions">
    Log in to the platform using the account credentials for the client (or your agency's manager account). Review the permissions and click **Allow** or **Authorize** to grant Oviond read access.
  </Step>

  <Step title="Return to Oviond">
    After authorization, the platform redirects you back to Oviond. The new auth profile now appears under that platform in your integrations list.
  </Step>
</Steps>

If you already have an auth profile for this platform (for example, you previously connected Google Ads for another client), you can skip Step 1 and proceed directly to linking the data source in Step 2.

## Step 2: Link a data source to a client

After authorization, you link the specific account or property to a client.

<Steps>
  <Step title="Navigate to the client">
    Go to **Clients** in the left sidebar and open the client you want to connect data to.
  </Step>

  <Step title="Open the Integrations tab">
    Click the **Integrations** tab on the client's profile page.
  </Step>

  <Step title="Add a data source">
    Click **+ Add Data Source**. A panel opens listing the platforms you have authorized.
  </Step>

  <Step title="Select the platform and auth profile">
    Choose the platform (for example, Google Ads) and select the auth profile to use. If you have multiple auth profiles for the same platform, select the one that has access to this client's account.
  </Step>

  <Step title="Select the specific account">
    From the account dropdown, select the specific account, property, or sub-account to link to this client (for example, the Google Ads account for this particular client). Only accounts accessible under the selected auth profile appear in this list.
  </Step>

  <Step title="Save the data source">
    Click **Save**. The data source is now linked to the client and available in report widgets.
  </Step>
</Steps>

## Test the connection

After linking a data source, verify it is returning data correctly before building widgets.

1. On the client's **Integrations** tab, find the data source you just linked.
2. Click the three-dot menu next to it and select **Test Connection**.
3. Oviond attempts to fetch data from the platform. A success message confirms the connection is active.

If the test fails, see [Common connection issues](#common-connection-issues) below.

## Reconnect an expired or revoked integration

OAuth tokens expire or are revoked when you change your password, revoke app access from within the marketing platform, or the platform's token policy expires the session. When this happens, widgets connected to that integration stop displaying data and the integration shows a warning status.

<Steps>
  <Step title="Identify the expired integration">
    Go to **Integrations** in the left sidebar. Expired or revoked auth profiles display a warning icon or a **Reconnect** prompt.
  </Step>

  <Step title="Click Reconnect">
    Click **Reconnect** next to the affected auth profile.
  </Step>

  <Step title="Re-authorize through OAuth">
    Complete the OAuth flow again using the same account credentials. Once you authorize, Oviond updates the auth profile with a fresh token.
  </Step>

  <Step title="Verify the connection">
    After reconnecting, use **Test Connection** on the affected data sources to confirm data is flowing again.
  </Step>
</Steps>

<Note>
  Reconnecting an auth profile restores all clients and widgets that used it — you do not need to re-link each client individually.
</Note>

## Common connection issues

<AccordionGroup>
  <Accordion title="Wrong account selected during OAuth">
    If you have multiple accounts on a platform (for example, both a personal Google account and an agency Google account), the OAuth window may default to the wrong one. To fix this:

    1. Go to **Integrations** and delete the incorrectly authorized auth profile.
    2. Click **Connect** again.
    3. In the OAuth window, click the account switcher or **Use a different account** and log in with the correct credentials.
  </Accordion>

  <Accordion title="Insufficient permissions">
    Oviond requires read access to the account you are connecting. If authorization succeeds but the connection test fails with a permissions error, verify that the account you used has at least read-level access in the marketing platform. For Google Ads, the account needs **Read only** access or higher. For Facebook Ads, the user must have the **Analyst** role or higher on the ad account.
  </Accordion>

  <Accordion title="Account not appearing in the data source list">
    If the account you expect does not appear after authorization:

    * Confirm the account is accessible under the login you used (for manager accounts, check that the sub-account is linked to your manager account).
    * Try disconnecting and re-authorizing the auth profile.
    * If using a Google Ads manager account, allow up to a few minutes for the full account hierarchy to load.
  </Accordion>

  <Accordion title="Connection test passes but widgets show no data">
    A successful connection test confirms the authorization is valid, but data in widgets may still be empty if:

    * The date range on the widget is set to a period with no activity.
    * The specific campaign, property, or segment selected in the widget has no data for that period.
    * The account was created recently and has not yet accumulated data.

    Check the widget's date range and data source settings before troubleshooting the integration further.
  </Accordion>

  <Accordion title="OAuth popup is blocked">
    Some browsers block OAuth popups by default. If clicking **Connect** does nothing, check your browser's popup blocker and allow popups for your Oviond domain, then try again.
  </Accordion>
</AccordionGroup>
