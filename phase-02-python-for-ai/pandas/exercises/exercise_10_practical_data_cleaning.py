import pandas as pd

# ============================================================
# PANDAS EXERCISE 10 — PRACTICAL DATA CLEANING
# Reference solution.
# ============================================================

customers = pd.DataFrame(
    {
        "CustomerId": [101, 102, 102, 103, 104, 105],
        "Name": [
            " amit ",
            "NEHA",
            "NEHA",
            "Rahul",
            " Priya",
            "Karan ",
        ],
        "City": [
            "hyderabad",
            "HYDERABAD",
            "HYDERABAD",
            "Pune",
            None,
            "Mumbai",
        ],
        "Income": [
            "75000",
            "45000",
            "45000",
            "95000",
            None,
            "65000",
        ],
        "Debt": [
            15000,
            30000,
            30000,
            10000,
            28000,
            None,
        ],
        "SignupDate": [
            "2025-01-10",
            "2025-04-15",
            "2025-04-15",
            "invalid",
            "2025-08-01",
            "2025-09-10",
        ],
        "UnusedColumn": ["x", "x", "x", "x", "x", "x"],
    }
)


# ------------------------------------------------------------
# 1. Print shape, data types, and missing-value counts.
# ------------------------------------------------------------

print("\n1. Shape:")
print(customers.shape)

print("\nData types:")
print(customers.dtypes)

print("\nMissing values:")
print(customers.isna().sum())


# ------------------------------------------------------------
# 2. Remove duplicate customers using CustomerId.
# ------------------------------------------------------------

customers = customers.drop_duplicates(subset=["CustomerId"])

print("\n2. After duplicate removal:")
print(customers)


# ------------------------------------------------------------
# 3. Clean Name using strip() and title().
# ------------------------------------------------------------

customers["Name"] = customers["Name"].str.strip().str.title()


# ------------------------------------------------------------
# 4. Clean City using strip() and title().
# ------------------------------------------------------------

customers["City"] = customers["City"].str.strip().str.title()


# ------------------------------------------------------------
# 5. Convert Income to numeric.
# ------------------------------------------------------------

# Invalid numeric values become NaN.
customers["Income"] = pd.to_numeric(
    customers["Income"],
    errors="coerce",
)


# ------------------------------------------------------------
# 6. Convert SignupDate to datetime.
# ------------------------------------------------------------

# Invalid dates become NaT.
customers["SignupDate"] = pd.to_datetime(
    customers["SignupDate"],
    errors="coerce",
)


# ------------------------------------------------------------
# 7. Fill missing City with "Unknown".
# ------------------------------------------------------------

customers["City"] = customers["City"].fillna("Unknown")


# ------------------------------------------------------------
# 8. Fill missing Income using median Income.
# ------------------------------------------------------------

median_income = customers["Income"].median()

customers["Income"] = customers["Income"].fillna(median_income)


# ------------------------------------------------------------
# 9. Fill missing Debt using median Debt.
# ------------------------------------------------------------

median_debt = customers["Debt"].median()

customers["Debt"] = customers["Debt"].fillna(median_debt)


# ------------------------------------------------------------
# 10. Drop UnusedColumn.
# ------------------------------------------------------------

customers = customers.drop(columns=["UnusedColumn"])


# ------------------------------------------------------------
# 11. Create DebtRatio.
# ------------------------------------------------------------

customers["DebtRatio"] = customers["Debt"] / customers["Income"]


# ------------------------------------------------------------
# 12. Create HighDebt.
# ------------------------------------------------------------

# True becomes 1, False becomes 0.
customers["HighDebt"] = (customers["DebtRatio"] > 0.50).astype(int)


# ------------------------------------------------------------
# 13. Create DaysSinceSignup.
# ------------------------------------------------------------

reference_date = pd.Timestamp("2026-09-12")

customers["DaysSinceSignup"] = (reference_date - customers["SignupDate"]).dt.days


# ------------------------------------------------------------
# 14. Print average Income by City.
# ------------------------------------------------------------

average_income_by_city = customers.groupby("City")["Income"].mean()

print("\n14. Average Income by City:")
print(average_income_by_city)


# ------------------------------------------------------------
# 15. Print two customers with highest DebtRatio.
# ------------------------------------------------------------

highest_debt_customers = customers.nlargest(
    2,
    "DebtRatio",
)

print("\n15. Two highest DebtRatio customers:")
print(highest_debt_customers)


# ------------------------------------------------------------
# 16. Create final feature DataFrame.
# ------------------------------------------------------------

features = customers[
    [
        "Income",
        "Debt",
        "DebtRatio",
        "HighDebt",
        "DaysSinceSignup",
    ]
].copy()


# ------------------------------------------------------------
# 17. Print final cleaned DataFrame and features.
# ------------------------------------------------------------

print("\n17. Final cleaned customer DataFrame:")
print(customers)

print("\nFinal feature DataFrame:")
print(features)


# ------------------------------------------------------------
# OPTIONAL FINAL CHECKS
# ------------------------------------------------------------

print("\nRemaining missing values in cleaned data:")
print(customers.isna().sum())

print("\nRemaining missing values in features:")
print(features.isna().sum())


# ------------------------------------------------------------
# OPTIONAL MODEL-READY VERSION
# ------------------------------------------------------------

# The invalid SignupDate creates a missing DaysSinceSignup.
# One simple option is to remove rows with missing model features.
model_ready_features = features.dropna()

print("\nModel-ready feature DataFrame:")
print(model_ready_features)
