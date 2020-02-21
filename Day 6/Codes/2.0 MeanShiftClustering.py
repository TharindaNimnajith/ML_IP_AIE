from sklearn import datasets

iris=datasets.load_iris()
data=iris.data

from sklearn import cluster

msClsfr=cluster.MeanShift() #hierarchichal clustering
msClsfr.fit(data)
labels=msClsfr.labels_
centers=msClsfr.cluster_centers_

print(centers)
