# GTM API Recipes

Use these with `gtm_request.js`.

## List accounts

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js GET /accounts
```

## List containers for an account

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js GET /accounts/123456/containers
```

## List workspaces for a container

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js GET /accounts/123456/containers/654321/workspaces
```

## Create a workspace

`workspace.json`

```json
{
  "name": "Hostname cleanup",
  "description": "Restrict GA4 firing to www.oviond.com only"
}
```

Dry run:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js POST /accounts/123456/containers/654321/workspaces ./workspace.json
```

Apply:

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js POST /accounts/123456/containers/654321/workspaces ./workspace.json --apply
```

## List tags in a workspace

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js GET /accounts/123456/containers/654321/workspaces/7/tags
```

## List triggers in a workspace

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js GET /accounts/123456/containers/654321/workspaces/7/triggers
```

## Update a tag

Prepare a full tag body from the existing object first. Then edit the changed fields.

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js PUT /accounts/123456/containers/654321/workspaces/7/tags/12 ./tag.json --apply
```

## Create a container version from a workspace

`version.json`

```json
{
  "name": "Restrict GA4 to www only",
  "notes": "Stops app host traffic from entering the marketing-site GA4 property."
}
```

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js POST /accounts/123456/containers/654321/workspaces/7:create_version ./version.json --apply
```

## Publish a container version

```bash
node /data/.openclaw/workspace/skills/google-tag-manager/scripts/gtm_request.js POST /accounts/123456/containers/654321/versions/33:publish --apply
```

## Notes

- Prefer creating a workspace before mutating live entities.
- Prefer updating existing entities from a fetched baseline rather than hand-writing a whole object from scratch.
- For non-GET requests, `gtm_request.js` requires `--apply`. Without it, the script stops before mutating anything.
