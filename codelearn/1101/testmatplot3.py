import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(9989)
x = pd.period_range(pd.datetime.now(),periods=200,freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200,3).cumsum(0)
plots = plt.plot(x,y)
plt.gcf().set_size_inches(8,4)
plt.legend(plots,('foo','bar','baz'),loc='best',framealpha=0.25)
plt.grid(True)

plt.title('Random Trends')
plt.xlabel('Date')
plt.ylabel('cumsum')
plt.figtext(0.995,0.01,'TCFST@2021',ha='right',va='bottom')

plt.show()