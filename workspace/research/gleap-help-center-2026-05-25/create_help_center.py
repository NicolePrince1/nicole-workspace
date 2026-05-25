#!/usr/bin/env python3
import json, os, re, sys, time
from pathlib import Path
sys.path.insert(0,'/data/.openclaw/workspace/skills/use-gleap/scripts')
from gleap_api import gleap_request

API_KEY=os.environ['GLEAP_API_KEY']; PROJECT_ID=os.environ['GLEAP_PROJECT_ID']; BASE=os.getenv('GLEAP_BASE_URL','https://api.gleap.io/v3')
OUT=Path('/data/.openclaw/workspace/research/gleap-help-center-2026-05-25')
DISALLOWED=['supabase','s3','sqs','resend','vercel','cron','raw_data','resource_type','resource_id','users table','accounts row','upstream api','jwt','openapi','swagger']

HELP_CENTER = [
  {
    'title':'Getting Started',
    'description':'Start here to understand Oviond and create your first client report.',
    'articles':[
      ('What is Oviond?', 'A simple overview of Oviond for agencies.', [
        ('Oviond is a white-label marketing reporting platform for agencies. It helps you connect client marketing data, build reports or dashboards, and share those reports under your own brand.', []),
        ('The basic workflow is simple: create a client, connect that client’s data sources, build a report or dashboard, then share it manually or schedule automatic delivery.', []),
        ('Use Oviond when you want client-ready reporting without rebuilding the same report manually every month.', [])
      ], ['Client','Data source','Report','Dashboard','Automation','White label']),
      ('Quick start checklist', 'The shortest path to your first useful Oviond report.', [
        ('Use this checklist when you are setting up Oviond for the first time.', ['Create or join your agency account.','Add your first client.','Connect at least one data source for that client.','Create a report or dashboard.','Add widgets that use the connected data source.','Share the report with your client or test an automation.']),
        ('If you get stuck, start by checking whether the client has a connected data source and whether the widget date range contains data.', [])
      ], []),
      ('Key terms in Oviond', 'Understand the words used across Oviond.', [
        ('These are the core terms you will see in the app.', ['Client: the business, brand, store, branch, or profile you are reporting for.','Data source: a connected marketing platform such as Google Ads, Meta, Google Analytics, or another supported platform.','Project: the container for a report or dashboard.','Report: a client-ready, paged project that can be shared or exported.','Dashboard: a live project view used to monitor data.','Widget: a chart, table, KPI, text block, or visual element inside a report or dashboard.','Template: a reusable report structure.','Automation: a scheduled report delivery.']),
        ('If two terms sound similar, remember this: clients hold data sources; projects hold pages and widgets.', [])
      ], []),
      ('Create your first client report', 'A beginner-friendly flow for creating a report.', [
        ('To create your first useful report, work in this order.', ['Open Clients and add the client you want to report on.','Connect at least one data source for that client.','Open the client and create a new project. Choose Report if you want a paged client-ready report.','Start from a template or a blank report.','Add widgets and choose the right data source for each widget.','Preview the report and check the date range.','Share the report link or schedule delivery.']),
        ('Tip: build the report with one client and one data source first. Once that works, add more pages, widgets, and integrations.', [])
      ], []),
      ('Where to get help', 'What to do when you need support.', [
        ('If something does not look right, collect the most useful details before contacting support.', ['Client name','Report or dashboard name','Data source name','The date range you are checking','A screenshot of the issue','Whether the issue affects one widget, one report, or multiple clients']),
        ('This helps the support team separate setup issues from data-source issues and get you a faster answer.', [])
      ], [])
    ]
  },
  {
    'title':'Clients',
    'description':'Create, manage, organize, and troubleshoot client workspaces.',
    'articles':[
      ('Add a client', 'Create a new client workspace.', [
        ('A client is the top-level workspace for a customer, brand, store, branch, or profile you report on.', []),
        ('To add one:', ['Open Clients.','Click Add Client.','Enter the client name.','Add optional details such as website, timezone, currency, manager, folder, and theme.','Save the client.']),
        ('Only the client name is usually required. You can add the rest later from the client settings.', [])
      ], []),
      ('Edit client details', 'Update the client name, website, timezone, currency, manager, or default theme.', [
        ('Use client settings when a client changes name, website, reporting timezone, currency, or account owner.', []),
        ('Recommended checks after editing a client:', ['Confirm the client name still looks correct in reports.','Check that date-based widgets use the expected timezone.','Check money widgets if you changed currency.','Refresh the client screenshot if the website changed.']),
        ('Changing client details should not remove existing reports or data sources.', [])
      ], []),
      ('Organize clients with folders', 'Keep a large client list easier to manage.', [
        ('Folders help agencies group clients by team, region, service, status, or account manager.', []),
        ('Good folder examples:', ['Active clients','Prospects','Enterprise clients','By account manager','By country or region','By service type']),
        ('A folder is only for organization. It should not change the client’s connected data sources or reports.', [])
      ], []),
      ('Refresh a client screenshot', 'Update the website thumbnail shown for a client.', [
        ('Oviond can use a client website screenshot as the visual thumbnail for that client.', []),
        ('Refresh the screenshot when:', ['The client has redesigned their website.','The website URL was added or corrected.','The thumbnail looks outdated or broken.']),
        ('If the screenshot still does not update, check that the client website is public, loads normally, and is not blocking automated screenshot tools.', [])
      ], []),
      ('Archive or delete a client', 'Understand what happens before removing a client.', [
        ('Warning: removing a client can affect reports, dashboards, connected data sources, and historical reporting access for that client.', []),
        ('Before removing a client:', ['Confirm you selected the correct client.','Check whether the client has active shared report links.','Check whether any scheduled reports still send to the client.','Export or save anything you may need later.']),
        ('If you are not sure whether the action is recoverable, pause and ask an account admin or Oviond support first.', [])
      ], [])
    ]
  },
  {
    'title':'Data Sources',
    'description':'Connect marketing platforms and troubleshoot missing or stale data.',
    'articles':[
      ('What are data sources?', 'Understand connected platforms in Oviond.', [
        ('A data source is a marketing platform account connected to a client in Oviond. Examples include ad platforms, analytics tools, social platforms, and other marketing data providers.', []),
        ('Most connections use a secure authorization flow. Oviond requests read access so it can pull reporting data into widgets.', []),
        ('A connected account must be linked to the correct client before it can be used in that client’s reports.', [])
      ], []),
      ('Connect a data source', 'Authorize a platform and link it to a client.', [
        ('Connecting a data source usually has two parts.', ['Authorize the platform account.','Link the specific account, property, or profile to the right client.']),
        ('Basic steps:', ['Open Integrations or the client’s Integrations area.','Choose the platform you want to connect.','Follow the authorization flow.','Select the account or profile that belongs to the client.','Save the connection.','Test the connection before building widgets.']),
        ('Use the account that has access to the client’s marketing data. If the wrong login is used, the account you need may not appear.', [])
      ], []),
      ('Choose the right account or profile', 'Avoid linking the wrong marketing account to a client.', [
        ('Many agencies manage several accounts under one login. Always confirm the exact account, property, page, profile, or ad account before saving a data source.', []),
        ('Before linking, check:', ['The platform account name.','The account ID if available.','The client it belongs to.','Whether the selected account has recent data.']),
        ('If you accidentally link the wrong account, remove it from the client and link the correct one.', [])
      ], []),
      ('Reconnect an expired data source', 'Fix a connection that stopped authorizing.', [
        ('Connections can expire when platform access changes, a password is reset, permissions are revoked, or the platform asks for authorization again.', []),
        ('To reconnect:', ['Open Integrations.','Find the affected platform or connected account.','Choose Reconnect.','Complete the authorization flow again using the correct login.','Test the connection after reconnecting.']),
        ('Reconnect with the same account where possible. That usually restores reports using the connection without rebuilding widgets.', [])
      ], []),
      ('Troubleshoot missing data', 'What to check when a widget shows no data.', [
        ('A working connection does not always mean every widget will show data for every date range.', []),
        ('Check these first:', ['Is the data source connected to the correct client?','Does the selected date range contain data?','Is the selected campaign, page, property, or profile active?','Does the platform account have enough permission for reporting data?','Does another widget using the same data source work?']),
        ('If only one widget is empty, check the widget settings. If every widget from the same platform is empty, test or reconnect the data source.', [])
      ], [])
    ]
  },
  {
    'title':'Reports & Dashboards',
    'description':'Build, edit, share, and export client reports and dashboards.',
    'articles':[
      ('Reports vs dashboards', 'Know which project type to use.', [
        ('Reports and dashboards are both projects in Oviond. The difference is how they are usually used.', ['Use a report when you want a client-ready, paged document that can be shared, exported, or delivered regularly.','Use a dashboard when you want a live view of performance for monitoring.']),
        ('If the output is going to a client every week or month, start with a report. If it is mainly for internal tracking, a dashboard may be better.', [])
      ], []),
      ('Create a report or dashboard', 'Start a new project for a client.', [
        ('Before you create a project, add the client and connect at least one data source.', []),
        ('Steps:', ['Open the client.','Go to the Projects area.','Click New Project.','Choose Report or Dashboard.','Name the project.','Start blank or choose a template.','Create the project and open the editor.']),
        ('The project belongs to the client you create it under.', [])
      ], []),
      ('Add and organize pages', 'Use pages to structure a report.', [
        ('Pages help split a report into clear sections such as Overview, Paid Ads, SEO, Social Media, Email, and Recommendations.', []),
        ('Good page structure makes reports easier for clients to read and easier for your team to maintain.', []),
        ('Keep page names short and descriptive. Avoid repeating the same metric across too many pages unless the client needs that view.', [])
      ], []),
      ('Add widgets', 'Use widgets to show charts, KPIs, tables, and text.', [
        ('Widgets are the building blocks of reports and dashboards.', []),
        ('When adding a widget, check:', ['The widget type matches the question you want to answer.','The correct client data source is selected.','The metric and date range are correct.','The chart title is clear for the client.']),
        ('If a widget looks empty, first check the date range and selected data source.', [])
      ], []),
      ('Share a report', 'Give clients access to a report or dashboard.', [
        ('You can share a project with a client using a public report link or scheduled delivery.', []),
        ('Before sharing:', ['Preview the report.','Check branding, logo, and theme.','Confirm date ranges.','Check that every widget loads.','Open the share link in a private browser window if possible.']),
        ('If the client sees a broken or outdated report, refresh the report and check whether the underlying data source is still connected.', [])
      ], []),
      ('Export a report as PDF', 'Create a PDF version of a report.', [
        ('PDF export is useful when clients want a downloadable or email-friendly report copy.', []),
        ('Before exporting:', ['Check that charts and tables load on screen.','Use the right report date range.','Keep pages tidy and avoid overly wide tables.','Preview the PDF before sending it to a client.']),
        ('If a PDF fails or looks incomplete, try refreshing the report data, reducing very large pages, and testing again.', [])
      ], [])
    ]
  },
  {
    'title':'Templates, Themes & Media',
    'description':'Reuse report layouts and keep client-facing reports on brand.',
    'articles':[
      ('Use a template', 'Start from a reusable report layout.', [
        ('Templates help agencies avoid rebuilding the same report from scratch for every client.', []),
        ('Use a template when:', ['You report on the same service every month.','You want a standard layout for similar clients.','You want new team members to follow the same reporting structure.']),
        ('After applying a template, always review the data sources and widgets for the specific client.', [])
      ], []),
      ('Create or update a template', 'Save a report structure for future use.', [
        ('A good template should be generic enough to reuse and specific enough to save time.', []),
        ('Before saving a template:', ['Remove client-specific notes that should not appear elsewhere.','Use clear page and widget names.','Check that the layout works for different clients.','Keep only the widgets your team actually uses.']),
        ('Update templates when your reporting process changes, not every time one client needs a small custom edit.', [])
      ], []),
      ('Apply a theme', 'Control the look of client-facing reports.', [
        ('Themes help keep reports consistent with your agency or client brand.', []),
        ('A theme may control colours, fonts, logo treatment, and other visual details depending on your setup.', []),
        ('After applying a theme, preview the report to make sure text is readable, charts still have enough contrast, and the logo appears correctly.', [])
      ], []),
      ('Upload and manage media', 'Use logos and images in reports.', [
        ('Media files can support report branding, client context, and visual explanations.', []),
        ('Best practices:', ['Use clear file names.','Avoid uploading huge images if a smaller version works.','Keep client logos organized.','Remove media that is no longer used.']),
        ('If an image does not appear in a report, check that it was uploaded successfully and that the report page has been refreshed.', [])
      ], []),
      ('Troubleshoot branding not showing', 'What to check when logos, themes, or domains look wrong.', [
        ('Branding issues usually come from the wrong theme, cached previews, missing media, or domain setup.', []),
        ('Check:', ['Is the correct theme applied to the report or client?','Is the logo uploaded and visible in settings?','Does the shared report link use the correct domain?','Have you refreshed the report after making branding changes?']),
        ('If a custom domain is involved, also check the domain status.', [])
      ], [])
    ]
  },
  {
    'title':'Automations & Email Delivery',
    'description':'Schedule report delivery and troubleshoot automated sends.',
    'articles':[
      ('Schedule report delivery', 'Send reports automatically on a recurring schedule.', [
        ('An automation sends a report to selected recipients on a schedule, such as daily, weekly, or monthly.', []),
        ('Before creating one:', ['Make sure the report is complete.','Check the date range and widgets.','Confirm recipient email addresses.','Choose the right sender and subject line.','Decide whether to include a PDF attachment.']),
        ('Always test an automation before relying on it for client delivery.', [])
      ], []),
      ('Test an automation', 'Send a report immediately to confirm it works.', [
        ('Testing an automation lets you check what the client will receive without waiting for the next scheduled send.', []),
        ('When testing, confirm:', ['The email arrives.','The subject and message are correct.','The report link opens.','The PDF, if attached, looks right.','The sender name and branding are acceptable.']),
        ('If the test fails, fix it before activating the schedule.', [])
      ], []),
      ('Pause or resume an automation', 'Temporarily stop or restart scheduled delivery.', [
        ('Pause an automation when a client is on hold, a report is being rebuilt, or data needs to be checked before the next send.', []),
        ('Resuming an automation should restart future scheduled sends. It should not send missed reports automatically unless the app clearly says it will.', []),
        ('After resuming, check the next scheduled send time.', [])
      ], []),
      ('Troubleshoot failed scheduled reports', 'What to check when an automated report does not send correctly.', [
        ('Start with the basics:', ['Is the automation active?','Is the schedule set to the expected timezone?','Are recipients valid?','Does the report open manually?','Do all widgets load?','Is the sending email setup complete?']),
        ('If the report opens manually but automation fails, check the automation history and email setup. If the report itself fails, troubleshoot the report or data source first.', [])
      ], []),
      ('Set up branded email sending', 'Send report emails from your agency identity.', [
        ('Branded email sending helps client reports feel like they come from your agency instead of a generic system sender.', []),
        ('Before using a branded sender:', ['Add the sending email or domain in email settings.','Complete any verification steps shown in Oviond.','Send a test email.','Check spam/junk placement if the email does not arrive.']),
        ('If verification is incomplete, use a verified sender until the domain is ready.', [])
      ], [])
    ]
  },
  {
    'title':'White Label & Sharing',
    'description':'Use your own brand, domains, and client-facing links.',
    'articles':[
      ('What white label means in Oviond', 'Understand branded client reporting.', [
        ('White label means your clients can experience reports under your agency’s brand instead of Oviond’s brand.', []),
        ('This can include report themes, logos, colours, custom domains, and branded email sending depending on your setup.', []),
        ('Before sending reports to clients, preview them as the client would see them.', [])
      ], []),
      ('Set up a custom domain', 'Use your own domain for shared reports.', [
        ('A custom domain lets shared report links use a branded domain controlled by your agency.', []),
        ('Typical setup:', ['Add the domain in Oviond.','Follow the DNS instructions shown in the app.','Wait for DNS changes to update.','Check the domain status in Oviond.','Test a shared report link on the domain.']),
        ('DNS changes can take time. If the domain does not verify immediately, wait and check again.', [])
      ], []),
      ('Check custom domain status', 'Know whether a branded domain is ready.', [
        ('Use the domain status check after adding or changing DNS records.', []),
        ('Common statuses:', ['Pending: DNS may not be updated yet.','Needs attention: records may be missing or incorrect.','Active or verified: the domain is ready to use.']),
        ('If the domain is still pending after DNS has had time to update, compare the records in your DNS provider with the records shown in Oviond.', [])
      ], []),
      ('Remove a custom domain', 'Stop using a domain for shared reports.', [
        ('Warning: removing a custom domain can affect client-facing links that use that domain.', []),
        ('Before removing a domain:', ['Confirm no active clients rely on it.','Update shared links if needed.','Tell your team which domain should be used instead.','Keep DNS records until you are sure the transition is complete.']),
        ('If in doubt, add the replacement domain and test it before removing the old one.', [])
      ], []),
      ('Share links safely', 'Best practices before sending report links to clients.', [
        ('Before sending a report link:', ['Open it yourself.','Check branding.','Check date ranges.','Confirm all widgets load.','Make sure the link is for the right client.']),
        ('Avoid reusing links across clients. A report link should only be sent to people who are meant to see that report.', []),
        ('If a client says a link does not work, test the link in a private browser window first.', [])
      ], [])
    ]
  },
  {
    'title':'Team, Account & Billing',
    'description':'Manage users, company settings, usage, billing, and account safety.',
    'articles':[
      ('Invite a team member', 'Add another person to your Oviond account.', [
        ('Invite team members when someone needs to help manage clients, reports, data sources, or account settings.', []),
        ('Before inviting someone:', ['Use their correct work email address.','Choose the right role or permission level.','Limit access if the person should only work on specific clients.','Ask them to accept the invitation from their email.']),
        ('If an invitation is not received, ask the user to check spam/junk and confirm the email address.', [])
      ], []),
      ('User roles and permissions', 'Control what team members can access.', [
        ('Permissions help protect client data and account settings.', []),
        ('Use the least access that still lets the person do their job.', ['Admins should be limited to trusted account managers or operators.','Reporting users may only need access to clients and projects.','Read-only access is best for people who need to review but not edit.']),
        ('Review user access regularly, especially when team members leave or change roles.', [])
      ], []),
      ('Update company settings', 'Keep your agency information current.', [
        ('Company settings can affect branding, defaults, and account-level details.', []),
        ('Keep these details current:', ['Company name','Website','Logo','Timezone','Default branding settings','Contact details where applicable']),
        ('After major company setting changes, preview a shared report to make sure client-facing branding still looks right.', [])
      ], []),
      ('View usage and plan limits', 'Understand how much of your account limit is being used.', [
        ('Usage shows how your account is tracking against plan limits such as clients, users, projects, or other included resources.', []),
        ('Check usage when:', ['You are close to adding many clients.','A user cannot create something new.','You are reviewing your subscription.','You are preparing for a migration or account cleanup.']),
        ('If something looks wrong, compare the usage page with your actual active clients and users before changing your plan.', [])
      ], []),
      ('Billing, invoices, and subscription help', 'Where to check billing details.', [
        ('Use the billing area to review subscription status, invoices, payment details, and plan information.', []),
        ('For billing questions, collect:', ['Account email','Company name','Invoice date or invoice number','What changed or what you expected to happen']),
        ('Do not share full card numbers or sensitive payment information in support messages.', [])
      ], [])
    ]
  },
  {
    'title':'Troubleshooting',
    'description':'Quick fixes for common account, report, data, and delivery issues.',
    'articles':[
      ('I cannot log in', 'Basic checks when sign-in fails.', [
        ('If you cannot log in, try these checks first:', ['Make sure you are using the correct email address.','Reset your password if needed.','If you were invited by an agency, use the invitation email.','Check whether your account admin removed or changed your access.','Try a private browser window to rule out browser cache issues.']),
        ('If the problem continues, contact support with the email address you are trying to use and any error message shown.', [])
      ], []),
      ('My integration account is not appearing', 'Why a platform account may not show after connecting.', [
        ('This usually means the login used during authorization does not have access to the account you expected.', []),
        ('Check:', ['Did you log in with the right platform user?','Does that user have access to the ad account, page, property, or profile?','Is the account under a manager account that may take time to load?','Did you accidentally authorize a personal account instead of an agency account?']),
        ('If needed, disconnect the wrong authorization and reconnect using the correct login.', [])
      ], []),
      ('Widgets are empty or showing zero', 'What to check when report data looks blank.', [
        ('Empty widgets are usually caused by date range, account selection, permissions, or genuinely missing platform data.', []),
        ('Check:', ['The widget date range.','The selected data source.','The selected campaign, page, property, or profile.','Whether the platform account has data for that date range.','Whether other widgets using the same connection work.']),
        ('If every widget from one platform is blank, test or reconnect the data source.', [])
      ], []),
      ('A report link is not working', 'Fix a broken or inaccessible shared report link.', [
        ('First, open the link in a private browser window. This shows what a client sees without your logged-in session.', []),
        ('Check:', ['The report still exists.','Sharing is enabled.','The custom domain, if used, is active.','The report loads inside Oviond.','The link was copied fully and not shortened incorrectly.']),
        ('If the link belongs to the wrong client or old report, generate a fresh share link.', [])
      ], []),
      ('PDF export or email delivery failed', 'Common checks for export and delivery problems.', [
        ('If a PDF or report email fails, first confirm the report itself opens and all widgets load.', []),
        ('Then check:', ['Very large report pages or wide tables.','Missing or broken images.','Invalid recipient email addresses.','Unverified branded sender settings.','Automation status and schedule.']),
        ('Run a manual test after fixing the issue before sending to a client.', [])
      ], [])
    ]
  }
]

