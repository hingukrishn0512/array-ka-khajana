import numpy as np

# 0-D array (scalar)
arr = np.array(1)

# 1-D array (vector)
arr1 = np.array([1, 1])

# 2-D array (matrix 2x2)
arr2 = np.array([[1, 2], [2, 4]])

# 2-D array (matrix 4x2)
arr3 = np.array([[2, 3], [32, 2], [2, 4], [4, 1]])

# 5-D array (this is interesting!)
arr4 = np.array([[2, 3]], ndmin=5)

# Print all arrays
print(arr)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

#method are same like the python indexing ,delete