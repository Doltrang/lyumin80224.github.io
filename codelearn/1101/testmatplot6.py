import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

labels = ['Physics','Chemistry','Literature','Peace']
data = [3,6,10,4]

xlocation = np.array(range(len(data))) + 0.5 # + 右空白寬度
plt.bar(xlocation,data,width=0.5)
plt.xticks(xlocation,labels)
plt.xlim((0,xlocation[-1]+0.5)) # xlocation[指定資料位置0為第1筆  -1最後一筆]  + 左空白寬度

plt.gca().get_xaxis().tick_top()
plt.gca().get_yaxis().tick_right()
plt.gcf().set_size_inches((8,4))




# plt.bar(range(4),data,width=0.5)
# plt.xticks(range(4),labels)
# #plt.yticks(range(12))
# plt.yticks([0,5,10,12])
plt.show()