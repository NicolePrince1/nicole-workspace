const { chromium } = require('playwright');
const https = require('https');
const { execFileSync } = require('child_process');
const fs = require('fs');

const OUT = 'outputs/app-add-client-real';
fs.mkdirSync(`${OUT}/raw`, { recursive: true });
fs.mkdirSync(`${OUT}/annotated`, { recursive: true });

function gmailReq(path) {
  const token = execFileSync('node', ['/data/.openclaw/secrets/gws-token.js', 'gmail.modify'], { encoding: 'utf8' }).trim();
  return new Promise((resolve, reject) => {
    https.get({ hostname: 'gmail.googleapis.com', path, headers: { Authorization: `Bearer ${token}` } }, res => {
      let b = '';
      res.on('data', d => b += d);
      res.on('end', () => res.statusCode >= 300 ? reject(new Error(res.statusCode + ' ' + b)) : resolve(JSON.parse(b)));
    }).on('error', reject);
  });
}
function b64(s) { return Buffer.from((s || '').replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8'); }
function walk(payload, out = []) { if (payload.body?.data) out.push(b64(payload.body.data)); for (const p of payload.parts || []) walk(p, out); return out; }
async function latestLink() {
  const q = encodeURIComponent('to:nicole@oviond.com from:hello@oviond.com newer_than:1d ("Confirm your email" OR "sign" OR "Oviond")');
  const list = await gmailReq(`/gmail/v1/users/me/messages?q=${q}&maxResults=5`);
  for (const m of list.messages || []) {
    const msg = await gmailReq(`/gmail/v1/users/me/messages/${m.id}?format=full`);
    const text = walk(msg.payload).join('\n');
    const links = [...text.matchAll(/https:\/\/app\.oviond\.com\/auth\/callback\?[^\s"'<>]+/g)].map(x => x[0].replace(/&amp;/g, '&'));
    if (links[0]) return links[0];
  }
  throw new Error('No Oviond auth callback link found in latest email');
}
async function maybeClick(page, locator, label) {
  try { await locator.first().click({ timeout: 5000 }); console.log('clicked', label); return true; }
  catch (e) { console.log('skip click', label, e.message.split('\n')[0]); return false; }
}
async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 980 }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  const errors = [];
  page.on('console', msg => { if (['error','warning'].includes(msg.type())) errors.push({ type: msg.type(), text: msg.text().slice(0, 300) }); });
  page.on('requestfailed', req => errors.push({ type: 'requestfailed', url: req.url(), error: req.failure()?.errorText }));

  const link = await latestLink();
  await page.goto(link, { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(3000);
  await page.screenshot({ path: `${OUT}/raw/01-after-login.png`, fullPage: false });

  // Close onboarding/help overlays if present.
  await maybeClick(page, page.getByRole('button', { name: /skip|close|dismiss|not now/i }), 'possible overlay');

  // Try known app routes first, then UI clicks.
  const candidateRoutes = [
    'https://app.oviond.com/clients',
    'https://app.oviond.com/client',
    'https://app.oviond.com/dashboard',
    'https://app.oviond.com'
  ];
  let clientsLoaded = false;
  for (const url of candidateRoutes) {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
    await page.waitForTimeout(1500);
    const txt = await page.locator('body').innerText().catch(()=>'');
    if (/clients?/i.test(txt) && (/add client|new client|create client/i.test(txt) || await page.getByText(/clients?/i).count())) { clientsLoaded = true; break; }
  }
  if (!clientsLoaded) {
    await maybeClick(page, page.getByText(/^Clients$/i), 'Clients nav');
    await page.waitForTimeout(2000);
  }
  await page.screenshot({ path: `${OUT}/raw/02-clients-screen.png`, fullPage: false });

  // Open add client screen/modal without submitting.
  const addLocators = [
    page.getByRole('button', { name: /add client/i }),
    page.getByRole('link', { name: /add client/i }),
    page.getByText(/add client/i),
    page.getByRole('button', { name: /new client/i }),
    page.getByText(/new client/i),
    page.locator('button').filter({ hasText: /^\+$/ })
  ];
  let clicked = false;
  for (const l of addLocators) { if (await maybeClick(page, l, 'Add Client')) { clicked = true; break; } }
  if (!clicked) throw new Error('Could not find Add Client action. Current URL: ' + page.url());
  await page.waitForTimeout(2500);
  await page.screenshot({ path: `${OUT}/raw/03-add-client-open.png`, fullPage: false });
  const body = await page.locator('body').innerText().catch(e => e.message);
  fs.writeFileSync(`${OUT}/page-text.txt`, body);
  fs.writeFileSync(`${OUT}/console-errors.json`, JSON.stringify(errors, null, 2));
  await context.storageState({ path: `${OUT}/auth-state.json` });
  console.log(JSON.stringify({ url: page.url(), outputs: [`${OUT}/raw/01-after-login.png`, `${OUT}/raw/02-clients-screen.png`, `${OUT}/raw/03-add-client-open.png`], textSample: body.slice(0,500) }, null, 2));
  await browser.close();
}
main().catch(e => { console.error(e); process.exit(1); });
