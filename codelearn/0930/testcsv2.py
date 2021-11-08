import csv
with open('MFI94U.csv',encoding='big5') as f:
    print('日期\t\t發行量加權股價報酬指數')
    for row in csv.DictReader(list(f)[1:]):
        print(row['日\u3000期'],row['發行量加權股價報酬指數'],sep='\t')