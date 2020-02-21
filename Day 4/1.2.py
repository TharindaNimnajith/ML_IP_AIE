from sklearn.datasets.samples_generator import make_circles

data,target=make_circles(100,factor=.1,noise=.1)

x=data[:,0]
y=data[:,1]

import numpy as np

r=np.exp(-(data**2).sum(1))   #rbf-radial bais function,one of the SVM Kernels


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

for i in range(100):

    if(target[i]==0):    
        ax.scatter(x[i],y[i],r[i],color='g')

    elif(target[i]==1):     
        ax.scatter(x[i],y[i],r[i],color='r')

plt.show()
