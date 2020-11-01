#coding=utf-8
import pymongo


client = pymongo.MongoClient("mongodb+srv://Ermaotie:Ermaotie@cluster0.xvlrf.mongodb.net/scut-bdt?retryWrites=true&w=majority")
db = client['scut-bdt']
collection = db['keywords']
data = collection.find()
keys = collection.find_one({'keyword':'测试'})
print(keys['value'])


def checkout(text):
    key = collection.find_one({'keyword': text})
    if key == None:
        return "没有该关键词"
    else:
        return key['value']