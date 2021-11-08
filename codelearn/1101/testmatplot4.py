import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(9989)
x = pd.period_range(pd.datetime.now(),periods=200,freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200,3).cumsum(0)
print(y[:,0])
print(y[:,1])
fig = plt.figure(figsize=(8,4))
ax = fig.add_axes((0.1,0.1,0.8,0.8)) # #left, bottom, width ,hight
ax.plot(x,y[:,1])
ax.set_title('Main Axes with Insert Child Axes')
ax.set_xlabel('Date')
ax.set_ylabel('Cumsum')

ax2 = fig.add_axes((0.15,0.55,0.3,0.3))
ax2.plot(x,y[:,0],color='g')
ax2.set_xticks([])
plt.show()