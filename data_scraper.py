import asyncio
from pyppeteer import launch

class DataScraper:

    async def scrape(self):

        browser = await launch()
        page = await browser.newPage()
        await page.goto('https://go.illinois.edu/COVIDTestingData')
        await page.waitFor(2000)
        single_results = await page.querySelectorAllEval('text.single-result', 'elem=>elem.map(item=>item.textContent)')
        self.total_tests, self.positivity_rate = single_results

        await browser.close()
