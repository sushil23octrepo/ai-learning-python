import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a * b)
print(np.dot(a, b))

# Real neural-network example
customer = np.array([0.72, 0.85, 0.25])  # Income  # Credit Score  # Debt

weights = np.array(
    [0.40, 0.90, -0.70]  # Income weight  # Credit Score weight  # Debt weight
)

weighted_sum = np.dot(customer, weights)
print(weighted_sum)

# Add bias
bias = -0.10
output = np.dot(customer, weights) + bias
print(output)
