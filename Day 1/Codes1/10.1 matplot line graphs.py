import numpy as np      #numerical python library
from matplotlib import pyplot as plt

x=np.arange(0,100,2)
y1=2*x
y2=3*x

plt.plot(x,y1,'r+')
plt.plot(x,y2,'g--')

plt.show()
