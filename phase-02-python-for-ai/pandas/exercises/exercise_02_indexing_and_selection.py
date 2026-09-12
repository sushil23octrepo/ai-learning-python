import pandas as pd

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
        "Experience": [5, 3, 8, 4, 2],
    }
)


print(employees.iloc[0])  # Select the first row using iloc.
print(employees.iloc[-2:])  # Select the last two rows using iloc.
print(employees.iloc[2, 2])  # Select the value 95000 using row and column positions.
print(
    employees.iloc[0:3, 0:2]
)  # Select the first three rows and the first two columns using iloc.

employees = employees.set_index("Name")  # Set Name as the DataFrame index.
print(employees.loc["Neha"])  # Select Neha's complete row using loc.
print()
print(employees.loc[["Amit", "Rahul"]])  # Select Amit and Rahul using their labels.
print()

print(
    employees.loc[:, "Salary":"Experience"]
)  # Select all rows, but only Salary and Experience, using loc.


print(
    employees.loc[employees["Salary"] > 70000, ["Department", "Salary"]]
)  # Select employees whose salary is greater than 70,000, displaying only Department and Salary.

# Update Karan's salary to 65,000 using loc, then print the final DataFrame.
employees.loc["Karan", "Salary"] = 65000
print(employees)
