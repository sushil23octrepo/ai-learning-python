import numpy as np

# --------------------------------
# RESHAPE 1D -> 2D
# --------------------------------

values = np.array([1, 2, 3, 4, 5, 6])

print("Original:")
print(values)
print("Shape:", values.shape)


# Same 6 values arranged as 2 rows x 3 columns
matrix_2x3 = values.reshape(2, 3)

print("\n2 x 3:")
print(matrix_2x3)
print("Shape:", matrix_2x3.shape)


# Same 6 values arranged as 3 rows x 2 columns
matrix_3x2 = values.reshape(3, 2)

print("\n3 x 2:")
print(matrix_3x2)
print("Shape:", matrix_3x2.shape)


# --------------------------------
# USING -1
# --------------------------------

# 2 rows, NumPy calculates required columns
auto_columns = values.reshape(2, -1)

print("\nReshape using -1:")
print(auto_columns)
print("Shape:", auto_columns.shape)


# --------------------------------
# ML SINGLE SAMPLE EXAMPLE
# --------------------------------

customer = np.array([0.72, 0.85, 0.25])

print("\nCustomer 1D shape:")
print(customer.shape)


# 1 sample, 3 features
customer_2d = customer.reshape(1, 3)

print("\nCustomer as 2D:")
print(customer_2d)
print("Shape:", customer_2d.shape)


# --------------------------------
# RAW DATA -> CUSTOMER DATASET
# --------------------------------

raw_values = np.array([0.72, 0.85, 0.25, 0.40, 0.55, 0.80, 0.91, 0.90, 0.10])


# Each customer has 3 features
# -1 lets NumPy infer number of customers
customers = raw_values.reshape(-1, 3)

print("\nCustomer dataset:")
print(customers)
print("Shape:", customers.shape)


# --------------------------------
# FLATTEN
# --------------------------------

matrix = np.array([[1, 2, 3], [4, 5, 6]])


# Convert 2D array into a new 1D array
flat = matrix.flatten()

print("\nOriginal matrix:")
print(matrix)

print("\nFlattened:")
print(flat)
print("Shape:", flat.shape)
