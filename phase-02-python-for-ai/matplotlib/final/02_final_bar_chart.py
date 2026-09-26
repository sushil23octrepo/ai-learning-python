import matplotlib.pyplot as plt
import pandas as pd

# ============================================================
# MODULE 02 — BAR CHARTS
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. BASIC VERTICAL BAR CHART
# ------------------------------------------------------------

departments = ["IT", "HR", "Finance", "Sales"]
employees = [25, 12, 10, 18]

# bar(x_categories, values) creates vertical bars.
plt.bar(
    departments,
    employees,
)

plt.show()


# ------------------------------------------------------------
# 2. TITLE AND AXIS LABELS
# ------------------------------------------------------------

plt.bar(
    departments,
    employees,
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()


# ------------------------------------------------------------
# 3. HORIZONTAL GRID LINES
# ------------------------------------------------------------

plt.bar(
    departments,
    employees,
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

# axis="y" adds horizontal grid lines.
plt.grid(axis="y")

plt.show()


# ------------------------------------------------------------
# 4. HORIZONTAL BAR CHART
# ------------------------------------------------------------

# barh() creates horizontal bars.
plt.barh(
    departments,
    employees,
)

plt.title("Employees by Department")
plt.xlabel("Employee Count")
plt.ylabel("Department")

plt.show()


# ------------------------------------------------------------
# 5. SORT DATA BEFORE PLOTTING
# ------------------------------------------------------------

department_data = pd.DataFrame(
    {
        "Department": ["IT", "HR", "Finance", "Sales"],
        "Employees": [25, 12, 10, 18],
    }
)

# Sort highest employee count first.
department_data = department_data.sort_values(
    "Employees",
    ascending=False,
)

plt.bar(
    department_data["Department"],
    department_data["Employees"],
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()


# ------------------------------------------------------------
# 6. ADD VALUES ABOVE BARS
# ------------------------------------------------------------

bars = plt.bar(
    departments,
    employees,
)

# bar_label() displays the numeric value on each bar.
plt.bar_label(bars)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()


# ------------------------------------------------------------
# 7. PRODUCT REVENUE EXAMPLE
# ------------------------------------------------------------

products = [
    "Laptop",
    "Phone",
    "Tablet",
    "Monitor",
]

revenue = [
    450000,
    380000,
    210000,
    170000,
]

bars = plt.bar(
    products,
    revenue,
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.bar_label(bars)

plt.grid(axis="y")
plt.show()


# ------------------------------------------------------------
# 8. PRACTICAL AI — CLASS DISTRIBUTION
# ------------------------------------------------------------

classes = [
    "Approved",
    "Rejected",
]

counts = [
    720,
    280,
]

bars = plt.bar(
    classes,
    counts,
)

plt.title("Loan Approval Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")

plt.bar_label(bars)

plt.show()


# ------------------------------------------------------------
# 9. PRACTICAL AI — MODEL COMPARISON
# ------------------------------------------------------------

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
]

accuracy = [
    0.82,
    0.79,
    0.88,
]

bars = plt.bar(
    models,
    accuracy,
)

plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")

plt.bar_label(bars)

plt.grid(axis="y")
plt.show()


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Vertical bar chart:
# plt.bar(categories, values)

# Horizontal bar chart:
# plt.barh(categories, values)

# Add chart title:
# plt.title("Title")

# Axis labels:
# plt.xlabel("X Label")
# plt.ylabel("Y Label")

# Horizontal grid lines:
# plt.grid(axis="y")

# Add values to bars:
# bars = plt.bar(categories, values)
# plt.bar_label(bars)

# Display chart:
# plt.show()

# Useful rule:
#
# Line chart -> trend / ordered progression
# Bar chart  -> compare categories
