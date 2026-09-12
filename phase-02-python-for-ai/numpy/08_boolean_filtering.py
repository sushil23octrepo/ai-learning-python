import numpy as np

scores = np.array([70, 85, 60, 92, 78])
mask = scores > 80
print(mask)

high_scores = scores[mask]
print(high_scores)

print(scores[scores > 80])  # Keep only values greater than 80
print(scores[scores >= 70])

similarities = np.array([0.92, 0.41, 0.87, 0.33, 0.81])
relevant = similarities[similarities >= 0.80]
print(relevant)

customers = np.array(
    [[0.72, 0.85, 0.25], [0.40, 0.55, 0.80], [0.91, 0.90, 0.10], [0.60, 0.70, 0.45]]
)
# Column 0 = Income,Column 1 = Credit Score,Column 2 = Debt
credit_scores = customers[:, 1]
mask = credit_scores > 0.80
selected_customers = customers[mask]  # Keep complete rows where mask is True
print(selected_customers)

print(customers[customers[:, 1] > 0.80])
low_debt_customer = customers[customers[:, 2] < 0.50]
print(low_debt_customer)
# Credit Score > 0.80 AND Debt < 0.30

cred_debt = customers[(customers[:, 1] > 0.80) & (customers[:, 2] < 0.30)]
print(cred_debt)

print(np.any(scores > 20))
