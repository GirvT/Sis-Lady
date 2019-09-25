import discord
from discord.ext import commands
from APIs.mhw_db import searchMHW
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Edit these
TOKEN = "NjI2MTE3OTg1NTQ3MDU5MjAx.XYpb5A.N7P1oaGZUR_YSkK7SJfoDM0MMr0"
prefix = '>>'

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('Logged in as ' + TOKEN)

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.startswith(prefix):
            await bot.process_commands(message)
        else:
            pass
            #On message do thing

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

@bot.command()
async def MHW(ctx, message):
    await ctx.send(embed=searchMHW(message, context='items'))

bot.run(TOKEN)