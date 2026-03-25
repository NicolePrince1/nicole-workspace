#!/usr/bin/env node
const fs = require('fs');
const {
  DEFAULTS,
  buildSuggestions,
  getDeveloperToken,
  printJson,
  resolveAccessToken,
  searchStream,
  stripCustomerId,
  summarizeGoogleAdsError,
} = require('./lib/google_ads');

function parseArgs(argv) {
  const args = {
    customerId: DEFAULTS.customerId,
    loginCustomerId: DEFAULTS.loginCustomerId,
    apiVersion: DEFAULTS.apiVersion,
    format: 'json',
    query: null,
    file: null,
    help: false,
  };

  const positional = [];
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--customer-id') args.customerId = stripCustomerId(argv[++i]);
    else if (arg === '--login-customer-id') args.loginCustomerId = stripCustomerId(argv[++i]);
    else if (arg === '--api-version') args.apiVersion = argv[++i];
    else if (arg === '--format') args.format = argv[++i];
    else if (arg === '--query') args.query = argv[++i];
    else if (arg === '--file') args.file = argv[++i];
    else if (arg === '--help' || arg === '-h') args.help = true;
    else positional.push(arg);
  }

  if (!args.query && !args.file && positional.length) {
    args.query = positional.join(' ');
  }

  return args;
}

function usage() {
  return [
    'Usage: node ads_query.js "SELECT ..."',
    '   or: node ads_query.js --file ./query.sql [--customer-id 2906154258] [--login-customer-id 6387956297] [--format json|pretty]',
    '',
    'Runs a Google Ads GAQL query using searchStream so larger reports do not require manual pagination.',
  ].join('\n');
}

function renderPretty(results) {
  return results.map((row, index) => `${index + 1}. ${JSON.stringify(row)}`).join('\n');
}

(async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    process.stdout.write(`${usage()}\n`);
    return;
  }

  const query = args.query || (args.file ? fs.readFileSync(args.file, 'utf8') : '').trim();
  if (!query) {
    process.stderr.write(`${usage()}\n`);
    process.exit(1);
  }

  const developerToken = getDeveloperToken();
  const tokenInfo = await resolveAccessToken();
  const result = await searchStream({
    query,
    customerId: args.customerId,
    loginCustomerId: args.loginCustomerId,
    token: tokenInfo.token,
    developerToken,
    apiVersion: args.apiVersion,
  });

  if (result.response.statusCode < 200 || result.response.statusCode >= 300) {
    const summary = summarizeGoogleAdsError(result.response);
    const payload = {
      ok: false,
      query,
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
    };
    printJson(payload);
    process.exit(1);
  }

  const payload = {
    ok: true,
    query,
    customerId: args.customerId,
    loginCustomerId: args.loginCustomerId,
    tokenSource: tokenInfo.source,
    totalRows: result.results.length,
    totalBatches: result.batches.length,
    fieldMask: result.fieldMask,
    results: result.results,
  };

  if (args.format === 'pretty') {
    process.stdout.write(`Rows: ${payload.totalRows}\n`);
    process.stdout.write(`${renderPretty(payload.results)}\n`);
  } else {
    printJson(payload);
  }
})().catch(error => {
  process.stderr.write(`${error.stack || error.message}\n`);
  process.exit(1);
});
