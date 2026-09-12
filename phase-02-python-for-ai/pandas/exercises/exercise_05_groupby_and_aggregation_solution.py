import pandas as pd

# ============================================================
# PANDAS EXERCISE 05 — GROUPBY AND AGGREGATION
# Reference solution.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal", "Ravi"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance"],
        "Salary": [85000, 65000, 95000, 72000, 60000, 88000, 78000],
        "Experience": [5, 3, 8, 4, 2, 6, 7],
    }
)

# 1. Average salary for each department.
print(employees.groupby("Department")["Salary"].mean())

# 2. Highest salary in each department.
print(employees.groupby("Department")["Salary"].max())

# 3. Number of employees in each department.
print(employees.groupby("Department").size())

# 4. Average Experience for each department.
print(employees.groupby("Department")["Experience"].mean())

# 5. Average Salary and Experience by department.
print(employees.groupby("Department")[["Salary", "Experience"]].mean())

# 6. Named aggregation summary.
summary = employees.groupby("Department").agg(
    AverageSalary=("Salary", "mean"),
    HighestSalary=("Salary", "max"),
    LowestSalary=("Salary", "min"),
    AverageExperience=("Experience", "mean"),
)

print(summary)

# 7. Convert Department index into a normal column.
summary_reset = summary.reset_index()
print(summary_reset)

# 8. Employees with at least 5 years of experience,
#    then calculate average Salary by department.
experienced_employees = employees[employees["Experience"] >= 5]

print(experienced_employees.groupby("Department")["Salary"].mean())

# 9. Average Salary by department, highest to lowest.
print(employees.groupby("Department")["Salary"].mean().sort_values(ascending=False))

# 10. Total Salary paid by each department.
print(employees.groupby("Department")["Salary"].sum())
