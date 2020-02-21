from matplotlib import pyplot as plt

x=[i for i in range(-5,6)]
#x=[-5,-4,-3,-2,......,4,5]

y=[i*i for i in range(-5,6)]


plt.plot(x,y,'r+')

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('X vs Y')


plt.show()
