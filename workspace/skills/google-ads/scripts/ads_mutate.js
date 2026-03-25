#!/usr/bin/env node
const fs = require('fs');
const {
  DEFAULTS,
  buildSuggestions,
  getDeveloperToken,
  printJson,
  mutate,
  resolveAccessToken,
  stripCustomerId,
  summarizeGoogleAdsError,
} = require('./lib/google_ads');

function parseArgs(argv) {
  const args = {
    customerId: DEFAULTS.customerId,
    loginCustomerId: DEFAULTS.loginCustomerId,
    apiVersion: DEFAULTS.apiVersion,
    validateOnly: true,
    partialFailure: true,
    responseContentType: 'MUTABLE_RESOURCE',
  };

  const positional = [];
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--customer-id') args.customerId = stripCustomerId(argv[++i]);
    else if (arg === '--login-customer-id') args.loginCustomerId = stripCustomerId(argv[++i]);
    else if (arg === '--api-version') args.apiVersion = argv[++i];
    else if (arg === '--validate-only') args.validateOnly = true;
    else if (arg === '--apply') args.validateOnly = false;
    else if (arg === '--partial-failure') args.partialFailure = true;
    else if (arg === '--no-partial-failure') args.partialFailure = false;
    else if (arg === '--response-content-type') args.responseContentType = argv[++i];
    else if (arg === '--help' || arg === '-h') args.help = true;
    else positional.push(arg);
  }

  args.resourceType = positional[0];
  args.operationsFile = positional[1];
  return args;
}

function usage() {
  return [
    'Usage: node ads_mutate.js <resourceType> <operations.json> [--validate-only|--apply]',
    '',
    'Examples:',
    '  node ads_mutate.js campaigns ./pause-campaign.json --validate-only',
    '  node ads_mutate.js campaignBudgets ./budget-change.json --apply',
    '',
    'Default mode is validate-only for safety.',
  ].join('\n');
}

(async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || !args.resourceType || !args.operationsFile) {
    process.stdout.write(`${usage()}\n`);
    if (!args.help) process.exit(1);
    return;
  }

  const operations = JSON.parse(fs.readFileSync(args.operationsFile, 'utf8'));
  const developerToken = getDeveloperToken();
  const tokenInfo = await resolveAccessToken();

  const response = await mutate({
    resourceType: args.resourceType,
    operations,
    customerId: args.customerId,
    loginCustomerId: args.loginCustomerId,
    token: tokenInfo.token,
    developerToken,
    apiVersion: args.apiVersion,
    validateOnly: args.validateOnly,
    partialFailure: args.partialFailure,
    responseContentType: args.responseContentType,
  });

  if (response.statusCode < 200 || response.statusCode >= 300 || response.body?.error) {
    const summary = summarizeGoogleAdsError(response);
    printJson({
      ok: false,
      mode: args.validateOnly ? 'validate-only' : 'apply',
      resourceType: args.resourceType,
      customerId: args.customerId,
      loginCustomerId: args.loginCustomerId,
      tokenSource: tokenInfo.source,
      error: summary,
      nextActions: buildSuggestions(summary, {
        customerId: args.customerId,
        loginCustomerId: args.loginCustomerId,
        serviceAccountEmail: tokenInfo.serviceAccount?.email,
        projectId: tokenInfo.serviceAccount?.projectId,
        projectNumber: tokenInfo.serviceAccount?.projectNumber,
      }),
    });
    process.exit(1);
  }

  printJson({
    ok: true,
    mode: args.validateOnly ? 'validate-only' : 'apply',
    resourceType: args.resourceType,
    customerId: args.customerId,
    loginCustomerId: args.loginCustomerId,
    tokenSource: tokenInfo.source,
    response: response.body,
  });
})().catch(error => {
  process.stderr.write(`${error.stack || error.message}\n`);
  process.exit(1);
});
