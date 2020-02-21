import random   #python inbuilt module

x=[i for i in range(20)]
y=[random.randint(0,100) for i in range(20)]

from matplotlib import pyplot as plt


plt.scatter(x,y)

plt.show()

