import pandas as pd
df = pd.read_json('nobel_winners.json')
df_grp =df.groupby('category')
print(df_grp.groups.keys())
phy_grp =df_grp.get_group('Physics')
print(phy_grp)

print(df_grp.get_group(''))