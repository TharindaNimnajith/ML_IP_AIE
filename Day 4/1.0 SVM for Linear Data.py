from sklearn import datasets
iris=datasets.load_iris()

data=iris.data
target=iris.target

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.3)

sepal_length=train_data[0:,1]