def text_node(text, marks=None):
    node={'type':'text','text':text}
    if marks: node['marks']=marks
    return node

def paragraph(text):
    return {'type':'paragraph','content':[text_node(text)]} if text else {'type':'paragraph'}

def heading(text, level=2):
    return {'type':'heading','attrs':{'level':level},'content':[text_node(text)]}

def bullet(items):
    return {'type':'bulletList','content':[{'type':'listItem','content':[paragraph(x)]} for x in items]}

def build_doc(blocks, bullets):
    content=[]
    first=True
    for text, items in blocks:
        if text.lower().startswith('warning:'):
            content.append(heading('Important',2)); content.append(paragraph(text))
        else:
            content.append(paragraph(text))
        if items:
            content.append(bullet(items))
    if bullets:
        content.append(heading('Related terms',2)); content.append(bullet(bullets))
    return {'type':'doc','content':content}

def plain(blocks, bullets):
    out=[]
    for text, items in blocks:
        out.append(text)
        for item in items: out.append('- '+item)
    if bullets:
        out.append('Related terms: '+', '.join(bullets))
    return '\n'.join(out)

def arr(payload):
    if isinstance(payload,list): return payload
    if isinstance(payload,dict):
        for k in ('collections','articles','items','data','results'):
            if isinstance(payload.get(k),list): return payload[k]
    return []

