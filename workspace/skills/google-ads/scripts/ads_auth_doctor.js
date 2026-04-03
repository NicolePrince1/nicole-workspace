#!/usr/bin/env node
const {
  DEFAULTS,
  buildSuggestions,
  getDeveloperToken,
  inspectCloudProject,
  listAccessibleCustomers,
  loadServiceAccount,
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
    authMode: DEFAULTS.authMode,
    json: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--customer-id') args.customerId = stripCustomerId(argv[++i]);
    else if (arg === '--login-customer-id') args.loginCustomerId = stripCustomerId(argv[++i]);
    else if (arg === '--api-version') args.apiVersion = argv[++i];
    else if (arg === '--auth-mode') args.authMode = argv[++i];
    else if (arg === '--json') args.json = true;
    else if (arg === '--help' || arg === '-h') args.help = true;
  }

  return args;
}

function usage() {
  return [
    'Usage: node ads_auth_doctor.js [--customer-id 2906154258] [--login-customer-id 6387956297] [--api-version v21] [--auth-mode auto|service-account|oauth-refresh-token] [--json]',
    '',
    'Diagnoses Google Ads auth using the configured developer token and account defaults.',
  ].join('\n');
}

function pushCheck(report, check) {
  report.checks.push(check);
  if (!check.ok) report.ok = false;
}

function formatCheck(check) {
  const mark = check.ok ? '✅' : '❌';
  const lines = [`${mark} ${check.name}: ${check.summary}`];
  if (check.detail) lines.push(`   ${check.detail}`);
  if (check.requestId) lines.push(`   requestId: ${check.requestId}`);
  return lines.join('\n');
}

