from pymongo import MongoClient
client= MongoClient()
db = client.nobel_prize #nobel_prize資料庫
coll = db.winners       #winners資料集Collection
coll.update_one({'age':60,},{'$set':{'nationality':'USA'}})

print(list(coll.find()))