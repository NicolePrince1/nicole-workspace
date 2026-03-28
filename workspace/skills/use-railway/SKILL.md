---
name: use-railway
description: >
  Operate Railway infrastructure: create projects, provision services and
  databases, manage object storage buckets, deploy code, configure environments
  and variables, manage domains, troubleshoot failures, check status and metrics,
  and query Railway docs. Use this skill whenever the user mentions Railway,
  deployments, services, environments, buckets, object storage, build failures,
  or infrastructure operations, even if they don't say "Railway" explicitly.
---

# Use Railway

Use Railway's CLI and GraphQL API helper to operate projects, environments, services, deployments, variables, domains, and troubleshooting workflows.

## Railway resource model

Railway organizes infrastructure in a hierarchy:

- **Workspace** is the billing and team scope.
- **Project** is a collection of services under one workspace.
- **Environment** is an isolated configuration plane inside a project.
- **Service** is a single deployable unit inside a project.
- **Bucket** is an S3-compatible object storage resource inside a project.
- **Deployment** is a point-in-time release of a service in an environment.

Most CLI commands operate on linked project/environment/service context. Use `railway status --json` to inspect that context, and prefer explicit `--project`, `--environment`, and `--service` flags when possible.

## Parsing Railway URLs

Users often paste Railway dashboard URLs. Extract IDs before doing anything else:

```text
https://railway.com/project/<PROJECT_ID>/service/<SERVICE_ID>?environmentId=<ENV_ID>
https://railway.com/project/<PROJECT_ID>/service/<SERVICE_ID>
```

If the environment ID is missing and the user specifies an environment by name, resolve it via `scripts/railway-api.sh`.

Prefer passing explicit IDs to CLI commands instead of running `railway link` when acting on a specific pasted URL.

## Preflight

Before any mutation, verify context:

```bash
command -v railway
railway whoami --json
railway --version
```

Rules:
- If the user provides a Railway URL, prefer the IDs from that URL over local linked context.
- If the CLI is missing, install or guide the user to install it.
- If authentication is missing, run `railway login`.
- If the CLI seems outdated, run `railway upgrade`.

## Common quick operations

```bash
railway status --json
railway whoami --json
railway project list --json
railway service status --all --json
railway variable list --service <svc> --json
railway variable set KEY=value --service <svc>
railway logs --service <svc> --lines 200 --json
railway up --detach -m "<summary>"
railway bucket list --json
railway bucket info --bucket <name> --json
railway bucket credentials --bucket <name> --json
```

## Routing

Load only the reference that matches the task.

| Intent | Reference | Use for |
|---|---|---|
| Analyze a Railway database service | `references/analyze-db.md` | Database introspection and performance analysis |
| Create or connect resources | `references/setup.md` | Projects, services, databases, buckets, templates, workspaces |
| Ship code or manage releases | `references/deploy.md` | Deploy, redeploy, restart, build config, monorepo, Dockerfile |
| Change configuration | `references/configure.md` | Environments, variables, config patches, domains, networking |
| Check health or debug failures | `references/operate.md` | Status, logs, metrics, build/runtime triage, recovery |
| Request from API, docs, or community | `references/request.md` | GraphQL API queries/mutations, metrics queries, official docs |

## Execution rules

1. Prefer Railway CLI.
2. Fall back to `scripts/railway-api.sh` for operations the CLI doesn't expose.
3. Use `--json` output where available for reliable parsing.
4. Resolve project/environment/service context before mutation.
5. Confirm destructive actions before executing them.
6. After mutations, verify results with a read-back command.

## User-only commands

Do not execute commands that modify live database internals directly. If a workflow needs those, show the exact command, explain the side effects, and wait for the user to run it.

## Composition patterns

- **First deploy**: setup -> configure -> deploy -> operate
- **Fix a failure**: operate -> configure -> deploy -> operate
- **Add a domain**: configure -> operate
- **Add object storage**: setup -> configure

Return one unified response that covers action, result, and next step.
