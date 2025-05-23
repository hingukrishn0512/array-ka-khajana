import numpy as np

a = np.array([[1,2,4]] , dtype=np.int64)
b = np.array([[3,2,4]] , dtype=np.int64)

print("Addition:\n", np.add(a,b))
print("Subtraction:\n", np.subtract(a,b))
print("Multiplication:\n", np.multiply(a,b))
print("Division:\n", np.divide(a,b))
print("Modulus:\n", np.mod(a,b))
print("Power:\n", np.power(a,b))
print("Square Root of a:\n", np.sqrt(a))

print("Sum of a:\n", np.sum(a))
print("Mean of a:\n", np.mean(a))
print("Max of a:\n", np.max(a))
print("Min of a:\n", np.min(a))


transpose_a = np.transpose(a)
print(transpose_a)

