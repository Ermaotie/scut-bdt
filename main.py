#coding=utf-8

import werobot
from function import *
from urllib import request
import os

robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wxccd39fd7bd00f08d"
robot.config["APP_SECRET"] = "8794656c2edb03f116fd1c49c394a1ff"
# robot.config["APP_ID"] = "wx7407f5c28abc23c0"
# robot.config["APP_SECRET"] = "0b0e1bf34d4253ff1e550830da0818f8"

@robot.filter('订阅通知')
def subscribe():
    return '欢迎订阅包打听'


@robot.text
def sub(message):
    text = message.content
    if "添加关键词" in text:
        text = text.split()
        try:
            if text[1]=="图片":
                request.urlretrieve(text[3], r"./demo.jpg")
                media_id = robot.client.upload_media("image", open(r"./demo.jpg", "rb"))['media_id']
                text[3] = media_id
                os.remove(r"./demo.jpg")
            res = insertKeyword(text)
        except:
            return "格式有误"
    elif "取消关键词" in text:
        text = text.split()
        try:
            res = cancelKeyword(text[1])
        except:
            res = "取消失败"
    else:
        res = checkout(text,message)
    return res

@robot.subscribe
def subscribe():
    message = '欢迎关注华工包打听'
    return message


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
