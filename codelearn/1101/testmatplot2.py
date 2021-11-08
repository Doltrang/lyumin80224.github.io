import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(9989)
x = pd.period_range(pd.datetime.now(),periods=200,freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200,3).cumsum(0)
plots = plt.plot(x,y)
plt.show()