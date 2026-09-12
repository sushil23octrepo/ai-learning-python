import pandas as pd

# ============================================================
# PANDAS EXERCISE 07 — COMBINING DATAFRAMES
# Reference solution.
# ============================================================

employees = pd.DataFrame(
    {
        "EmployeeId": [101, 102, 103, 104],
        "Name": ["Amit", "Neha", "Rahul", "Priya"],
        "DepartmentId": [1, 2, 1, 3],
    }
)

departments = pd.DataFrame(
    {
        "DepartmentId": [1, 2, 3, 4],
        "DepartmentName": ["IT", "HR", "Finance", "Operations"],
    }
)

salaries = pd.DataFrame(
    {
        "EmployeeId": [101, 102, 103, 105],
        "Salary": [85000, 65000, 95000, 70000],
    }
)


# ------------------------------------------------------------
# 1. Inner join employees and departments.
# ------------------------------------------------------------

print(
    pd.merge(
        employees,
        departments,
        on="DepartmentId",
        how="inner",
    )
)


# ------------------------------------------------------------
# 2. Left join employees and departments.
# ------------------------------------------------------------

print(
    pd.merge(
        employees,
        departments,
        on="DepartmentId",
        how="left",
    )
)


# ------------------------------------------------------------
# 3. Outer join employees and departments.
# ------------------------------------------------------------

print(
    pd.merge(
        employees,
        departments,
        on="DepartmentId",
        how="outer",
    )
)


# ------------------------------------------------------------
# 4. Inner join employees and salaries.
# ------------------------------------------------------------

print(
    pd.merge(
        employees,
        salaries,
        on="EmployeeId",
        how="inner",
    )
)


# ------------------------------------------------------------
# 5. Left join employees and salaries.
# ------------------------------------------------------------

print(
    pd.merge(
        employees,
        salaries,
        on="EmployeeId",
        how="left",
    )
)


# ------------------------------------------------------------
# 6. Outer join employees and salaries.
# ------------------------------------------------------------

print(
    pd.merge(
        employees,
        salaries,
        on="EmployeeId",
        how="outer",
    )
)


# ------------------------------------------------------------
# 7. Vertical concat.
# ------------------------------------------------------------

employees_part1 = pd.DataFrame(
    {
        "EmployeeId": [201, 202],
        "Name": ["Ravi", "Sonal"],
    }
)

employees_part2 = pd.DataFrame(
    {
        "EmployeeId": [203, 204],
        "Name": ["Karan", "Pooja"],
    }
)

vertical_concat = pd.concat(
    [employees_part1, employees_part2],
    ignore_index=True,
)

print(vertical_concat)


# ------------------------------------------------------------
# 8. Horizontal concat.
# ------------------------------------------------------------

basic_info = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul"],
    }
)

extra_info = pd.DataFrame(
    {
        "Experience": [5, 3, 8],
    }
)

horizontal_concat = pd.concat(
    [basic_info, extra_info],
    axis=1,
)

print(horizontal_concat)


# ------------------------------------------------------------
# 9. Index-based join().
# ------------------------------------------------------------

employee_info = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul"],
    },
    index=[101, 102, 103],
)

employee_ratings = pd.DataFrame(
    {
        "Rating": [4.5, 4.0, 4.8],
    },
    index=[101, 102, 103],
)

print(employee_info.join(employee_ratings))


# ------------------------------------------------------------
# 10. Final employee dataset:
#     Name + DepartmentName + Salary
# ------------------------------------------------------------

# First add DepartmentName to employee records.
employee_with_department = pd.merge(
    employees,
    departments,
    on="DepartmentId",
    how="left",
)

# Then add Salary.
final_employee_data = pd.merge(
    employee_with_department,
    salaries,
    on="EmployeeId",
    how="left",
)

# Select only the requested final columns.
final_employee_data = final_employee_data[["Name", "DepartmentName", "Salary"]]

print(final_employee_data)
