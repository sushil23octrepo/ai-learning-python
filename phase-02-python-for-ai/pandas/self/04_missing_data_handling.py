import pandas as pd
import numpy as np

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", None, "Finance", "HR"],
        "Salary": [85000, None, 95000, 72000, 60000],
        "Experience": [5, 3, 8, None, 2],
    }
)

# Detect missing values with isna()
print(employees.isnull())
print(employees.isnull().sum())

# Check whether the DataFrame contains any missing values
print(employees.isnull().any())

# To check the entire DataFrame:
print()
print(employees.isna().any().any())

# Find rows containing missing values
print()
print(employees[employees.isna().any(axis=1)])

# Drop rows with missing values
print()
print(employees.dropna())

# Drop rows only when specific columns are missing
print()
print(employees.dropna(subset="Salary"))

# Fill missing values with fillna()
print()
employees["Department"] = employees["Department"].fillna("Unknown")
print(employees)

# Fill missing numeric values using the mean
print()
avg_salary = employees["Salary"].mean()
employees["Salary"] = employees["Salary"].fillna(avg_salary)
print(employees)

# Fill different columns differently
employees = employees.fillna(
    {
        "Department": "Unknown",
        "Salary": employees["Salary"].mean(),
        "Experience": employees["Experience"].median(),
    }
)
