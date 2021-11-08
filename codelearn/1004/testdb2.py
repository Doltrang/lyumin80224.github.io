import pandas as pd
url='https://od.cdc.gov.tw/eic/Age_County_Gender_19Cov.csv'
df = pd.read_csv(url,encoding='utf8')
# mask = df.發病年份==2020
# print(df[mask])

# df[mask].to_csv('cov19_2020.csv',encoding='big5',index=False)
print(df.index)
df.index+=1
mask = df.發病年份==2020
print(df[mask])
df[mask].to_csv('cov19_2020.csv',encoding='big5')