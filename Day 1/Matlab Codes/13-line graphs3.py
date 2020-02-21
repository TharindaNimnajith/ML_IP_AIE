from matplotlib import pyplot as plt
import numpy as np

x=np.arange(-2*np.pi,2*np.pi,0.1)
y1=np.sin(x)
y2=np.cos(x)


plt.plot(x,y1,'r+',label='sin(x)')
plt.plot(x,y2,'c--',label='cos(x)')

plt.legend()

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('X vs Y')

plt.savefig('linegraph.png')

plt.show()
