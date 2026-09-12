import pandas as pd

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
        "Salary": [85000, 65000, 95000, 72000, 60000, 88000],
        "Experience": [5, 3, 8, 4, 2, 6],
    }
)


high_salary = employees["Salary"] > 70000
print(employees[high_salary])
print(employees[employees["Salary"] > 70000])

# Use & for AND:
filtered = employees[(employees["Department"] == "HR") & (employees["Salary"] > 90000)]
print(filtered)

# Use | for OR:
filtered = employees[(employees["Department"] == "HR") | (employees["Salary"] > 90000)]
print(filtered)

print()

# Use ~ for NOT:
not_hr = employees[~(employees["Department"] == "HR")]
print(not_hr)
print()

# isin() — check multiple possible values
print(employees[employees["Department"].isin(["IT", "Finance"])])

# not in
print(employees[~employees["Department"].isin(["IT", "Finance"])])

print()
print(employees[employees["Salary"].between(70000, 90000)])

print()
# Sorting by one column
print(employees.sort_values("Salary"))
print()
print(employees.sort_values("Salary", ascending=False))
print()

# Sorting by multiple columns
print(employees.sort_values(by=["Department", "Salary"], ascending=[True, False]))

# Sorting by index
employees_by_name = employees.set_index("Name")
print(employees_by_name.sort_index())

print()
# using query
print(employees.query("Salary>70000 and Experience>5"))

# variable inside query
print()
min_salary = 80000
print(employees.query("Salary>@min_salary"))

# Get the highest or lowest rows
print()
print(employees.nlargest(3, "Salary"))

print()
print(employees.nsmallest(2, "Experience"))
