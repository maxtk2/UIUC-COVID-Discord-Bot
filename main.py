import time
from discord.ext import commands
import discord
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

now = datetime.now() # current date and time
today_date = now.strftime("%m/%d/%Y")

session = webdriver.Chrome()
prefix = '-' # Used to call commands on the bot
bot = commands.Bot(command_prefix=prefix)

positivityRate = 'DEFAULT_RATE'
totalTests = 0

browser = webdriver.Chrome()
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
totalTests = data_divs[0].text
positivityRate = data_divs[1].text


@bot.event
async def on_ready():
    print('UIUC COVID DATA BOT IS ONLINE')


@bot.command(name='ping')
async def ping(ctx):
    '''
    Prints the ping of the bot.
    '''

    latency = bot.latency
    await ctx.send('Pong!! jk.\n\nPing is: ' + str(latency))


@bot.command(name='data')
async def data(ctx):
    '''
    Prints current covid data for UIUC.
    '''

    embed = discord.Embed(title='Covid Data for ' + today_date,
                          description='',
                          color=0xff9705,
                          url="https://covid19.illinois.edu/on-campus-covid-19-testing-data-dashboard/")
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Illinois_Fighting_Illini_logo.svg/800px-Illinois_Fighting_Illini_logo.svg.png")
    embed.add_field(name='7-day positivity rate', value=positivityRate)
    embed.add_field(name='Total tests', value=str(totalTests))
    embed.set_footer(text='Make sure to wear your mask and practice social distancing!')
    await ctx.send(embed=embed)

bot.run('INPUT_KEY_HERE') # Token for the bot that would allow me to login. Kept private for security
