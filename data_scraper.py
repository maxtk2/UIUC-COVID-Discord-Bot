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
        home_page = browser.get('https://covid19.illinois.edu/on-campus-covid-19-testing-data-dashboard/')
        home_html = browser.page_source
        homeSoup = BeautifulSoup(home_html, 'lxml')
        link = homeSoup.find('a', href=True, text='View the Testing Data Dashboard here')
        url = link.get('href')
        data_page = browser.get(url)
        time.sleep(4) # This is bad, but was the only way I could get the page to load before scraping.
        data_html = browser.page_source
        dataSoup = BeautifulSoup(data_html, 'lxml')
        data_divs = dataSoup.find_all('text', {"class": "single-result"})

        self.total_tests = data_divs[0].text
        self.positivity_rate = data_divs[1].text
        browser.quit()
