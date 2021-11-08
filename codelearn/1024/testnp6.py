import numpy as np
data = np.arange(10)
data = data * 10
print(data)
print(data[7:])
print(data[1:-1])
print(data[::-1])
print(data[-3:])
print(np.linspace(1,10,4).astype('int'))