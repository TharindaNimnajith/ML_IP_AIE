import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

#x & y are numpy arrays with the size of 200 with random integers from 0 to 100

x = np.random.randint(0, 100, (200))
print(x, '\n')

y = np.random.randint(0, 100, (200))
print(y, '\n')

#data = np.array((200, 2))
#print(data, '\n')

data = np.zeros((200, 2))
print(data, '\n')

data[:, 0] = x
print(data[:, 0], '\n')

data[:, 1] = y
print(data[:, 1], '\n')

classifier = KMeans(n_clusters = 3)
classifier.fit(data)

labels = classifier.labels_
print(labels, '\n')

#plt.plot(x, y, 'b.')

#loop iterates 200 times
for i in range(len(labels)):
    if(labels[i] == 0):
        plt.plot(data[i][0], data[i][1], 'b.')
    elif(labels[i] == 1):
        plt.plot(data[i][0], data[i][1], 'g.')
    elif(labels[i] == 2):
        plt.plot(data[i][0], data[i][1], 'r.')

#centroids is a 2d array --> centroids[no of clusters][no of features] --> centroids[3][2]
centroids = classifier.cluster_centers_
print(centroids, '\n')

plt.plot(centroids[0][0], centroids[0][1], 'bx')
plt.plot(centroids[1][0], centroids[1][1], 'gx')
plt.plot(centroids[2][0], centroids[2][1], 'rx')

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Cluster Graph')
plt.savefig('1.0 Cluster.png')
plt.show()
