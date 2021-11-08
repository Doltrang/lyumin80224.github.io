import pickle

with open('data.pickle','rb') as fr:
    data=pickle.load(fr)
    print(data)