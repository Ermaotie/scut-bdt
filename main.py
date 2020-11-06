#coding=utf-8

import werobot
from function import *
from urllib import request
import os

robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wx7407f5c28abc23c0"
robot.config["APP_SECRET"] = "0b0e1bf34d4253ff1e550830da0818f8"


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
            elif text[1] == "推文":
                request.urlretrieve(text[5], r"./demo.jpg")
                media_id = robot.client.upload_media("image", open(r"./demo.jpg", "rb"))['media_id']
                text[5] = media_id
                os.remove(r"./demo.jpg")
            res = insertKeyword(text)
        except:
            return "格式有误"
    else:
        res = checkout(text,message)
    return res

@robot.subscribe
def subscribe():
    message = '欢迎关注二茂铁Fe，如需订阅华工通知请发送\n订阅通知\n于本公众号。\n操作流程较长，若遇到问题请访问：\n https://1b.mk/2020/08/08/subscribe/'
    return message


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
