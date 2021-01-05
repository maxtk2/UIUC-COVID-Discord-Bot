from discord.ext import commands
prefix = ">"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("UIUC COVID DATA BOT IS ONLINE")

@bot.event
async def on_message(message):
    message.content.lower()
    if message.author == bot.user:
        return
    if message.content.startswith("deez"):
        await message.channel.send("Nuts!")

@bot.command(name='ping')
async def ping(ctx):
    '''
    Prints the ping of the bot.
    '''

    latency = bot.latency
    await ctx.send(latency)

bot.run('Nzk1NzEwNDU2Mjk1MTk0NjQ0.X_NVHA.I9E22zdenClo_9oI4dUW9Haopio')
