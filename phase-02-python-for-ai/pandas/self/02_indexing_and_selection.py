import pandas as pd

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
        "Experience": [5, 3, 8, 4, 2],
    }
)

print(employees.iloc[0])  # Select the first row by position.
print(employees.iloc[2])  # Select the first row by position.
print(employees.iloc[-1])  # Select the last row.

print(employees.iloc[0:1])  # First row as a DataFrame
print(employees.iloc[[0, 2]])  # First and third rows

# df.iloc[row_selection, column_selection]
print(employees.iloc[0, 2])  ## Row 0, column 2 -> Amit's salary.

print(employees.iloc[:, 2])  ## Row 0, column 2 -> Amit's salary.

print(employees.iloc[0:3, 0:2])  # First three rows and first two columns.

# loc uses labels. With the current default index, the row labels are integers, so this works:
print(employees.loc[0])  # Select the row whose index label is 0.
print(employees.loc[0:2])  # Select rows with labels 0 through 2.
employees = employees.set_index("Name")
print()
print(employees.loc["Amit"])
print(employees.loc[["Amit", "Rahul"]])

print(employees.loc["Amit":"Rahul"])  # Includes both Amit and Rahul.

# Select rows from Amit through Rahul,
# and columns from Department through Salary.
print(employees.loc["Amit":"Rahul", "Department":"Salary"])

# All rows, only Salary and Experience.
print(employees.loc[:, ["Salary", "Experience"]])

# All rows, columns at positions 1 and 2.
print(employees.iloc[:, [1, 2]])

high_salary = employees["Salary"] > 7000  # Create a boolean condition using a column.
print(employees.loc[high_salary])  # Select complete rows where the condition is True.

print(employees.loc[employees["Salary"] > 7000, ["Department", "Salary"]])

# Employees in IT with more than 5 years of experience.
mask = (employees["Department"] == "IT") & (employees["Experience"] > 5)

print(employees.loc[mask])

employees.loc["Amit", "Salary"] = 9000

# Give IT employees a 100 rs salary increase.

employees.loc[employees["Department"] == "IT", "Salary"] += 100
print(employees)
