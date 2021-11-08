import matplotlib.pyplot as plt
import numpy as np

np.random.seed(9989)
number_points = 100
x = np.array(range(number_points))
y = np.random.randn(number_points) * 10 + x * 0.5

#print(x)
#print(y)
fig , ax = plt.subplots(figsize=(8,4))

colors = np.random.rand(number_points)
size = np.pi * (2+np.random.rand(number_points)*10) ** 2
ax.scatter(x,y,c=colors,s=size,alpha=0.5)

m,c = np.polyfit(x,y,1)
ax.plot(x,m*x+c)

plt.show()