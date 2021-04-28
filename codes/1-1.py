import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

data = np.loadtxt('olympic100m.txt', delimiter=',')
year = data[:,0]
time = data[:,1]

# 画出数据方便观察
plt.plot(year,time,'ro')
plt.xlabel('奥运会届数')
plt.ylabel('夺冠耗时(秒)')
plt.show()