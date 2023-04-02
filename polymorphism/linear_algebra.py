#Linear Algebra
import numpy as np
from scipy.linalg import solve

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

x = solve(A, b)

print(x)
