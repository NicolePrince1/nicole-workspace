const { chromium } = require('playwright');
const fs = require('fs');

async function main(){
  const cfg = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: cfg.viewport || { width: 1440, height: 980 }, deviceScaleFactor: cfg.deviceScaleFactor || 1 });
  const page = await context.newPage();
  await page.goto(cfg.url, { waitUntil: cfg.waitUntil || 'networkidle', timeout: cfg.timeout || 60000 });
  if (cfg.waitForSelector) await page.waitForSelector(cfg.waitForSelector, { timeout: cfg.selectorTimeout || 30000 });
  if (cfg.hideSelectors) {
    await page.addStyleTag({ content: cfg.hideSelectors.map(s => `${s}{visibility:hidden!important}`).join('\n') });
  }
  if (cfg.evaluate) await page.evaluate(cfg.evaluate);
  await page.screenshot({ path: cfg.output, fullPage: !!cfg.fullPage });
  await browser.close();
  console.log(JSON.stringify({ output: cfg.output, url: cfg.url }));
}
main().catch(e => { console.error(e); process.exit(1); });
