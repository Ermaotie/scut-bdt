#coding=utf-8
import pymongo
from werobot.replies import ArticlesReply, ImageReply, MusicReply, TextReply, Article

client = pymongo.MongoClient("mongodb+srv://Ermaotie:Ermaotie@cluster0.xvlrf.mongodb.net/scut-bdt?retryWrites=true&w=majority")
db = client['scut-bdt']
collection = db['keywords']

"""
暂定document的key
_id
type
time
根据type类型添加不同的键值
text --> content
img  --> media_id     需要提前上传到素材库，并获取id
article --> title,description,img,url

eg:
from werobot.replies import ArticlesReply, Article
reply = ArticlesReply(message=message)
article = Article(
    title="WeRoBot",
    description="WeRoBot是一个微信机器人框架",
    img="https://github.com/apple-touch-icon-144.png",
    url="https://github.com/whtsky/WeRoBot"
)
reply.add_article(article)
"""

def ImgReturn(key,message):
    return ImageReply(
        message,
        media_id=key['media_id']
    )

def ArticleReturn(key,message):
    article = Article(
        title=key["title"],
        description=key["description"],
        img=key["img"],
        url=key["url"]
    )
    reply = ArticlesReply(message)
    reply.add_article(article)
    return reply

def TextReturn(key,message):
    return key["content"]


def insertText(item):
    doc ={
        "keyword": item[1],
        "content": item[2]
    }
    collection.insert_one(doc)

def insertImg(item):
    doc = {
        "keyword": item[1],
        "media_id": item[2]
    }
    collection.insert_one(doc)

def insertArticle(item):
    doc = {
        "keyword": item[1],
        "title": item[2],
        "description": item[3],
        "img": item[4],
        "url": item[5]
    }
    collection.insert_one(doc)

def switch(key,message):
    cases = {
        "text": TextReturn,
        "img": ImgReturn,
        "article": ArticleReturn
    }

    method = cases.get(key['type'])
    if method:
        return method(key,message)

def checkout(text,message):
    item = collection.find_one({'keyword': text})
    if item is None:
        return "没有该关键词"
    else:
        return switch(item,message)


def insertKeyword(item):
    types = {
        "text": insertText,
        "img": insertImg,
        "article": insertArticle,
    }
    method = types.get(item[1])
    if method:
        method(item)
        return "添加成功"
    else:
        return "添加失败"


