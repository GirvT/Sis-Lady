import discord
import os
from numpy import zeros
from requests import get

def chunkMessage(message: str) -> list:
    '''
    Given a string that is more than 2000 characters,
    Return a list of 2000 characters or less strings that contain
    each part of the original string.
    '''
    chunkList = list()
    #if the message is too long
    while len(message) > 2000:
        #Find the nearest whitespace for this chunk
        idx = message[:2000].rfind(" ")
        chunkList.append(message[:idx])
        
        #Slice the message once we have chunked it
        message = message[idx:]
    chunkList.append(message)
    return chunkList

def getDump(link):
    response = get(link)
    if response.status_code == 200:
        dump = response.json()
    else:
        dump = response.status_code
    return dump  

def generateEmbed(title, desc, image='https://cdn.discordapp.com/embed/avatars/0.png'):
    embed = discord.Embed(title=title, description=desc)
    embed.set_image(url=image)
    embed.add_field(name="Value", value="Value of thing")
    embed.add_field(name="Inline Value", value="Inline Value of thing", inline=True)
    return embed

def levenshtein(a, b):
    mtx = zeros((len(a) + 1, len(b) + 1))
    mtx[:, 0] = list(range(len(a) + 1))
    mtx[0] = list(range(len(b) + 1))
    for x in range(1, len(a) + 1):
        for y in range(1, len(b) + 1):
            floor = min(mtx[x-1, y] + 1, mtx[x, y-1] + 1)
            if a[x-1] == b[y-1]:
                mtx [x,y] = min(floor, mtx[x-1, y-1])
            else:
                mtx [x,y] = min(floor, mtx[x-1,y-1] + 1)
    return (mtx[len(a), len(b)])

def relPath(rel_dir, rel_path):
    fixed_dir =  os.path.abspath(os.path.dirname(rel_dir))
    return fixed_dir + rel_path