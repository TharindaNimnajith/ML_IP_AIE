from sklearn.datasets.samples_generator import make_circles
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

data, target = make_circles(100, factor = .1, noise = .1)

x = data[:, 0]
y = data[:, 1]

r = np.exp(-(data**2).sum(1))  #rbf - radial bias function (one of the SVM kernels)
#converting the graph into a higher dimention to seperate classes using a hyperplane

figure = plt.figure()
ax = figure.add_subplot(111, projection = '3d')

ax.scatter(x[0], y[0], r[0], color = 'g', label = '0')
ax.scatter(x[1], y[1], r[1], color = 'r', label = '1')

for i in range(len(target)):
    if(target[i] == 0):
        ax.scatter(x[i], y[i], r[i], color = 'g')
    elif(target[i] == 1):
        ax.scatter(x[i], y[i], r[i], color = 'r')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.zlabel('Z-axis')
plt.legend()
plt.title('Non-Linear Data Graph')
plt.savefig('2.1 Non-Linear Data Graph.png')
plt.show()        
