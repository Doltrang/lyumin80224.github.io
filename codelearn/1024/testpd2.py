import pandas as pd
df = pd.read_json('nobel_winners.json')
df = df.set_index('year')
print(df.columns)
print(df.index)
print(df.loc[1901])