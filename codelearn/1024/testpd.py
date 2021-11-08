import pandas as pd
df = pd.read_json('nobel_winners.json')
print(df.head())
print(df.columns)
# Index(['born_in', 'category', 'country', 'date_of_birth', 'date_of_death',
#        'gender', 'link', 'name', 'place_of_birth', 'place_of_death', 'text',
#        'year']
print(df.index)
df = df.set_index('name')
print(df.columns)
print(df.index)
# print(df.loc['Auguste Beernaert']) #loc針對文字形標籤索引
# print(df.iloc[4]) #iloc無法針對文字做使用
# print(df.loc[['Auguste Beernaert','Maurice Maeterlinck']])
print(df.loc[['Auguste Beernaert','Maurice Maeterlinck'],['category','year','country']])
print(df.iloc[4:6,[1,10,2]])
df2 = df.iloc[4:6,[1,10,2]]
print(type(df2))
print(df2)
print(df.iloc[[4,5,8,9,10],[1,10,2]])
print(df.iloc[list(range(4,6))+list(range(8,11)),[1,10,2]])