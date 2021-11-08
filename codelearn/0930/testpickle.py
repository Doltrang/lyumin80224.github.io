import pickle
data = [10,20,30,40,50]

with open('data.pickle','wb') as fw:
    pickle.dump(data,fw)