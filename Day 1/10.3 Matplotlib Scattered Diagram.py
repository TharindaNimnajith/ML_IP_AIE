import random

#Random value from 0 to 100
x = [i for i in range(20)]
print(x)

#print()

#20 random values from 0 to 20
#y is a list
y = [random.randint(0, 100) for i in range(20)]
print(y)

#print()

from matplotlib import pyplot as plt

plt.scatter(x, y)
plt.show()
