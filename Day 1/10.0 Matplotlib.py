from matplotlib import pyplot as plt
#pyplot is a sub library of the matplotlib library

x = [i for i in range(-10, 11)]
y = [i * i for i in range(-10, 11)]

plt.plot(x, y)
plt.show()
