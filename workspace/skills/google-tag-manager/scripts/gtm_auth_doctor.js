#!/usr/bin/env node
const { execFileSync } = require('child_process');

const SCOPE = 'https://www.googleapis.com/auth/tagmanager.readonly';

function parseArgs(argv) {
  return { json: argv.includes('--json'), help: argv.includes('--help') || argv.includes('-h') };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    console.log('Usage: node gtm_auth_doctor.js [--json]\nChecks GTM read auth via Google Workspace service-account impersonation.');
    return;
  }
  const report = { ok: true, timestamp: new Date().toISOString(), authMode: 'google-workspace-service-account-impersonation', checks: [] };
  try {
    const token = execFileSync('node', ['/data/.openclaw/secrets/gws-token.js', SCOPE], { encoding: 'utf8' }).trim();
    report.checks.push({ name: 'Access token mint', ok: true, detail: `token length ${token.length}` });
    const res = await fetch('https://tagmanager.googleapis.com/tagmanager/v2/accounts', { headers: { Authorization: `Bearer ${token}` } });
    const body = await res.json().catch(async () => ({ raw: await res.text() }));
    report.checks.push({ name: 'GTM accounts list', ok: res.ok, status: res.status, count: Array.isArray(body.account) ? body.account.length : 0, body: res.ok ? undefined : body });
    if (!res.ok) report.ok = false;
  } catch (error) {
    report.ok = false;
    report.checks.push({ name: 'GTM auth', ok: false, error: error.message });
  }
  if (args.json) console.log(JSON.stringify(report, null, 2));
  else {
    for (const c of report.checks) console.log(`${c.ok ? '✅' : '❌'} ${c.name}${c.status ? ` (${c.status})` : ''}${c.detail ? ` — ${c.detail}` : ''}${c.count !== undefined ? ` — ${c.count} account(s)` : ''}`);
  }
  if (!report.ok) process.exit(1);
}

main();
