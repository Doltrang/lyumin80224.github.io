data = [[10,20],[30,40],[50,60],[70,80]]
data2 =[]
for d1 in data:
    # print(d1)
    for d2 in d1:
        data2.append(d2)
        # print(d2)
print(data2)

print([d2 for d1 in data for d2 in d1])