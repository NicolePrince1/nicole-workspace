const { chromium } = require('playwright');
const https = require('https');
const { execFileSync } = require('child_process');
const fs = require('fs');

const OUT = 'outputs/app-real-product-correction';
fs.mkdirSync(`${OUT}/raw`, { recursive: true });
fs.mkdirSync(`${OUT}/annotated`, { recursive: true });

async function requestMagicLink(page) {
  await page.goto('https://app.oviond.com/signin', { waitUntil: 'networkidle', timeout: 90000 });
  await page.locator('input[type="email"]').fill('nicole@oviond.com');
  await page.getByRole('button', { name: /magic link/i }).click();
  await page.waitForTimeout(4000);
}
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
  const q = encodeURIComponent('to:nicole@oviond.com from:hello@oviond.com subject:("Sign in to Oviond") newer_than:10m');
  const list = await gmailReq(`/gmail/v1/users/me/messages?q=${q}&maxResults=8`);
  for (const m of list.messages || []) {
    const msg = await gmailReq(`/gmail/v1/users/me/messages/${m.id}?format=full`);
    const text = walk(msg.payload).join('\n');
    const links = [...text.matchAll(/https:\/\/app\.oviond\.com\/auth\/callback\?[^\s"'<>]+/g)].map(x => x[0].replace(/&amp;/g, '&'));
    if (links[0]) return links[0];
  }
  throw new Error('No Oviond auth callback link found');
}
async function clickContinue(page) {
  const candidates = [page.getByRole('button', { name: /continue/i }), page.getByRole('button', { name: /finish/i }), page.locator('button').last()];
  for (const c of candidates) {
    try { await c.click({ timeout: 5000 }); return true; } catch {}
  }
  return false;
}
async function fillVisibleInputs(page, values) {
  const inputs = await page.locator('input:visible').all();
  for (let i=0; i<inputs.length && i<values.length; i++) {
    await inputs[i].fill(values[i]);
  }
}
async function handleOnboarding(page) {
  for (let step=1; step<=8; step++) {
    await page.waitForTimeout(1200);
    await page.screenshot({ path: `${OUT}/raw/onboarding-step-${step}.png`, fullPage: false });
    const text = await page.locator('body').innerText().catch(()=> '');
    fs.writeFileSync(`${OUT}/onboarding-step-${step}.txt`, text);
    if (!/step \d|what should we call you|company|client|website|onboarding|finish/i.test(text)) break;
    if (/what should we call you|full name/i.test(text)) {
      await fillVisibleInputs(page, ['Nicole Prince']);
    } else if (/company/i.test(text) && /name/i.test(text)) {
      await fillVisibleInputs(page, ['Nicole QA Agency']);
    } else if (/website|domain/i.test(text)) {
      await fillVisibleInputs(page, ['https://oviond.com']);
    } else if (/how many|clients|client volume/i.test(text) && (await page.locator('input:visible').count()) === 0) {
      const opts = [page.getByText(/6\s*[–-]\s*20|6.*20/i), page.getByText(/1\s*[–-]\s*5|1.*5/i), page.getByRole('button').nth(1)];
      for (const o of opts) { try { await o.click({ timeout: 3000 }); break; } catch {} }
    } else if (/first client|client name|client website/i.test(text)) {
      await fillVisibleInputs(page, ['QA Screenshot Client', 'https://qa-screenshot.example.com']);
    } else if (/template|dashboard|report/i.test(text)) {
      const buttons = [page.getByText(/digital marketing|blank|default|continue|finish/i), page.getByRole('button').filter({hasText:/continue|finish/i})];
      for (const b of buttons) { try { await b.first().click({timeout:3000}); await page.waitForTimeout(500); break; } catch {} }
    }
    if (!(await clickContinue(page))) break;
  }
}
async function findAndOpenAddClient(page) {
  const routes = ['https://app.oviond.com/clients', 'https://app.oviond.com'];
  for (const url of routes) {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(()=>{});
    await page.waitForTimeout(2500);
    const text = await page.locator('body').innerText().catch(()=> '');
    if (/add client|clients/i.test(text)) break;
  }
  // If sidebar client link exists, click it.
  for (const loc of [page.getByRole('link', {name:/clients/i}), page.getByRole('button', {name:/clients/i}), page.getByText(/^Clients$/i)]) {
    try { await loc.first().click({timeout:2500}); await page.waitForTimeout(2000); break; } catch {}
  }
  await page.screenshot({ path: `${OUT}/raw/clients-before-add.png`, fullPage: false });
  fs.writeFileSync(`${OUT}/clients-before-add.txt`, await page.locator('body').innerText().catch(e=>e.message));
  const adders = [page.getByRole('button', {name:/add client/i}), page.getByRole('link', {name:/add client/i}), page.getByText(/add client/i), page.getByRole('button', {name:/new client/i}), page.getByText(/new client/i)];
  for (const loc of adders) {
    try { await loc.first().click({timeout:5000}); await page.waitForTimeout(2500); break; } catch {}
  }
  await page.screenshot({ path: `${OUT}/raw/add-client-open.png`, fullPage: false });
  fs.writeFileSync(`${OUT}/add-client-open.txt`, await page.locator('body').innerText().catch(e=>e.message));
}
async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 980 }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  await requestMagicLink(page);
  await page.waitForTimeout(6000);
  const link = await latestLink();
  await page.goto(link, { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(3000);
  await page.screenshot({ path: `${OUT}/raw/after-login.png`, fullPage: false });
  let text = await page.locator('body').innerText().catch(()=> '');
  if (/onboarding|what should we call you|step \d/i.test(text)) await handleOnboarding(page);
  await findAndOpenAddClient(page);
  await context.storageState({ path: `${OUT}/auth-state.json` });
  console.log(JSON.stringify({ out: OUT, url: page.url(), addClientText: (await page.locator('body').innerText().catch(()=> '')).slice(0,700) }, null, 2));
  await browser.close();
}
main().catch(e => { console.error(e); process.exit(1); });
