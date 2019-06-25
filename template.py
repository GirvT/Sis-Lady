import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Edit these
TOKEN = ""
Botspace = 'sample-name'
prefix = '$'

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('Logged in as ' + TOKEN)

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.startswith(prefix):
            await bot.process_commands(message)
        elif message.channel.name == Botspace:
            #do bot stuff here

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

@bot.command()
async def createBotspace(ctx):
    createBotspace = True
    for channel in ctx.guild.channels:
        if channel.name == Botspace:
            createBotspace = False
    if (createBotspace):
        await ctx.guild.create_text_channel(Botspace)

bot.run(TOKEN)