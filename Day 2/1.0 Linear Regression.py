from sklearn.linear_model import LinearRegression #importing linear regression model linear_model in sklearn library (scikit-learn)
from sklearn.metrics import r2_score              #importing accuracy testing tools (r squared) from metrics in scikit-learn library
from matplotlib import pyplot as plt
import numpy as np

train_data   = [[78], [76], [45], [63], [75], [80], [80], [75], [59], [52], [45], [88], [50], [58], [45], [50], [42], [70], [65], [69], [60], [72]]
train_target = [[180], [175], [165], [172], [174], [170], [172], [170], [170], [160], [150], [175], [160], [150], [160], [146], [162], [165], [158], [175], [160], [163]]

print('\nTrain Data    : ', train_data)
print('\nTrain Targets : ', train_target)
print('\nNumber of Training Data : ', len(train_data))
print('Number of Train Targets : ', len(train_target))

plt.scatter(train_data, train_target, label = 'Train Data vs. Train Targets') #scatter -> dots, plot -> line
plt.xlabel('Weigths(kg)')
plt.ylabel('Heights(h)')

classifier = LinearRegression()          #loading the linear regression model
classifier.fit(train_data, train_target) #need to pass data & target in 2d arrays to train the classifier

m = classifier.coef_[0]   #coefficient / gradient(m)
c = classifier.intercept_ #intercept(c)

x = np.arange(40, 90, 2) #x is a numpy array that has values 40, 42, 44, ..., 86, 88
y = m * x + c #y is an array that is the same size of x
#y[0] = m * x[0] + c etc. as numpy arrays are intelligent

testValues   = [[84], [78], [60]]    #testing data
actualScores = [[182], [178], [165]] #actucal data
predictedResults = classifier.predict(testValues) #passing testing data and assigning the predicted result to results

print('\nGradient  : ', m, '\nIntercept : ', c) #print m & c (gradient & intercept)
print('\nTest Data        : ', testValues)
print('Actual Scores    : ', actualScores)
print('Predicted Height : ', predictedResults)

plt.plot(x, y, 'r',  label = 'Best Fit Line') #Plotting the line graph (best fit line)
plt.scatter(testValues, predictedResults, label = 'Predicted Result') #Plotting the predicted result for the given test data/feature
#plt.scatter(testValues, testValues * m + c)

accuracy = r2_score(actualScores, predictedResults)
print('\nAccuracy : ', accuracy, '\n')

plt.legend()
plt.title('Weight & Height Graph')
plt.savefig('1.0 Weight & Height Graph.png')
plt.show()
