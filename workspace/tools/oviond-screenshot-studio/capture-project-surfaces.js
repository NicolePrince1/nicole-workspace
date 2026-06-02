const { chromium } = require('playwright');
const fs = require('fs');
const OUT='outputs/help-center-rollout';
fs.mkdirSync(`${OUT}/raw`, {recursive:true});
async function snap(page,name){await page.waitForTimeout(1500); await page.screenshot({path:`${OUT}/raw/${name}.png`, fullPage:false}); fs.writeFileSync(`${OUT}/raw/${name}.txt`, await page.locator('body').innerText().catch(e=>e.message)); console.log('snap', name, page.url());}
async function click(page, locator, name){try{await locator.first().click({timeout:8000}); await snap(page,name); return true;}catch(e){console.log('skip', name, e.message.split('\n')[0]); return false;}}
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}, storageState:'outputs/app-real-product-correction/auth-state.json'});
 const page=await context.newPage();
 await page.goto('https://app.oviond.com/mwWXbBjNSJhM5kFUV/projects', {waitUntil:'networkidle', timeout:60000}); await snap(page,'client-projects-list');
 await click(page, page.getByRole('button',{name:/add project/i}), 'project-add-drawer'); await page.keyboard.press('Escape').catch(()=>{});
 await page.goto('https://app.oviond.com/mwWXbBjNSJhM5kFUV/projects', {waitUntil:'networkidle', timeout:60000});
 await click(page, page.getByText(/Digital Marketing Dashboard/i), 'project-dashboard-open');
 // Try common project controls if present.
 for(const [name,re] of [['project-edit',/edit/i],['project-share',/share/i],['project-export',/export|pdf/i],['project-add-widget',/add widget|widget/i]]){
   await click(page, page.getByRole('button',{name:re}), name);
   await page.keyboard.press('Escape').catch(()=>{});
 }
 await browser.close();
})();
