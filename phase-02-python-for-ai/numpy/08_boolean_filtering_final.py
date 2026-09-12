import numpy as np

# --------------------------------
# BASIC BOOLEAN MASK
# --------------------------------

scores = np.array([70, 85, 60, 92, 78])

mask = scores > 80  # Compare every score with 80

print("Boolean mask:")
print(mask)


# Keep only values where the mask is True
high_scores = scores[mask]

print("\nScores above 80:")
print(high_scores)


# Same filter written directly
high_scores_direct = scores[scores > 80]

print("\nDirect filtering:")
print(high_scores_direct)


# --------------------------------
# RAG / SIMILARITY EXAMPLE
# --------------------------------

similarities = np.array([0.92, 0.41, 0.87, 0.33, 0.81])

relevant = similarities[similarities >= 0.80]  # Keep similarity scores of at least 0.80

print("\nRelevant similarity scores:")
print(relevant)


# --------------------------------
# CUSTOMER DATASET
# --------------------------------

# Columns:
# 0 = Income
# 1 = Credit Score
# 2 = Debt
customers = np.array(
    [[0.72, 0.85, 0.25], [0.40, 0.55, 0.80], [0.91, 0.90, 0.10], [0.60, 0.70, 0.45]]
)


# All rows where credit score > 0.80
high_credit_customers = customers[customers[:, 1] > 0.80]

print("\nHigh credit-score customers:")
print(high_credit_customers)


# All rows where debt < 0.50
low_debt_customers = customers[customers[:, 2] < 0.50]

print("\nLow-debt customers:")
print(low_debt_customers)


# --------------------------------
# MULTIPLE CONDITIONS - AND
# --------------------------------

eligible_customers = customers[(customers[:, 1] >= 0.80) & (customers[:, 2] <= 0.30)]

print("\nEligible customers:")
print(eligible_customers)


# --------------------------------
# MULTIPLE CONDITIONS - OR
# --------------------------------

selected_customers = customers[(customers[:, 0] > 0.80) | (customers[:, 1] > 0.85)]

print("\nIncome > 0.80 OR Credit Score > 0.85:")
print(selected_customers)


# --------------------------------
# COUNT / ANY / ALL
# --------------------------------

above_80_mask = scores > 80

count_above_80 = above_80_mask.sum()  # Count True values

print("\nCount above 80:")
print(count_above_80)


has_score_above_90 = np.any(scores > 90)  # At least one match?

print("\nAny score above 90:")
print(has_score_above_90)


all_scores_at_least_60 = np.all(scores >= 60)  # Every value matches?

print("\nAll scores at least 60:")
print(all_scores_at_least_60)
