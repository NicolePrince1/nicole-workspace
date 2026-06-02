const { chromium } = require('playwright');
const fs = require('fs');
const OUT='outputs/help-center-rollout';
fs.mkdirSync(`${OUT}/raw`, {recursive:true});
async function snap(page,name){await page.waitForTimeout(1200); await page.screenshot({path:`${OUT}/raw/${name}.png`, fullPage:false}); fs.writeFileSync(`${OUT}/raw/${name}.txt`, await page.locator('body').innerText().catch(e=>e.message)); console.log('snap', name, page.url());}
async function click(page, locator, name){try{await locator.first().click({timeout:7000}); await snap(page,name); return true;}catch(e){console.log('skip', name, e.message.split('\n')[0]); return false;}}
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}, storageState:'outputs/app-real-product-correction/auth-state.json'});
 const page=await context.newPage();
 // Top-level surfaces
 await page.goto('https://app.oviond.com/', {waitUntil:'networkidle', timeout:60000}); await snap(page,'clients-home');
 await click(page, page.getByRole('button',{name:/add client/i}), 'clients-add-drawer'); await page.keyboard.press('Escape').catch(()=>{});
 for (const [url,name] of [['/templates','templates-list'],['/automations','automations-list'],['/notifications','notifications'],['/settings','settings-my-account']]) {
  await page.goto('https://app.oviond.com'+url, {waitUntil:'networkidle', timeout:60000}); await snap(page,name);
 }
 // Template preview
 await page.goto('https://app.oviond.com/templates', {waitUntil:'networkidle'}); await click(page, page.getByRole('button',{name:/preview/i}), 'templates-preview'); await page.keyboard.press('Escape').catch(()=>{});
 // Automation drawer/modal
 await page.goto('https://app.oviond.com/automations', {waitUntil:'networkidle'}); await click(page, page.getByRole('button',{name:/new automation|create automation/i}), 'automations-new'); await page.keyboard.press('Escape').catch(()=>{});
 // AI connectors overlay from home
 await page.goto('https://app.oviond.com/', {waitUntil:'networkidle'}); await click(page, page.getByRole('button',{name:/AI Connectors/i}), 'ai-connectors'); await page.keyboard.press('Escape').catch(()=>{});
 // Settings tabs
 await page.goto('https://app.oviond.com/settings', {waitUntil:'networkidle'}); await snap(page,'settings-start');
 const tabs=['Company','Users','Billing','Api Keys','Activity Log','Domains','Emails','Data Sources','Archive'];
 for (const tab of tabs) { await click(page, page.getByText(new RegExp('^'+tab+'$','i')), 'settings-'+tab.toLowerCase().replace(/\s+/g,'-')); }
 // Client project and settings surfaces
 await page.goto('https://app.oviond.com/', {waitUntil:'networkidle'}); await click(page, page.getByRole('button',{name:/open/i}), 'client-projects');
 const clientUrl=page.url().replace(/\/projects.*/, '');
 await click(page, page.getByRole('button',{name:/add project/i}), 'client-add-project'); await page.keyboard.press('Escape').catch(()=>{});
 await page.goto(clientUrl + '/client/settings', {waitUntil:'networkidle'}); await snap(page,'client-settings-general');
 await browser.close();
})();
