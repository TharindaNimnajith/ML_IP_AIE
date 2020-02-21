from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

iris = datasets.load_iris()

data    = iris.data
targets = iris.target

train_data, test_data, train_targets, test_targets = train_test_split(data, targets, test_size = 0.2)

classifier = svm.SVC(kernel = 'linear')
classifier.fit(train_data, train_targets)

results = classifier.predict(test_data)

accuracy = metrics.accuracy_score(test_targets, results)
print('Accuracy: ', accuracy)

figure = plt.figure()

ax = figure.add_subplot(111, projection = '3d')

ax.scatter(train_data[0][0], train_data[0][1], train_data[0][2], color = 'g', label = 'Setosa')
ax.scatter(train_data[1][0], train_data[1][1], train_data[1][2], color = 'r', label = 'Versicolor')
ax.scatter(train_data[2][0], train_data[2][1], train_data[2][2], color = 'b', label = 'Virginica')

for i in range(len(train_targets)):
    if(train_targets[i] == 0):
        ax.scatter(train_data[i][0], train_data[i][1], train_data[i][2], color = 'g')
    elif(train_targets[i] == 1):
        ax.scatter(train_data[i][0], train_data[i][1], train_data[i][2], color = 'r')
    elif(train_targets[i] == 2):
        ax.scatter(train_data[i][0], train_data[i][1], train_data[i][2], color = 'b')

print(test_targets[0], results[0])
ax.scatter(test_data[0][0], test_data[0][1], test_data[0][2], color = 'c', marker = 'x')

ax.set_xlabel('Sepel Length(cm)')
ax.set_ylabel('Sepel Width(cm)')
ax.set_zlabel('Petal Length(cm)')

plt.legend()
plt.title('Iris Flowers Graph')
plt.savefig('1.0 Iris Flowers Graph.png')
plt.show()
