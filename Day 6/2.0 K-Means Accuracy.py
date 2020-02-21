from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

iris = load_iris()

data = iris.data
target = iris.target

train_data, test_data, train_target, test_target = train_test_split(data, target, test_size = 0.5)

supervised_classifier = KNeighborsClassifier()
supervised_classifier.fit(train_data, train_target)
supervised_results = supervised_classifier.predict(test_data)

unsupervised_classifier = KMeans(n_clusters = 3)
unsupervised_classifier.fit(test_data)
unsupervised_results = unsupervised_classifier.labels_

accuracy1 = accuracy_score(supervised_results, unsupervised_results)
accuracy2 = accuracy_score(test_target, unsupervised_results)

print('Accuracy (supervised vs. unsupervised): ', accuracy1)
print('Accuracy (actual vs. unsupervised)    : ', accuracy2)
