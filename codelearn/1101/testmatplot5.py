import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(9989)
x = pd.period_range(pd.datetime.now(),periods=200,freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200,3).cumsum(0)
print(y[:,0])
print(y[:,1])
print(y[:,2])
# fig = plt.figure(figsize=(8,4))
# ax = fig.add_axes((0.1,0.1,0.8,0.8))
# ax.plot(x,y[:,0])

# ax2 = fig.add_axes((0.15,0.15,0.3,0.3))
# ax2.plot(x,y[:,1],color='g')
# ax2.set_xticks([])
# plt.show()