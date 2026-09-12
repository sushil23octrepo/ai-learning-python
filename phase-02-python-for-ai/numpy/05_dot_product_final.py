import numpy as np

# --------------------------------
# ELEMENT-WISE MULTIPLICATION
# --------------------------------

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

element_wise = a * b  # Multiply matching positions separately

print("Element-wise multiplication:")
print(element_wise)


# --------------------------------
# DOT PRODUCT
# --------------------------------

dot_product = np.dot(a, b)  # Multiply matching positions, then sum

print("\nDot product:")
print(dot_product)


# --------------------------------
# AI / NEURAL NETWORK EXAMPLE
# --------------------------------

# Input features:
# 0 = Income
# 1 = Credit Score
# 2 = Debt
customer = np.array([0.72, 0.85, 0.25])

# Each input has a corresponding learned weight
weights = np.array([0.40, 0.90, -0.70])

weighted_sum = np.dot(customer, weights)  # x1*w1 + x2*w2 + x3*w3

print("\nWeighted sum:")
print(weighted_sum)


# Bias is added after the weighted sum
bias = -0.10

neuron_output = weighted_sum + bias

print("\nNeuron output before activation:")
print(neuron_output)


# --------------------------------
# @ OPERATOR
# --------------------------------

same_result = a @ b  # For 1D vectors, @ also performs dot product

print("\nDot product using @:")
print(same_result)
