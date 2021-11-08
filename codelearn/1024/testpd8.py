import pandas as pd
from sqlalchemy import create_engine
df = pd.read_json('nobel_winners.json')
engine=create_engine("mysql+pymysql://root:Tcfst123456!@localhost:3306/mydb2")
df.to_sql('nobel_winners',engine,index=False)