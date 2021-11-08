with open('123.jpg','rb') as fr:
    with open('1234.jpg','wb') as fw:
        fw.write(fr.read())