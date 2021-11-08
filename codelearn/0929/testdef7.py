data= ['abcd','BCD','cD']
print(sorted(data)) #B 66, a 97 ,c 99
print(sorted(data,key=len))
# print(ord('B'))
# print(ord('a'))
# print(ord('c'))
print(sorted(data,key=str.upper))
print(sorted(data,key=str.lower))