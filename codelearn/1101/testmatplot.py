import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(9989)
x = pd.period_range(pd.datetime.now(),periods=200,freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200,3).cumsum(0)
plots = plt.plot([2,3,4,5,6],[8,4,3,5,1])
plt.show()