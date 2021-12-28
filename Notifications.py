import requests

#https://discord.com/api/v9/channels/906478400921817102/messages URL for main channel

header = {
    'authorization': 'OTA2NDc3NDQ2MDA4ODE5NzEz.YYZNsw.6VjP8ne-jtdROB2gfZnz9xWRqiE'
}

def postMessageGeneral(classNum):
    payload = {
        'content': "@everyone " + str(classNum) + " seat currently available!"
    }
    requests.post('https://discord.com/api/v9/channels/906478400921817102/messages', data=payload, headers=header)

def BeginTesting():
    payload = {
        'content': "Beginning Testing..."
    }
    requests.post('https://discord.com/api/v9/channels/906609313978675230/messages', data=payload, headers=header)