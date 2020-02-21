x=[1,5,1.5,8,1,9]
y=[2,8,1.8,8,0.6,11]

import numpy as np

data=np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])

from sklearn import cluster

kmeans=cluster.KMeans(n_clusters=2)
kmeans.fit(data)

labels=kmeans.labels_

print(labels)

from matplotlib import pyplot as plt
from matplotlib import style

for i in range(len(data)):

    if(labels[i]==0):

        plt.plot(data[i][0],data[i][1],'g.')

    elif(labels[i]==1):

        plt.plot(data[i][0],data[i][1],'r.')

style.use('ggplot')
plt.show()
