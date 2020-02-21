import numpy as np  #numerical python library
from matplotlib import pyplot as plt

#x = np.arange(starting value, ending value, increment)
x = np.arange(0, 100, 1)
print(x)

print()

y = np.arange(0, 100, 2)
print(y)

#x and y are numpy arrays (not lists)

print()

z = 2 * x
print(z)

print()

w = y + 1
print(w)

#Calculation is performed for each and every element of the numpy array

x = np.arange(0, 100, 2)
y1 = 2 * x
y2 = 3 * x

##plt.plot(x, y1)
##plt.plot(x, y2)
##
##plt.plot(x, y1, 'y')
##plt.plot(x, y2, 'g')

plt.plot(x, y1, 'r.')
plt.plot(x, y2, 'b--')

plt.show()