def title_en(obj):
    t=obj.get('title') or {}
    return t.get('en') if isinstance(t,dict) else str(t)

def create_or_get_collection(title, description):
    cols=arr(gleap_request('GET','/helpcenter/collections/all',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
    for c in cols:
        if title_en(c)==title:
            return c
    payload={'title':{'en':title},'description':{'en':description},'iconUrl':'','targetAudience':'all'}
    return gleap_request('POST','/helpcenter/collections',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE,data=payload)

created={'collections':[], 'articles':[], 'skipped_articles':[]}
for col in HELP_CENTER:
    c=create_or_get_collection(col['title'], col['description'])
    cid=c.get('id') or c.get('_id')
    created['collections'].append({'id':cid,'title':col['title']})
    existing=arr(gleap_request('GET',f'/helpcenter/collections/{cid}/articles',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
    existing_titles={title_en(a) for a in existing}
    for title, desc, blocks, terms in col['articles']:
        pc=plain(blocks, terms)
        dis=[d for d in DISALLOWED if d in (title+' '+desc+' '+pc).lower()]
        if dis:
            raise SystemExit(f'Disallowed public term(s) in {title}: {dis}')
        if title in existing_titles:
            created['skipped_articles'].append({'collection':col['title'],'title':title})
            continue
        payload={
            'title':{'en':title},
            'description':{'en':desc},
            'content':{'en':build_doc(blocks, terms)},
            'plainContent':{'en':pc},
            'isDraft':False,
            'tags':['launch-mvp']
        }
        a=gleap_request('POST',f'/helpcenter/collections/{cid}/articles',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE,data=payload)
        aid=a.get('id') or a.get('_id')
        created['articles'].append({'id':aid,'collection':col['title'],'title':title})
        time.sleep(0.05)

# verify
cols=arr(gleap_request('GET','/helpcenter/collections/all',api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
verify=[]; total=0
for c in cols:
    arts=arr(gleap_request('GET',f"/helpcenter/collections/{c.get('id') or c.get('_id')}/articles",api_key=API_KEY,project_id=PROJECT_ID,base_url=BASE))
    verify.append({'id':c.get('id') or c.get('_id'),'title':title_en(c),'articles':len(arts)})
    total+=len(arts)
summary={'collections':len(cols),'articles':total,'created':created,'verify':verify}
(OUT/'gleap-help-center-launch-mvp-summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False))
(OUT/'gleap-help-center-launch-mvp-plan.json').write_text(json.dumps(HELP_CENTER,indent=2,ensure_ascii=False))
print(json.dumps({'collections':len(cols),'articles':total,'created_articles':len(created['articles']),'skipped_articles':len(created['skipped_articles']),'verify':verify}, indent=2, ensure_ascii=False))
