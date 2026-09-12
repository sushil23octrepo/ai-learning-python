import pandas as pd

# ============================================================
# MODULE 04 — MISSING DATA HANDLING
# Complete reference implementation for later revision.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", None, "Finance", "HR"],
        "Salary": [85000, None, 95000, 72000, 60000],
        "Experience": [5, 3, 8, None, 2],
    }
)

print("\nOriginal DataFrame:")
print(employees)


# ------------------------------------------------------------
# 1. DETECT MISSING VALUES — isna()
# ------------------------------------------------------------

# isna() checks every value in the DataFrame.
# True  -> value is missing
# False -> value exists
print("\n1. Missing-value boolean DataFrame:")
print(employees.isna())


# ------------------------------------------------------------
# 2. COUNT MISSING VALUES
# ------------------------------------------------------------

# isna() creates True/False values.
# sum() counts True values in each column.
print("\n2. Missing values per column:")
print(employees.isna().sum())


# ------------------------------------------------------------
# 3. isnull() — ALIAS OF isna()
# ------------------------------------------------------------

# isnull() and isna() are equivalent for normal usage.
print("\n3. Using isnull():")
print(employees.isnull())


# ------------------------------------------------------------
# 4. CHECK WHICH COLUMNS HAVE MISSING VALUES
# ------------------------------------------------------------

# any() checks whether at least one True value exists.
# The result tells us which columns contain missing values.
print("\n4. Columns containing missing values:")
print(employees.isna().any())


# ------------------------------------------------------------
# 5. CHECK WHETHER ANY VALUE IS MISSING ANYWHERE
# ------------------------------------------------------------

# First any() -> checks each column.
# Second any() -> checks those results.
has_missing_values = employees.isna().any().any()

print("\n5. Does the DataFrame contain missing values?")
print(has_missing_values)


# ------------------------------------------------------------
# 6. FIND ROWS CONTAINING MISSING VALUES
# ------------------------------------------------------------

# axis=1 means check across columns for each row.
# One True/False value is produced for each employee.
missing_rows = employees[employees.isna().any(axis=1)]

print("\n6. Rows containing at least one missing value:")
print(missing_rows)


# ------------------------------------------------------------
# 7. DROP ALL ROWS CONTAINING MISSING VALUES
# ------------------------------------------------------------

# dropna() removes rows containing at least one missing value.
# The original DataFrame remains unchanged unless reassigned.
complete_rows = employees.dropna()

print("\n7. Rows with no missing values:")
print(complete_rows)


# ------------------------------------------------------------
# 8. DROP ROWS BASED ON SPECIFIC COLUMNS
# ------------------------------------------------------------

# Only remove rows where Salary is missing.
salary_available = employees.dropna(subset=["Salary"])

print("\n8. Rows where Salary exists:")
print(salary_available)


# Check multiple required columns.
# A row is removed if Salary OR Experience is missing.
required_values = employees.dropna(subset=["Salary", "Experience"])

print("\n9. Rows with Salary and Experience available:")
print(required_values)


# ------------------------------------------------------------
# 9. KEEP ORIGINAL DATA AND CREATE A CLEANING COPY
# ------------------------------------------------------------

# copy() creates a separate DataFrame for cleaning.
# This preserves the original raw dataset.
cleaned_employees = employees.copy()


# ------------------------------------------------------------
# 10. FILL MISSING TEXT VALUES
# ------------------------------------------------------------

# Replace missing Department values with a meaningful label.
cleaned_employees["Department"] = cleaned_employees["Department"].fillna("Unknown")

print("\n10. Department after fillna():")
print(cleaned_employees)


# ------------------------------------------------------------
# 11. FILL NUMERIC VALUES USING A CONSTANT
# ------------------------------------------------------------

# Filling Experience with 0 is technically possible.
# But 0 means zero experience, which may be different from
# "experience is unknown".
#
# Example only:
#
# employees["Experience"] = (
#     employees["Experience"].fillna(0)
# )


# ------------------------------------------------------------
# 12. FILL MISSING VALUES USING THE MEAN
# ------------------------------------------------------------

# mean() ignores missing values by default.
average_salary = cleaned_employees["Salary"].mean()

print("\n11. Average Salary:")
print(average_salary)

# Replace the missing Salary with the calculated average.
cleaned_employees["Salary"] = cleaned_employees["Salary"].fillna(average_salary)

print("\n12. Salary after mean replacement:")
print(cleaned_employees)


# ------------------------------------------------------------
# 13. FILL MISSING VALUES USING THE MEDIAN
# ------------------------------------------------------------

# median() returns the middle value after sorting.
# Median is often useful when extreme values/outliers exist.
median_experience = cleaned_employees["Experience"].median()

print("\n13. Median Experience:")
print(median_experience)

cleaned_employees["Experience"] = cleaned_employees["Experience"].fillna(
    median_experience
)

print("\n14. Experience after median replacement:")
print(cleaned_employees)


# ------------------------------------------------------------
# 14. FILL MULTIPLE COLUMNS IN ONE OPERATION
# ------------------------------------------------------------

# Start again from the raw DataFrame for this example.
another_cleaned_copy = employees.copy()

# Each column can use a different missing-value strategy.
another_cleaned_copy = another_cleaned_copy.fillna(
    {
        "Department": "Unknown",
        "Salary": another_cleaned_copy["Salary"].mean(),
        "Experience": another_cleaned_copy["Experience"].median(),
    }
)

print("\n15. Fill multiple columns:")
print(another_cleaned_copy)


# ------------------------------------------------------------
# 15. FORWARD FILL — ffill()
# ------------------------------------------------------------

temperature = pd.DataFrame({"Temperature": [30, None, None, 35, 36]})

print("\n16. Original temperature data:")
print(temperature)

# ffill() replaces a missing value with the previous valid value.
print("\n17. Forward filled:")
print(temperature.ffill())


# ------------------------------------------------------------
# 16. BACKWARD FILL — bfill()
# ------------------------------------------------------------

# bfill() replaces a missing value with the next valid value.
print("\n18. Backward filled:")
print(temperature.bfill())


# ------------------------------------------------------------
# 17. VERIFY CLEANED DATA
# ------------------------------------------------------------

print("\n19. Missing values remaining:")
print(cleaned_employees.isna().sum())

print("\n20. Any missing values remaining?")
print(cleaned_employees.isna().any().any())


# ------------------------------------------------------------
# 18. FINAL CLEANED DATAFRAME
# ------------------------------------------------------------

print("\n21. Final cleaned DataFrame:")
print(cleaned_employees)


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Detect missing values:
# df.isna()

# Count missing values in each column:
# df.isna().sum()

# Check whether each column contains a missing value:
# df.isna().any()

# Check whether the entire DataFrame contains a missing value:
# df.isna().any().any()

# Find rows containing at least one missing value:
# df[df.isna().any(axis=1)]

# Remove rows containing missing values:
# df.dropna()

# Remove rows only when selected columns are missing:
# df.dropna(subset=["Salary", "Experience"])

# Fill with a constant:
# df["Department"].fillna("Unknown")

# Fill with mean:
# df["Salary"].fillna(df["Salary"].mean())

# Fill with median:
# df["Experience"].fillna(df["Experience"].median())

# Fill several columns:
# df.fillna({
#     "Department": "Unknown",
#     "Salary": df["Salary"].mean(),
#     "Experience": df["Experience"].median(),
# })

# Use previous available value:
# df.ffill()

# Use next available value:
# df.bfill()

# IMPORTANT:
# Missing does NOT automatically mean zero.
#
# Mean/median/dropna are not universal solutions.
# The correct strategy depends on what the column represents.
