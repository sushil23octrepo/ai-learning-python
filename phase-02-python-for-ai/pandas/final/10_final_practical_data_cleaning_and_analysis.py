import pandas as pd

# ============================================================
# MODULE 10 — PRACTICAL DATA CLEANING AND ANALYSIS
# Complete reference implementation for later revision.
# ============================================================

customers = pd.DataFrame(
    {
        "CustomerId": [1, 2, 2, 3, 4, 5],
        "Name": [" Amit ", "Neha", "Neha", "RAHUL", "Priya", "Karan"],
        "City": ["Hyderabad", "hyderabad", "hyderabad", "Pune", None, "Mumbai"],
        "Income": ["72000", "40000", "40000", "91000", None, "60000"],
        "Debt": [15000, 32000, 32000, 9000, 27000, None],
        "SignupDate": [
            "2025-01-10",
            "2025-03-15",
            "2025-03-15",
            "invalid-date",
            "2025-06-20",
            "2025-08-01",
        ],
        "TemporaryColumn": ["x", "x", "x", "x", "x", "x"],
    }
)

print("\nOriginal DataFrame:")
print(customers)


# ------------------------------------------------------------
# 1. INSPECT THE DATA
# ------------------------------------------------------------

print("\n1. First rows:")
print(customers.head())

print("\n2. Shape:")
print(customers.shape)

print("\n3. Data types:")
print(customers.dtypes)

print("\n4. DataFrame info:")
customers.info()

print("\n5. Missing values per column:")
print(customers.isna().sum())


# ------------------------------------------------------------
# 2. REMOVE DUPLICATES
# ------------------------------------------------------------

# Remove duplicate customers using CustomerId.
customers = customers.drop_duplicates(subset=["CustomerId"])

print("\n6. After removing duplicate CustomerId values:")
print(customers)


# ------------------------------------------------------------
# 3. CLEAN TEXT COLUMNS
# ------------------------------------------------------------

# str.strip() removes spaces from both ends.
# str.title() standardizes capitalization.
customers["Name"] = customers["Name"].str.strip().str.title()

customers["City"] = customers["City"].str.strip().str.title()

print("\n7. Cleaned Name and City:")
print(customers[["Name", "City"]])


# ------------------------------------------------------------
# 4. CONVERT NUMERIC TEXT TO NUMBERS
# ------------------------------------------------------------

# errors="coerce" converts invalid numeric values to NaN.
customers["Income"] = pd.to_numeric(
    customers["Income"],
    errors="coerce",
)

print("\n8. Income converted to numeric:")
print(customers.dtypes)


# ------------------------------------------------------------
# 5. CONVERT DATE TEXT TO DATETIME
# ------------------------------------------------------------

# Invalid dates become NaT.
customers["SignupDate"] = pd.to_datetime(
    customers["SignupDate"],
    errors="coerce",
)

print("\n9. SignupDate converted to datetime:")
print(customers)


# ------------------------------------------------------------
# 6. HANDLE MISSING TEXT VALUES
# ------------------------------------------------------------

customers["City"] = customers["City"].fillna("Unknown")

print("\n10. Missing City filled:")
print(customers[["Name", "City"]])


# ------------------------------------------------------------
# 7. HANDLE MISSING NUMERIC VALUES
# ------------------------------------------------------------

# Median is used here as a practical example.
median_income = customers["Income"].median()

customers["Income"] = customers["Income"].fillna(median_income)

median_debt = customers["Debt"].median()

customers["Debt"] = customers["Debt"].fillna(median_debt)

print("\n11. Missing Income and Debt filled:")
print(customers)


# ------------------------------------------------------------
# 8. DROP UNNECESSARY COLUMNS
# ------------------------------------------------------------

customers = customers.drop(columns=["TemporaryColumn"])

print("\n12. TemporaryColumn removed:")
print(customers)


# ------------------------------------------------------------
# 9. CREATE DebtRatio FEATURE
# ------------------------------------------------------------

# Feature engineering:
# Convert Income and Debt into a useful ratio.
customers["DebtRatio"] = customers["Debt"] / customers["Income"]

print("\n13. DebtRatio created:")
print(customers[["Income", "Debt", "DebtRatio"]])


# ------------------------------------------------------------
# 10. CREATE BINARY FEATURE
# ------------------------------------------------------------

# Boolean condition:
# True  -> 1
# False -> 0
customers["HighDebt"] = (customers["DebtRatio"] > 0.50).astype(int)

print("\n14. HighDebt feature:")
print(customers[["DebtRatio", "HighDebt"]])


# ------------------------------------------------------------
# 11. CREATE DATE-BASED FEATURE
# ------------------------------------------------------------

# Use a fixed reference date so the example is reproducible.
reference_date = pd.Timestamp("2026-09-12")

