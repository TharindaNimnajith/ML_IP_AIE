from sklearn.cluster import MeanShift
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data

#classifier = MeanShift()
classifier = MeanShift(bandwidth = 0.85)

classifier.fit(data)
labels = classifier.labels_

centroids = classifier.cluster_centers_
print(len(centroids))
