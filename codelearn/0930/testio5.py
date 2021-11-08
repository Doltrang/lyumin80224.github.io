with open('data3.txt','r',encoding='utf8') as f:
    print(f.tell())
    for line in f:
        print(line)
    print(f.tell())
    f.close()
print('-----------------------------------')
with open('data3.txt','rb') as f:
    print(f.tell())
    for line in f:
        print(f.tell())
        print(line)
    print(f.tell())
    f.close()