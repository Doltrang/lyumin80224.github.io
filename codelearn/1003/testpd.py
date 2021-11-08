import pandas as pd
url='https://od.cdc.gov.tw/eic/Age_County_Gender_19Cov.csv'
df = pd.read_csv(url,encoding='utf8')
print(df)
print(df.columns)

print(df.確定病例數.sum())

mask = df.縣市 == '空值' #遮罩
print(df[mask].確定病例數.sum()) #境外移入總人數

mask2 = (df.縣市 == '台北市')&(df.鄉鎮 == '大安區') #遮罩
print(df[mask2].確定病例數.sum()) #台北市大安區病例數總人數

mask3 = (df.縣市 == '台北市')&(df.鄉鎮 == '大安區')&(df.性別 == 'M') #遮罩
print(df[mask3].確定病例數.sum()) #台北市大安區男性病例數總人數

mask4 = (df.縣市 == '台北市')&(df.鄉鎮 == '大安區')&(df.性別 == 'F') #遮罩
print(df[mask4].確定病例數.sum()) #台北市大安區女性病例數總人數

print(df.info())

print('2020年男性病例總人數:',df[(df.發病年份==2020)&(df.性別=='M')].確定病例數.sum())
print('2020年女性病例總人數:',df[(df.發病年份==2020)&(df.性別=='F')].確定病例數.sum())
print('2021年男性病例總人數:',df[(df.發病年份==2021)&(df.性別=='M')].確定病例數.sum())
print('2021年女性病例總人數:',df[(df.發病年份==2021)&(df.性別=='F')].確定病例數.sum())