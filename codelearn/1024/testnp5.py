import numpy as np
o = np.ones((2,3))
# o = np.ones([2,3]) # 也可以寫成這樣
print(o)
o = o.astype('int32')
print(o)

z = np.zeros([2,3])
print(z,'\n',z.dtype)

print(np.random.random([2,3]))
print(np.random.random_sample([2,3]))
print(np.random.rand(2,3))
print(np.random.randint(1,40,[5,5]))
#1~39
print(np.linspace(1,10,5)) #會使用到最大值
print(np.arange(2,10,2)) #停止在結束值