> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Report Branding and Appearance

> Apply your agency's color palette, fonts, and logo to all client-facing Oviond reports. Use the live preview mode to review changes before saving.

Branding settings control the visual appearance of client-facing reports — the colors, fonts, and logo your clients see when they open a shared report link. These settings apply to the presentation layer of the report itself, separate from your agency identity settings in white labeling.

## White-label settings vs. branding settings

Oviond has two distinct layers of brand control:

| Setting                  | What it controls                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **White-label settings** | Your agency identity in the report frame — name, logo in the header, custom domain, email sender name. These are account-wide. |
| **Branding settings**    | The visual design of client-facing report content — the color palette, fonts, and logo that appear inside reports.             |

Configure white-label settings once to establish your agency's identity across all shared reports. Use branding settings to define the visual style of report content — either as a default for all reports or as a baseline your per-report themes build on. See [White-Label Reporting for Your Agency](/custom-domains/list) for the account-level identity settings.

## Open the branding settings panel

<Steps>
  <Step title="Open your account settings">
    Click your avatar or initials in the bottom-left corner of the sidebar, then select **Account Settings**.
  </Step>

  <Step title="Select the Branding tab">
    In the account settings panel, click the **Branding** tab. This panel contains all visual design options for client-facing reports.
  </Step>
</Steps>

## Customize the color palette

The color palette you set here applies to client-facing report views. It determines the primary accent color, supporting accent, and background used throughout reports.

<Steps>
  <Step title="Open the Branding panel">
    Go to **Account Settings** > **Branding**.
  </Step>

  <Step title="Set the primary color">
    Click the **Primary color** swatch and enter a hex value or use the color picker. The primary color appears in headers, buttons, and dominant UI elements in client-facing report views.
  </Step>

  <Step title="Set the accent color">
    Click the **Accent color** swatch and enter a hex value. The accent color is used for highlights and secondary interactive elements.
  </Step>

  <Step title="Set the background color">
    Click the **Background color** swatch and enter a hex value. This sets the base background of the client-facing report view.
  </Step>

  <Step title="Preview your changes">
    Use the live preview panel on the right to see how your color choices look in a sample report view before saving.
  </Step>

  <Step title="Save your changes">
    Click **Save** to apply the palette across all client-facing reports.
  </Step>
</Steps>

<Tip>
  Match these colors to your agency's brand guide. Consistent color usage across reports, proposals, and your website reinforces your agency's professionalism to every client.
</Tip>

## Set a report-level logo

The branding settings panel includes a separate logo upload for report content — distinct from the header logo you set in white-label settings. This logo can appear as a watermark or header element within the report pages themselves.

<Steps>
  <Step title="Open the Branding panel">
    Go to **Account Settings** > **Branding**.
  </Step>

  <Step title="Upload the logo">
    Under **Report logo**, click **Upload** and select your image file. PNG or SVG with a transparent background works best.
  </Step>

  <Step title="Adjust positioning (if available)">
    If a positioning option is shown, choose where the logo appears within the report layout.
  </Step>

  <Step title="Save your changes">
    Click **Save**.
  </Step>
</Steps>

<Note>
  The report logo is separate from the logo in your white-label header settings. The white-label logo appears in the report frame (the outer chrome). The report logo appears inside the report content area itself.
</Note>

## Set fonts for reports

Font settings control the typefaces used for headings and body text inside client-facing report views.

<Steps>
  <Step title="Open the Branding panel">
    Go to **Account Settings** > **Branding**.
  </Step>

  <Step title="Choose a heading font">
    Use the **Heading font** dropdown to select the typeface for titles and section headers inside reports.
  </Step>

  <Step title="Choose a body font">
    Use the **Body font** dropdown to select the typeface for all other text — labels, descriptions, and widget text.
  </Step>

  <Step title="Preview your changes">
    Check the preview panel to see how the font pairing looks in context.
  </Step>

  <Step title="Save your changes">
    Click **Save**.
  </Step>
</Steps>

## Preview mode

Before saving any branding change, use the built-in preview to see how the update will look in a real report context.

The preview panel displays a sample report view using your current settings. Changes you make in the branding panel are reflected in the preview in real time. Save only when you're satisfied with the result — unsaved changes do not affect live client-facing reports.

## How branding settings interact with per-report themes

Branding settings establish the default visual style for all client-facing reports. Per-report themes, configured at the project level, can override these defaults for individual reports.

| Level                 | Scope                  | Overrides                                    |
| --------------------- | ---------------------- | -------------------------------------------- |
| **Branding settings** | All reports by default | —                                            |
| **Per-report theme**  | A single project       | Overrides branding defaults for that project |

If a project has a theme applied, that theme's colors and fonts take effect for that project's client-facing view. Projects without an applied theme fall back to your branding settings. See [Design Report Themes](/themes/list) for how to create and apply per-report themes.

<Tip>
  For most agencies, the best workflow is to set branding defaults that match your agency brand, then create per-client themes when a client's brand colors differ significantly from your own.
</Tip>
