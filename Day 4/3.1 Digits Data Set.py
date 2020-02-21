from sklearn import datasets
from matplotlib import pyplot as plt

digits = datasets.load_digits()

data = digits.data
target = digits.target
images = digits.images

##print(len(target)) #1797
##
##print(data.shape)  #(1797, 64)
##data is a 2D Array
##
##print(data[0])
##[ 0.  0.  5. 13.  9.  1.  0.  0.  0.  0. 13. 15. 10. 15.  5.  0.  0.  3.
## 15.  2.  0. 11.  8.  0.  0.  4. 12.  0.  0.  8.  8.  0.  0.  5.  8.  0.
##  0.  9.  8.  0.  0.  4. 11.  0.  1. 12.  7.  0.  0.  2. 14.  5. 10. 12.
##  0.  0.  0.  0.  6. 13. 10.  0.  0.  0.]
##
##plt.imshow(images[1], cmap = 'binary')
##plt.show()

