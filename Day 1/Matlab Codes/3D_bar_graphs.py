from matplotlib import pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d
import numpy as np

style.use('ggplot')
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,8,7,9,10,5,3,2,7]
z=[0,2,0,1,0,0,0,0,0,1]

dx=[10,1,1,1,1,1,1,1,1,1]
dy=[1,1,1,1,1,1,1,1,1,1]
dz=[2,3,4,5,6,8,7,6,8,4]

ax1.bar3d(x,y,z,dx,dy,dz)
plt.show()
