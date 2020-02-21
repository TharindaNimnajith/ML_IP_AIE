from matplotlib import pyplot as plt

x=[i for i in range(-5,6)]
#x=[-5,-4,-3,-2,......,4,5]

y1=[i*i for i in range(-5,6)]
y2=[2*i for i in range(-5,6)]


plt.plot(x,y1,'r+',label='y=x^2')
plt.plot(x,y2,'c--',label='y=2x')

plt.legend()

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('X vs Y')

plt.savefig('linegraph.png')

plt.show()
