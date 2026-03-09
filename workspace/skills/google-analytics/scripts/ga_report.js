#!/usr/bin/env node
// GA4 Report Runner
// Usage: node ga_report.js <report_json_file_or_inline_json> [property_id]
// The report JSON should match the GA4 Data API RunReportRequest format
// If property_id not provided, uses GA4_PROPERTY_ID env var

const https = require('https');
const fs = require('fs');
const { execSync } = require('child_process');

const token = process.env.GA_TOKEN ||
  execSync('node /data/.openclaw/secrets/gws-analytics-token.js', { encoding: 'utf8' });

const propertyId = process.argv[3] || process.env.GA4_PROPERTY_ID;
if (!propertyId) {
  console.error('GA4 property ID required. Pass as arg or set GA4_PROPERTY_ID env var.');
  console.error('Usage: node ga_report.js <report.json> [property_id]');
  console.error('Run ga_discover.js to find your property ID.');
  process.exit(1);
}

const input = process.argv[2];
if (!input) {
  console.error('Usage: node ga_report.js <report.json|inline_json> [property_id]');
  process.exit(1);
}

let reportBody;
try {
  // Try as file first
  if (fs.existsSync(input)) {
    reportBody = fs.readFileSync(input, 'utf8');
  } else {
    reportBody = input;
  }
  JSON.parse(reportBody); // validate
} catch (e) {
  console.error('Invalid JSON:', e.message);
  process.exit(1);
}

const req = https.request({
  hostname: 'analyticsdata.googleapis.com',
  path: `/v1beta/properties/${propertyId}:runReport`,
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

      // Pretty-print results
      const dims = (parsed.dimensionHeaders || []).map(h => h.name);
      const mets = (parsed.metricHeaders || []).map(h => h.name);
      const rows = parsed.rows || [];

      console.log(`Results: ${rows.length} rows`);
      console.log(`Dimensions: ${dims.join(', ') || '(none)'}`);
      console.log(`Metrics: ${mets.join(', ')}`);
      console.log('---');

      // If no dimensions, just show totals
      if (dims.length === 0 && parsed.totals && parsed.totals.length > 0) {
        console.log('Totals:');
        const totals = parsed.totals[0].metricValues || [];
        mets.forEach((m, i) => console.log(`  ${m}: ${totals[i]?.value || 'N/A'}`));
      }

      // Show rows
      for (const row of rows) {
        const dimVals = (row.dimensionValues || []).map(v => v.value);
        const metVals = (row.metricValues || []).map(v => v.value);
        if (dims.length > 0) {
          console.log(`${dimVals.join(' | ')}`);
          mets.forEach((m, i) => console.log(`  ${m}: ${metVals[i]}`));
        } else {
          mets.forEach((m, i) => console.log(`${m}: ${metVals[i]}`));
        }
      }

      // Also output raw JSON for programmatic use
      console.log('\n--- RAW JSON ---');
      console.log(JSON.stringify(parsed, null, 2));
    } catch (e) {
      console.error('Failed to parse response:', data.substring(0, 500));
      process.exit(1);
    }
  });
});

req.write(reportBody);
req.end();
