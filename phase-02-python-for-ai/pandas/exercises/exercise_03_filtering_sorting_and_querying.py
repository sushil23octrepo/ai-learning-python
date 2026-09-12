import pandas as pd

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
        "Salary": [85000, 65000, 95000, 72000, 60000, 88000],
        "Experience": [5, 3, 8, 4, 2, 6],
    }
)

# Select employees whose salary is greater than 80000.
print(employees[employees["Salary"] > 80000])

# Select employees from IT with at least 6 years of experience.
print()
print(employees[(employees["Department"] == "IT") & (employees["Experience"] >= 6)])
# Select employees from either HR or Finance using isin().
print()
print(employees[employees["Department"].isin(["HR", "Finance"])])
# Select employees whose salary is between 70000 and 90000.
print()
print(employees[employees["Salary"].between(70000, 90000)])
# Sort all employees by salary from highest to lowest.
print()
print(employees.sort_values("Salary", ascending=False))
# Sort by Department ascending and Salary descending.
print(employees.sort_values(by=["Department", "Salary"], ascending=[True, False]))
# Show the three employees with the highest salaries.
print(employees.nlargest(3, "Salary"))
# Show the two employees with the lowest experience.
print(employees.nsmallest(2, "Experience"))

print()
minimum_salary = 85000
print(employees.query("Salary>=@minimum_salary"))

# query() salary > 70000 and experience >= 5
print(employees.query("Salary>70000 and Experience>=5 "))
