#!/usr/bin/env node
const crypto = require('crypto');
const fs = require('fs');
const https = require('https');
const path = require('path');

const DEFAULTS = {
  customerId: stripCustomerId(process.env.GOOGLE_ADS_CUSTOMER_ID || '2906154258'),
  loginCustomerId: stripCustomerId(process.env.GOOGLE_ADS_LOGIN_CUSTOMER_ID || '6387956297'),
  apiVersion: process.env.GOOGLE_ADS_API_VERSION || 'v21',
  scope: 'https://www.googleapis.com/auth/adwords',
  authMode: (process.env.GOOGLE_ADS_AUTH_MODE || 'auto').trim().toLowerCase(),
  cloudPlatformScope: 'https://www.googleapis.com/auth/cloud-platform',
};

function stripCustomerId(value) {
  return String(value || '').replace(/\D/g, '');
}

function toBase64Url(value) {
  return Buffer.from(value).toString('base64url');
}

function defaultServiceAccountPath() {
  const candidates = [
    process.env.GOOGLE_ADS_SERVICE_ACCOUNT_JSON,
    '/data/.openclaw/secrets/gws-service-account.json',
  ].filter(Boolean);

  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) return candidate;
  }

  return null;
}

function hasServiceAccountConfig() {
  return Boolean(process.env.GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT || defaultServiceAccountPath());
}

function getOAuthClientConfig() {
  const clientId = process.env.GOOGLE_ADS_OAUTH_CLIENT_ID || process.env.GOOGLE_ADS_CLIENT_ID || null;
  const clientSecret = process.env.GOOGLE_ADS_OAUTH_CLIENT_SECRET || process.env.GOOGLE_ADS_CLIENT_SECRET || null;
  const refreshToken = process.env.GOOGLE_ADS_REFRESH_TOKEN || null;

  if (!clientId && !clientSecret && !refreshToken) {
    return null;
  }

  const missing = [
    !clientId ? 'GOOGLE_ADS_OAUTH_CLIENT_ID or GOOGLE_ADS_CLIENT_ID' : null,
    !clientSecret ? 'GOOGLE_ADS_OAUTH_CLIENT_SECRET or GOOGLE_ADS_CLIENT_SECRET' : null,
    !refreshToken ? 'GOOGLE_ADS_REFRESH_TOKEN' : null,
  ].filter(Boolean);

  if (missing.length) {
    throw new Error(`OAuth refresh-token auth is partially configured. Missing: ${missing.join(', ')}`);
  }

  return {
    clientId,
    clientSecret,
    refreshToken,
  };
}

function getPreferredAuthMode(explicitMode) {
  const mode = String(explicitMode || DEFAULTS.authMode || 'auto').trim().toLowerCase();
  const validModes = new Set(['auto', 'service-account', 'oauth-refresh-token']);
  if (!validModes.has(mode)) {
    throw new Error(
      `Unsupported auth mode "${mode}". Valid values: auto, service-account, oauth-refresh-token.`
    );
  }
  return mode;
}

function loadServiceAccount() {
  if (process.env.GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT) {
    const creds = JSON.parse(process.env.GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT);
    return {
      credentials: creds,
      path: 'env:GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT',
    };
  }

  const jsonPath = defaultServiceAccountPath();
  if (!jsonPath) {
    throw new Error(
      'No service-account JSON found. Set GOOGLE_ADS_SERVICE_ACCOUNT_JSON or GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT, or place credentials at /data/.openclaw/secrets/gws-service-account.json.'
    );
  }

  const creds = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  return { credentials: creds, path: jsonPath };
}

function requestJson({ hostname, path: requestPath, method = 'GET', headers = {}, body }) {
  return new Promise((resolve, reject) => {
    const payload = body == null ? null : typeof body === 'string' ? body : JSON.stringify(body);
    const req = https.request(
      {
        hostname,
        path: requestPath,
        method,
        headers: {
          ...headers,
          ...(payload != null
            ? {
                'Content-Length': Buffer.byteLength(payload),
              }
            : {}),
        },
      },
      res => {
        let raw = '';
        res.on('data', chunk => {
          raw += chunk;
        });
        res.on('end', () => {
          let parsed = null;
          if (raw.length) {
            try {
              parsed = JSON.parse(raw);
            } catch (error) {
              parsed = null;
            }
          }

          resolve({
            statusCode: res.statusCode || 0,
            headers: res.headers,
            body: parsed,
            rawBody: raw,
          });
        });
      }
    );

    req.on('error', reject);
    if (payload != null) req.write(payload);
    req.end();
  });
}

