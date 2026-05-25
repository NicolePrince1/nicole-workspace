const { chromium } = require('playwright');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}});
 const page=await context.newPage();
 await page.goto('https://app.oviond.com/signin', {waitUntil:'networkidle', timeout:90000});
 await page.locator('input[type="email"]').fill('nicole@oviond.com');
 await page.getByRole('button', {name:/magic link/i}).click();
 await page.waitForTimeout(5000);
 await page.screenshot({path:'outputs/raw/app-magic-link-requested.png', fullPage:false});
 console.log('URL', page.url());
 console.log(await page.locator('body').innerText().catch(e=>e.message));
 await browser.close();
})();
