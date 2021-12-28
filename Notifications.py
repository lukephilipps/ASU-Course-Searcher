import requests

header = {
    'authorization': '"""paste discord account authorization code here between single quotes"""'
}

# This method posts a message to a discord channel provided you put the channels url in the post method
# The classNum parameter is so that the message can contain which class is open since you can check for multiple at once
def postMessageGeneral(classNum):
    payload = {
        'content': "@everyone " + str(classNum) + " seat currently available!"
    }
    requests.post('"""paste discord channel url here between single quotes"""', data=payload, headers=header)

# This method is completely optional, I set it up so that the bot posts a message when you first run the program.
# Feel free to reimplement it if desired or ignore it.
"""def BeginTesting():
    payload = {
        'content': "Beginning Testing..."
    }
    requests.post(''"""paste discord channel url here between single quotes"""'', data=payload, headers=header)
"""
