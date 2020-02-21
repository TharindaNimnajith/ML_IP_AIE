from sklearn import datasets, cluster, metrics

iris = datasets.load_iris()
data = iris.data
target = iris.target

#default iterations = 300, can change it with n_init & max_iter parameters
#classifier = cluster.KMeans(n_clusters = 3)
#classifier = cluster.KMeans(n_clusters = 3, n_init = 1000)
#classifier = cluster.KMeans(n_clusters = 3, max_iter = 1000)

classifier = cluster.KMeans(n_clusters = 3, n_init = 1000, max_iter = 1000)
classifier.fit(data)
results = classifier.labels_

accuracy = metrics.accuracy_score(target, results)
print('Accuracy: ', accuracy)
