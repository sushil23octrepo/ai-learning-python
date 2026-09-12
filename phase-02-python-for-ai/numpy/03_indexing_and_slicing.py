import numpy as np

# Columns:
# 0 = Income
# 1 = Credit Score
# 2 = Debt
customers = np.array(
    [[0.72, 0.85, 0.25], [0.40, 0.55, 0.80], [0.91, 0.90, 0.10], [0.60, 0.70, 0.45]]
)

print(customers[0])  # Access one complete row
print(customers[0, 1])  # Access one individual value
print(customers[:, 0])  # : = all rows, 0 = column 0
print(customers[0:2])  # Start at row 0, stop before row 2
print(customers[0:2, :])  # Rows 0-1, all columns
print(customers[0:3, 0:2])  # Rows 0-2, columns 0-1
print(customers[2:])  # Start at row 2, continue to end
print(customers[:2])  # Start from beginning, stop before row 2
print(customers[:, 1:3])  # All rows, columns 1 and 2
print(customers[-1])  # Last row
print(customers[0:1])  # Keeps shape as (1, 3)
