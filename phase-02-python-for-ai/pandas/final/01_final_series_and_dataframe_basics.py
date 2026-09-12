import pandas as pd

# ============================================================
# MODULE 01 — SERIES AND DATAFRAME BASICS
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. SERIES — A one-dimensional labeled array
# ------------------------------------------------------------

# Pandas automatically creates integer index labels starting at 0.
scores = pd.Series([80, 70, 90, 85])

print("\n1. Basic Series")
print(scores)


# Create a Series with custom index labels.
# The index list must have the same number of elements as the values.
named_scores = pd.Series(
    [80, 70, 90],
    index=["Amit", "Neha", "Rahul"],
)

print("\n2. Series with custom index")
print(named_scores)

# Select a value using its index label.
print("\nNeha's score:")
print(named_scores["Neha"])


# ------------------------------------------------------------
# 2. DATAFRAME — A two-dimensional labeled table
# ------------------------------------------------------------

# Each dictionary key becomes a column name.
# Each list contains the values for that column.
# All columns must contain the same number of rows.
customers = pd.DataFrame(
    {
        "Customer": ["Amit", "Neha", "Rahul", "Priya"],
        "Income": [72000, 40000, 91000, 60000],
        "CreditScore": [750, 650, 820, 700],
        "Debt": [15000, 32000, 9000, 27000],
    }
)

print("\n3. Complete DataFrame")
print(customers)


# ------------------------------------------------------------
# 3. DATAFRAME PROPERTIES
# ------------------------------------------------------------

# shape returns (number_of_rows, number_of_columns).
print("\n4. Shape:")
print(customers.shape)

# size returns the total number of values: rows * columns.
print("\n5. Size:")
print(customers.size)

# ndim returns the number of dimensions.
print("\n6. Number of dimensions:")
print(customers.ndim)

# columns returns the column labels.
print("\n7. Column names:")
print(customers.columns)

# index returns the row index labels.
print("\n8. Row index:")
print(customers.index)

# dtypes returns the data type of every column.
print("\n9. Column data types:")
print(customers.dtypes)


# ------------------------------------------------------------
# 4. PREVIEWING AND INSPECTING DATA
# ------------------------------------------------------------

# head(n) returns the first n rows.
# Without an argument, head() returns the first 5 rows.
print("\n10. First two rows:")
print(customers.head(2))

# tail(n) returns the last n rows.
print("\n11. Last two rows:")
print(customers.tail(2))

# info() displays column types, non-null counts, and memory usage.
# It prints its summary directly and returns None.
print("\n12. DataFrame information:")
customers.info()

# describe() calculates summary statistics for numeric columns.
# It includes count, mean, std, min, quartiles, and max.
print("\n13. Numeric summary:")
print(customers.describe())


# ------------------------------------------------------------
# 5. SELECTING COLUMNS
# ------------------------------------------------------------

# Selecting one column using its name returns a Series.
income = customers["Income"]

print("\n14. Income column as Series:")
print(income)
print(type(income))

# Double brackets contain a list of column names.
# Selecting multiple columns returns a DataFrame.
selected_columns = customers[["Customer", "Income"]]

print("\n15. Customer and Income columns:")
print(selected_columns)
print(type(selected_columns))

# Selecting one column with a list preserves DataFrame structure.
income_dataframe = customers[["Income"]]

print("\n16. Income as a DataFrame:")
print(income_dataframe)
print(type(income_dataframe))


# ------------------------------------------------------------
# 6. BASIC NUMERIC CALCULATIONS
# ------------------------------------------------------------

# mean() calculates the arithmetic average of the selected column.
print("\n17. Average income:")
print(customers["Income"].mean())

# max() returns the largest value in the selected column.
print("\n18. Highest credit score:")
print(customers["CreditScore"].max())

# sum() adds all values in the selected column.
print("\n19. Total debt:")
print(customers["Debt"].sum())


# ------------------------------------------------------------
# 7. CREATING A NEW COLUMN
# ------------------------------------------------------------

# Pandas performs the division element-wise across the columns.
# A new column is created when assigning to a new column name.
customers["DebtRatio"] = customers["Debt"] / customers["Income"]

print("\n20. DataFrame with DebtRatio:")
print(customers)


# ------------------------------------------------------------
# 8. IMPORTANT SYNTAX REVISION
# ------------------------------------------------------------

# Properties do not use parentheses:
# customers.shape
# customers.size
# customers.ndim
# customers.columns
# customers.index
# customers.dtypes

# Methods execute an operation and use parentheses:
# customers.head()
# customers.tail()
# customers.info()
# customers.describe()
# customers["Income"].mean()
# customers["CreditScore"].max()

# One column -> Series:
# customers["Income"]

# One column wrapped in a list -> DataFrame:
# customers[["Income"]]

# Multiple columns -> DataFrame:
# customers[["Customer", "Income"]]

# Pandas Series and DataFrames have index labels.
# Label-based and position-based selection will be covered
# in the next lesson using loc and iloc.
