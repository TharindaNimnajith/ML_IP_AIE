from sklearn.datasets.samples_generator import make_circles

data,target=make_circles(100,factor=.1,noise=.1)

#print(data)

from matplotlib import pyplot as plt

x=data[:,0]
y=data[:,1]

for i in range(100):

    if(target[i]==0):
    
        plt.scatter(x[i],y[i],color='r')

    elif(target[i]==1):

        plt.scatter(x[i],y[i],color='g')

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.3)

from sklearn import svm

clsfr=svm.SVC(kernel='rbf')
clsfr.fit(train_data,train_target)

results=clsfr.predict(test_data)

from sklearn import metrics

accuracy=metrics.accuracy_score(test_target,results)
print('accuracy:',accuracy)

plt.show()
