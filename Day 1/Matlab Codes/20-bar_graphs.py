from matplotlib import pyplot as plt


x=[i for i in range(1,11)]
y=[30,40,100,38,96,47,30,19,49,78]

plt.bar(x,y,color='r')

plt.xlabel('x values')
plt.ylabel('y values')

plt.show()
