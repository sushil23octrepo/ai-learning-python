import pandas as pd

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
        "Experience": [5, 3, 8, 4, 2],
    }
)

# Add a new column
employees["Bonus"] = employees["Salary"] * 0.10
employees["TotalCompensation"] = employees["Salary"] + employees["Bonus"]
print(employees)

# Add column conditionaly
print()
employees["ExperienceLevel"] = "Junior"
print(employees)
employees.loc[employees["Experience"] >= 5, "ExperienceLevel"] = "Experienced"
print(employees)

# apply() — transform values using a function
print()


def salary_band(salary):
    if salary >= 90000:
        return "High"
    elif salary >= 70000:
        return "Medium"

    return "Low"


# apply() runs the function once for each Series value.
employees["SalaryBand"] = employees["Salary"].apply(salary_band)
print(employees)

# map() — replace or transform Series values
print()
department_names = {
    "IT": "Information Technology",
    "HR": "Human Resources",
    "Finance": "Finance",
}
# map() is particularly useful for translating one value into another using a dictionary.
employees["DepartmentFullName"] = employees["Department"].map(department_names)
print(employees)

# Replace values with replace()
print()
employees["Department"] = employees["Department"].replace(
    {
        "IT": "Technology",
        "HR": "Human Resources",
    }
)
print(employees)

# Rename columns
print()
employees = employees.rename(columns={"Name": "EmployeeName", "Salary": "AnnualSalary"})
print(employees)

# Drop one column
print()
employees = employees.drop(columns=["Experience"])
# To drop several columns:
employees = employees.drop(columns=["Bonus", "SalaryBand"])
print(employees)

# Drop rows
print()
employees = employees.drop(index=[0])
print(employees)

# Insert a column at a specific position
print()
employees.insert(1, "EmployeeId", [101, 102, 103, 104])
print(employees)

# Convert data types with astype()
employees["EmployeeId"] = employees["EmployeeId"].astype(str)

# String transformations
print()
employees["NameUpper"] = employees["EmployeeName"].str.upper()
print(employees)
