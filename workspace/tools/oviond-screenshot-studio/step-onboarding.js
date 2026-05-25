const { chromium } = require('playwright');
const fs = require('fs');
const OUT='outputs/app-real-product-correction';
async function cont(page){
 const b=page.getByRole('button',{name:/continue|finish/i}).first();
 await b.waitFor({state:'visible', timeout:10000});
 await page.waitForFunction(() => [...document.querySelectorAll('button')].some(b => /continue|finish/i.test(b.innerText) && !b.disabled), null, {timeout:10000}).catch(()=>{});
 await b.click({timeout:10000});
 await page.waitForTimeout(1500);
}
async function dump(page, name){ await page.screenshot({path:`${OUT}/raw/${name}.png`, fullPage:false}); fs.writeFileSync(`${OUT}/${name}.txt`, await page.locator('body').innerText().catch(e=>e.message)); }
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}, storageState:`${OUT}/auth-state.json`});
 const page=await context.newPage();
 await page.goto('https://app.oviond.com/onboarding',{waitUntil:'networkidle', timeout:60000});
 for(let i=1;i<=8;i++){
  await dump(page,`real-onboarding-${i}-before`);
  const text=await page.locator('body').innerText().catch(()=>'');
  console.log('\nSTEP',i,page.url(),JSON.stringify(text.slice(0,300)));
  const inputs=await page.locator('input:visible').all();
  console.log('visible inputs', inputs.length, await page.locator('input:visible').evaluateAll(els=>els.map(e=>({name:e.name,id:e.id,placeholder:e.placeholder,value:e.value,type:e.type}))));
  if(/What should we call you|Full Name/i.test(text)) { await page.locator('input[name="name"], #onboarding-name, input').first().fill('Nicole Prince'); await cont(page); continue; }
  if(/first client|Client Name/i.test(text) && inputs.length) { if(inputs[0]) await inputs[0].fill('QA Screenshot Client'); if(inputs[1]) await inputs[1].fill('qa-screenshot.example.com'); await cont(page); continue; }
  if(/website|domain/i.test(text) && inputs.length) { await inputs[0].fill('oviond.com'); await cont(page); continue; }
  if(/how many/i.test(text)) { for(const loc of [page.getByText(/6\s*-\s*20/i), page.getByText(/1\s*-\s*5/i), page.locator('input[name="client_count"][value="6 to 20"]')]) { try { await loc.first().click({timeout:3000}); break;} catch{} } await cont(page); continue; }
  if(/company/i.test(text) && inputs.length) { await inputs[0].fill('Nicole QA Agency'); await cont(page); continue; }
  if(/template|dashboard|report|ready|finish/i.test(text)) { for(const loc of [page.getByText(/digital marketing/i), page.getByText(/blank/i), page.locator('button').filter({hasText:/continue|finish/i})]) { try { await loc.first().click({timeout:3000}); await page.waitForTimeout(500); break; } catch{} } await cont(page).catch(()=>{}); continue; }
  break;
 }
 await dump(page,'after-onboarding-final');
 await context.storageState({path:`${OUT}/auth-state.json`});
 await browser.close();
})();