async function mintServiceAccountToken({ credentials, scope = DEFAULTS.scope, subject = null }) {
  const now = Math.floor(Date.now() / 1000);
  const header = toBase64Url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const claimSet = {
    iss: credentials.client_email,
    scope,
    aud: 'https://oauth2.googleapis.com/token',
    iat: now,
    exp: now + 3600,
  };
  if (subject) claimSet.sub = subject;

  const payload = toBase64Url(
    JSON.stringify(claimSet)
  );

  const signer = crypto.createSign('RSA-SHA256');
  signer.update(`${header}.${payload}`);
  signer.end();
  const signature = signer.sign(credentials.private_key, 'base64url');
  const assertion = `${header}.${payload}.${signature}`;

  const tokenResponse = await requestJson({
    hostname: 'oauth2.googleapis.com',
    path: '/token',
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=${assertion}`,
  });

  if (tokenResponse.statusCode < 200 || tokenResponse.statusCode >= 300 || !tokenResponse.body?.access_token) {
    const detail = tokenResponse.body ? JSON.stringify(tokenResponse.body, null, 2) : tokenResponse.rawBody;
    throw new Error(`Token mint failed (${tokenResponse.statusCode}): ${detail}`);
  }

  return tokenResponse.body.access_token;
}

async function mintRefreshTokenAccessToken({ clientId, clientSecret, refreshToken }) {
  const tokenResponse = await requestJson({
    hostname: 'oauth2.googleapis.com',
    path: '/token',
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: [
      ['client_id', clientId],
      ['client_secret', clientSecret],
      ['refresh_token', refreshToken],
      ['grant_type', 'refresh_token'],
    ]
      .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
      .join('&'),
  });

  if (tokenResponse.statusCode < 200 || tokenResponse.statusCode >= 300 || !tokenResponse.body?.access_token) {
    const detail = tokenResponse.body ? JSON.stringify(tokenResponse.body, null, 2) : tokenResponse.rawBody;
    throw new Error(`Refresh-token exchange failed (${tokenResponse.statusCode}): ${detail}`);
  }

  return tokenResponse.body.access_token;
}

function maskValue(value, { start = 6, end = 4 } = {}) {
  const raw = String(value || '');
  if (!raw) return null;
  if (raw.length <= start + end) return raw;
  return `${raw.slice(0, start)}…${raw.slice(-end)}`;
}

async function resolveAccessToken({ scope = DEFAULTS.scope, authMode } = {}) {
  const preferredMode = getPreferredAuthMode(authMode);
  if (process.env.GOOGLE_ADS_TOKEN) {
    return {
      token: process.env.GOOGLE_ADS_TOKEN,
      source: 'env:GOOGLE_ADS_TOKEN',
      authMode: 'env-token',
      serviceAccount: null,
      oauthClient: null,
    };
  }

  const serviceAccountAvailable = hasServiceAccountConfig();
  let oauthConfig = null;
  try {
    oauthConfig = getOAuthClientConfig();
  } catch (error) {
    if (preferredMode === 'oauth-refresh-token') throw error;
    throw error;
  }

  const tryServiceAccount = preferredMode === 'service-account' || preferredMode === 'auto';
  const tryRefreshToken =
    preferredMode === 'oauth-refresh-token' || (preferredMode === 'auto' && !serviceAccountAvailable);

  let serviceAccountError = null;

  if (tryServiceAccount && serviceAccountAvailable) {
    try {
      const { credentials, path: credentialsPath } = loadServiceAccount();
      const token = await mintServiceAccountToken({
        credentials,
        scope,
        subject: process.env.GOOGLE_ADS_SERVICE_ACCOUNT_SUBJECT || null,
      });
      return {
        token,
        source: 'service-account',
        authMode: preferredMode,
        serviceAccount: {
          path: credentialsPath,
          email: credentials.client_email,
          projectId: credentials.project_id,
          projectNumber: credentials.project_number || null,
          clientId: credentials.client_id || null,
          subject: process.env.GOOGLE_ADS_SERVICE_ACCOUNT_SUBJECT || null,
        },
        oauthClient: null,
      };
    } catch (error) {
      serviceAccountError = error;
      if (preferredMode === 'service-account') throw error;
    }
  }

  if (tryRefreshToken) {
    if (!oauthConfig) {
      throw new Error(
        'OAuth refresh-token auth requested, but no full OAuth client config is present. Set GOOGLE_ADS_OAUTH_CLIENT_ID (or GOOGLE_ADS_CLIENT_ID), GOOGLE_ADS_OAUTH_CLIENT_SECRET (or GOOGLE_ADS_CLIENT_SECRET), and GOOGLE_ADS_REFRESH_TOKEN.'
      );
    }

    const token = await mintRefreshTokenAccessToken(oauthConfig);
    return {
      token,
      source: 'oauth-refresh-token',
      authMode: preferredMode,
      serviceAccount: null,
      oauthClient: {
        clientId: maskValue(oauthConfig.clientId),
      },
    };
  }

  if (serviceAccountError) throw serviceAccountError;

  throw new Error(
    'No Google Ads auth path is configured. Provide a service-account JSON (GOOGLE_ADS_SERVICE_ACCOUNT_JSON / GOOGLE_ADS_SERVICE_ACCOUNT_JSON_CONTENT) or configure OAuth refresh-token auth.'
  );
}

function getDeveloperToken() {
  const developerToken = process.env.GOOGLE_ADS_DEVELOPER_TOKEN;
  if (!developerToken) {
    throw new Error('Missing GOOGLE_ADS_DEVELOPER_TOKEN env var');
  }
  return developerToken;
}

async function callGoogleAds({
  method = 'POST',
  path: requestPath,
  body,
  token,
  developerToken,
  loginCustomerId,
}) {
  return requestJson({
    hostname: 'googleads.googleapis.com',
    path: requestPath,
    method,
    headers: {
      Authorization: `Bearer ${token}`,
      'developer-token': developerToken,
      'Content-Type': 'application/json',
      ...(loginCustomerId ? { 'login-customer-id': stripCustomerId(loginCustomerId) } : {}),
    },
    body,
  });
}

function getGoogleAdsErrorRoot(response) {
  if (response?.body?.error) return response.body.error;
  if (Array.isArray(response?.body)) {
    const item = response.body.find(entry => entry?.error);
    if (item?.error) return item.error;
  }
  return null;
}

function extractGoogleAdsErrors(response) {
  const root = getGoogleAdsErrorRoot(response);
  return root?.details?.flatMap(detail => detail?.errors || []).filter(Boolean) || [];
}

function summarizeGoogleAdsError(response) {
  const topLevel = getGoogleAdsErrorRoot(response);
  const errors = extractGoogleAdsErrors(response).map(error => ({
    code: Object.entries(error.errorCode || {}).map(([family, value]) => ({ family, value })),
    message: error.message,
  }));

  return {
    httpStatus: response?.statusCode || 0,
    status: topLevel?.status || null,
    message: topLevel?.message || null,
    requestId:
      topLevel?.details?.find(detail => detail?.requestId)?.requestId ||
      response?.headers?.['request-id'] ||
      response?.headers?.['request-id'.toLowerCase()] ||
      null,
    errors,
    raw: topLevel || response?.body || response?.rawBody || null,
  };
}

function collectErrorCodes(summary) {
  const codes = new Set();
  for (const error of summary?.errors || []) {
    for (const entry of error.code || []) {
      if (entry.value) codes.add(entry.value);
    }
  }
  if (summary?.status) codes.add(summary.status);
  return [...codes];
}

function buildSuggestions(summary, context = {}) {
  const codes = new Set(collectErrorCodes(summary));
  const suggestions = [];

  if (codes.has('PROJECT_DISABLED')) {
    suggestions.push(
      `Enable Google Ads API access for Cloud project ${context.projectNumber || context.projectId || 'behind the service account'} and confirm this project is the one intended to call Google Ads.`
    );
    suggestions.push(
      'If the API is already enabled, verify the project/developer-token setup with Google Ads API Center or Google Ads API support before retrying.'
    );
    suggestions.push(
      'If the project is definitely correct and still returns PROJECT_DISABLED, create a fresh Google Cloud project with Google Ads API enabled, mint fresh credentials there, and retry with the same intended developer token.'
    );
  }

  if (codes.has('USER_PERMISSION_DENIED')) {
    suggestions.push(
      `Add ${context.serviceAccountEmail || 'the service account email'} as a user in the manager account ${context.loginCustomerId || '(manager account)'} with at least Standard access.`
    );
    suggestions.push(
      `Confirm manager ${context.loginCustomerId || '(manager account)'} is actually linked to client ${context.customerId || '(client account)'} and keep that manager ID in the login-customer-id header.`
    );
  }

  if (codes.has('UNAUTHENTICATED')) {
    suggestions.push('Regenerate the access token and ensure the service-account JSON private key is valid and current.');
  }

  if (codes.has('DEVELOPER_TOKEN_NOT_APPROVED') || codes.has('DEVELOPER_TOKEN_INVALID')) {
    suggestions.push('Verify GOOGLE_ADS_DEVELOPER_TOKEN is correct and approved for the type of account access you need.');
  }

  if (!suggestions.length) {
    suggestions.push('Review the raw error payload and compare it with the Google Ads API auth and call-structure docs.');
  }

  return suggestions;
}

function summarizeGenericGoogleApiError(response) {
  const error = response?.body?.error || null;
  const reason =
    error?.details
      ?.find(detail => detail?.['@type'] === 'type.googleapis.com/google.rpc.ErrorInfo')
      ?.reason || null;

  return {
    httpStatus: response?.statusCode || 0,
    status: error?.status || null,
    message: error?.message || response?.rawBody || null,
    reason,
    raw: error || response?.body || response?.rawBody || null,
  };
}

async function inspectCloudProject({ credentials, projectId, projectNumber }) {
  const token = await mintServiceAccountToken({ credentials, scope: DEFAULTS.cloudPlatformScope });
  const projectRef = projectId || projectNumber;

  const projectMetadata = projectId
    ? await requestJson({
        hostname: 'cloudresourcemanager.googleapis.com',
        path: `/v1/projects/${projectId}`,
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
    : null;

  const googleAdsApiService = projectRef
    ? await requestJson({
        hostname: 'serviceusage.googleapis.com',
        path: `/v1/projects/${projectRef}/services/googleads.googleapis.com`,
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
    : null;

  return {
    projectMetadata: projectMetadata
      ? {
          ok: projectMetadata.statusCode >= 200 && projectMetadata.statusCode < 300,
          response: projectMetadata,
          summary:
            projectMetadata.statusCode >= 200 && projectMetadata.statusCode < 300
              ? { message: `Cloud project ${projectMetadata.body?.projectId || projectId} is reachable.` }
              : summarizeGenericGoogleApiError(projectMetadata),
        }
      : null,
    googleAdsApiService: googleAdsApiService
      ? {
          ok:
            googleAdsApiService.statusCode >= 200 &&
            googleAdsApiService.statusCode < 300 &&
            googleAdsApiService.body?.state === 'ENABLED',
          response: googleAdsApiService,
          summary:
            googleAdsApiService.statusCode >= 200 && googleAdsApiService.statusCode < 300
              ? {
                  message: `googleads.googleapis.com state: ${googleAdsApiService.body?.state || 'unknown'}`,
                  state: googleAdsApiService.body?.state || null,
                }
              : summarizeGenericGoogleApiError(googleAdsApiService),
        }
      : null,
  };
}

async function listAccessibleCustomers({ token, developerToken, apiVersion = DEFAULTS.apiVersion }) {
  return callGoogleAds({
    method: 'GET',
    path: `/${apiVersion}/customers:listAccessibleCustomers`,
    token,
    developerToken,
  });
}

async function searchStream({
  query,
  customerId = DEFAULTS.customerId,
  loginCustomerId = DEFAULTS.loginCustomerId,
  token,
  developerToken,
  apiVersion = DEFAULTS.apiVersion,
}) {
  const response = await callGoogleAds({
    method: 'POST',
    path: `/${apiVersion}/customers/${stripCustomerId(customerId)}/googleAds:searchStream`,
    body: { query },
    token,
    developerToken,
    loginCustomerId,
  });

  const batches = Array.isArray(response.body) ? response.body : [];
  const results = batches.flatMap(batch => batch.results || []);
  return {
    response,
    batches,
    results,
    fieldMask: batches.flatMap(batch => batch.fieldMask || []),
  };
}

async function mutate({
  resourceType,
  operations,
  customerId = DEFAULTS.customerId,
  loginCustomerId = DEFAULTS.loginCustomerId,
  token,
  developerToken,
  apiVersion = DEFAULTS.apiVersion,
  validateOnly = true,
  partialFailure = true,
  responseContentType = 'MUTABLE_RESOURCE',
}) {
  const endpoints = {
    campaigns: 'campaigns:mutate',
    adGroups: 'adGroups:mutate',
    adGroupCriteria: 'adGroupCriteria:mutate',
    adGroupAds: 'adGroupAds:mutate',
    campaignBudgets: 'campaignBudgets:mutate',
    biddingStrategies: 'biddingStrategies:mutate',
    assetGroups: 'assetGroups:mutate',
    assets: 'assets:mutate',
  };

  const endpoint = endpoints[resourceType];
  if (!endpoint) {
    throw new Error(`Unknown resource type: ${resourceType}. Valid types: ${Object.keys(endpoints).join(', ')}`);
  }

  return callGoogleAds({
    method: 'POST',
    path: `/${apiVersion}/customers/${stripCustomerId(customerId)}/${endpoint}`,
    body: {
      ...operations,
      partialFailure,
      validateOnly,
      responseContentType,
    },
    token,
    developerToken,
    loginCustomerId,
  });
}

function printJson(value) {
  process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
}

module.exports = {
  DEFAULTS,
  buildSuggestions,
  callGoogleAds,
  collectErrorCodes,
  extractGoogleAdsErrors,
  getDeveloperToken,
  getPreferredAuthMode,
  hasServiceAccountConfig,
  inspectCloudProject,
  listAccessibleCustomers,
  loadServiceAccount,
  mintServiceAccountToken,
  mutate,
  printJson,
  resolveAccessToken,
  searchStream,
  stripCustomerId,
  summarizeGenericGoogleApiError,
  summarizeGoogleAdsError,
};
