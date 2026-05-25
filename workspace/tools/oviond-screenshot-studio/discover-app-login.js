const { chromium } = require('playwright');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:980}});
 page.on('console', msg=>console.log('CONSOLE', msg.type(), msg.text().slice(0,200)));
 page.on('requestfailed', req=>console.log('REQFAIL', req.method(), req.url(), req.failure()?.errorText));
 await page.goto('https://app.oviond.com', {waitUntil:'networkidle', timeout:90000});
 await page.screenshot({path:'outputs/raw/app-login-discovery.png', fullPage:false});
 console.log('URL', page.url());
 console.log(await page.locator('body').innerText({timeout:10000}).catch(e=>'BODY_ERR '+e.message));
 console.log('inputs', await page.locator('input').evaluateAll(els=>els.map(e=>({type:e.type, placeholder:e.placeholder, name:e.name, aria:e.getAttribute('aria-label'), value:e.value}))));
 console.log('buttons', await page.locator('button').evaluateAll(els=>els.slice(0,20).map(e=>({text:e.innerText, type:e.type}))));
 await browser.close();
})();
