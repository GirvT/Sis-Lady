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
