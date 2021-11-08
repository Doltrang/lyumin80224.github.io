import csv
with open('MFI94U.csv',encoding='big5') as f:
    print('日期\t\t發行量加權股價報酬指數')
    for row in csv.reader(list(f)[2:]):
        print(row[0],row[1],sep='\t')