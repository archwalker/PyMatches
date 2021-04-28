from matplotlib import pyplot as plt
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

from matplotlib import cm
import numpy as np

# 载入数据
data = np.loadtxt('olympic100m.txt', delimiter=',')
num = data[:,0]
time = data[:,1]

# 定义损失函数
def loss_func(w1, w2):
	total_loss = 0
	for ni, ti in zip(num, time):
		total_loss += (w1 * ni + w2 * ti + 1)**2
	return total_loss / len(num)

# 将损失函数和参数w_1, w_2的取值关系画出来
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
w1_space = np.linspace(-1, 1, 100)
w2_space = np.linspace(-1, 1, 100)
w1_mesh, w2_mesh = np.meshgrid(w1_space, w2_space)
L = np.empty(shape=(100, 100))
for i, w1 in enumerate(w1_space):
	for j, w2 in enumerate(w2_space):
		L[i,j] = loss_func(w1, w2)

surf = ax.plot_surface(w1_mesh, w2_mesh, L, cmap=cm.Reds)
ax.view_init(30, 10) # 调整视角
ax.set_xlabel(r'$w_1$')
ax.set_ylabel(r'$w_2$')
ax.zaxis.set_rotate_label(False)
ax.set_zlabel(r'$\mathcal{L}$', rotation=0)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
