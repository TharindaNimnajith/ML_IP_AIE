from sklearn import datasets

iris=datasets.load_iris()       #loading the iris dataset into iris

#print(iris.feature_names)
#print(iris.target_names)

data=iris.data
target=iris.target

from sklearn import model_selection

train_data,test_data,train_target,test_target=model_selection.train_test_split(data,target,test_size=0.2)


from sklearn import neighbors

clsfr=neighbors.KNeighborsClassifier(n_jobs=3)  #loading the clsfr

clsfr.fit(train_data,train_target)       #train the KNN model

results=clsfr.predict(test_data)        #testing the model

from sklearn import metrics

accuracy=metrics.accuracy_score(test_target,results)

print('Accuracy:',accuracy)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

for i in range(len(train_target)):

    if(train_target[i]==0):     #if target is setosa
        ax.scatter(train_data[i][0],train_data[i][1],train_data[i][2],color='g',label='Setosa')

    elif(train_target[i]==1):   #versicolor    
        ax.scatter(train_data[i][0],train_data[i][1],train_data[i][2],color='r',label='Versicolor')

    elif(train_target[i]==2):   #verginica
        ax.scatter(train_data[i][0],train_data[i][1],train_data[i][2],color='b',label='Verginica')

print(test_target[0],results[0])

ax.scatter(test_data[0][0],test_data[0][1],test_data[0][2],color='c',marker='x')

ax.set_xlabel('Sepal Length(cm)')
ax.set_ylabel('Sepal Width(cm)')
ax.set_zlabel('Petal Length(cm)')
ax.legend()

plt.show()
