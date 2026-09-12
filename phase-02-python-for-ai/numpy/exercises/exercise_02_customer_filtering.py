import numpy as np

# Columns:
# 0 = Income
# 1 = Credit Score
# 2 = Debt
customers = np.array(
    [
        [0.72, 0.85, 0.25],
        [0.40, 0.55, 0.80],
        [0.91, 0.90, 0.10],
        [0.60, 0.70, 0.45],
        [0.82, 0.78, 0.20],
        [0.55, 0.88, 0.35],
    ]
)

print(customers[:, 0].mean())  # Average Income
print(customers[:, 1].max())  # Highest Credit Score
print(customers[customers[:, 1] > 0.80])  # Matching complete rows
income_debt_conditon = (customers[:, 0] > 0.60) & (customers[:, 2] < 0.30)
print(income_debt_conditon.sum())  # Matching complete rows
print(customers[income_debt_conditon])  # Number of matching customers
print(customers[:, 0:2])  # Income and Credit Score columns
print(customers.mean(axis=0))  # Average of each feature
