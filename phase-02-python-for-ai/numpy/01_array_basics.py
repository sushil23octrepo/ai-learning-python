import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(type(numbers))


python_numbers = [1, 2, 3, 4]

numpy_numbers = np.array([1, 2, 3, 4])
print(python_numbers * 2)
print(numpy_numbers * 2)

values = np.array([10, 20, 30, 40])
print(values + 5)
print(values - 5)
print(values * 2)

print(values.dtype)

numbers1 = np.array([5, 10, 15, 20], dtype=float)
print(numbers1)
