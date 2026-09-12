import pandas as pd

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
# Use concat() when DataFrames have the same or similar columns and you want to add rows together.
# ignore_index=True creates a fresh index:
employees = pd.concat([employees_part1, employees_part2], ignore_index=True)
print(employees)

# You can also combine DataFrames side by side:
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

combined = pd.concat([basic_info, salary_info], axis=1)
print()
print(combined)


# merge() — SQL-style joins
print()
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
# Conceptually: JOIN departmentsON employees.DepartmentId = departments.DepartmentId
result = pd.merge(employees, departments, on="DepartmentId")
print(result)
# You can also make it explicit:
result = pd.merge(employees, departments, on="DepartmentId", how="inner")
result = pd.merge(employees, departments, on="DepartmentId", how="left")
result = pd.merge(employees, departments, on="DepartmentId", how="right")
result = pd.merge(
    employees, departments, on="DepartmentId", how="outer"
)  # This keeps records from both DataFrames, even when they do not match.

# Sometimes the columns have different names.
employees = pd.DataFrame(
    {
        "EmployeeId": [101, 102, 103],
        "DeptId": [1, 2, 1],
    }
)

departments = pd.DataFrame(
    {
        "DepartmentId": [1, 2],
        "DepartmentName": ["IT", "HR"],
    }
)
result = pd.merge(
    employees, departments, left_on="DeptId", right_on="DepartmentId", how="left"
)

print(result)

# Duplicate column names and suffixes
print()
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

result = pd.merge(left, right, on="Id", suffixes=("_Employee", "_Team"))

print(result)
