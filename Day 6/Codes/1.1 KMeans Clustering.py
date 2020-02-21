import numpy as np

data=np.random.randint(200,size=(100,3))

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

for feature in data:

    ax.scatter(feature[0],feature[1],feature[2],color='g')

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')

plt.show()
