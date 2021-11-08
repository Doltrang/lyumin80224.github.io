import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'
df=pd.read_csv(url,encoding='utf8')
x=list(df.Site.head(-5))
y=list(df.PM25.head(-5))
# print(x)
# print(y)

xlocation = np.array(range(len(y))) + 0.5 # + 右空白寬度
plt.bar(xlocation,y,width=0.5) # 資料間寬度
plt.xticks(xlocation,x)
plt.xlim((0,xlocation[-1]+0.5)) # xlocation[指定資料位置0為第1筆  -1最後一筆]  + 左空白寬度

plt.gca().get_xaxis().tick_top()
plt.gca().get_yaxis().tick_right()
plt.gcf().set_size_inches((20,10))
plt.show()