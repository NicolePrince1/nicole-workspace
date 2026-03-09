#!/usr/bin/env node
// Google Search Console Query Runner
// Usage: node gsc_query.js <report_json_file_or_inline_json>
const https = require('https');
const fs = require('fs');
const { execSync } = require('child_process');

const SITE_URL = 'sc-domain:oviond.com';

const token = process.env.GSC_TOKEN ||
  execSync('node /data/.openclaw/secrets/gws-gsc-token.js', { encoding: 'utf8' });

const input = process.argv[2];
if (!input) {
  console.error('Usage: node gsc_query.js <report.json|inline_json>');
  process.exit(1);
}

let reportBody;
try {
  if (fs.existsSync(input)) {
    reportBody = fs.readFileSync(input, 'utf8');
  } else {
    reportBody = input;
  }
  // Handle relative dates
  let report = JSON.parse(reportBody);
  const today = new Date();
  const fmt = d => d.toISOString().split('T')[0];
  if (report.startDate === '30daysAgo') report.startDate = fmt(new Date(today - 30*86400000));
  if (report.startDate === '7daysAgo') report.startDate = fmt(new Date(today - 7*86400000));
  if (report.startDate === '90daysAgo') report.startDate = fmt(new Date(today - 90*86400000));
  if (report.endDate === 'today') report.endDate = fmt(new Date(today - 3*86400000)); // GSC has ~3 day delay
  reportBody = JSON.stringify(report);
} catch (e) {
  console.error('Invalid JSON:', e.message);
  process.exit(1);
}

const req = https.request({
  hostname: 'searchconsole.googleapis.com',
  path: '/webmasters/v3/sites/' + encodeURIComponent(SITE_URL) + '/searchAnalytics/query',
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(reportBody),
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
      const rows = parsed.rows || [];
      console.log(`Results: ${rows.length} rows\n`);
      for (const r of rows) {
        const keys = r.keys.join(' | ');
        console.log(`${keys}`);
        console.log(`  clicks: ${r.clicks}  impressions: ${r.impressions}  CTR: ${(r.ctr*100).toFixed(1)}%  position: ${r.position.toFixed(1)}`);
      }
      console.log('\n--- RAW JSON ---');
      console.log(JSON.stringify(parsed, null, 2));
    } catch (e) {
      console.error('Failed to parse:', data.substring(0, 500));
      process.exit(1);
    }
  });
});
req.write(reportBody);
req.end();
