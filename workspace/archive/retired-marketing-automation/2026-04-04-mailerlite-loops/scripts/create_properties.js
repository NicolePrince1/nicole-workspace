const https = require('https');
const props = [
  {name: "subscriptionStatus", type: "string"},
  {name: "trialing", type: "boolean"},
  {name: "trialEndsAt", type: "date"},
  {name: "currentPeriodEnd", type: "date"},
  {name: "planName", type: "string"},
  {name: "billingInterval", type: "string"},
  {name: "mrr", type: "number"},
  {name: "isLifetimeUser", type: "boolean"},
  {name: "pastDue", type: "boolean"},
  {name: "paused", type: "boolean"},
  {name: "projectsCount", type: "number"},
  {name: "dashboardsCount", type: "number"},
  {name: "clientsCount", type: "number"},
  {name: "connectedSourcesCount", type: "number"},
  {name: "firstReportCreatedAt", type: "date"},
  {name: "lastActiveAt", type: "date"},
  {name: "hasCreatedReport", type: "boolean"},
  {name: "hasSharedReport", type: "boolean"},
  {name: "hasConnectedDataSource", type: "boolean"},
  {name: "hasInvitedTeamMember", type: "boolean"},
  {name: "customerType", type: "string"},
  {name: "agencySize", type: "string"},
  {name: "country", type: "string"},
  {name: "leadSource", type: "string"},
  {name: "needsUpgrade", type: "boolean"},
  {name: "atRisk", type: "boolean"}
];

async function createProp(p) {
  return new Promise((resolve) => {
    const data = JSON.stringify(p);
    const req = https.request({
      hostname: 'app.loops.so',
      path: '/api/v1/contacts/properties',
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + process.env.LOOPS,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data)
      }
    }, res => {
      let b = '';
      res.on('data', d => b += d);
      res.on('end', () => {
        console.log(p.name + ':', res.statusCode, b);
        resolve();
      });
    });
    req.write(data);
    req.end();
  });
}

(async () => {
  for (const p of props) await createProp(p);
})();
