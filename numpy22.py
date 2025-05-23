import numpy as np

# Create a list of numbers from 0 to 19995 with a step of 5
x = list(range(0, 20000, 5))

# Convert the list into a numpy array
arr = np.array(x)

# Find the index where the value is 5000
res = np.where(arr == 5000)
print(res)

# Print the element at index 1100
print(arr[res])
# seraching the element

x1 = list(range(0, 20000, 5))

# Convert the list into a numpy array
arr1 = np.sort(x1)
# only ascending order are done
print(arr1)
