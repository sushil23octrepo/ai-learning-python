import pandas as pd

# ============================================================
# MODULE 06 — COLUMN OPERATIONS AND TRANSFORMATIONS
# Complete reference implementation for later revision.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
        "Experience": [5, 3, 8, 4, 2],
    }
)

print("\nOriginal DataFrame:")
print(employees)

# 1. Add a new column using vectorized arithmetic.
employees["Bonus"] = employees["Salary"] * 0.10

# 2. Create a column from multiple existing columns.
employees["TotalCompensation"] = employees["Salary"] + employees["Bonus"]

# 3. Conditional column creation.
employees["ExperienceLevel"] = "Junior"
employees.loc[employees["Experience"] >= 5, "ExperienceLevel"] = "Experienced"


# 4. apply() for custom Python logic.
def salary_band(salary):
    if salary >= 90000:
        return "High"
    elif salary >= 70000:
        return "Medium"
    return "Low"


employees["SalaryBand"] = employees["Salary"].apply(salary_band)

# 5. Prefer vectorized arithmetic for simple calculations.
employees["SalaryInLakhs"] = employees["Salary"] / 100000

# 6. map() transforms values using a dictionary.
department_names = {
    "IT": "Information Technology",
    "HR": "Human Resources",
    "Finance": "Finance",
}
employees["DepartmentFullName"] = employees["Department"].map(department_names)

# 7. replace() changes only listed values; unmatched values stay unchanged.
print("\nDepartment values using replace():")
print(employees["Department"].replace({"IT": "Technology", "HR": "Human Resources"}))

# 8. Rename selected columns.
employees = employees.rename(columns={"Name": "EmployeeName", "Salary": "AnnualSalary"})

# 9. Insert a column at a specific position.
employees.insert(0, "EmployeeId", [101, 102, 103, 104, 105])

# 10. Convert a column data type.
employees["EmployeeId"] = employees["EmployeeId"].astype(str)

# 11. Vectorized string transformation.
employees["EmployeeNameUpper"] = employees["EmployeeName"].str.upper()

# 12. Drop a column.
employees_without_band = employees.drop(columns=["SalaryBand"])
print("\nAfter dropping SalaryBand:")
print(employees_without_band)

# 13. Filtering is often clearer than dropping rows by hard-coded index.
high_salary_employees = employees[employees["AnnualSalary"] >= 70000]
print("\nEmployees with AnnualSalary >= 70000:")
print(high_salary_employees)

# 14. Practical AI / feature-engineering example.
customers = pd.DataFrame(
    {
        "Income": [72000, 40000, 91000],
        "Debt": [15000, 32000, 9000],
    }
)

# Ratio feature created from existing numeric columns.
customers["DebtRatio"] = customers["Debt"] / customers["Income"]

# Convert a boolean condition into a 0/1 numeric feature.
customers["HighDebt"] = (customers["DebtRatio"] > 0.50).astype(int)

print("\nCustomer feature engineering:")
print(customers)

# ============================================================
# IMPORTANT REVISION
# ============================================================

# Add a column:
# df["Bonus"] = df["Salary"] * 0.10

# Conditional assignment:
# df["Level"] = "Junior"
# df.loc[df["Experience"] >= 5, "Level"] = "Experienced"

# Custom transformation:
# df["Band"] = df["Salary"].apply(function)

# Simple arithmetic should usually stay vectorized:
# df["SalaryInLakhs"] = df["Salary"] / 100000

# Map known values:
# df["Department"].map(mapping_dictionary)

# Replace selected values:
# df["Department"].replace({...})

# Rename columns:
# df.rename(columns={"OldName": "NewName"})

# Insert at a specific column position:
# df.insert(0, "EmployeeId", values)

# Convert dtype:
# df["EmployeeId"] = df["EmployeeId"].astype(str)

# String transformation:
# df["Name"].str.upper()

# Drop columns:
# df.drop(columns=["ColumnName"])

# Feature engineering:
# df["DebtRatio"] = df["Debt"] / df["Income"]
