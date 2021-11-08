import dataset
db = dataset.connect('sqlite:///nobel_prize.db')
db['winners'].drop()

print(list(db['winners'].find()))