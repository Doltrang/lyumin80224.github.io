with open('Data.txt','rb') as f:
    print('位置 :',f.tell())
    for line in f:
        print('位置 :',f.tell())
        print(line,end='')
    f.seek(0)
    print()
    print(list(f))