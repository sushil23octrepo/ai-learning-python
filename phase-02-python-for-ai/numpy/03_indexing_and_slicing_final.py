import numpy as np

# Columns:
# 0 = Income
# 1 = Credit Score
# 2 = Debt
customers = np.array(
    [[0.72, 0.85, 0.25], [0.40, 0.55, 0.80], [0.91, 0.90, 0.10], [0.60, 0.70, 0.45]]
)


# Get row 0 with all features
first_customer = customers[0]

print("First customer:")
print(first_customer)


# Syntax: array[row, column]
# Row 0, column 1 = first customer's credit score
credit_score = customers[0, 1]

print("\nFirst customer credit score:")
print(credit_score)


# : means all rows
# Column 0 = Income
income = customers[:, 0]

print("\nAll income values:")
print(income)


# All rows, column 1 = Credit Score
credit_scores = customers[:, 1]

print("\nAll credit scores:")
print(credit_scores)


# All rows, column 2 = Debt
debts = customers[:, 2]

print("\nAll debt values:")
print(debts)


# Rows 0 and 1
# End index 2 is excluded
first_two_customers = customers[0:2]

print("\nFirst two customers:")
print(first_two_customers)


# Rows 0-2 and columns 0-1
# 0:3 -> rows 0, 1, 2
# 0:2 -> columns 0, 1
selected = customers[0:3, 0:2]

print("\nFirst three customers - Income and Credit Score:")
print(selected)


# All rows, columns 1 and 2
credit_and_debt = customers[:, 1:3]

print("\nCredit Score and Debt:")
print(credit_and_debt)


# -1 means the last row
last_customer = customers[-1]

print("\nLast customer:")
print(last_customer)


# All rows, -1 means the last column
last_feature = customers[:, -1]

print("\nLast feature column:")
print(last_feature)


# Direct indexing removes one dimension
# Shape becomes (3,)
single_customer_1d = customers[0]

print("\nSingle customer as 1D:")
print(single_customer_1d)
print("Shape:", single_customer_1d.shape)


# Slicing keeps the row dimension
# Shape remains (1 sample, 3 features)
single_customer_2d = customers[0:1]

print("\nSingle customer as 2D:")
print(single_customer_2d)
print("Shape:", single_customer_2d.shape)