(async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    process.stdout.write(`${usage()}\n`);
    return;
  }

  const report = {
    ok: true,
    timestamp: new Date().toISOString(),
    config: {
      customerId: args.customerId,
      loginCustomerId: args.loginCustomerId,
      apiVersion: args.apiVersion,
      authMode: args.authMode,
      developerTokenPresent: false,
    },
    auth: {
      source: null,
      resolvedAuthMode: null,
      serviceAccountEmail: null,
      serviceAccountPath: null,
      serviceAccountProjectId: null,
      serviceAccountProjectNumber: null,
      serviceAccountSubject: null,
      oauthClientId: null,
    },
    accessibleCustomerIds: [],
    checks: [],
    nextActions: [],
  };

  let developerToken;
  try {
    developerToken = getDeveloperToken();
    report.config.developerTokenPresent = true;
    pushCheck(report, {
      name: 'Developer token',
      ok: true,
      summary: `Present (length ${developerToken.length})`,
    });
  } catch (error) {
    pushCheck(report, {
      name: 'Developer token',
      ok: false,
      summary: error.message,
    });
    report.nextActions.push('Set GOOGLE_ADS_DEVELOPER_TOKEN before retrying.');
    if (args.json) {
      printJson(report);
    } else {
      process.stdout.write(`${formatCheck(report.checks[0])}\n`);
    }
    process.exit(1);
  }

  let tokenInfo;
  try {
    tokenInfo = await resolveAccessToken({ authMode: args.authMode });
    report.auth.source = tokenInfo.source;
    report.auth.resolvedAuthMode = tokenInfo.authMode || args.authMode;
    report.auth.serviceAccountEmail = tokenInfo.serviceAccount?.email || null;
    report.auth.serviceAccountPath = tokenInfo.serviceAccount?.path || null;
    report.auth.serviceAccountProjectId = tokenInfo.serviceAccount?.projectId || null;
    report.auth.serviceAccountProjectNumber = tokenInfo.serviceAccount?.projectNumber || null;
    report.auth.serviceAccountSubject = tokenInfo.serviceAccount?.subject || null;
    report.auth.oauthClientId = tokenInfo.oauthClient?.clientId || null;

    pushCheck(report, {
      name: 'Access token mint',
      ok: true,
      summary: `Succeeded via ${tokenInfo.source}`,
      detail: tokenInfo.serviceAccount
        ? `${tokenInfo.serviceAccount.email} (${tokenInfo.serviceAccount.projectId || 'unknown project'})${tokenInfo.serviceAccount.subject ? ` as ${tokenInfo.serviceAccount.subject}` : ''}`
        : tokenInfo.oauthClient
          ? `OAuth refresh-token flow via client ${tokenInfo.oauthClient.clientId}`
          : 'Using explicit GOOGLE_ADS_TOKEN override',
    });
  } catch (error) {
    pushCheck(report, {
      name: 'Access token mint',
      ok: false,
      summary: 'Failed to mint token',
      detail: error.message,
    });
    report.nextActions.push(
      args.authMode === 'oauth-refresh-token'
        ? 'Provide a full OAuth refresh-token config (client ID, client secret, refresh token) or switch auth mode before retrying.'
        : 'Fix the selected Google Ads auth configuration before testing Google Ads access again.'
    );

    if (args.json) {
      printJson(report);
    } else {
      process.stdout.write(`${report.checks.map(formatCheck).join('\n')}\n`);
      process.stdout.write(`\nNext actions:\n- ${report.nextActions.join('\n- ')}\n`);
    }
    process.exit(1);
  }

  if (tokenInfo.source === 'service-account' && report.auth.serviceAccountProjectId) {
    try {
      const { credentials } = loadServiceAccount();
      const cloudReport = await inspectCloudProject({
        credentials,
        projectId: report.auth.serviceAccountProjectId,
        projectNumber: report.auth.serviceAccountProjectNumber,
      });

      if (cloudReport.projectMetadata) {
        pushCheck(report, {
          name: 'Cloud project metadata',
          ok: cloudReport.projectMetadata.ok,
          summary: cloudReport.projectMetadata.summary.message || 'Unable to read Cloud project metadata',
          detail: cloudReport.projectMetadata.ok
            ? report.auth.serviceAccountProjectId
            : cloudReport.projectMetadata.summary.reason || null,
        });
      }

      if (cloudReport.googleAdsApiService) {
        pushCheck(report, {
          name: 'Google Ads API service state',
          ok: cloudReport.googleAdsApiService.ok,
          summary: cloudReport.googleAdsApiService.summary.message || 'Unable to inspect googleads.googleapis.com state',
          detail: cloudReport.googleAdsApiService.ok
            ? report.auth.serviceAccountProjectId
            : cloudReport.googleAdsApiService.summary.reason || null,
        });
      }
    } catch (error) {
      pushCheck(report, {
        name: 'Cloud project diagnostics',
        ok: false,
        summary: 'Failed to run service-account Cloud project diagnostics',
        detail: error.message,
      });
    }
  }

  const context = {
    customerId: args.customerId,
    loginCustomerId: args.loginCustomerId,
    serviceAccountEmail: report.auth.serviceAccountEmail,
    projectId: report.auth.serviceAccountProjectId,
    projectNumber: report.auth.serviceAccountProjectNumber,
  };

  const accessibleResponse = await listAccessibleCustomers({
    token: tokenInfo.token,
    developerToken,
    apiVersion: args.apiVersion,
  });

  if (accessibleResponse.statusCode >= 200 && accessibleResponse.statusCode < 300) {
    const resourceNames = accessibleResponse.body?.resourceNames || [];
    report.accessibleCustomerIds = resourceNames.map(name => name.split('/').pop()).filter(Boolean);
    pushCheck(report, {
      name: 'Accessible customers',
      ok: true,
      summary: `${report.accessibleCustomerIds.length} customer(s) visible to the authenticated principal`,
      detail: report.accessibleCustomerIds.length ? report.accessibleCustomerIds.join(', ') : 'No accessible customers returned',
    });
  } else {
    const summary = summarizeGoogleAdsError(accessibleResponse);
    pushCheck(report, {
      name: 'Accessible customers',
      ok: false,
      summary: summary.message || 'Google Ads rejected customers:listAccessibleCustomers',
      detail: summary.errors.map(error => error.message).join(' | ') || null,
      requestId: summary.requestId,
    });
    report.nextActions.push(...buildSuggestions(summary, context));
  }

  const accountSummaryQuery = `SELECT customer.id, customer.descriptive_name, customer.currency_code, customer.time_zone FROM customer LIMIT 1`;
  const accountQuery = await searchStream({
    query: accountSummaryQuery,
    customerId: args.customerId,
    loginCustomerId: args.loginCustomerId,
    token: tokenInfo.token,
    developerToken,
    apiVersion: args.apiVersion,
  });

  if (accountQuery.response.statusCode >= 200 && accountQuery.response.statusCode < 300) {
    const row = accountQuery.results[0] || {};
    pushCheck(report, {
      name: 'Target account query',
      ok: true,
      summary: 'Successfully queried the target Google Ads account',
      detail: row.customer ? JSON.stringify(row.customer) : 'Query returned no rows',
    });
  } else {
    const summary = summarizeGoogleAdsError(accountQuery.response);
    pushCheck(report, {
      name: 'Target account query',
      ok: false,
      summary: summary.message || 'Failed to query the target Google Ads account',
      detail: summary.errors.map(error => error.message).join(' | ') || null,
      requestId: summary.requestId,
    });
    report.nextActions.push(...buildSuggestions(summary, context));
  }

  const managerLinkQuery = `SELECT customer_client.client_customer, customer_client.descriptive_name, customer_client.manager, customer_client.level FROM customer_client WHERE customer_client.id = ${args.customerId} LIMIT 1`;
  const managerQuery = await searchStream({
    query: managerLinkQuery,
    customerId: args.loginCustomerId,
    loginCustomerId: args.loginCustomerId,
    token: tokenInfo.token,
    developerToken,
    apiVersion: args.apiVersion,
  });

  if (managerQuery.response.statusCode >= 200 && managerQuery.response.statusCode < 300) {
    const row = managerQuery.results[0] || {};
    pushCheck(report, {
      name: 'Manager → client linkage query',
      ok: true,
      summary: row.customerClient ? 'Manager can see the target client linkage' : 'Manager query worked but returned no matching client row',
      detail: row.customerClient ? JSON.stringify(row.customerClient) : `Checked manager ${args.loginCustomerId} for client ${args.customerId}`,
    });
  } else {
    const summary = summarizeGoogleAdsError(managerQuery.response);
    pushCheck(report, {
      name: 'Manager → client linkage query',
      ok: false,
      summary: summary.message || 'Failed to query manager linkage',
      detail: summary.errors.map(error => error.message).join(' | ') || null,
      requestId: summary.requestId,
    });
    report.nextActions.push(...buildSuggestions(summary, context));
  }

  report.nextActions = [...new Set(report.nextActions)];

  if (args.json) {
    printJson(report);
  } else {
    process.stdout.write(`${report.checks.map(formatCheck).join('\n')}\n`);
    if (report.nextActions.length) {
      process.stdout.write(`\nNext actions:\n- ${report.nextActions.join('\n- ')}\n`);
    }
    process.stdout.write(`\nOverall: ${report.ok ? 'READY' : 'BLOCKED'}\n`);
  }

  if (!report.ok) process.exit(1);
})().catch(error => {
  process.stderr.write(`${error.stack || error.message}\n`);
  process.exit(1);
});
