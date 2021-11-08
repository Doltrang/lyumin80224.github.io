import pandas as pd
from sqlalchemy import create_engine
connstr = 'mysql+mysqlconnector://root:Tcfst123456!@localhost:3306/mydb'
engine = create_engine(connstr)
# df = pd.read_sql('SELECT * FROM emp2',engine)
# print(df)
df = pd.read_csv('Age_County_Gender_19Cov.csv',encoding='utf8')
print(df)
df.to_sql('cov19',engine,index=False,if_exists='replace') #if_exists='replace' 蓋掉原資料
