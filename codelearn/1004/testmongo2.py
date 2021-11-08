from pymongo import MongoClient
client= MongoClient()
db = client.nobel_prize #nobel_prize資料庫
coll = db.winners       #winners資料集Collection
print(list(coll.find({'category':'Physics'})))
print(list(coll.find({'age':{'$gt':0}}))) #age>0
print(list(coll.find({'age':60})))