from ...Tools.Tools_General import chunkMessage # pylint: disable=relative-beyond-top-level

def _importTranslation_(path):
    import json
    with open(path, 'r') as JSON:
        return json.load(JSON)

def translate(message):
    json_dict = _importTranslation_('tranlation.json')
    sendMsg = ''
    for i in message.content.lower():
        if i in json_dict:
            sendMsg += ':' + json_dict[i] + ":"
        elif i.isnumeric():
            sendMsg += ":" + json_dict[i] + ":"
        elif i.isalpha():
                sendMsg += ":regional_indicator_" + i + ":"
        else:
            sendMsg += '         '
        sendMsg += ' '
    for chunk in chunkMessage(sendMsg):
        if chunk:
            await message.channel.send(chunk)