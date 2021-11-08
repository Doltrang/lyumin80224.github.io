nobel_winners = [
{'category': 'Physics',
'name': 'Albert Einstein',
'nationality': 'Swiss',
'sex': 'male',
'year': 1921},
{'category': 'Physics',
'name': 'Paul Dirac',
'nationality': 'British',
'sex': 'male',
'year': 1933},
{'category': 'Chemistry',
'name': 'Marie Curie',
'nationality': 'Polish',
'sex': 'female',
'year': 1911}
]


from pymongo import MongoClient
client= MongoClient()
db = client.nobel_prize #nobel_prize資料庫
coll = db.winners       #winners資料集Collection
# coll.insert_many(nobel_winners)
# coll.insert_one({'category': 'Chemistry',
# 'nationality': 'USA',
# 'age': 60})
coll.insert_one( {'category': 'Peace', 'link':'https://xxx.xxx.xxx.xx'} )