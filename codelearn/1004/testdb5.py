import pandas as pd
from sqlalchemy import create_engine
connstr = 'mysql+mysqlconnector://root:Tcfst123456!@localhost:3306/mydb'
engine = create_engine(connstr)
url='https://od.cdc.gov.tw/eic/Age_County_Gender_19Cov.csv'
df = pd.read_csv(url,encoding='utf8')
mask = df.發病年份==2020
print(df[mask])
df[mask].to_sql('cov2020',engine,index=False,if_exists='replace')