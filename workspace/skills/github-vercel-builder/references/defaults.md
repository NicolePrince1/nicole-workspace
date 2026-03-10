# Current defaults for github-vercel-builder

## Accounts and scope

- GitHub owner: `NicolePrince1`
- Vercel user: `nicoleprince1`
- Vercel default team slug: `nicoleprince1s-projects`

These were discovered from the current authenticated tokens and should be treated as the default publish/deploy targets unless the user asks otherwise.

## Folder convention

Create projects in:

- `projects/<slug>`

Keep each project self-contained.

Recommended minimum files for every project:
- `brief.md`
- app/source files
- `.gitignore`
- optional `README.md` if the repo needs handoff context

## Git defaults

- Default branch: `main`
- Default repo visibility: `private`
- Default commit message for first ship: `Initial commit`

## Deployment defaults

- Default deployment path: deploy the built project directory directly to Vercel via API
- Return a shareable URL after each deploy
- Prefer preview/shareable deployments for experiments
- Use production semantics only when the user explicitly wants that behavior

## Stack defaults

- Landing pages: static HTML/CSS/JS
- Simple tools: static first, then Vite if needed
- Full app behavior: Next.js

## Ask-before actions

Get approval before:
- public repos
- custom domains
- DNS changes
- paid integrations
- destructive repo rewrites
