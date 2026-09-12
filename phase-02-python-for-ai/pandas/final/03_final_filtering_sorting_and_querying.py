import pandas as pd

# ============================================================
# MODULE 03 — FILTERING, SORTING, AND QUERYING
# Complete reference implementation for later revision.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
        "Salary": [85000, 65000, 95000, 72000, 60000, 88000],
        "Experience": [5, 3, 8, 4, 2, 6],
    }
)

print("\nOriginal DataFrame:")
print(employees)


# ------------------------------------------------------------
# 1. BASIC BOOLEAN FILTERING
# ------------------------------------------------------------

# A comparison creates a boolean Series containing True/False.
high_salary = employees["Salary"] > 70000

print("\n1. Boolean mask:")
print(high_salary)

# Use the boolean mask to keep only matching rows.
print("\n2. Employees with Salary > 70000:")
print(employees[high_salary])

# The condition can also be written directly.
print("\n3. Direct filtering:")
print(employees[employees["Salary"] > 80000])


# ------------------------------------------------------------
# 2. MULTIPLE CONDITIONS
# ------------------------------------------------------------

# '&' performs element-wise AND.
# Each comparison should be inside parentheses.
it_experienced = employees[
    (employees["Department"] == "IT") & (employees["Experience"] >= 5)
]

print("\n4. IT employees with Experience >= 5:")
print(it_experienced)


# '|' performs element-wise OR.
hr_or_high_salary = employees[
    (employees["Department"] == "HR") | (employees["Salary"] > 90000)
]

print("\n5. HR OR Salary > 90000:")
print(hr_or_high_salary)


# '~' negates a boolean condition.
not_hr = employees[~(employees["Department"] == "HR")]

print("\n6. Employees not in HR:")
print(not_hr)


# ------------------------------------------------------------
# 3. ISIN()
# ------------------------------------------------------------

# isin() checks whether each value exists in the supplied list.
selected_departments = employees[employees["Department"].isin(["IT", "Finance"])]

print("\n7. IT or Finance:")
print(selected_departments)


# ------------------------------------------------------------
# 4. BETWEEN()
# ------------------------------------------------------------

# between() checks whether values fall within a range.
# Both boundaries are included by default.
salary_range = employees[
    employees["Salary"].between(
        70000,
        90000,
    )
]

print("\n8. Salary between 70000 and 90000:")
print(salary_range)


# Equivalent explicit condition:
salary_range_explicit = employees[
    (employees["Salary"] >= 70000) & (employees["Salary"] <= 90000)
]


# ------------------------------------------------------------
# 5. SORT BY ONE COLUMN
# ------------------------------------------------------------

# sort_values() sorts by the values in a column.
# Ascending order is the default.
print("\n9. Salary ascending:")
print(employees.sort_values("Salary"))

# ascending=False sorts highest to lowest.
print("\n10. Salary descending:")
print(
    employees.sort_values(
        "Salary",
        ascending=False,
    )
)


# ------------------------------------------------------------
# 6. SORT BY MULTIPLE COLUMNS
# ------------------------------------------------------------

# Department -> ascending
# Salary -> descending within each department
sorted_employees = employees.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False],
)

print("\n11. Department ascending, Salary descending:")
print(sorted_employees)


# ------------------------------------------------------------
# 7. ORIGINAL DATAFRAME VS SORTED RESULT
# ------------------------------------------------------------

# This creates a new sorted DataFrame.
sorted_copy = employees.sort_values("Salary")

# The original DataFrame is unchanged.
print("\n12. Original DataFrame:")
print(employees)

# Explicit assignment replaces the variable with the sorted result:
# employees = employees.sort_values("Salary")


# ------------------------------------------------------------
# 8. SORT BY INDEX
# ------------------------------------------------------------

employees_by_name = employees.set_index("Name")

print("\n13. Sort by Name index:")
print(employees_by_name.sort_index())


# ------------------------------------------------------------
# 9. QUERY()
# ------------------------------------------------------------

# query() provides a readable filtering expression.
result = employees.query("Salary > 70000 and Experience >= 5")

print("\n14. Salary > 70000 and Experience >= 5:")
print(result)


# Query string can also compare text columns.
it_high_salary = employees.query("Department == 'IT' and Salary > 80000")

print("\n15. IT employees with Salary > 80000:")
print(it_high_salary)


# ------------------------------------------------------------
# 10. USE PYTHON VARIABLES INSIDE QUERY()
# ------------------------------------------------------------

minimum_salary = 85000

# '@' tells query() to use an external Python variable.
result = employees.query("Salary >= @minimum_salary")

print("\n16. Salary >= minimum_salary:")
print(result)


# ------------------------------------------------------------
# 11. NLARGEST()
# ------------------------------------------------------------

# nlargest() returns the rows with the largest values
# without manually sorting the entire DataFrame.
top_three = employees.nlargest(
    3,
    "Salary",
)

print("\n17. Three highest salaries:")
print(top_three)


# ------------------------------------------------------------
# 12. NSMALLEST()
# ------------------------------------------------------------

# nsmallest() returns rows with the smallest values.
least_experienced = employees.nsmallest(
    2,
    "Experience",
)

print("\n18. Two least experienced employees:")
print(least_experienced)


# ------------------------------------------------------------
# IMPORTANT REVISION
# ------------------------------------------------------------

# Basic filtering:
# employees[employees["Salary"] > 70000]

# AND:
# (
#     (condition_1)
#     & (condition_2)
# )

# OR:
# (
#     (condition_1)
#     | (condition_2)
# )

# NOT:
# ~(condition)

# Multiple possible values:
# employees["Department"].isin(["IT", "Finance"])

# Range:
# employees["Salary"].between(70000, 90000)

# Sort descending:
# employees.sort_values("Salary", ascending=False)

# Multiple-column sorting:
# employees.sort_values(
#     ["Department", "Salary"],
#     ascending=[True, False]
# )

# Query:
# employees.query(
#     "Salary > 70000 and Experience >= 5"
# )

# External Python variable inside query:
# employees.query(
#     "Salary >= @minimum_salary"
# )

# Highest values:
# employees.nlargest(3, "Salary")

# Lowest values:
# employees.nsmallest(2, "Experience")
