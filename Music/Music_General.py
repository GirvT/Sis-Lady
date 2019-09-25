import youtube_dl
def joinChannel(ctx):
    user = ctx.message.author
    channel = user.voice_channel
    await channel.connect()

def leaveChannel(bot, ctx):
    channel = bot.voice_client
    await channel.disconnect()

def playURL(bot, ctx, url):
    voice_client = bot.voice_client
    player = await voice_client.create_ytld_player(url)
    player.start()