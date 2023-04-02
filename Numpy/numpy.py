import numpy as np

# create a 1-dimensional array
a = np.array([1, 2, 3, 4, 5])

# create a 2-dimensional array
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Accessing elements:

a = np.array([1, 2, 3, 4, 5])

# access the first element of the array
print(a[0])

# access the last element of the array
print(a[-1])

# mathematical operations
a = np.array([1, 2, 3, 4, 5])

# add 2 to each element of the array
b = a + 2

# multiply each element of the array by 2
c = a * 2

# take the square root of each element of the array
d = np.sqrt(a)

#Reshaping arrays:

a = np.array([1, 2, 3, 4, 5, 6])

# reshape the array to a 2x3 array
b = np.reshape(a, (2, 3))
