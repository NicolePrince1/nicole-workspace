---
name: oviond-docs
version: 0.1.0
description: Use this skill when writing, reviewing, or updating Oviond Mintlify documentation, including user guides, REST API reference, MCP docs, changelog entries, and troubleshooting content.
---

# Oviond docs skill

Use this skill to create and maintain Oviond’s Mintlify documentation.

## Product context

Oviond is a white-label marketing reporting platform for agencies.

Users use Oviond to:

- create clients
- connect marketing data sources
- build reports and dashboards
- share reports through branded links and custom domains
- automate client report delivery
- manage team access
- use REST API and MCP tools for agent-native reporting workflows

## Documentation goals

Every page should help a user or agent complete a real task with confidence.

Prioritize:

1. Correctness
2. Clarity
3. Consistency
4. Agent-readiness
5. Brevity

## Canonical terminology

- **Client**: A workspace for one client, store, profile, franchise branch, or reporting entity.
- **Project**: A container for a report or dashboard.
- **Report**: A paged project for client-ready reporting.
- **Dashboard**: A live, single-scroll project for ongoing monitoring.
- **Client project**: A project inside one client workspace.
- **Agency report**: An account-level project not tied to one client.
- **Widget**: A visual/content element inside a page.
- **Data source**: A connected marketing account/profile used in reports.
- **Integration**: An authorized connection to a platform.
- **API key**: Credential sent as a Bearer token for REST API calls.
- **MCP server**: Oviond’s remote Model Context Protocol server.

## Writing rules

- Use second person.
- Use active voice.
- Keep paragraphs to two sentences max.
- Lead with what/why before how.
- Put prerequisites before steps.
- Use sentence case headings.
- One concept per page.
- Link related pages instead of duplicating long explanations.
- Avoid filler phrases: just, simply, easily, obviously, leverage, robust, seamless, delve.

## Mintlify rules

Use Mintlify components where they improve clarity.

| Need | Use |
| --- | --- |
| Sequential instructions | `<Steps>` / `<Step>` |
| Destructive warning | `<Warning>` |
| Caveat | `<Note>` |
| Best practice | `<Tip>` |
| Related pages | `<CardGroup>` / `<Card>` |
| API params | `ParamField` or OpenAPI-generated params |
| Response fields | `ResponseField` or OpenAPI schema |
| Code | fenced code blocks with language |
| Language variants | `Tabs` |

## API reference rules

Every endpoint page must include:

- method and path
- auth requirement
- required permissions
- parameters
- request example
- success response example
- common errors
- side effects/warnings
- related endpoints

Use this placeholder:

```bash
Authorization: Bearer $OVIOND_API_KEY
```

Do not expose sample API specs or example APIs unrelated to Oviond.

Use OpenAPI-valid path params:

```diff
- /v1/clients/:id
+ /v1/clients/{id}
```

## MCP rules

MCP docs must explain:

- supported clients and versions where known
- remote streamable HTTP transport
- OAuth authorization
- user permission inheritance
- destructive action risks
- revocation
- audit trail/activity logs

Do not claim every MCP client supports remote HTTP/OAuth.

## Forbidden public implementation details

Avoid public docs mentions of internal implementation unless required for user setup:

- Supabase
- S3
- SQS
- Resend
- Vercel
- cron scheduler
- database rows/tables
- internal flags such as `account.onboarding`

Use user-facing language instead.

## Review checklist

Before finishing a docs change, check:

- [ ] Page has valid frontmatter title and description.
- [ ] Page has exactly one H1.
- [ ] H1 is specific.
- [ ] Terminology matches this skill.
- [ ] No internal/vendor leaks.
- [ ] No passive/run-on/generated-sounding prose.
- [ ] API examples match OpenAPI.
- [ ] Links are valid.
- [ ] Page is short enough for agents to parse reliably.
- [ ] Mintlify validation passes.

## Output format for audits

When auditing docs, output:

| Severity | File/Page | Issue | Suggested fix |
| --- | --- | --- | --- |
| Critical/High/Medium | path | exact issue | PR-ready diff or rewrite guidance |

Severity:

- **Critical**: blocks launch or damages trust immediately.
- **High**: should fix before launch.
- **Medium**: polish/follow-up.
