import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('MI_5MINS_HIST.csv',encoding='big5',skiprows=1)
# print(df.info())
df['日期2']=df['日期'].str.replace('110/','2021/')
# print(df['日期2'])
df['收盤指數2']=df['收盤指數'].str.replace(',','')
# print(df['收盤指數2'])
df[['日期2']]=df[['日期2']].astype('datetime64')
df['收盤指數2']=df['收盤指數2'].astype('float')
# x=pd.to_datetime(df['日期2'])
print(df.info())
x=df['日期2']
y=df['收盤指數2']
fig = plt.figure(figsize=(8,4))
# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
ax = fig.add_axes((0.1,0.1,0.8,0.8))
ax.plot(x,y)
ax.set_title('110年10月收盤指數')
ax.set_xlabel('日期')
ax.set_ylabel('收盤指數')
plt.show()