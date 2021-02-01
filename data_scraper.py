import asyncio
from playwright import async_playwright
import pandas as pd


class DataScraper:

    async def scrape(self):
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            context = await browser.newContext(acceptDownloads=True)
            page = await context.newPage()
            await page.goto("https://go.illinois.edu/COVIDTestingData")

            await page.hover("text=\"Daily New Cases\"")
            await page.click("//div[3]/div/div/div[2]/div/div[3]/div/a[1][normalize-space(.)='Export']/i")
            async with page.expect_download() as download_info:
                await page.click("div[aria-label=\"Modal footer\"] >> text=\"Export\"")
            download = await download_info.value
            cases_df = pd.read_csv(await download.path())

            await page.hover("text=\"Total Daily Tests Results\"")
            await page.click("//div[4]/div/div/div[2]/div/div[3]/div/a[1][normalize-space(.)='Export']/i")
            async with page.expect_download() as download_info:
                await page.click("div[aria-label=\"Modal footer\"] >> text=\"Export\"")
            download = await download_info.value
            tests_df = pd.read_csv(await download.path())

            await page.close()
            await context.close()
            await browser.close()

            self.df = pd.concat(
                [cases_df[["_time", "New Cases"]], tests_df["Total Daily Tests Results"]], axis=1)
            self.positivity_rate = df["New Cases"].tail(
                7).sum() / df["Total Daily Tests Results"].tail(7).sum()
            self.total_tests = df["Total Daily Tests Results"].sum()
