#!/usr/bin/env node
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const API_ROOT = 'https://tagmanager.googleapis.com/tagmanager/v2';
const READONLY_SCOPE = 'https://www.googleapis.com/auth/tagmanager.readonly';
const WRITE_SCOPES = [
  'https://www.googleapis.com/auth/tagmanager.readonly',
  'https://www.googleapis.com/auth/tagmanager.edit.containers',
  'https://www.googleapis.com/auth/tagmanager.edit.containerversions',
  'https://www.googleapis.com/auth/tagmanager.publish',
  'https://www.googleapis.com/auth/tagmanager.manage.accounts',
];

function usage() {
  return [
    'Usage: node gtm_request.js METHOD /path [body.json|inline-json] [--apply] [--json]',
    '',
    'GET requests run read-only. Non-GET requests require --apply.',
    'Auth: Google Workspace service-account impersonation via /data/.openclaw/secrets/gws-token.js.',
  ].join('\n');
}

function parseArgs(argv) {
  const args = { apply: false, json: false };
  const positional = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--apply') args.apply = true;
    else if (a === '--json') args.json = true;
    else if (a === '--help' || a === '-h') args.help = true;
    else positional.push(a);
  }
  args.method = (positional[0] || '').toUpperCase();
  args.apiPath = positional[1];
  args.bodyArg = positional[2];
  return args;
}

function getToken(scopes) {
  const helper = '/data/.openclaw/secrets/gws-token.js';
  return execFileSync('node', [helper, scopes.join(',')], { encoding: 'utf8' }).trim();
}

function readBody(bodyArg) {
  if (!bodyArg) return undefined;
  const candidate = path.resolve(process.cwd(), bodyArg);
  if (fs.existsSync(candidate)) return fs.readFileSync(candidate, 'utf8');
  return bodyArg;
}

async function request({ method, apiPath, bodyArg, apply }) {
  if (!method || !apiPath) throw new Error(usage());
  if (!apiPath.startsWith('/')) throw new Error('API path must start with /, e.g. /accounts');
  if (method !== 'GET' && !apply) {
    return {
      dryRun: true,
      ok: true,
      message: 'Non-GET request blocked. Re-run with --apply after reviewing target and body.',
      method,
      path: apiPath,
      bodyPreview: bodyArg ? readBody(bodyArg).slice(0, 4000) : null,
    };
  }

  const scopes = method === 'GET' ? [READONLY_SCOPE] : WRITE_SCOPES;
  const token = getToken(scopes);
  const bodyText = method === 'GET' ? undefined : readBody(bodyArg);
  const res = await fetch(API_ROOT + apiPath, {
    method,
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: bodyText,
  });
  const text = await res.text();
  let body;
  try { body = text ? JSON.parse(text) : null; } catch { body = text; }
  return { ok: res.ok, status: res.status, method, path: apiPath, body };
}

(async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) { console.log(usage()); return; }
  try {
    const result = await request(args);
    if (args.json) console.log(JSON.stringify(result, null, 2));
    else if (result.dryRun) console.log(JSON.stringify(result, null, 2));
    else if (result.body && typeof result.body === 'object') console.log(JSON.stringify(result.body, null, 2));
    else console.log(result.body || '');
    if (!result.ok) process.exit(1);
  } catch (err) {
    console.error(err.message || err);
    process.exit(1);
  }
})();
