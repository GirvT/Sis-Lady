import youtube_dl

def playURL(ctx, url):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = await voice_client.create_ytld_player(url)
    player.start()