import numpy as np  # as "alias"

array = np.array([[1, 2, 3,], [4, 5, 6,]])  # multi-dimensional array (matrix)
print(array)
print(array.shape)  # returns (rows, columns)
array2 = np.zeros((3, 4))  # first param is a tuple of (r,c) # dtype=float/int
print(array2)
  # np.ones
  # np.full ((tuple), number, dtype=int/float)
  # np.random.random((3,4)) ,  random array

array_r = np.random.random((3,4))
print(array_r[0,0])  # index 0,0 of random array
print(array_r > 0.2)  # will print boolean values
print(array_r[array_r > 0.2])  # if true will print

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch *2.54
print(dimensions_cm)