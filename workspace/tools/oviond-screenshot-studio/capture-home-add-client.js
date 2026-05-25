const { chromium } = require('playwright');
const fs = require('fs');
const OUT='outputs/app-real-product-correction';
async function dump(page,name){await page.screenshot({path:`${OUT}/raw/${name}.png`,fullPage:false}); fs.writeFileSync(`${OUT}/${name}.txt`, await page.locator('body').innerText().catch(e=>e.message));}
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}, storageState:`${OUT}/auth-state.json`});
 const page=await context.newPage();
 await page.goto('https://app.oviond.com/',{waitUntil:'networkidle',timeout:60000});
 await page.waitForTimeout(2000);
 await dump(page,'real-clients-home');
 await page.getByRole('button',{name:/add client/i}).click({timeout:10000});
 await page.waitForTimeout(2000);
 await dump(page,'real-add-client-modal');
 console.log('url',page.url());
 console.log(await page.locator('body').innerText());
 await browser.close();
})();
