import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = np.arange(-10, 11, 1)
print(x)

x = x[:, np.newaxis]
print(x)

y = 2 * (x ** 2) + 3 * x #y is a second order polynomial function (degree = 2)

plt.plot(x, y, 'r')

ye = [] #y with some small errors

for i in y:
    ye.append(i + np.random.randint(-5, 5)) #append adds an element to the end

ye = np.array(ye)

#plt.plot(x, y, 'r', label = 'Curve without errors')
plt.scatter(x, ye, label = 'Curve with errors')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

classifier = LinearRegression()

poly = PolynomialFeatures(degree = 3, include_bias = False)
xnew = poly.fit_transform(x)

#classifier.fit(xnew, ye)
#classifier.fit([x], [ye])
results = classifier.fit(xnew, ye)

m = classifier.coef_[0]
c = classifier.intercept_
print('\n', m, '\n\n', c, '\n')

x_vals = np.arange(-10, 11, 1)
y_vals = m[0] * x_vals + m[1] * (x_vals ** 2) + m[2] * (x_vals ** 3)

plt.plot(x_vals, y_vals, 'g')

plt.legend()
plt.title('Curve')
plt.savefig('2.0 Curve.png')
plt.show()
