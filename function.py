#coding=utf-8
import pymongo


client = pymongo.MongoClient("mongodb+srv://Ermaotie:Ermaotie@cluster0.xvlrf.mongodb.net/scut-bdt?retryWrites=true&w=majority")
db = client['scut-bdt']
collection = db['keywords']


def checkout(text):
    key = collection.find_one({'keyword': text})
    if key == None:
        return "没有该关键词"
    else:
        return key['value']


def insertKeyword(key,value):
    doc = {'keyword':key,'value':value}
    collection.insert_one(doc)
    res = checkout(key)
    if res == "没有该关键词":
        return "添加失败"
    else:
        return "添加成功"
