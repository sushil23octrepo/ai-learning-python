import pandas as pd

# ============================================================
# MODULE 05 — GROUPBY AND AGGREGATION
# Complete reference implementation for later revision.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
        "Salary": [85000, 65000, 95000, 72000, 60000, 88000],
        "Experience": [5, 3, 8, 4, 2, 6],
    }
)

print("\nOriginal DataFrame:")
print(employees)

# 1. Basic groupby(): average Salary per Department.
department_salary = employees.groupby("Department")["Salary"].mean()
print("\nAverage salary by department:")
print(department_salary)

# 2. Multiple aggregations on the Salary column.
salary_summary = employees.groupby("Department")["Salary"].agg(["mean", "min", "max"])
print("\nSalary summary:")
print(salary_summary)

# 3. size() counts all rows in each group.
employee_count = employees.groupby("Department").size()
print("\nEmployee count by department:")
print(employee_count)

# 4. count() counts non-missing values in the selected column.
name_count = employees.groupby("Department")["Name"].count()
print("\nNon-missing Name count:")
print(name_count)

# 5. Aggregate multiple numeric columns.
department_averages = employees.groupby("Department")[["Salary", "Experience"]].mean()
print("\nAverage Salary and Experience:")
print(department_averages)

# 6. Named aggregation lets us control output column names.
department_summary = employees.groupby("Department").agg(
    AverageSalary=("Salary", "mean"),
    HighestSalary=("Salary", "max"),
    LowestSalary=("Salary", "min"),
    AverageExperience=("Experience", "mean"),
)
print("\nNamed aggregation summary:")
print(department_summary)

# 7. reset_index() converts Department from index to a normal column.
department_summary_reset = department_summary.reset_index()
print("\nDepartment as a normal column:")
print(department_summary_reset)

# 8. Group by multiple columns.
employees_with_level = employees.copy()
employees_with_level["Level"] = ["Mid", "Junior", "Senior", "Mid", "Junior", "Senior"]

multi_group_summary = employees_with_level.groupby(["Department", "Level"])[
    "Salary"
].mean()

print("\nAverage Salary by Department and Level:")
print(multi_group_summary)

# 9. Filter first, then group.
experienced = employees[employees["Experience"] >= 4]

experienced_summary = experienced.groupby("Department")["Salary"].mean()

print("\nAverage salary for employees with Experience >= 4:")
print(experienced_summary)

# 10. Group, aggregate, then sort.
sorted_department_salary = (
    employees.groupby("Department")["Salary"].mean().sort_values(ascending=False)
)

print("\nDepartment average salary descending:")
print(sorted_department_salary)

# 11. Practical transaction example.
transactions = pd.DataFrame(
    {
        "Customer": ["Amit", "Neha", "Amit", "Rahul", "Neha", "Amit"],
        "Amount": [500, 700, 300, 1000, 400, 800],
    }
)

print("\nTransactions:")
print(transactions)

print("\nTotal spend by customer:")
print(transactions.groupby("Customer")["Amount"].sum())

print("\nAverage transaction by customer:")
print(transactions.groupby("Customer")["Amount"].mean())

print("\nTransaction count by customer:")
print(transactions.groupby("Customer").size())

# 12. AI / feature-engineering example.
# Convert many transactions per customer into one feature row.
customer_features = (
    transactions.groupby("Customer")
    .agg(
        TotalSpend=("Amount", "sum"),
        AverageSpend=("Amount", "mean"),
        TransactionCount=("Amount", "count"),
    )
    .reset_index()
)

print("\nCustomer features:")
print(customer_features)

# ============================================================
# IMPORTANT REVISION
# ============================================================

# Basic grouping:
# df.groupby("Department")["Salary"].mean()

# Count rows:
# df.groupby("Department").size()

# Multiple aggregations:
# df.groupby("Department")["Salary"].agg(["mean", "min", "max"])

# Multiple columns:
# df.groupby("Department")[["Salary", "Experience"]].mean()

# Named aggregation:
# df.groupby("Department").agg(
#     AverageSalary=("Salary", "mean"),
#     HighestSalary=("Salary", "max"),
# )

# Convert grouped index to normal column:
# result.reset_index()

# Filter, then group:
# filtered = df[df["Experience"] >= 5]
# filtered.groupby("Department")["Salary"].mean()

# Group, aggregate, then sort:
# (
#     df.groupby("Department")["Salary"]
#     .mean()
#     .sort_values(ascending=False)
# )
