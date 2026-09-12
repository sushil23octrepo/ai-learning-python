import numpy as np

# ----------------------------
# 1D ARRAY
# ----------------------------
numbers = np.array([10, 20, 30, 40])

print("1D array")
print(numbers)

print("Dimensions")
print(numbers.ndim)

print("Shape")
print(numbers.shape)

print("Total elements")
print(numbers.size)

# ----------------------------
# 2D ARRAY
# ----------------------------

matrix = np.array([[10, 20, 30], [40, 50, 60]])
print("\n2D array:")
print(matrix)

print("Dimensions:")
print(matrix.ndim)

print("Shape:")
print(matrix.shape)


# ----------------------------
# ML DATASET EXAMPLE
# ----------------------------

# Each row = one customer/sample
# Columns:
# 0 = Income
# 1 = Credit Score
# 2 = Debt

customers = np.array([[0.72, 0.85, 0.25], [0.40, 0.55, 0.80], [0.91, 0.90, 0.10]])
print("\nCustomer dataset:")
print(customers)

print("Dimensions:")
print(customers.ndim)

print("Shape:")
print(customers.shape)

print("Total values:")
print(customers.size)

sample_count = customers.shape[0]
feature_count = customers.shape[1]

print("Number of samples:", sample_count)
print("Number of features:", feature_count)


# ----------------------------
# 3D ARRAY
# ----------------------------

data_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("\n3D array:")
print(data_3d)

print("Dimensions:")
print(data_3d.ndim)

print("Shape:")
print(data_3d.shape)

print("Total elements:")
print(data_3d.size)
