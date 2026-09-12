import numpy as np

# --------------------------------
# SCALAR BROADCASTING
# --------------------------------

values = np.array([10, 20, 30])

result = values + 5  # Broadcast 5 across every array element

print("Add scalar:")
print(result)


# --------------------------------
# 1D ARRAY BROADCAST OVER ROWS
# --------------------------------

matrix = np.array([[10, 20, 30], [40, 50, 60]])

column_offsets = np.array([1, 2, 3])

# Shape (3,) matches the matrix's 3 columns
# The same offsets are applied to every row
result = matrix + column_offsets

print("\nColumn offsets:")
print(result)


# --------------------------------
# FEATURE-CENTERING EXAMPLE
# --------------------------------

customers = np.array([[10, 20, 30], [20, 30, 40], [30, 40, 50]])


# axis=0 gives one mean per feature/column
feature_means = customers.mean(axis=0)

# Shape (3,) is broadcast across all customer rows
centered = customers - feature_means

print("\nFeature means:")
print(feature_means)

print("\nCentered customer data:")
print(centered)


# --------------------------------
# BROADCAST ONE VALUE PER ROW
# --------------------------------

matrix = np.array([[10, 20, 30], [40, 50, 60]])


# Shape (2, 1):
# one offset for each row
row_offsets = np.array([[100], [200]])

# Each row offset is broadcast across that row's columns
result = matrix + row_offsets

print("\nRow offsets:")
print(result)


# --------------------------------
# NEURAL NETWORK BIAS EXAMPLE
# --------------------------------

# Rows = samples
# Columns = neuron outputs
outputs = np.array([[0.50, 0.70, 0.20], [0.40, 0.60, 0.30], [0.90, 0.80, 0.10]])


# One bias value for each neuron/column
biases = np.array([0.10, -0.05, 0.20])


# Bias vector is applied to every sample row
outputs_with_bias = outputs + biases

print("\nOutputs with bias:")
print(outputs_with_bias)
