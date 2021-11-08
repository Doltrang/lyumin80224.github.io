import pandas as pd
import numpy as np
df = pd.read_json('nobel_winners.json')
df_phy =df[df.category == 'Physics']
print(df_phy)
print()
print(df[df.category == ''])
print
df.loc[104,'category'] = np.nan
print(df.loc[104])
print(df[df.category.isna()]) # 透過df.欄位.isna()找出欄位中null的資料
print()
df['year2']=df['year'] +10 #新增欄位 =舊欄位+10
print(df.head())
print()
df['year2']=np.log10(df['year']) #新增欄位 =舊欄位取log
print(df.head())