customers["DaysSinceSignup"] = (reference_date - customers["SignupDate"]).dt.days

print("\n15. DaysSinceSignup:")
print(customers[["SignupDate", "DaysSinceSignup"]])


# ------------------------------------------------------------
# 12. CHECK FOR REMAINING MISSING VALUES
# ------------------------------------------------------------

print("\n16. Remaining missing values:")
print(customers.isna().sum())

# Note:
# SignupDate for an invalid original date remains NaT,
# therefore DaysSinceSignup for that row is also NaN.
#
# Whether to remove or replace that value depends on
# the business meaning and model requirements.


# ------------------------------------------------------------
# 13. ANALYZE AVERAGE INCOME BY CITY
# ------------------------------------------------------------

average_income_by_city = customers.groupby("City")["Income"].mean()

print("\n17. Average Income by City:")
print(average_income_by_city)


# ------------------------------------------------------------
# 14. FIND CUSTOMERS WITH HIGHEST DEBT RATIO
# ------------------------------------------------------------

highest_debt = customers.nlargest(
    3,
    "DebtRatio",
)

print("\n18. Customers with highest DebtRatio:")
print(highest_debt)


# ------------------------------------------------------------
# 15. FILTER HIGH-DEBT CUSTOMERS
# ------------------------------------------------------------

high_debt_customers = customers[customers["HighDebt"] == 1]

print("\n19. High-debt customers:")
print(high_debt_customers)


# ------------------------------------------------------------
# 16. CREATE FINAL ML FEATURE DATAFRAME
# ------------------------------------------------------------

# Select only numeric features intended for the model.
features = customers[
    [
        "Income",
        "Debt",
        "DebtRatio",
        "HighDebt",
        "DaysSinceSignup",
    ]
].copy()

print("\n20. Final feature DataFrame:")
print(features)


# ------------------------------------------------------------
# 17. OPTIONAL: REMOVE ROWS WITH MISSING MODEL FEATURES
# ------------------------------------------------------------

# Some ML algorithms cannot accept missing values.
# For this example, remove rows with missing final features.
model_ready_features = features.dropna()

print("\n21. Model-ready features:")
print(model_ready_features)


# ------------------------------------------------------------
# 18. SORT CLEANED DATA
# ------------------------------------------------------------

# Highest income first.
sorted_customers = customers.sort_values(
    "Income",
    ascending=False,
)

print("\n22. Customers sorted by Income:")
print(sorted_customers)


# ------------------------------------------------------------
# 19. SAVE CLEANED DATA
# ------------------------------------------------------------

# Example:
#
# customers.to_csv(
#     "customers_cleaned.csv",
#     index=False
# )
#
# features.to_csv(
#     "customer_features.csv",
#     index=False
# )


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Inspect:
# df.head()
# df.shape
# df.dtypes
# df.info()
# df.isna().sum()

# Remove duplicates:
# df.drop_duplicates()
# df.drop_duplicates(subset=["CustomerId"])

# Clean text:
# df["Name"].str.strip()
# df["Name"].str.title()

# Convert numeric text:
# pd.to_numeric(
#     df["Income"],
#     errors="coerce"
# )

# Convert date:
# pd.to_datetime(
#     df["SignupDate"],
#     errors="coerce"
# )

# Fill text:
# df["City"].fillna("Unknown")

# Fill numeric:
# df["Income"].fillna(
#     df["Income"].median()
# )

# Drop unnecessary columns:
# df.drop(columns=["UnusedColumn"])

# Create ratio:
# df["DebtRatio"] = (
#     df["Debt"] / df["Income"]
# )

# Create binary feature:
# df["HighDebt"] = (
#     df["DebtRatio"] > 0.50
# ).astype(int)

# Create date-based feature:
# df["DaysSinceSignup"] = (
#     reference_date - df["SignupDate"]
# ).dt.days

# Group and aggregate:
# df.groupby("City")["Income"].mean()

# Highest values:
# df.nlargest(3, "DebtRatio")

# Final ML features:
# features = df[
#     [
#         "Income",
#         "Debt",
#         "DebtRatio",
#         "HighDebt",
#         "DaysSinceSignup",
#     ]
# ]

# Remove rows with missing model features:
# model_ready_features = features.dropna()


# ============================================================
# COMPLETE DATA-PREPARATION FLOW
# ============================================================

# Raw data
#    ↓
# Inspect
#    ↓
# Remove duplicates
#    ↓
# Clean text
#    ↓
# Convert data types
#    ↓
# Handle missing values
#    ↓
# Drop unnecessary columns
#    ↓
# Feature engineering
#    ↓
# Analyze / validate
#    ↓
# Select model features
#    ↓
# Handle remaining missing model values
#    ↓
# Machine Learning
