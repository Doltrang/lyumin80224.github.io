nobel_winners = [
                {'name': 'Albert Einstein','category': 'Physics'},
                {'name': 'Paul Dirac','category': 'Physics'},
                {'name': 'Marie Curie','category': 'Chemistry'}
                ]
import pandas as pd
df=pd.DataFrame.from_dict(nobel_winners)
print(df)
df.to_json('nobel.json')
df.to_json('nobel_split.json',orient='split')
df.to_json('nobel_index.json',orient='index')
df.to_json('nobel_columns.json',orient='columns')
df.to_json('nobel_records.json',orient='records')
df.to_json('nobel_values.json',orient='values')