from sklearn import datasets, tree, metrics
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

data = iris.data
targets = iris.target

train_data, test_data, train_target, test_target = train_test_split(data, targets, test_size = 0.5)

classifier = tree.DecisionTreeClassifier()
classifier.fit(train_data, train_target)

results = classifier.predict(test_data)

accuracy = metrics.accuracy_score(test_target, results)
print('Accuracy: ', accuracy)

print()

print('S/W: ', min(data[:, 0]), max(data[:, 0]))
print('S/L: ', min(data[:, 1]), max(data[:, 1]))
print('P/W: ', min(data[:, 2]), max(data[:, 2]))
print('P/L: ', min(data[:, 3]), max(data[:, 3]))
