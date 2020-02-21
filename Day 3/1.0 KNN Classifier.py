#from sklearn import * #importing all from sklearn
from sklearn import datasets #to import a toy dataset
from sklearn import model_selection
from sklearn import neighbors
from sklearn import metrics
from mpl_toolkits.mplot3d import Axes3D #to plot a 3D graph
from matplotlib import pyplot as plt

iris = datasets.load_iris() #loading the iris data set into iris 2D-array[150][5] (150 columns & 5 rows)
#print(iris.feature_names)
#print(iris.target_names)
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#['setosa' 'versicolor' 'virginica']

data    = iris.data   #data[150][4] <- 2D Array
targets = iris.target #targets[150] <- 1D Array

train_data, test_data, train_targets, test_targets = model_selection.train_test_split(data, targets, test_size = 0.2) #take 30 rows for testing, 120 for training
#train_test_split() function takes data randomly, not in order

#classifier = neighbors.KNeighborsClassifier() #loading the KNN classifier (by default, k = 1)
classifier  = neighbors.KNeighborsClassifier(n_jobs = 3) #can define k using n_jobs (here, k = 3)
classifier.fit(train_data, train_targets) #training the KNN model (train_data[120][4], train_targets[120])
results = classifier.predict(test_data)   #testing the KNN model (test_data[30][4], results[30])

accuracy = metrics.accuracy_score(test_targets, results)
print('Accuracy: ', accuracy)

figure = plt.figure()
ax = figure.add_subplot(111, projection = '3d')

ax.scatter(train_data[0][0], train_data[0][1], train_data[0][2], color = 'g', label = 'Setosa')
ax.scatter(train_data[1][0], train_data[1][1], train_data[1][2], color = 'r', label = 'Versicolor')
ax.scatter(train_data[2][0], train_data[2][1], train_data[2][2], color = 'b', label = 'Virginica')

for i in range(len(train_targets)): #loops 120 times due to test_size = 0.2 parameter in train_test_spit() function
    if(train_targets[i] == 0):   #if target is setosa
        ax.scatter(train_data[i][0], train_data[i][1], train_data[i][2], color = 'g')
    elif(train_targets[i] == 1): #if target is versicolor
        ax.scatter(train_data[i][0], train_data[i][1], train_data[i][2], color = 'r')
    elif(train_targets[i] == 2): #if target is virginica
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
