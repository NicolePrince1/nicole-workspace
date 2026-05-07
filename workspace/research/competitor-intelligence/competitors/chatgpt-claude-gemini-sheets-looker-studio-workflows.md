# ChatGPT / Claude / Gemini + Sheets / Looker Studio workflows

Last verified: 2026-05-07
Priority: Tier 1
Category: AI/DIY workflow threat
Source category: [AI-native and agentic analytics threats](../categories/ai-native-threats.md)

---

## Threat type 1: ChatGPT / Claude / Gemini + Sheets / Looker Studio workflows

### Positioning

- **ChatGPT**: broad work assistant with file analysis, charts, connected apps, and custom GPT/app workflows. Business pricing copy says ChatGPT Business includes “60+ apps” such as Google Drive, SharePoint, Slack, GitHub, Atlassian, plus data analysis, canvas, shared projects, and custom workspace GPTs. Source: https://chatgpt.com/pricing/
- **Claude**: broad reasoning assistant with Projects, connectors, custom MCP connectors, and interactive connector surfaces. Claude positions connectors as a way for Claude to access apps/services, retrieve data, and take actions with inherited permissions. Source: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- **Gemini + Google Workspace**: AI embedded into Sheets, Docs, Gmail, Drive, and Looker ecosystem. Gemini in Sheets can create tables/formulas, generate analysis and insights, build charts, summarize Drive/Gmail context, and perform spreadsheet actions. Source: https://support.google.com/docs/answer/14218565
- **Looker Studio + Sheets**: not AI-native by itself, but free/low-cost dashboards plus Sheets as a staging layer remain the cheapest reporting stack. Gemini/ChatGPT/Claude supply the missing insight narrative.

### Pricing

- ChatGPT Business pricing page shows per-user monthly pricing but extraction did not expose the exact current number; Business includes apps/connectors and data analysis. Source: https://chatgpt.com/pricing/
- Claude pricing page is available at https://claude.com/pricing but extraction was mostly blocked; connector support is documented for Pro/Max/Team/Enterprise flows. Source: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- Google Workspace includes Gemini AI in Business plans. Fetched EU pricing showed Business Starter/Standard/Plus at €6.80/€13.60/€21.10 per user/month standard list after promo, with Gemini in Gmail on Starter and fuller Gemini in Docs/Meet/more on Standard+. Source: https://workspace.google.com/pricing.html

### Capabilities

- **File analysis**: ChatGPT supports spreadsheets (.xls, .xlsx, .csv), PDFs, JSON/XML/YAML/TXT/MD; can summarize trends/outliers, create tables/charts, run Python calculations, and explain assumptions. Source: https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt
- **Connected sources**: ChatGPT supports connected files from Google Drive, OneDrive, and SharePoint when available. Apps capabilities include interactive, search, deep research, sync/write, and custom MCP by plan. Source: https://help.openai.com/en/articles/11487775
- **Claude connectors/MCP**: Claude connectors can retrieve data and take actions in external services; custom connectors use remote MCP servers reachable from Anthropic cloud; Team/Enterprise owners can restrict actions. Sources: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities and https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- **Gemini in Sheets**: can generate analysis, charts, pivot tables, formulas, conditional formatting, sorting/filtering, and action preview cards. Source: https://support.google.com/docs/answer/14218565

### Data connection model

- Upload files manually; attach files from Drive/OneDrive/SharePoint; use Google Sheets as the live data table; use Looker Studio dashboards connected to Sheets/marketing connectors; use MCP/custom connectors for live app access.
- Weakness: most workflows are not a durable client-reporting system. They lack client portals, white-label delivery, scheduled client-safe snapshots, permissioned multi-client management, and consistent metric definitions unless an operator builds discipline around them.

### API/MCP/agent posture

- ChatGPT now explicitly supports custom MCP capabilities on higher plans and apps/connectors across plans. Source: https://help.openai.com/en/articles/11487775
- Claude is the strongest MCP-native posture: Anthropic created MCP, supports local/remote/custom connectors, and allows interactive connector surfaces. Source: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- Gemini benefits from Google-owned Workspace/GA/Ads context and official GA MCP/Gemini CLI examples.

### Reporting-output quality

- Strong for **ad hoc explanations, commentary drafts, variance summaries, and quick charts**.
- Weak for **repeatable, branded, client-ready reporting** unless the agency has a stable data pipeline and review process.
- Hallucination/incorrect method risk remains material. OpenAI explicitly recommends reviewing generated code, outputs, and assumptions before relying on analysis. Source: https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt

### Strengths

- Already adopted by agency teams; near-zero switching friction.
- Excellent narrative summary and client-commentary drafting.
- Fast for messy one-off questions.
- Good enough for small clients who only need a monthly explanation, not a portal.

### Weaknesses / adoption friction for agencies

- Requires manual data prep or third-party connectors.
- Hard to maintain client segregation and repeatable templates.
- Outputs need human QA.
- Client-facing sharing is awkward: a chat transcript is not a branded report.
- Permissions and privacy concerns increase with connected apps/MCP.

### What Oviond must defend

- “Your client reporting system” rather than “another place to ask questions.”
- Multi-client setup, white-label presentation, stable scheduled reports, repeatable KPIs, permissioning, and agency-grade delivery.
- Make the monthly report easier than exporting data to Sheets and prompting an AI assistant.

### How Oviond can use API/MCP without sounding hypey

- Public language: “Connect your reporting workflow to the tools you already use.”
- Product language: “Use Oviond data in your internal automations,” “Ask questions across client reporting data,” “Generate report commentary from approved metrics,” “Bring your reporting data into your AI assistant when you need it.”
- Avoid homepage hero claims like “agentic analytics platform.” Keep the hero on simple agency reporting.

---
