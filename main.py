from discord.ext import commands, tasks
import discord
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import config
from data_scraper import DataScraper
from pathlib import Path

Path("images").mkdir(parents=True, exist_ok=True)

bot = commands.Bot(command_prefix=config.prefix)

data_scraper = DataScraper()


@bot.event
async def on_ready():
    print('UIUC COVID DATA BOT IS ONLINE')
    scrape.start()


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

    today_date = datetime.now().strftime("%m/%d/%Y")
    embed = discord.Embed(title='Covid Data for ' + today_date,
                          description='',
                          color=0xff9705,
                          url="https://covid19.illinois.edu/on-campus-covid-19-testing-data-dashboard/")
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Illinois_Fighting_Illini_logo.svg/800px-Illinois_Fighting_Illini_logo.svg.png")
    embed.add_field(name='7-day positivity rate',
                    value='{:0.2f}%'.format(data_scraper.positivity_rate * 100))
    embed.add_field(name='Total tests', value='{:,}'.format(
        data_scraper.total_tests))
    embed.set_footer(
        text='Make sure to wear your mask and practice social distancing!')
    await ctx.send(embed=embed)


@bot.command(name='graph')
async def graph(ctx):
    '''
    Displays a graph of case positivity % over time.
    '''

    plt.style.use('dark_background')
    dates = matplotlib.dates.date2num(data_scraper.df['_time'])
    plt.plot_date(dates, 100 * data_scraper.df["New Cases"] /
                  data_scraper.df["Total Daily Tests Results"], '-')
    plt.xlabel('Date')
    plt.ylabel('Daily Positivity %')
    plt.savefig('images/graph.png', transparent=True)
    plt.close()

    await ctx.send(file=discord.File('images/graph.png'))

# Should loop once a day


@tasks.loop(seconds=30)
async def scrape():
    print("Starting scrape")
    await data_scraper.scrape()
    print("Done scraping")


# Token for the bot that would allow me to login. Kept private for security
bot.run(config.token)
