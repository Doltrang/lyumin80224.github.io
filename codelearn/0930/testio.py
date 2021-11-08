with open('data.txt','r') as fr:
    with open('data2.txt','w') as fw:
        print(fr.read())
        fr.seek(0)
        fw.write(fr.read())