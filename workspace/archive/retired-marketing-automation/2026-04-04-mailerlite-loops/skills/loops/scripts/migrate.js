#!/usr/bin/env node
const https = require('https');
const fs = require('fs');

const ML_TOKEN = process.env.MAILER_LITE;
const LOOPS_TOKEN = process.env.LOOPS;

const MAPPING = {
  '1.1. 🚀 Trial Users - All (0 to 15 Days)': 'cmmjb3d6a01c00iwn55sld83u',
  '3.2. 💳 Active Paying Customers - All': 'cmmjb3z3b2uj20iwgar195n78',
  '4.1. 🔄 Lapsed Customer - Reactivation Cancelled or Stale Trial  (0-180 Days)': 'cmmjb4inp01h90isyddn5hhzv',
  '5.1. 🌟 Lifetime Free Users - All': 'cmmjb4jt82vao0iy58hy8bnot'
};

// Map ML field names to Loops property names
const FIELD_MAP = {
  'subscription_status': 'subscriptionStatus',
  'trialing': 'trialing',
  'plan': 'planName',
  'active_plan': 'planName',
  'is_lifetime_user': 'isLifetimeUser',
  'projects_count': 'projectsCount',
  'dashboards_count': 'dashboardsCount',
  'clients_count': 'clientsCount',
  'customer_id': 'userId'
};

async function mlGet(path) {
  return new Promise((resolve) => {
    const req = https.request({
      hostname: 'connect.mailerlite.com', path, method: 'GET',
      headers: { 'Authorization': 'Bearer ' + ML_TOKEN }
    }, res => {
      let b = '';
      res.on('data', d => b += d);
      res.on('end', () => resolve(JSON.parse(b)));
    });
    req.end();
  });
}

async function loopsUpsert(contact) {
  return new Promise((resolve) => {
    const data = JSON.stringify(contact);
    const req = https.request({
      hostname: 'app.loops.so', path: '/api/v1/contacts/update', method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + LOOPS_TOKEN,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data)
      }
    }, res => {
      let b = '';
      res.on('data', d => b += d);
      res.on('end', () => resolve(res.statusCode));
    });
    req.write(data);
    req.end();
  });
}

async function migrate() {
  const groups = await mlGet('/api/groups');
  for (const group of groups.data) {
    if (!MAPPING[group.name]) continue;
    
    console.log('Migrating group:', group.name, '->', MAPPING[group.name]);
    let page = 1;
    while (true) {
      const subs = await mlGet(`/api/groups/${group.id}/subscribers?limit=50&page=${page}`);
      if (!subs.data || subs.data.length === 0) break;
      
      for (const s of subs.data) {
        const contact = {
          email: s.email,
          firstName: s.fields?.name || '',
          lastName: s.fields?.last_name || '',
          mailingLists: { [MAPPING[group.name]]: true }
        };

        // Add custom fields
        if (s.fields) {
            for (const [mlField, loopsField] of Object.entries(FIELD_MAP)) {
                if (s.fields[mlField] !== undefined && s.fields[mlField] !== null) {
                    contact[loopsField] = s.fields[mlField];
                }
            }
        }
        
        const status = await loopsUpsert(contact);
        console.log('  Upserted:', s.email, status);
      }
      if (!subs.meta?.next_cursor) break;
      page++;
    }
  }
}

migrate();
