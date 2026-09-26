import matplotlib.pyplot as plt
import pandas as pd

# ============================================================
# MODULE 03 — SCATTER PLOTS
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. BASIC SCATTER PLOT
# ------------------------------------------------------------

experience = [1, 2, 3, 4, 5, 6]
salary = [40000, 45000, 52000, 60000, 70000, 82000]

# scatter(x_values, y_values)
# Each pair becomes one independent point.
plt.scatter(
    experience,
    salary,
)

plt.show()


# ------------------------------------------------------------
# 2. TITLE AND AXIS LABELS
# ------------------------------------------------------------

plt.scatter(
    experience,
    salary,
)

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.show()


# ------------------------------------------------------------
# 3. ADD GRID LINES
# ------------------------------------------------------------

plt.scatter(
    experience,
    salary,
)

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 4. LINE CHART VS SCATTER PLOT
# ------------------------------------------------------------

# Line chart:
# plt.plot(x, y)
#
# Use when point order or progression matters.
#
# Scatter plot:
# plt.scatter(x, y)
#
# Use when each point is an observation and you want
# to inspect the relationship between two numeric variables.


# ------------------------------------------------------------
# 5. PRACTICAL REGRESSION EXAMPLE
# ------------------------------------------------------------

house_size = [
    800,
    1000,
    1200,
    1500,
    1800,
    2200,
]

house_price = [
    250000,
    300000,
    340000,
    420000,
    500000,
    610000,
]

plt.scatter(
    house_size,
    house_price,
)

plt.title("House Size vs Price")
plt.xlabel("House Size")
plt.ylabel("House Price")

plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 6. SCATTER PLOT USING PANDAS
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "Experience": [1, 2, 3, 4, 5, 6],
        "Salary": [40000, 45000, 52000, 60000, 70000, 82000],
    }
)

# Pandas Series can be passed directly to scatter().
plt.scatter(
    employees["Experience"],
    employees["Salary"],
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 7. MULTIPLE GROUPS
# ------------------------------------------------------------

it_experience = [2, 4, 6, 8]
it_salary = [50000, 65000, 80000, 95000]

hr_experience = [1, 3, 5, 7]
hr_salary = [40000, 50000, 62000, 75000]

# label= identifies each group for the legend.
plt.scatter(
    it_experience,
    it_salary,
    label="IT",
)

plt.scatter(
    hr_experience,
    hr_salary,
    label="HR",
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

# legend() displays the labels supplied above.
plt.legend()

plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 8. PRACTICAL AI / ML CONNECTION
# ------------------------------------------------------------

study_hours = [1, 2, 3, 4, 5, 6, 7]
exam_scores = [45, 52, 60, 68, 75, 82, 90]

plt.scatter(
    study_hours,
    exam_scores,
)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.grid(True)
plt.show()


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Create scatter plot:
# plt.scatter(x_values, y_values)

# Add title:
# plt.title("Title")

# Axis labels:
# plt.xlabel("X Label")
# plt.ylabel("Y Label")

# Grid:
# plt.grid(True)

# Multiple groups:
# plt.scatter(x1, y1, label="Group 1")
# plt.scatter(x2, y2, label="Group 2")
# plt.legend()

# Display:
# plt.show()

# Chart selection:
#
# Line chart
# -> ordered progression / trend
#
# Bar chart
# -> category comparison
#
# Scatter plot
# -> relationship between two numeric variables

# Scatter plots can help reveal:
#
# correlation
# clusters
# outliers
# unusual patterns
#
# But visual correlation does NOT prove causation.
