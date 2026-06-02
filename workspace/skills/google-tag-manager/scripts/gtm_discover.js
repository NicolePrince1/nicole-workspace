#!/usr/bin/env node
const { execFileSync } = require('child_process');

function run(apiPath) {
  const out = execFileSync('node', [__dirname + '/gtm_request.js', 'GET', apiPath, '--json'], { encoding: 'utf8' });
  const parsed = JSON.parse(out);
  if (!parsed.ok) throw new Error(JSON.stringify(parsed.body));
  return parsed.body || {};
}

function parseArgs(argv) {
  return { json: argv.includes('--json') };
}

(async function main() {
  const args = parseArgs(process.argv.slice(2));
  const result = { accounts: [] };
  const accounts = run('/accounts').account || [];
  for (const account of accounts) {
    const accountEntry = { accountId: account.accountId, name: account.name, path: account.path, containers: [] };
    const containers = run(`/${account.path}/containers`).container || [];
    for (const container of containers) {
      const containerEntry = { containerId: container.containerId, name: container.name, publicId: container.publicId, usageContext: container.usageContext, path: container.path, workspaces: [] };
      const workspaces = run(`/${container.path}/workspaces`).workspace || [];
      containerEntry.workspaces = workspaces.map(w => ({ workspaceId: w.workspaceId, name: w.name, path: w.path }));
      accountEntry.containers.push(containerEntry);
    }
    result.accounts.push(accountEntry);
  }
  if (args.json) console.log(JSON.stringify(result, null, 2));
  else {
    for (const a of result.accounts) {
      console.log(`${a.name} — ${a.path}`);
      for (const c of a.containers) {
        console.log(`  ${c.name} (${c.publicId || 'no publicId'}) — ${c.path}`);
        for (const w of c.workspaces) console.log(`    workspace ${w.name} — ${w.path}`);
      }
    }
  }
})().catch(err => { console.error(err.message); process.exit(1); });
