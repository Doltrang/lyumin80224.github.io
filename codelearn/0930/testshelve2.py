import shelve
data = shelve.open('data.shelve')
print(data['A'])
print(data['B'])
data['C']=[70,80,90]
data.close()