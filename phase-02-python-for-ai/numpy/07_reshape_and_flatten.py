import numpy as np

values = np.array([1, 2, 3, 4, 5, 6])
print(values)
print(values.shape)
# Reshape it into 2 rows and 3 columns
matrix = values.reshape(2, 3)  # 2 rows, 3 columns
print(matrix)
print(matrix.shape)
print(values.reshape(2, -1))  # 2 rows, NumPy calculates columns
# Convert 1D into a single-row 2D array
values = np.array([10, 20, 30])
row = values.reshape(1, 3)  # 1 sample, 3 features
print(row)
print(row.shape)
print(row.ndim)

# Reshaping an existing 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
reshaped = matrix.reshape(3, 2)
print(reshaped)

# Now flatten()
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # Convert multi-dimensional array to 1D
flat = matrix.flatten()
print(flat)

flat1 = matrix.reshape(-1)  # Infer one dimension containing all values
print(flat1)
