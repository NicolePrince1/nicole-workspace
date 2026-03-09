#!/usr/bin/env node
// Discover GA4 properties accessible to nicole@oviond.com
const https = require('https');
const { execSync } = require('child_process');

const token = process.env.GA_TOKEN ||
  execSync('node /data/.openclaw/secrets/gws-analytics-token.js', { encoding: 'utf8' });

const req = https.request({
  hostname: 'analyticsadmin.googleapis.com',
  path: '/v1beta/accountSummaries',
  method: 'GET',
  headers: { 'Authorization': `Bearer ${token}` },
}, res => {
  let body = '';
  res.on('data', d => body += d);
  res.on('end', () => {
    const parsed = JSON.parse(body);
    if (parsed.error) {
      console.error(JSON.stringify(parsed.error, null, 2));
      process.exit(1);
    }
    const summaries = parsed.accountSummaries || [];
    for (const acct of summaries) {
      console.log(`Account: ${acct.displayName} (${acct.account})`);
      for (const prop of (acct.propertySummaries || [])) {
        console.log(`  Property: ${prop.displayName} — ID: ${prop.property.replace('properties/', '')}`);
      }
    }
    if (summaries.length === 0) console.log('No GA4 properties found for this user.');
    console.log('\nRaw:', JSON.stringify(parsed, null, 2));
  });
});
req.end();
