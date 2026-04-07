#!/usr/bin/env python3
import argparse
import base64
import json
import subprocess
import sys
import urllib.request
from email.message import EmailMessage
from pathlib import Path

TOKEN_HELPER = "/data/.openclaw/secrets/gws-token.js"
DEFAULT_FROM = "nicole@oviond.com"


def get_token():
    proc = subprocess.run(
        ["node", TOKEN_HELPER, "gmail.send"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr or "Failed to mint Gmail access token\n")
        sys.exit(proc.returncode or 1)
    token = proc.stdout.strip()
    if not token:
        sys.stderr.write("Token helper returned an empty token\n")
        sys.exit(1)
    return token


def build_message(sender, to, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    return raw


def send_message(token, raw_message):
    data = json.dumps({"raw": raw_message}).encode("utf-8")
    req = urllib.request.Request(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Send a plain-text Gmail message via the Workspace service-account helper")
    parser.add_argument("--to", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--from-address", default=DEFAULT_FROM)
    args = parser.parse_args()

    body = Path(args.body_file).read_text(encoding="utf-8")
    token = get_token()
    raw = build_message(args.from_address, args.to, args.subject, body)
    result = send_message(token, raw)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
