import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# MODULE 08 — PANDAS WITH MATPLOTLIB
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. PLOT DIRECTLY FROM DATAFRAME COLUMNS
# ------------------------------------------------------------

sales = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Revenue": [120000, 135000, 128000, 150000, 165000],
    }
)

# Pandas Series can be passed directly to Matplotlib.
plt.plot(
    sales["Month"],
    sales["Revenue"],
    marker="o",
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 2. FILTER WITH PANDAS, THEN VISUALIZE
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
    }
)

# Pandas handles the filtering.
high_salary = employees[employees["Salary"] > 70000]

# Matplotlib visualizes the filtered result.
bars = plt.bar(
    high_salary["Name"],
    high_salary["Salary"],
)

plt.title("Employees with Salary Above 70000")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.bar_label(bars)

plt.show()


# ------------------------------------------------------------
# 3. GROUPBY THEN VISUALIZE
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "Department": [
            "IT",
            "HR",
            "IT",
            "Finance",
            "HR",
            "IT",
        ],
        "Salary": [
            85000,
            65000,
            95000,
            72000,
            60000,
            88000,
        ],
    }
)

# Calculate average salary by department.
department_salary = employees.groupby("Department")["Salary"].mean().reset_index()

print(department_salary)

bars = plt.bar(
    department_salary["Department"],
    department_salary["Salary"],
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(bars)

plt.show()


# ------------------------------------------------------------
# 4. SORT BEFORE PLOTTING
# ------------------------------------------------------------

department_salary = department_salary.sort_values(
    "Salary",
    ascending=False,
)

bars = plt.bar(
    department_salary["Department"],
    department_salary["Salary"],
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(bars)

plt.grid(axis="y")

plt.show()


# ------------------------------------------------------------
# 5. HISTOGRAM FROM A PANDAS COLUMN
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "Salary": [
            45000,
            50000,
            52000,
            60000,
            65000,
            70000,
            80000,
            90000,
            95000,
        ]
    }
)

plt.hist(
    employees["Salary"],
    bins=5,
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Employee Count")

plt.grid(axis="y")

plt.show()


# ------------------------------------------------------------
# 6. SCATTER PLOT FROM DATAFRAME COLUMNS
# ------------------------------------------------------------

customers = pd.DataFrame(
    {
        "Income": [
            30000,
            45000,
            60000,
            75000,
            90000,
        ],
        "Debt": [
            12000,
            18000,
            20000,
            25000,
            30000,
        ],
    }
)

plt.scatter(
    customers["Income"],
    customers["Debt"],
)

plt.title("Income vs Debt")
plt.xlabel("Income")
plt.ylabel("Debt")

plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 7. DATE COLUMN WITH MATPLOTLIB
# ------------------------------------------------------------

orders = pd.DataFrame(
    {
        "OrderDate": [
            "2026-09-01",
            "2026-09-02",
            "2026-09-03",
            "2026-09-04",
        ],
        "Orders": [
            100,
            125,
            118,
            140,
        ],
    }
)

# Convert string date to Pandas datetime.
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

plt.plot(
    orders["OrderDate"],
    orders["Orders"],
    marker="o",
)

plt.title("Daily Orders")
plt.xlabel("Date")
plt.ylabel("Order Count")

plt.xticks(
    rotation=45,
)

plt.grid(True)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 8. REALISTIC DATA PREPARATION + VISUALIZATION
# ------------------------------------------------------------

customers = pd.DataFrame(
    {
        "Name": [
            "Amit",
            "Neha",
            "Rahul",
            "Priya",
            "Karan",
        ],
        "Income": [
            "50000",
            "65000",
            "invalid",
            "80000",
            "95000",
        ],
    }
)

# Convert string data into numeric values.
# Invalid values become NaN.
customers["Income"] = pd.to_numeric(
    customers["Income"],
    errors="coerce",
)

# Remove rows where Income is missing.
customers = customers.dropna(subset=["Income"])

plt.hist(
    customers["Income"],
    bins=4,
)

plt.title("Customer Income Distribution")
plt.xlabel("Income")
plt.ylabel("Customer Count")

plt.grid(axis="y")

plt.show()


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Pandas is normally responsible for:
#
# loading
# cleaning
# filtering
# sorting
# grouping
# aggregation
# type conversion
# feature preparation


# Matplotlib is normally responsible for:
#
# visualization
# trends
# comparisons
# distributions
# relationships


# Typical workflow:
#
# DataFrame
#     ↓
# clean / filter
#     ↓
# group / aggregate
#     ↓
# sort
#     ↓
# select columns
#     ↓
# Matplotlib


# Example:
#
# summary = (
#     df
#     .groupby("Category")["Value"]
#     .sum()
#     .reset_index()
# )
#
# plt.bar(
#     summary["Category"],
#     summary["Value"],
# )
#
# plt.show()


# ============================================================
# AI / ML CONNECTION
# ============================================================

# Before model training, Pandas and Matplotlib are commonly used
# together to inspect:
#
# class balance
# numeric distributions
# outliers
# relationships between features
# missing data effects
# aggregated business patterns
#
# Pandas prepares the data.
# Matplotlib helps you understand it visually.
