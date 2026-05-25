const { chromium } = require('playwright');
const fs = require('fs');
const OUT='outputs/app-real-product-correction';
async function dump(page,name){await page.screenshot({path:`${OUT}/raw/${name}.png`,fullPage:false}); fs.writeFileSync(`${OUT}/${name}.txt`, await page.locator('body').innerText().catch(e=>e.message));}
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}, storageState:`${OUT}/auth-state.json`});
 const page=await context.newPage();
 for(const url of ['https://app.oviond.com','https://app.oviond.com/clients','https://app.oviond.com/client','https://app.oviond.com/dashboard']){
   await page.goto(url,{waitUntil:'networkidle',timeout:60000}).catch(e=>console.log('goto fail', url, e.message));
   await page.waitForTimeout(3000);
   await dump(page, 'route-'+url.replace(/https:\/\/app\.oviond\.com\/?/,'').replace(/\W+/g,'_') || 'home');
   const text=await page.locator('body').innerText().catch(()=>'');
   console.log('ROUTE',url,'=>',page.url(), JSON.stringify(text.slice(0,300)));
 }
 for(const loc of [page.getByRole('link',{name:/clients/i}), page.getByRole('button',{name:/clients/i}), page.getByText(/^Clients$/i)]){try{await loc.first().click({timeout:3000}); await page.waitForTimeout(2000); break;}catch(e){}}
 await dump(page,'clients-before-add-2');
 const adders=[page.getByRole('button',{name:/add client/i}),page.getByRole('link',{name:/add client/i}),page.getByText(/add client/i),page.getByRole('button',{name:/new client/i}),page.getByText(/new client/i),page.locator('button').filter({hasText:/^\+$/})];
 let ok=false;
 for(const loc of adders){try{await loc.first().click({timeout:5000}); ok=true; break;}catch(e){}}
 await page.waitForTimeout(2500);
 await dump(page,'add-client-open-2');
 console.log('clickedAdd',ok,'url',page.url(), JSON.stringify((await page.locator('body').innerText().catch(()=>'')).slice(0,500)));
 await browser.close();
})();
