const { chromium } = require('playwright');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:980}, storageState:'outputs/app-real-product-correction/auth-state.json'});
 const page=await context.newPage();
 await page.goto('https://app.oviond.com/onboarding', {waitUntil:'networkidle', timeout:60000});
 await page.waitForTimeout(2000);
 console.log('url', page.url());
 console.log('body', await page.locator('body').innerText());
 console.log('inputs', await page.locator('input,textarea,[contenteditable=true]').evaluateAll(els=>els.map((e,i)=>({i, tag:e.tagName, type:e.getAttribute('type'), value:e.value||e.textContent, placeholder:e.getAttribute('placeholder'), name:e.getAttribute('name'), disabled:e.disabled, classes:e.className, html:e.outerHTML.slice(0,300)}))));
 console.log('buttons', await page.locator('button').evaluateAll(els=>els.map((e,i)=>({i,text:e.innerText,disabled:e.disabled,classes:e.className, html:e.outerHTML.slice(0,200)}))));
 await page.locator('input').first().fill('Nicole Prince');
 await page.waitForTimeout(500);
 console.log('after fill', await page.locator('input').first().inputValue());
 console.log('buttons2', await page.locator('button').evaluateAll(els=>els.map((e,i)=>({i,text:e.innerText,disabled:e.disabled,classes:e.className}))));
 await page.screenshot({path:'outputs/app-real-product-correction/raw/debug-after-fill.png', fullPage:false});
 await browser.close();
})();
