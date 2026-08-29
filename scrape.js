const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  // Navigate and wait for network to be idle
  await page.goto('https://roles.tv/u/tuk7', { waitUntil: 'networkidle2' });
  
  // Wait a bit for svelte to render the roles
  await page.waitForTimeout(3000);
  
  const roles = await page.evaluate(() => {
    // Looking at common class names for roles.tv... Let's just grab all text and images.
    // We want the streamer name, profile picture, and follower count.
    const cards = document.querySelectorAll('.role-card, .channel-card, .role, .channel, a[href^="/u/"]');
    let results = [];
    
    // A more generic approach: get all images and their adjacent text
    const elements = document.querySelectorAll('.roles-container a, main a');
    for (const el of elements) {
      const img = el.querySelector('img');
      const text = el.innerText;
      if (img && text && text.includes('followers')) {
        results.push({
          name: text.split('\n')[0].trim(),
          followers: text.match(/([\d,]+)\s*followers/i)?.[1] || '',
          image: img.src
        });
      }
    }
    
    // If the above fails, let's grab the raw HTML of the container
    return {
      structured: results,
      rawHtml: document.querySelector('.roles-container')?.innerHTML || document.body.innerHTML.substring(0, 5000)
    };
  });

  console.log(JSON.stringify(roles, null, 2));
  await browser.close();
})();
