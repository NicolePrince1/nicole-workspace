---
name: github-vercel-builder
description: Build and ship small web projects, landing pages, microsites, demos, and lightweight tools using a Codex ACP coding session pinned to openai-codex/gpt-5.4, then publish the result to GitHub and deploy it to Vercel. Use when a user wants a new little project delivered end-to-end with a testable URL. Best for static sites, marketing pages, small Next.js apps, MVPs, and simple internal tools. Not for one-line edits inside an existing repo, non-web projects with no Vercel target, or work that should remain local only.
---

# GitHub + Vercel Builder

Use this skill to take a web project from brief → files → GitHub repo → live Vercel URL.

## Defaults

Read `references/defaults.md` before publishing or deploying. It contains the current GitHub owner, Vercel scope, folder convention, and shipping defaults for this workspace.

## Safety rules

Ask before any of these:
- making the GitHub repo public
- touching a custom domain or DNS
- overwriting an existing production deployment on purpose
- adding paid third-party services or new secrets
- deleting or force-pushing an existing repo

Default to:
- private GitHub repos
- preview/shareable deployments unless the user explicitly wants production semantics
- simple stacks over clever stacks

## Project selection

Pick the lightest stack that can do the job:
- **Single landing page / brochure / splash page:** plain HTML/CSS/JS
- **Small interactive frontend:** Vite or static HTML first; only use React when it genuinely helps
- **App with routing / server needs / forms / auth / data fetching:** Next.js

Avoid overbuilding. A scary hello-world page does not need a full framework.

## Standard workflow

1. Choose a slug and create `projects/<slug>`.
2. Write a tiny `brief.md` in the project root with:
   - goal
   - audience
   - required pages
   - visual direction
   - launch assumptions
3. For substantial builds, spawn a Codex ACP session pinned to `openai-codex/gpt-5.4` with `runtime: "acp"`, `agentId: "codex"`, and `cwd` set to the project folder.
4. Build the project files.
5. Run the smallest sensible smoke test:
   - static site: open locally or inspect files
   - framework app: install deps, run build, fix obvious errors
6. Initialize git in the project folder if needed and make a clean commit.
7. Publish to GitHub.
8. Deploy to Vercel.
9. Return the repo URL and the live deployment URL.

## ACP spawn template

Use this shape for substantial implementation work:

```json
{
  "task": "Build the requested web project in the current cwd. Keep the stack minimal, finish the files, and leave the repo ready to publish and deploy.",
  "runtime": "acp",
  "agentId": "codex",
  "model": "openai-codex/gpt-5.4",
  "cwd": "/data/.openclaw/workspace/projects/<slug>",
  "mode": "run",
  "streamTo": "parent"
}
```

If ACP is unavailable, build directly in the current session and keep the same folder + publish/deploy workflow.

## Brief discipline

Do not start with a blank vibe-only prompt when the project matters. Capture at least:
- what the page/app must do
- what success looks like
- any required copy or CTA
- whether speed or polish matters more

If the user gives a loose brief, fill in reasonable defaults and move.

## Publishing and deploying

Use `scripts/publish_and_deploy.py` from this skill for the final shipping step. It is the deterministic part of the workflow.

Expected behavior:
- create or reuse the GitHub repo
- commit and push the project
- deploy the project directory to Vercel
- print machine-readable JSON with repo + deployment details

## Output standard

When finished, report:
- what you built
- stack used
- GitHub repo URL
- live Vercel URL
- any assumptions you made
- the next obvious improvement, if there is one
