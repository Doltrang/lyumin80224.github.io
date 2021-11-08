import numpy as np
s =np.array([56,32,45,78,30,65])
print(s>50)

s2 = np.arange(8).reshape([2,4])
print(s2)
print(s2.min(axis=1))
print(s2.min(axis=0))
print(s2.mean(axis=1))
print(s2.max(axis=1))
print(s2.std(axis=1))
print(s2.sum(axis=1))