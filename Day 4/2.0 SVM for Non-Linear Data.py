from sklearn.datasets.samples_generator import make_circles
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

data, target = make_circles(100, factor = .1, noise = .1) #data is a 2D array, target is a 1D array (0 or 1)

##print(data) 
##print(target)

x = data[:, 0]
y = data[:, 1]

plt.scatter(x[0], y[0], color = 'r', label = '0')
plt.scatter(x[1], y[1], color = 'g', label = '1')

for i in range(100):
    if(target[i] == 0):
        plt.scatter(x[i], y[i], color = 'r')
    elif(target[i] == 1):
        plt.scatter(x[i], y[i], color = 'g')

train_data, test_data, train_target, test_target = train_test_split(data, target, test_size = 0.2)

#classifier = svm.SVC(kernel = 'linear')
classifier  = svm.SVC(kernel = 'rbf')
classifier.fit(train_data, train_target)

results = classifier.predict(test_data)

accuracy = metrics.accuracy_score(test_target, results)
print('Accuracy: ', accuracy)  #Accuracy is very low for linear kernel and very high for rbf kernel

##plt.scatter(x, y, c = y, s = 50, cmap = 'autum')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Non-Linear Data Graph')
plt.savefig('2.0 Non-Linear Data Graph.png')
plt.show()
