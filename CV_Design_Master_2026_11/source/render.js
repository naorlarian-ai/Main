// Render an HTML CV to PDF with headless Chromium and report layout metrics.
// Usage: node render.js <input.html> <output.pdf>
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [, , input, output] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input));
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });

  const metrics = await page.evaluate(() => {
    const pt = (px) => +(px * 0.75).toFixed(1);           // CSS px -> pt
    const pageEl = document.getElementById('page');
    const pr = pageEl.getBoundingClientRect();
    const padBottom = parseFloat(getComputedStyle(pageEl).paddingBottom);
    const limit = pr.bottom - padBottom;
    const colBottom = (sel) => {
      const kids = document.querySelectorAll(sel + ' > *');
      let b = 0; kids.forEach(k => { b = Math.max(b, k.getBoundingClientRect().bottom); });
      return b;
    };
    const main = colBottom('.col--main'), side = colBottom('.col--side');
    const fontsLoaded = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.weight + f.style);
    return {
      page_overflow: pageEl.scrollHeight > pageEl.clientHeight + 1,
      main_bottom_pt: pt(main - pr.top), side_bottom_pt: pt(side - pr.top),
      content_limit_pt: pt(limit - pr.top),
      main_slack_pt: pt(limit - main), side_slack_pt: pt(limit - side),
      fonts_loaded: fontsLoaded,
    };
  });

  await page.pdf({ path: output, preferCSSPageSize: true, printBackground: true });
  await browser.close();
  console.log(JSON.stringify(metrics));
})();
