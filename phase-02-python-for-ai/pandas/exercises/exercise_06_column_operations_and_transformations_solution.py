import pandas as pd

# ============================================================
# PANDAS EXERCISE 06 — COLUMN OPERATIONS AND TRANSFORMATIONS
# Reference solution.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
        "Experience": [5, 3, 8, 4, 2],
    }
)

# 1. Bonus = 10% of Salary.
employees["Bonus"] = employees["Salary"] * 0.10

# 2. TotalCompensation = Salary + Bonus.
employees["TotalCompensation"] = employees["Salary"] + employees["Bonus"]

# 3. Create ExperienceLevel.
employees["ExperienceLevel"] = "Junior"
employees.loc[employees["Experience"] >= 5, "ExperienceLevel"] = "Experienced"


# 4. Create SalaryBand using a function and apply().
def salary_band(salary):
    if salary >= 90000:
        return "High"
    elif salary >= 70000:
        return "Medium"
    return "Low"


employees["SalaryBand"] = employees["Salary"].apply(salary_band)

# 5. SalaryInLakhs using vectorized division.
employees["SalaryInLakhs"] = employees["Salary"] / 100000

# 6. DepartmentFullName using map().
department_names = {
    "IT": "Information Technology",
    "HR": "Human Resources",
    "Finance": "Finance",
}
employees["DepartmentFullName"] = employees["Department"].map(department_names)

# 7. Rename Name to EmployeeName.
employees = employees.rename(columns={"Name": "EmployeeName"})

# 8. Insert EmployeeId at column position 0.
employees.insert(0, "EmployeeId", [101, 102, 103, 104, 105])

# 9. Convert EmployeeId to string.
employees["EmployeeId"] = employees["EmployeeId"].astype(str)

# 10. Create EmployeeNameUpper using a Pandas string operation.
employees["EmployeeNameUpper"] = employees["EmployeeName"].str.upper()

# 11. Drop SalaryBand.
employees = employees.drop(columns=["SalaryBand"])

# 12. Print final DataFrame and dtypes.
print("\nFinal DataFrame:")
print(employees)

print("\nData types:")
print(employees.dtypes)
