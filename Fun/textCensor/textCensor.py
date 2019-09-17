def _importText_(path):
    censorText = list()
    f = open(path, "r",  encoding="utf8")
    for line in f:
        censorText.append(line.rstrip('\n').lower())
    f.close()
    return censorText

def textCensor(message):
    censorText = _importText_('text.txt')
    for word in censorText:
        if word in message.content.lower():
            await message.delete()
            await message.channel.set_permissions(message.author, read_messages=True, send_messages=False)
