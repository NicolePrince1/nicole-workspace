#!/usr/bin/env python3
import argparse
import base64
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "OpenClaw github-vercel-builder"
IGNORE_PARTS = {".git", ".vercel", "node_modules", ".next", "dist", "build", "__pycache__"}
IGNORE_FILES = {".DS_Store"}


def eprint(*args):
    print(*args, file=sys.stderr)


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def http_json(method: str, url: str, token: str, payload=None):
    data = None
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
            return json.loads(raw.decode("utf-8")) if raw else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {url} failed with {exc.code}: {body}") from exc


def gh_request(method: str, path: str, payload=None):
    token = require_env("GITHUB_TOKEN")
    return http_json(method, f"https://api.github.com{path}", token, payload)


def vercel_request(method: str, path: str, payload=None, *, slug=None, extra_query=None):
    token = require_env("VERCEL")
    query = dict(extra_query or {})
    if slug:
        query["slug"] = slug
    url = f"https://api.vercel.com{path}"
    if query:
        url += "?" + urllib.parse.urlencode(query)
    return http_json(method, url, token, payload)


def run(cmd, cwd: Path):
    result = subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {' '.join(cmd)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result.stdout.strip()


def git_repo_exists(project_dir: Path) -> bool:
    return (project_dir / ".git").exists()


def ensure_git_repo(project_dir: Path, branch: str, git_name: str, git_email: str):
    if not git_repo_exists(project_dir):
        run(["git", "init", "-b", branch], project_dir)
    run(["git", "config", "user.name", git_name], project_dir)
    run(["git", "config", "user.email", git_email], project_dir)
    current_branch = run(["git", "branch", "--show-current"], project_dir) or branch
    if current_branch != branch:
        run(["git", "branch", "-M", branch], project_dir)


def ensure_commit(project_dir: Path, message: str):
    run(["git", "add", "-A"], project_dir)
    status = run(["git", "status", "--porcelain"], project_dir)
    if status:
        run(["git", "commit", "-m", message], project_dir)
    return run(["git", "rev-parse", "HEAD"], project_dir)


def github_viewer():
    return gh_request("GET", "/user")


def ensure_github_repo(owner: str, repo: str, private: bool, description: str):
    payload = {"name": repo, "private": private, "description": description, "auto_init": False}
    try:
        created = gh_request("POST", "/user/repos", payload)
        return created.get("html_url") or f"https://github.com/{owner}/{repo}", created.get("clone_url") or f"https://github.com/{owner}/{repo}.git"
    except RuntimeError as exc:
        if " 422:" not in str(exc):
            raise
        existing = gh_request("GET", f"/repos/{owner}/{repo}")
        return existing.get("html_url") or f"https://github.com/{owner}/{repo}", existing.get("clone_url") or f"https://github.com/{owner}/{repo}.git"


def push_to_github(project_dir: Path, owner: str, repo: str, branch: str):
    token = require_env("GITHUB_TOKEN")
    clean_url = f"https://github.com/{owner}/{repo}.git"
    auth_url = f"https://x-access-token:{token}@github.com/{owner}/{repo}.git"
    remotes = run(["git", "remote"], project_dir).splitlines()
    if "origin" in remotes:
        run(["git", "remote", "set-url", "origin", clean_url], project_dir)
    else:
        run(["git", "remote", "add", "origin", clean_url], project_dir)
    try:
        run(["git", "remote", "set-url", "origin", auth_url], project_dir)
        run(["git", "push", "-u", "origin", branch], project_dir)
    finally:
        run(["git", "remote", "set-url", "origin", clean_url], project_dir)


def collect_files(project_dir: Path):
    files = []
    for path in sorted(project_dir.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(project_dir)
        if any(part in IGNORE_PARTS for part in rel.parts):
            continue
        if path.name in IGNORE_FILES:
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
            files.append({"file": rel.as_posix(), "data": text, "encoding": "utf-8"})
        except UnicodeDecodeError:
            files.append({
                "file": rel.as_posix(),
                "data": base64.b64encode(raw).decode("ascii"),
                "encoding": "base64",
            })
    if not files:
        raise RuntimeError("Project directory has no deployable files")
    return files


def create_vercel_deployment(project_name: str, project_dir: Path, team_slug: str, *, sha: str, repo_url: str, branch: str, git_name: str, git_email: str):
    payload = {
        "name": project_name,
        "public": True,
        "files": collect_files(project_dir),
        "projectSettings": {
            "framework": None,
            "buildCommand": None,
            "installCommand": None,
            "outputDirectory": None,
            "rootDirectory": None,
        },
        "gitMetadata": {
            "remoteUrl": repo_url,
            "commitAuthorName": git_name,
            "commitAuthorEmail": git_email,
            "commitMessage": "Initial deploy",
            "commitRef": branch,
            "commitSha": sha,
            "dirty": False,
        },
        "meta": {
            "githubCommitSha": sha,
            "githubRepo": repo_url,
            "source": "github-vercel-builder",
        },
    }
    return vercel_request(
        "POST",
        "/v13/deployments",
        payload,
        slug=team_slug,
        extra_query={"forceNew": 1, "skipAutoDetectionConfirmation": 1},
    )


def wait_for_vercel_ready(deployment_id: str, team_slug: str, timeout: int):
    deadline = time.time() + timeout
    last_state = None
    while time.time() < deadline:
        data = vercel_request("GET", f"/v13/deployments/{deployment_id}", slug=team_slug)
        state = data.get("readyState") or data.get("state") or "UNKNOWN"
        if state != last_state:
            eprint(f"vercel state: {state}")
            last_state = state
        if state == "READY":
            return data
        if state in {"ERROR", "CANCELED"}:
            raise RuntimeError(json.dumps(data, indent=2))
        time.sleep(2)
    raise RuntimeError(f"Deployment {deployment_id} did not become READY within {timeout}s")


def main():
    parser = argparse.ArgumentParser(description="Create/reuse a GitHub repo, push a project, and deploy it to Vercel.")
    parser.add_argument("project_dir")
    parser.add_argument("--repo-name", required=True)
    parser.add_argument("--project-name")
    parser.add_argument("--owner")
    parser.add_argument("--team-slug", default="nicoleprince1s-projects")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--private", dest="private", action="store_true", default=True)
    parser.add_argument("--public-repo", dest="private", action="store_false", help="Create or use a public GitHub repo instead of the default private repo")
    parser.add_argument("--description", default="")
    parser.add_argument("--git-name", default="Nicole")
    parser.add_argument("--git-email", default="nicole@oviond.com")
    parser.add_argument("--commit-message", default="Initial commit")
    parser.add_argument("--wait-seconds", type=int, default=180)
    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()
    if not project_dir.exists() or not project_dir.is_dir():
        raise SystemExit(f"Project directory does not exist: {project_dir}")

    viewer = github_viewer()
    owner = args.owner or viewer.get("login")
    if not owner:
        raise SystemExit("Could not determine GitHub owner from token")

    ensure_git_repo(project_dir, args.branch, args.git_name, args.git_email)
    sha = ensure_commit(project_dir, args.commit_message)
    repo_html_url, repo_clone_url = ensure_github_repo(owner, args.repo_name, args.private, args.description)
    push_to_github(project_dir, owner, args.repo_name, args.branch)

    deployment = create_vercel_deployment(
        args.project_name or args.repo_name,
        project_dir,
        args.team_slug,
        sha=sha,
        repo_url=repo_clone_url,
        branch=args.branch,
        git_name=args.git_name,
        git_email=args.git_email,
    )
    deployment_id = deployment.get("id")
    if not deployment_id:
        raise RuntimeError(json.dumps(deployment, indent=2))
    ready = wait_for_vercel_ready(deployment_id, args.team_slug, args.wait_seconds)
    url = ready.get("url") or deployment.get("url")
    final_url = f"https://{url}" if url and not str(url).startswith("http") else url

    result = {
        "github": {
            "owner": owner,
            "repo": args.repo_name,
            "url": repo_html_url,
            "branch": args.branch,
            "commit": sha,
            "private": args.private,
        },
        "vercel": {
            "teamSlug": args.team_slug,
            "deploymentId": deployment_id,
            "url": final_url,
            "readyState": ready.get("readyState") or ready.get("state"),
            "projectId": ready.get("projectId"),
            "public": ready.get("public", deployment.get("public")),
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
