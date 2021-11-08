import numpy as np #pip install numpy
s = np.array([1,2,3,4,5,6,7,8])
print(s.dtype)
s = s.astype('int64')
print(s.dtype)
s = s.astype('float')
print(s.dtype)
print(s)

s2 = np.array(['100','200','300'])
s2 = s2.astype('int32')
print(s2)
print(s2.dtype)