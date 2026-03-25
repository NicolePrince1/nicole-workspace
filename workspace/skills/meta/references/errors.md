# Meta error guide

## Invalid OAuth 2.0 Access Token

Meaning:
- You used the system-user token directly against a Page endpoint that expects a page access token, or the token is invalid.

Fix:
- Fetch a page token first from `/{page_id}?fields=access_token` using the system token.
- Then call Page endpoints with the page token.
- `meta_doctor.py` does this automatically.

## (#100) Invalid insights metric

Meaning:
- The metric name is stale, not valid for the object, or requires a different request shape.

Fix:
- Prefer the bundled reporting scripts instead of inventing raw insights metric names.
- If using raw Graph calls, verify the metric against the current API docs for the exact object type.

## Validation errors on writes

Meaning:
- The JSON spec is missing required params, has the wrong enum value, or nests JSON incorrectly.

Fix:
- Use `meta_mutate.py preview` first.
- Then run `meta_mutate.py validate` when the operation supports it.
- Keep nested objects inside `params` as real JSON; the script serializes them for Graph.

## Data looks inconsistent

Meaning:
- You may be mixing objectives, time windows, or action definitions.

Fix:
- Re-run the report with one explicit primary action type.
- Check `action-types` output first when custom conversions are involved.
- Avoid calling link clicks and LPVs the same thing.
