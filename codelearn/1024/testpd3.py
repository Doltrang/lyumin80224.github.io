import pandas as pd
df = pd.read_json('nobel_winners.json')
print(df.columns)
df = df.set_index('year')
df = df.reset_index() # reset後會在最前面
print(df.columns)