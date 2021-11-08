import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(9989)
number_points = 100
x = np.array(range(number_points))
y = np.random.randn(number_points) * 10 + x * 0.5

df = pd.DataFrame({'dummy x':x,'dummy y':y})
print(df.head())
sns.lmplot('dummy x','dummy y',df,height=4,aspect=2)
plt.show()