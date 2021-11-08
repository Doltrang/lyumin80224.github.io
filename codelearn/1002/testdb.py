import pandas as pd
df = pd.read_csv('Age_County_Gender_19Cov.csv',encoding='utf8')
print(df[df.縣市=='台北市'].確定病例數.sum())