from discord import Embed
import os
from numpy import zeros
from requests import get

def searchMHW(term, context=''):
    f = open(relPath(__file__, '/MHW/MHWDBurls.txt'), 'r')
    levenDict = dict()
    searchLength = [line[:-1] for line in f.readlines()]
    if context in searchLength:
        searchLength = [context]
    for i in searchLength:
        for j in getDump('https://mhw-db.com/' + i + '/'):
            levenDict[levenshtein(j['name'], term)] = (i, j)
    if levenDict[min(levenDict)][0] == 'items':
        embed = generateItemsEmbed(levenDict[min(levenDict)][1])
    else:
        embed = Embed(title='No Result!')
    return embed

def generateItemsEmbed(dump):
    embed = Embed(title=dump['name'], description=dump['description'])
    embed.add_field(name='Rarity', value=dump['rarity'], inline = True)
    embed.add_field(name='Carry Limit', value=dump['carryLimit'], inline = True)
    embed.add_field(name='Money value', value=str(dump['value']) + ' Z', inline = True)
    return embed

def getDump(link):
    response = get(link)
    if response.status_code == 200:
        dump = response.json()
    else:
        dump = response.status_code
    return dump  

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