#!/usr/bin/env node
const { execFileSync } = require('child_process');

function parseArgs(argv) {
  const args = { json: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--container-path') args.containerPath = argv[++i];
    else if (a === '--workspace-path') args.workspacePath = argv[++i];
    else if (a === '--json') args.json = true;
    else if (a === '--help' || a === '-h') args.help = true;
  }
  return args;
}

function run(apiPath) {
  const out = execFileSync('node', [__dirname + '/gtm_request.js', 'GET', apiPath, '--json'], { encoding: 'utf8' });
  const parsed = JSON.parse(out);
  if (!parsed.ok) throw new Error(JSON.stringify(parsed.body));
  return parsed.body || {};
}

function usage() {
  return 'Usage: node gtm_audit.js --container-path accounts/123/containers/456 [--json]\n   or: node gtm_audit.js --workspace-path accounts/123/containers/456/workspaces/7 [--json]';
}

(async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || (!args.containerPath && !args.workspacePath)) { console.log(usage()); return; }
  const base = args.workspacePath || args.containerPath;
  const scope = args.workspacePath ? 'workspace' : 'container';
  const endpoints = scope === 'workspace'
    ? ['tags', 'triggers', 'variables', 'folders', 'built_in_variables', 'templates']
    : ['workspaces', 'versions'];
  const audit = { scope, path: base, generatedAt: new Date().toISOString(), resources: {} };
  for (const ep of endpoints) {
    try {
      const body = run(`/${base}/${ep}`);
      const key = Object.keys(body).find(k => Array.isArray(body[k])) || ep;
      audit.resources[ep] = { count: Array.isArray(body[key]) ? body[key].length : 0, items: body[key] || [] };
    } catch (error) {
      audit.resources[ep] = { error: error.message };
    }
  }
  if (args.json) console.log(JSON.stringify(audit, null, 2));
  else {
    console.log(`GTM audit: ${scope} ${base}`);
    for (const [name, value] of Object.entries(audit.resources)) {
      console.log(`- ${name}: ${value.error ? `error: ${value.error}` : value.count}`);
    }
  }
})().catch(err => { console.error(err.message); process.exit(1); });
