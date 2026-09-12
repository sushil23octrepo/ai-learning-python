import pandas as pd

# ============================================================
# PANDAS EXERCISE 04 — MISSING DATA HANDLING
# Reference solution.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", None, "Finance", "HR", None],
        "Salary": [85000, None, 95000, 72000, 60000, 88000],
        "Experience": [5, 3, 8, None, 2, 6],
    }
)


# ------------------------------------------------------------
# 1. Print the complete DataFrame.
# ------------------------------------------------------------

print("\n1. Original DataFrame:")
print(employees)


# ------------------------------------------------------------
# 2. Print boolean values showing missing data.
# ------------------------------------------------------------

# True means the value is missing.
print("\n2. Missing-value boolean DataFrame:")
print(employees.isna())


# ------------------------------------------------------------
# 3. Count missing values in each column.
# ------------------------------------------------------------

# Boolean True behaves like 1 when summed.
print("\n3. Missing values per column:")
print(employees.isna().sum())


# ------------------------------------------------------------
# 4. Print rows containing at least one missing value.
# ------------------------------------------------------------

# axis=1 checks across columns for each row.
missing_rows = employees[employees.isna().any(axis=1)]

print("\n4. Rows containing missing values:")
print(missing_rows)


# ------------------------------------------------------------
# 5. Create a DataFrame removing rows with missing Salary.
# ------------------------------------------------------------

# subset limits dropna() to the Salary column.
employees_with_salary = employees.dropna(subset=["Salary"])

print("\n5. Employees where Salary exists:")
print(employees_with_salary)


# ------------------------------------------------------------
# Create a separate copy for cleaning.
# ------------------------------------------------------------

# Preserve the original/raw DataFrame.
cleaned_employees = employees.copy()


# ------------------------------------------------------------
# 6. Fill missing Department with "Unknown".
# ------------------------------------------------------------

cleaned_employees["Department"] = cleaned_employees["Department"].fillna("Unknown")


# ------------------------------------------------------------
# 7. Fill missing Salary using average Salary.
# ------------------------------------------------------------

# mean() ignores NaN values by default.
average_salary = cleaned_employees["Salary"].mean()

cleaned_employees["Salary"] = cleaned_employees["Salary"].fillna(average_salary)


# ------------------------------------------------------------
# 8. Fill missing Experience using median Experience.
# ------------------------------------------------------------

median_experience = cleaned_employees["Experience"].median()

cleaned_employees["Experience"] = cleaned_employees["Experience"].fillna(
    median_experience
)


# ------------------------------------------------------------
# 9. Check whether missing values still exist.
# ------------------------------------------------------------

has_missing_values = cleaned_employees.isna().any().any()

print("\n9. Does cleaned data contain missing values?")
print(has_missing_values)


# Also useful for seeing the count for every column.
print("\nMissing values by column:")
print(cleaned_employees.isna().sum())


# ------------------------------------------------------------
# 10. Print the final cleaned DataFrame.
# ------------------------------------------------------------

print("\n10. Final cleaned DataFrame:")
print(cleaned_employees)
