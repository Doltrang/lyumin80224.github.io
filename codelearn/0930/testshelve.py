import shelve
data = shelve.open('data.shelve')
data['A']=[10,20,30]
data['B']=[40,50,60]
data.close()