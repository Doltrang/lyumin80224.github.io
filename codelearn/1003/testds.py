import dataset
db = dataset.connect('sqlite:///nobel_prize.db')
print(list(db['winners']))

# wtable = db['winners']
# winners = wtable.find()
# winners = list(winners)
# print(winners)