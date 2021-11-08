# import pandas as pd
# from sqlalchemy import create_engine
# engine=create_engine("mysql+pymysql://root:Tcfst123456!@localhost:3306/mydb2")
# df=pd.read_sql('nobel_winners',engine,index=False)
import pandas as pd
from pandas.io.sql import read_sql
df=pd.read_json('nobel_winners.json')
print(df.info())
print(df[(df.gender.isna()) & (df.category != 'Peace')])
print(df.loc[696])