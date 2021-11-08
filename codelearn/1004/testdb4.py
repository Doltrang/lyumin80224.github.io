import pandas as pd
from sqlalchemy import create_engine
connstr = 'mysql+mysqlconnector://root:Tcfst123456!@localhost:3306/cmdev'
engine = create_engine(connstr)
df = pd.read_sql('SELECT * FROM emp',engine)
print(df)
df.to_csv('emp.csv',encoding='utf8',index=False)