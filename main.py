from discord.ext import commands
import discord
from datetime import datetime
import config
from data_scraper import DataScraper

now = datetime.now() # current date and time
today_date = now.strftime("%m/%d/%Y")

bot = commands.Bot(command_prefix=config.prefix)

data_scraper = DataScraper()
data_scraper.scrape()

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
    embed.add_field(name='7-day positivity rate', value=data_scraper.positivity_rate)
    embed.add_field(name='Total tests', value=str(data_scraper.total_tests))
    embed.set_footer(text='Make sure to wear your mask and practice social distancing!')
    await ctx.send(embed=embed)

bot.run(config.token) # Token for the bot that would allow me to login. Kept private for security
