const { chromium } = require('playwright');
const fs = require('fs');
const OUT='outputs/help-center-rollout';
fs.mkdirSync(`${OUT}/raw`, {recursive:true});
async function snap(page,name){await page.waitForTimeout(1500); await page.screenshot({path:`${OUT}/raw/${name}.png`, fullPage:false}); fs.writeFileSync(`${OUT}/raw/${name}.txt`, await page.locator('body').innerText().catch(e=>e.message));}
async function clickText(page, re, name){try{await page.getByText(re).first().click({timeout:5000}); await snap(page,name); console.log('clicked text', name, page.url()); return true;}catch(e){console.log('skip',name,e.message.split('\n')[0]); return false;}}
async function clickRole(page, role, re, name){try{await page.getByRole(role,{name:re}).first().click({timeout:5000}); await snap(page,name); console.log('clicked role', name, page.url()); return true;}catch(e){console.log('skip',name,e.message.split('\n')[0]); return false;}}
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}, storageState:'outputs/app-real-product-correction/auth-state.json'});
 const page=await context.newPage();
 await page.goto('https://app.oviond.com/', {waitUntil:'networkidle', timeout:60000}); await snap(page,'home-clients');
 console.log('home text', (await page.locator('body').innerText()).slice(0,500));
 console.log('links/buttons', await page.locator('a,button').evaluateAll(els=>els.map((e,i)=>({i,tag:e.tagName,text:e.innerText.trim(),href:e.href||'', disabled:e.disabled})).filter(x=>x.text).slice(0,100)));
 const nav=[['Templates',/^Templates$/i],['Automations',/^Automations$/i],['Settings',/^Settings$/i],['AI Connectors',/^AI Connectors$/i],['Help',/^Help$/i],['Notifications',/^Notifications$/i]];
 for(const [name,re] of nav){ await page.goto('https://app.oviond.com/', {waitUntil:'networkidle'}); await clickText(page,re,`nav-${name.toLowerCase().replace(/\W+/g,'-')}`); }
 await page.goto('https://app.oviond.com/', {waitUntil:'networkidle'}); await clickRole(page,'button',/add client/i,'modal-add-client'); await page.keyboard.press('Escape').catch(()=>{});
 await page.goto('https://app.oviond.com/', {waitUntil:'networkidle'}); await clickText(page,/Open/i,'client-open');
 console.log('client links/buttons', await page.locator('a,button').evaluateAll(els=>els.map((e,i)=>({i,tag:e.tagName,text:e.innerText.trim(),href:e.href||'', disabled:e.disabled})).filter(x=>x.text).slice(0,100)));
 for(const [name,re] of [['Projects',/^Projects$/i],['Settings',/^Settings$/i],['Home',/^Home$/i]]){ await clickText(page,re,`client-${name.toLowerCase()}`); }
 await clickRole(page,'button',/add project/i,'modal-add-project');
 await browser.close();
})();
