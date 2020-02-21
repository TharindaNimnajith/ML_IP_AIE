import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 2 * np.pi, 0.2)
y1 = np.sin(x)
y2 = np.cos(x)

print(x)
print()

print(y1)
print()

print(y2)
print()

plt.plot(x, y1, 'r+', label = 'Sin(x)')
plt.plot(x, y2, 'b>', label = 'Cos(x)')

plt.xlabel('X values(rads)')
plt.ylabel('sin(x) or cos(x)')

plt.legend()

plt.title('Trigonometric Functions')

plt.savefig('10.2 Sin(x) and Cos(x) Graphs.png')

plt.show()
