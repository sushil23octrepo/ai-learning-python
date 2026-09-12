import pandas as pd

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
        "Salary": [85000, 65000, 95000, 72000, 60000, 88000],
        "Experience": [5, 3, 8, 4, 2, 6],
    }
)
# Basic groupby()
# Suppose you want the average salary for each department:
print(employees.groupby("Department")["Salary"].mean())

# You can calculate several aggregations together using agg():
print()
print(employees.groupby("Department")["Salary"].agg(["mean", "min", "max"]))

# Count employees per department
print()
print(employees.groupby("Department").size())

# count() counts non-missing values in the selected column.
print()
print(employees.groupby("Department")["Name"].count())

# Aggregate multiple columns
print()
print(employees.groupby("Department")[["Salary", "Experience"]].mean())

# Named aggregations
print()
print(
    employees.groupby("Department").agg(
        AverageSalary=("Salary", "mean"),
        HighestSalary=("Salary", "max"),
        AverageExperience=("Salary", "mean"),
    )
)


# You can group by more than one field.
print()
employees["Level"] = [
    "Mid",
    "Junior",
    "Senior",
    "Mid",
    "Junior",
    "Senior",
]
print(employees.groupby(["Department", "Level"])["Salary"].mean())

# Filter groups before grouping
print()
print(employees[employees["Experience"] > 4].groupby("Department")["Salary"].mean())

# Sort aggregated results
print()
print(employees.groupby("Department")["Salary"].mean().sort_values(ascending=False))
