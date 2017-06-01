import werobot

robot = werobot.WeRoBot(token='kongyi')

@robot.handler
def hello(message):
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '192.168.1.1'
robot.config['PORT'] = 80
robot.run()