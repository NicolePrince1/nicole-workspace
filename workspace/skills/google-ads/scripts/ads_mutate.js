#!/usr/bin/env node
// Google Ads Mutate Operations Runner
// Usage: node ads_mutate.js <resource_type> <operations_json_file>
// Example: node ads_mutate.js campaigns ./pause_campaign.json
// Env: GOOGLE_ADS_TOKEN (or auto-generates), GOOGLE_ADS_DEVELOPER_TOKEN

const https = require('https');
const fs = require('fs');
const { execSync } = require('child_process');

const CUSTOMER_ID = '2906154258';
const LOGIN_CUSTOMER_ID = '6387956297';
const API_VERSION = 'v21';

// Get token
const token = process.env.GOOGLE_ADS_TOKEN ||
  execSync('node /data/.openclaw/secrets/gws-ads-token.js', { encoding: 'utf8' });

const devToken = process.env.GOOGLE_ADS_DEVELOPER_TOKEN || 'z7adyM4vUm79lJCxNi0Ydg';

const resourceType = process.argv[2];
const opsFile = process.argv[3];

if (!resourceType || !opsFile) {
  console.error('Usage: node ads_mutate.js <resource_type> <operations_json_file>');
  console.error('Resource types: campaigns, adGroups, adGroupCriteria, campaignBudgets');
  process.exit(1);
}

const operations = JSON.parse(fs.readFileSync(opsFile, 'utf8'));
const body = JSON.stringify(operations);

// Map resource types to API endpoints
const endpoints = {
  campaigns: 'campaigns:mutate',
  adGroups: 'adGroups:mutate',
  adGroupCriteria: 'adGroupCriteria:mutate',
  adGroupAds: 'adGroupAds:mutate',
  campaignBudgets: 'campaignBudgets:mutate',
  biddingStrategies: 'biddingStrategies:mutate',
};

const endpoint = endpoints[resourceType];
if (!endpoint) {
  console.error(`Unknown resource type: ${resourceType}`);
  console.error(`Valid types: ${Object.keys(endpoints).join(', ')}`);
  process.exit(1);
}

const req = https.request({
  hostname: 'googleads.googleapis.com',
  path: `/${API_VERSION}/customers/${CUSTOMER_ID}/${endpoint}`,
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
      console.log(JSON.stringify(parsed, null, 2));
      if (parsed.error) process.exit(1);
    } catch (e) {
      console.error('Failed to parse response:', data.substring(0, 500));
      process.exit(1);
    }
  });
});

req.write(body);
req.end();
