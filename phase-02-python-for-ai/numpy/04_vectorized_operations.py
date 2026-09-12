import numpy as np

# --------------------------------
# OPERATIONS WITH A SINGLE ARRAY
# --------------------------------

values = np.array([10, 20, 30, 40])

print("Original values:")
print(values)

print("\nAdd 5:")
print(values + 5)  # Add 5 to every element

print("\nSubtract 5:")
print(values - 5)  # Subtract 5 from every element

print("\nMultiply by 2:")
print(values * 2)  # Multiply every element by 2

print("\nDivide by 2:")
print(values / 2)  # Divide every element by 2


# --------------------------------
# OPERATIONS BETWEEN TWO ARRAYS
# --------------------------------

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\nArray addition:")
print(a + b)  # Add elements at the same positions

print("\nArray subtraction:")
print(a - b)  # Subtract elements at the same positions

print("\nElement-wise multiplication:")
print(a * b)  # 10*1, 20*2, 30*3

print("\nElement-wise division:")
print(a / b)  # 10/1, 20/2, 30/3


# --------------------------------
# SIMPLE AI-STYLE NORMALIZATION
# --------------------------------

scores = np.array([20, 40, 60, 80, 100])

normalized_scores = scores / 100  # Apply division to every score

print("\nNormalized scores:")
print(normalized_scores)


# --------------------------------
# VECTORIZED 2D OPERATIONS
# --------------------------------

customers = np.array([[10, 20, 30], [40, 50, 60]])

doubled_customers = customers * 2  # Multiply every matrix value

print("\nDoubled matrix:")
print(doubled_customers)


# --------------------------------
# VECTORIZED COMPARISONS
# --------------------------------

exam_scores = np.array([70, 85, 60, 92])

above_80 = exam_scores > 80  # Compare every score against 80

print("\nScores above 80:")
print(above_80)


values = np.array([1, 2, 3, 2])

equal_to_two = values == 2  # Compare every element with 2

print("\nValues equal to 2:")
print(equal_to_two)
