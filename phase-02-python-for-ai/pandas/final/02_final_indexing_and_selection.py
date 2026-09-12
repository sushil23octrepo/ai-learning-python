import pandas as pd

# ============================================================
# MODULE 02 — INDEXING AND SELECTION
# Complete reference implementation for later revision.
# ============================================================

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
        "Experience": [5, 3, 8, 4, 2],
    }
)

print("\nOriginal DataFrame:")
print(employees)


# ------------------------------------------------------------
# 1. ILOC — SELECT USING INTEGER POSITIONS
# ------------------------------------------------------------

# iloc uses zero-based row and column positions.
print("\n1. First row:")
print(employees.iloc[0])

# Negative positions work just like Python indexing.
print("\n2. Last row:")
print(employees.iloc[-1])

# A slice preserves DataFrame structure.
print("\n3. First row as DataFrame:")
print(employees.iloc[0:1])

# Select multiple specific row positions.
print("\n4. First and third rows:")
print(employees.iloc[[0, 2]])

# Select the last two rows while preserving their original order.
print("\n5. Last two rows:")
print(employees.iloc[-2:])


# ------------------------------------------------------------
# 2. SELECT ROW AND COLUMN USING ILOC
# ------------------------------------------------------------

# Syntax:
# df.iloc[row_position, column_position]

# Row 0, column 2 -> Amit's Salary.
print("\n6. Amit's salary:")
print(employees.iloc[0, 2])

# ':' means all rows.
# Column position 2 is Salary.
print("\n7. Salary column using iloc:")
print(employees.iloc[:, 2])

# Select rows 0, 1, 2 and columns 0, 1.
# iloc slicing excludes the stop position.
print("\n8. First 3 rows and first 2 columns:")
print(employees.iloc[0:3, 0:2])


# ------------------------------------------------------------
# 3. LOC — SELECT USING LABELS
# ------------------------------------------------------------

# With the default integer index, loc uses index labels.
print("\n9. Row whose index label is 0:")
print(employees.loc[0])

# loc label slicing includes the ending label.
print("\n10. Index labels 0 through 2:")
print(employees.loc[0:2])


# ------------------------------------------------------------
# 4. USE A MEANINGFUL INDEX
# ------------------------------------------------------------

# set_index() uses an existing column as the row index.
# By default, Name is removed from the normal columns.
employees = employees.set_index("Name")

print("\n11. DataFrame with Name as index:")
print(employees)


# ------------------------------------------------------------
# 5. SELECT ROWS USING LOC LABELS
# ------------------------------------------------------------

# Select one employee using the index label.
print("\n12. Amit:")
print(employees.loc["Amit"])

# Select multiple labels using a list.
print("\n13. Amit and Rahul:")
print(employees.loc[["Amit", "Rahul"]])

# Select one exact row and column value.
print("\n14. Amit's Salary:")
print(employees.loc["Amit", "Salary"])


# ------------------------------------------------------------
# 6. LABEL-BASED SLICING
# ------------------------------------------------------------

# loc includes the ending label in a label slice.
print("\n15. Amit through Rahul:")
print(employees.loc["Amit":"Rahul"])

# Row labels Amit through Rahul.
# Column labels Department through Salary.
print("\n16. Row and column label slicing:")
print(
    employees.loc[
        "Amit":"Rahul",
        "Department":"Salary",
    ]
)


# ------------------------------------------------------------
# 7. SELECT SPECIFIC COLUMNS
# ------------------------------------------------------------

# ':' means all rows.
# A list selects specific named columns.
print("\n17. Salary and Experience using loc:")
print(
    employees.loc[
        :,
        ["Salary", "Experience"],
    ]
)

# iloc can perform the same selection using positions.
# Department=0, Salary=1, Experience=2 after Name became index.
print("\n18. Salary and Experience using iloc:")
print(employees.iloc[:, [1, 2]])


# ------------------------------------------------------------
# 8. BOOLEAN FILTERING WITH LOC
# ------------------------------------------------------------

# Create one True/False value per employee.
high_salary = employees["Salary"] > 70000

print("\n19. Boolean mask:")
print(high_salary)

# Use the mask to select complete matching rows.
print("\n20. Employees with Salary > 70000:")
print(employees.loc[high_salary])

# Select matching rows but display only selected columns.
print("\n21. Department and Salary where Salary > 70000:")
print(
    employees.loc[
        employees["Salary"] > 70000,
        ["Department", "Salary"],
    ]
)


# ------------------------------------------------------------
# 9. MULTIPLE CONDITIONS
# ------------------------------------------------------------

# Each comparison must be inside parentheses.
# '&' performs element-wise AND.
mask = (employees["Department"] == "IT") & (employees["Experience"] > 5)

print("\n22. IT employees with Experience > 5:")
print(employees.loc[mask])


# ------------------------------------------------------------
# 10. UPDATE VALUES USING LOC
# ------------------------------------------------------------

# Update one exact cell using row and column labels.
employees.loc["Amit", "Salary"] = 90000

print("\n23. Updated Amit Salary:")
print(employees.loc["Amit", "Salary"])


# ------------------------------------------------------------
# 11. CONDITIONAL UPDATE
# ------------------------------------------------------------

# Increase salaries of all IT employees by 10%.
employees.loc[
    employees["Department"] == "IT",
    "Salary",
] *= 1.10

print("\n24. After IT salary increase:")
print(employees)


# ------------------------------------------------------------
# IMPORTANT REVISION
# ------------------------------------------------------------

# iloc -> integer positions
# employees.iloc[0]
# employees.iloc[0, 1]

# loc -> labels
# employees.loc["Amit"]
# employees.loc["Amit", "Salary"]

# iloc slice:
# employees.iloc[0:3]
# Stop position 3 is excluded.

# loc label slice:
# employees.loc["Amit":"Rahul"]
# Ending label Rahul is included.

# All rows:
# employees.loc[:, ["Salary", "Experience"]]

# Boolean filtering:
# employees.loc[employees["Salary"] > 70000]

# Filtering rows + selecting columns:
# employees.loc[
#     employees["Salary"] > 70000,
#     ["Department", "Salary"]
# ]

# Multiple conditions:
# (
#     (condition_1)
#     & (condition_2)
# )

# Updating a value:
# employees.loc["Karan", "Salary"] = 65000
