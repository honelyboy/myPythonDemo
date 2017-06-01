import requests
import itchat

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


def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    # 智能机器人接口
    apiUrl = 'http://www.tuling123.com/openapi/api'


    # 笑话机器人
    # apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT,isFriendChat=True, isGroupChat=True, isMpChat=True)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    print('------'+msg['FromUserName']+'++++++'+msg['Text'])
    if '@c2bafd07b878f7c877cde88efc08c792996eb87ad5c20d07edad3af00086224c'== msg['FromUserName']:
        reply = get_response(msg['Text'])
        # reply = get_joke_response(msg['Text'])
        return reply or defaultReply

    if '@@338c554136a1f8d28d72ef30e4e1e5102bc8f96ca51f6e765833a2d9b04dd13d' == msg['FromUserName']:
        reply = get_joke_response(msg['Text'])

        return reply or defaultReply


    if '@b3a02d09859aaa4662a853129b35d9b112bd298fb02558101870f57ff9b46d72' == msg['FromUserName']:
        reply = get_response(msg['Text'])
        return reply or defaultReply

    # if '@@338c554136a1f8d28d72ef30e4e1e5102bc8f96ca51f6e765833a2d9b04dd13d' == msg['FromUserName']:
    #
    #     reply = get_response(msg['Text'])
    #     return reply or defaultReply
    # 如果图灵Key出现问题，那么reply将会是None
    # reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    # return reply or defaultReply

@itchat.msg_register(itchat.content.PICTURE,isFriendChat=True, isGroupChat=True, isMpChat=True)
def tulin_pic_reply(msg):
    # print('++++++++'+msg['Picture'])
    print("picture--------")
    # if '@@338c554136a1f8d28d72ef30e4e1e5102bc8f96ca51f6e765833a2d9b04dd13d' == msg['FromUserName']:
    #     return itchat.send_image('/pic/desk_005.jpg')
    # itchat.send_image('gz.gif', toUserName=msg['FromUserName'])

    if '@c2bafd07b878f7c877cde88efc08c792996eb87ad5c20d07edad3af00086224c' == msg['FromUserName']:
        itchat.send_image('gz.gif', toUserName= msg['FromUserName'])
        return



# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(enableCmdQR=True)
itchat.run()
