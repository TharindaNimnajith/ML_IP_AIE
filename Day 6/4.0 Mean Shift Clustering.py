import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift

x = np.random.randint(0, 100, (200))
y = np.random.randint(0, 100, (200))
data = np.zeros((200, 2))
data[:, 0] = x
data[:, 1] = y

classifier = MeanShift(bandwidth = 21)
classifier.fit(data)

centroids = classifier.cluster_centers_
number_of_clusters = len(classifier.cluster_centers_)
print(number_of_clusters)

color_array = ['r', 'g', 'b', 'w', 'k', 'c', 'y', 'm']
labels = classifier.labels_

for i in range(len(labels)):
    for no in range(number_of_clusters):
        if(labels[i] == no):
            plt.plot(data[i][0], data[i][1], color_array[no] + str('.'))
        plt.plot(centroids[no][0], centroids[no][1], color_array[no] + str('x'))
            
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Cluster Graph')
plt.savefig('4.0 Mean Shift Clustering.png')
plt.show()
