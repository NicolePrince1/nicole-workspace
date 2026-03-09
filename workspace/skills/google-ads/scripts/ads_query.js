#!/usr/bin/env node
// Google Ads GAQL Query Runner
// Usage: node ads_query.js "SELECT ... FROM ... WHERE ..."
// Env: GOOGLE_ADS_TOKEN (or auto-generates), GOOGLE_ADS_DEVELOPER_TOKEN

const https = require('https');
const { execSync } = require('child_process');

const CUSTOMER_ID = '2906154258';
const LOGIN_CUSTOMER_ID = '6387956297';
const API_VERSION = 'v21';

// Get token
const token = process.env.GOOGLE_ADS_TOKEN ||
  execSync('node /data/.openclaw/secrets/gws-ads-token.js', { encoding: 'utf8' });

// Get developer token
const devToken = process.env.GOOGLE_ADS_DEVELOPER_TOKEN || 'z7adyM4vUm79lJCxNi0Ydg';

const query = process.argv[2];
if (!query) {
  console.error('Usage: node ads_query.js "GAQL query"');
  process.exit(1);
}

const body = JSON.stringify({ query, pageSize: 10000 });

const req = https.request({
  hostname: 'googleads.googleapis.com',
  path: `/${API_VERSION}/customers/${CUSTOMER_ID}/googleAds:search`,
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'developer-token': devToken,
    'login-customer-id': LOGIN_CUSTOMER_ID,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(body),
  },
}, res => {
  let data = '';
  res.on('data', d => data += d);
  res.on('end', () => {
    try {
      const parsed = JSON.parse(data);
      if (parsed.error) {
        console.error(JSON.stringify(parsed.error, null, 2));
        process.exit(1);
      }
      // Format results
      const results = parsed.results || [];
      console.log(JSON.stringify({ totalResults: results.length, results }, null, 2));
    } catch (e) {
      console.error('Failed to parse response:', data.substring(0, 500));
      process.exit(1);
    }
  });
});

req.write(body);
req.end();
