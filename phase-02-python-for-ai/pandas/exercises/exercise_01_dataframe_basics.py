import pandas as pd

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
        "Experience": [5, 3, 8, 4, 2],
    }
)

print(employees)  # Print the complete DataFrame.
print(employees.shape, employees.size, employees.ndim)
print(employees.head(3))  # Print the first three rows.
print(
    employees["Name"].dtype,
    employees["Department"].dtype,
    employees["Salary"].dtype,
    employees["Experience"].dtype,
)  # Print the data type of every column.

print(employees["Salary"])  # Select only the Salary column as a Series.
print(employees[["Name", "Salary"]])  # Select Name and Salary as a DataFrame.
print(employees["Salary"].mean())  # Calculate the average salary.
print(employees["Experience"].max())  # Find the highest experience.
employees["SalaryAfterBonus"] = (
    employees["Salary"] + employees["Salary"] / 10
)  # Create a new column named SalaryAfterBonus by increasing each salary by 10%.
print(employees)  # Print the final DataFrame.
