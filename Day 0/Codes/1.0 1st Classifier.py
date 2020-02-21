from sklearn import datasets  #importing sckit learn datasets (toy dataset)

iris = datasets.load_iris()   #importing the iris data set (table)
data = iris.data              #splitting the data (data[150][4])
target = iris.target          #splitting the targets (target[150])

#setosa -> 0
print(data[0])
print(target[0])

#versicolor -> 1
print(data[60])
print(target[60])

#virginica -> 2
print(data[110])
print(target[110])

import numpy as np  #importing numpy library as "np"

#assigning the 1st, 51st, 101th rows in the table to the 
test_samples = [0, 50, 100]

#calling the delete function in np library

#deleting the data of the 3 rows and assining the remaining data of the 147 rows to train_data
train_data = np.delete(data, test_samples, axis = 0)

#deleting the targets of the 3 rows and assining the remaining targets of the 147 rows to train_target
train_target = np.delete(target, test_samples)

from sklearn import neighbors

#loading the KNeighborsClassifier classifier
classifier = neighbors.KNeighborsClassifier()

#training the classifier
classifier.fit(train_data, train_target)

#testing using the data from the 3 deleted rows
test_data = data[test_samples]

#assigning the predicted target of the test_data to results array
results = classifier.predict(test_data)

print()

#printing the predicted results array
print("Predicted Results: ", results)

#assigning the actual targets of the tests to test_results array
test_results = target[test_samples]

#predicting the actual results array
print("Actual Results: ", test_results)
