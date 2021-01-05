from discord.ext import commands
import random
prefix = '-'
bot = commands.Bot(command_prefix=prefix)

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

bot.run('Nzk1NzEwNDU2Mjk1MTk0NjQ0.X_NVHA.ezGXi9wHlVXMFjfY2Uk-WMJlVXk')
