import numpy as np

data=np.random.randint(200,size=(100,3))

from sklearn import cluster

kmClsfr=cluster.KMeans(n_clusters=3)
kmClsfr.fit(data)
labels=kmClsfr.labels_
centroids=kmClsfr.cluster_centers_
print(centroids)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

for i in range(len(data)):

    if(labels[i]==0):
        ax.scatter(data[i][0],data[i][1],data[i][2],color='g')
    elif(labels[i]==1):
        ax.scatter(data[i][0],data[i][1],data[i][2],color='r')
    elif(labels[i]==2):
        ax.scatter(data[i][0],data[i][1],data[i][2],color='b')

for point in centroids:

    ax.scatter(point[0],point[1],point[2],color='c',marker='x')
        
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')

plt.show()
