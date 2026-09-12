import pandas as pd

# ============================================================
# MODULE 07 — COMBINING DATAFRAMES
# Complete reference implementation for later revision.
# ============================================================

# ------------------------------------------------------------
# 1. CONCATENATE ROWS WITH concat()
# ------------------------------------------------------------

employees_part1 = pd.DataFrame(
    {
        "Name": ["Amit", "Neha"],
        "Department": ["IT", "HR"],
        "Salary": [85000, 65000],
    }
)

employees_part2 = pd.DataFrame(
    {
        "Name": ["Rahul", "Priya"],
        "Department": ["IT", "Finance"],
        "Salary": [95000, 72000],
    }
)

# axis=0 is the default and stacks rows vertically.
# ignore_index=True creates a fresh 0..N-1 index.
employees = pd.concat(
    [employees_part1, employees_part2],
    ignore_index=True,
)

print("\n1. Vertical concat:")
print(employees)


# ------------------------------------------------------------
# 2. CONCATENATE COLUMNS
# ------------------------------------------------------------

basic_info = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul"],
        "Department": ["IT", "HR", "IT"],
    }
)

salary_info = pd.DataFrame(
    {
        "Salary": [85000, 65000, 95000],
        "Experience": [5, 3, 8],
    }
)

# axis=1 combines columns side by side.
# Row indexes must align correctly.
combined_columns = pd.concat(
    [basic_info, salary_info],
    axis=1,
)

print("\n2. Horizontal concat:")
print(combined_columns)


# ------------------------------------------------------------
# 3. BASIC merge() — SQL-STYLE JOIN
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "EmployeeId": [101, 102, 103, 104],
        "Name": ["Amit", "Neha", "Rahul", "Priya"],
        "DepartmentId": [1, 2, 1, 3],
    }
)

departments = pd.DataFrame(
    {
        "DepartmentId": [1, 2, 3],
        "DepartmentName": ["IT", "HR", "Finance"],
    }
)

# Default merge type is inner join.
employee_departments = pd.merge(
    employees,
    departments,
    on="DepartmentId",
)

print("\n3. Inner merge:")
print(employee_departments)


# ------------------------------------------------------------
# 4. INNER JOIN
# ------------------------------------------------------------

inner_result = pd.merge(
    employees,
    departments,
    on="DepartmentId",
    how="inner",
)

print("\n4. Explicit inner join:")
print(inner_result)


# ------------------------------------------------------------
# 5. LEFT JOIN
# ------------------------------------------------------------

# Keeps every row from employees.
# Missing matches on the right become NaN.
left_result = pd.merge(
    employees,
    departments,
    on="DepartmentId",
    how="left",
)

print("\n5. Left join:")
print(left_result)


# ------------------------------------------------------------
# 6. RIGHT JOIN
# ------------------------------------------------------------

# Keeps every row from departments.
right_result = pd.merge(
    employees,
    departments,
    on="DepartmentId",
    how="right",
)

print("\n6. Right join:")
print(right_result)


# ------------------------------------------------------------
# 7. OUTER JOIN
# ------------------------------------------------------------

# Keeps all rows from both DataFrames.
outer_result = pd.merge(
    employees,
    departments,
    on="DepartmentId",
    how="outer",
)

print("\n7. Outer join:")
print(outer_result)


# ------------------------------------------------------------
# 8. DIFFERENT KEY NAMES
# ------------------------------------------------------------

employees_different_key = pd.DataFrame(
    {
        "EmployeeId": [101, 102, 103],
        "DeptId": [1, 2, 1],
    }
)

departments_different_key = pd.DataFrame(
    {
        "DepartmentId": [1, 2],
        "DepartmentName": ["IT", "HR"],
    }
)

# left_on identifies the key in the left DataFrame.
# right_on identifies the key in the right DataFrame.
different_key_result = pd.merge(
    employees_different_key,
    departments_different_key,
    left_on="DeptId",
    right_on="DepartmentId",
)

print("\n8. Merge using different key names:")
print(different_key_result)


# ------------------------------------------------------------
# 9. DUPLICATE COLUMN NAMES AND suffixes
# ------------------------------------------------------------

left = pd.DataFrame(
    {
        "Id": [1, 2],
        "Name": ["Amit", "Neha"],
    }
)

right = pd.DataFrame(
    {
        "Id": [1, 2],
        "Name": ["IT Team", "HR Team"],
    }
)

# suffixes makes duplicate non-key column names clear.
suffix_result = pd.merge(
    left,
    right,
    on="Id",
    suffixes=("_Employee", "_Team"),
)

print("\n9. Merge with suffixes:")
print(suffix_result)


# ------------------------------------------------------------
# 10. join() — INDEX-BASED COMBINING
# ------------------------------------------------------------

employees_indexed = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul"],
        "Salary": [85000, 65000, 95000],
    },
    index=[101, 102, 103],
)

ratings = pd.DataFrame(
    {
        "Rating": [4.5, 4.0, 4.8],
    },
    index=[101, 102, 103],
)

# join() matches rows using their indexes.
joined_result = employees_indexed.join(ratings)

print("\n10. Index-based join:")
print(joined_result)


# ------------------------------------------------------------
# 11. PRACTICAL AI / FEATURE-TABLE EXAMPLE
# ------------------------------------------------------------

customers = pd.DataFrame(
    {
        "CustomerId": [1, 2, 3],
        "Income": [72000, 40000, 91000],
    }
)

transactions = pd.DataFrame(
    {
        "CustomerId": [1, 2, 3],
        "TotalSpend": [30000, 45000, 10000],
        "TransactionCount": [20, 35, 8],
    }
)

# Combine customer profile data with behavioral features.
model_data = pd.merge(
    customers,
    transactions,
    on="CustomerId",
    how="left",
)

print("\n11. Final model feature table:")
print(model_data)


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Stack rows:
# pd.concat([df1, df2], ignore_index=True)

# Combine columns:
# pd.concat([df1, df2], axis=1)

# Inner join:
# pd.merge(left, right, on="Id", how="inner")

# Left join:
# pd.merge(left, right, on="Id", how="left")

# Right join:
# pd.merge(left, right, on="Id", how="right")

# Outer join:
# pd.merge(left, right, on="Id", how="outer")

# Different key names:
# pd.merge(
#     left,
#     right,
#     left_on="LeftKey",
#     right_on="RightKey"
# )

# Duplicate columns:
# pd.merge(
#     left,
#     right,
#     on="Id",
#     suffixes=("_Left", "_Right")
# )

# Index-based combination:
# left.join(right)

# SQL mental model:
# concat(axis=0) -> similar to UNION ALL
# merge(inner)   -> INNER JOIN
# merge(left)    -> LEFT JOIN
# merge(right)   -> RIGHT JOIN
# merge(outer)   -> FULL OUTER JOIN
