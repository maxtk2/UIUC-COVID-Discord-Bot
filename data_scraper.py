from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class DataScraper:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.headless = True


    def scrape(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        data_page = browser.get('https://go.illinois.edu/COVIDTestingData')
        time.sleep(4) # This is bad, but was the only way I could get the page to load before scraping.
        data_html = browser.page_source
        dataSoup = BeautifulSoup(data_html, 'lxml')
        data_divs = dataSoup.find_all('text', {"class": "single-result"})

        self.total_tests = data_divs[0].text
        self.positivity_rate = data_divs[1].text
        browser.quit()
