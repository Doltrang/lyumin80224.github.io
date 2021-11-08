import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
print(df.head())
pal = {'Female':'red','Male':'blue'}
hue_kws= {'marker':['D','s']}
g = sns.FacetGrid(df,col='smoker',hue='sex',palette=pal,height=4,aspect=1,hue_kws=hue_kws)
g.map(plt.scatter,'total_bill','tip',alpha=.4)
g.add_legend()
plt.show()