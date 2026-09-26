import matplotlib.pyplot as plt
import pandas as pd

# ============================================================
# MODULE 04 — HISTOGRAM
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. BASIC HISTOGRAM
# ------------------------------------------------------------

ages = [
    22,
    25,
    27,
    29,
    31,
    33,
    35,
    36,
    38,
    40,
    42,
    45,
    47,
    50,
    52,
]

# hist() groups numeric values into ranges called bins.
plt.hist(ages)

plt.show()


# ------------------------------------------------------------
# 2. CONTROL NUMBER OF BINS
# ------------------------------------------------------------

# bins controls how many numeric ranges are created.
plt.hist(
    ages,
    bins=5,
)

plt.show()


# ------------------------------------------------------------
# 3. TITLE AND AXIS LABELS
# ------------------------------------------------------------

plt.hist(
    ages,
    bins=5,
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()


# ------------------------------------------------------------
# 4. ADD HORIZONTAL GRID LINES
# ------------------------------------------------------------

plt.hist(
    ages,
    bins=5,
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Horizontal grid lines make the frequency easier to compare.
plt.grid(axis="y")

plt.show()


# ------------------------------------------------------------
# 5. SALARY DISTRIBUTION EXAMPLE
# ------------------------------------------------------------

salaries = [
    45000,
    50000,
    52000,
    55000,
    58000,
    60000,
    62000,
    65000,
    70000,
    75000,
    80000,
    85000,
    90000,
    95000,
    120000,
]

plt.hist(
    salaries,
    bins=6,
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Employee Count")

plt.grid(axis="y")
plt.show()


# ------------------------------------------------------------
# 6. HISTOGRAM USING PANDAS
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "Salary": [
            45000,
            50000,
            52000,
            55000,
            58000,
            60000,
            65000,
            70000,
            80000,
            90000,
        ]
    }
)

# A Pandas Series can be passed directly to hist().
plt.hist(
    employees["Salary"],
    bins=5,
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.grid(axis="y")
plt.show()


# ------------------------------------------------------------
# 7. PRACTICAL AI / ML EXAMPLE
# ------------------------------------------------------------

income = [
    30000,
    32000,
    35000,
    37000,
    40000,
    42000,
    45000,
    48000,
    50000,
    52000,
    55000,
    60000,
    65000,
    90000,
    200000,
]

plt.hist(
    income,
    bins=6,
)

plt.title("Customer Income Distribution")
plt.xlabel("Income")
plt.ylabel("Customer Count")

plt.grid(axis="y")
plt.show()


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Create histogram:
# plt.hist(values)

# Control grouping:
# plt.hist(values, bins=5)

# Add title:
# plt.title("Title")

# Axis labels:
# plt.xlabel("X Label")
# plt.ylabel("Y Label")

# Horizontal grid:
# plt.grid(axis="y")

# Display:
# plt.show()

# Histogram helps inspect:
#
# distribution
# spread
# concentration
# skewness
# outliers

# Important distinction:
#
# Bar chart
# -> compares categories
#
# Histogram
# -> shows distribution of numeric values
#
# bins
# -> numeric ranges used to group values
