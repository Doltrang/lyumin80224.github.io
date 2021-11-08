text = 'Hello'
nums = range(len(text))

print(list(text))
print(list(nums))

print(list(zip(nums,text)))

for n,t in zip(nums,text):
    print(n,t)

for n,t in zip(range(len(text)),text):
    print(n,t)
print('------------------------------------------------')
text = 'Hello'
nums = range(1,len(text)+1)

print(list(text))
print(list(nums))

print(list(zip(nums,text)))

for n,t in zip(nums,text):
    print(n,t)

for n,t in zip(range(len(text)),text):
    print(n,t)