import requests

#https://discord.com/api/v9/channels/906478400921817102/messages URL for main channel

header = {
    'authorization': ''
}

def postMessageGeneral(classNum):
    payload = {
        'content': "@everyone " + str(classNum) + " seat currently available!"
    }
    requests.post('', data=payload, headers=header)

# This method is completely optional, I set it up so that the bot posts a message when you first run the program.
# Feel free to reimplement it if desired or ignore it.
def BeginTesting():
    payload = {
        'content': "Beginning Testing..."
    }
    requests.post('', data=payload, headers=header)
