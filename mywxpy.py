from wxpy import *
import requests

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_joke_response(msg):

    apiUrl = 'http://www.tuling123.com/openapi/api'

    data = {
        "key": KEY,
        "info": msg
    }

    try:
        r = requests.post(apiUrl,data = data).json()
        return r.get('text')
    except:
        return

bot = Bot(console_qr=-2)

my_friend = bot.friends().search("吹～_～风")

my_qun = bot.groups().search("老汉推车")


@bot.register(my_qun)
def reply_my_friend(msg):

    defaultReply = 'I received: ' + msg.text
    # print('------' + msg.chat + '++++++' + msg.text)
    reply = get_joke_response(msg.text)

    return reply or defaultReply

embed()