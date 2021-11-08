text='Hello'
print(list(enumerate(text)))
for n,t in enumerate(text):
    print(n,t)
print('----------------------------------------')
text='Hello'
print(list(enumerate(text,1)))
for n,t in enumerate(text,1):
    print(n,t)