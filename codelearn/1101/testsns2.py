import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
print(df.head())
pal = {'Female':'red','Male':'blue'}
g = sns.FacetGrid(df,col='smoker',palette=pal,height=4,aspect=1)
g.map(plt.scatter,'total_bill','tip',alpha=.4)
g.add_legend()
plt.show()