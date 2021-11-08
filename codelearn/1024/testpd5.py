import pandas as pd
url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'
df = pd.read_csv(url,encoding='utf8')
df_grp =df.groupby('county')
print(df_grp.groups.keys())
cy_grp =df_grp.get_group('嘉義市')
print(cy_grp)

print(df_grp.agg(['mean','count','std','max','min','sum','median']))