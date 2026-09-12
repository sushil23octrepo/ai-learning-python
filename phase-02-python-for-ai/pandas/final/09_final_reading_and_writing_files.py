from pathlib import Path
import pandas as pd

# ============================================================
# MODULE 09 — READING AND WRITING FILES
# Complete reference implementation for later revision.
# ============================================================

# ------------------------------------------------------------
# 1. BUILD A SAFE FILE PATH
# ------------------------------------------------------------

# This Python file is inside:
# pandas/self/
#
# employees.csv is inside:
# pandas/docs/

current_folder = Path(__file__).parent

csv_file = current_folder.parent / "docs" / "employees.csv"

print("\nCSV file path:")
print(csv_file)


# ------------------------------------------------------------
# 2. READ A CSV FILE
# ------------------------------------------------------------

employees = pd.read_csv(csv_file)

print("\n1. Complete CSV data:")
print(employees)


# ------------------------------------------------------------
# 3. INSPECT DATA AFTER LOADING
# ------------------------------------------------------------

print("\n2. First rows:")
print(employees.head())

print("\n3. Shape:")
print(employees.shape)

print("\n4. Data types:")
print(employees.dtypes)

print("\n5. DataFrame information:")
employees.info()


# ------------------------------------------------------------
# 4. READ ONLY SELECTED COLUMNS
# ------------------------------------------------------------

selected_columns = pd.read_csv(
    csv_file,
    usecols=[
        "Name",
        "Department",
        "Salary",
    ],
)

print("\n6. Selected columns:")
print(selected_columns)


# ------------------------------------------------------------
# 5. READ ONLY LIMITED ROWS
# ------------------------------------------------------------

first_three = pd.read_csv(
    csv_file,
    nrows=3,
)

print("\n7. First three rows:")
print(first_three)


# ------------------------------------------------------------
# 6. HANDLE CUSTOM MISSING VALUES
# ------------------------------------------------------------

# Additional text values can be treated as missing.
employees_with_missing_rules = pd.read_csv(
    csv_file,
    na_values=[
        "NA",
        "N/A",
        "Unknown",
        "-",
    ],
)

print("\n8. Data with custom missing-value rules:")
print(employees_with_missing_rules)


# ------------------------------------------------------------
# 7. PARSE DATE COLUMNS WHILE READING
# ------------------------------------------------------------

# parse_dates converts JoinDate to datetime during loading.
employees = pd.read_csv(
    csv_file,
    parse_dates=["JoinDate"],
)

print("\n9. Data types after parse_dates:")
print(employees.dtypes)


# ------------------------------------------------------------
# 8. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n10. Missing values per column:")
print(employees.isna().sum())


# ------------------------------------------------------------
# 9. FILL MISSING SALARY
# ------------------------------------------------------------

average_salary = employees["Salary"].mean()

employees["Salary"] = employees["Salary"].fillna(average_salary)

print("\n11. After filling missing Salary:")
print(employees)


# ------------------------------------------------------------
# 10. CREATE A NEW COLUMN
# ------------------------------------------------------------

employees["SalaryAfterBonus"] = employees["Salary"] * 1.10

print("\n12. Salary after 10% bonus:")
print(employees)


# ------------------------------------------------------------
# 11. SAVE TO CSV
# ------------------------------------------------------------

cleaned_csv_file = current_folder.parent / "docs" / "employees_cleaned.csv"

# index=False prevents the Pandas row index
# from being written as an extra CSV column.
employees.to_csv(
    cleaned_csv_file,
    index=False,
)

print("\n13. Cleaned CSV created:")
print(cleaned_csv_file)


# ------------------------------------------------------------
# 12. READ THE SAVED CSV AGAIN
# ------------------------------------------------------------

verified_data = pd.read_csv(
    cleaned_csv_file,
    parse_dates=["JoinDate"],
)

print("\n14. Verified cleaned CSV:")
print(verified_data)


# ------------------------------------------------------------
# 13. WRITE TO EXCEL
# ------------------------------------------------------------

cleaned_excel_file = current_folder.parent / "docs" / "employees_cleaned.xlsx"

employees.to_excel(
    cleaned_excel_file,
    index=False,
)

print("\n15. Cleaned Excel file created:")
print(cleaned_excel_file)


# ------------------------------------------------------------
# 14. READ FROM EXCEL
# ------------------------------------------------------------

# openpyxl may be required:
# pip install openpyxl

excel_data = pd.read_excel(cleaned_excel_file)

print("\n16. Data read from Excel:")
print(excel_data)


# ------------------------------------------------------------
# 15. WRITE MULTIPLE EXCEL SHEETS
# ------------------------------------------------------------

department_summary = (
    employees.groupby("Department")
    .agg(
        AverageSalary=("Salary", "mean"),
        EmployeeCount=("Name", "count"),
    )
    .reset_index()
)

report_file = current_folder.parent / "docs" / "employee_report.xlsx"

with pd.ExcelWriter(report_file) as writer:
    employees.to_excel(
        writer,
        sheet_name="Employees",
        index=False,
    )

    department_summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False,
    )

print("\n17. Multi-sheet Excel report created:")
print(report_file)


# ------------------------------------------------------------
# 16. PRACTICAL AI / ML DATA PIPELINE
# ------------------------------------------------------------

# Typical workflow:
#
# Load
# -> inspect
# -> clean
# -> transform
# -> save
# -> use for model training

model_data = pd.read_csv(
    csv_file,
    parse_dates=["JoinDate"],
)

# Remove records if required model fields are missing.
model_data = model_data.dropna(subset=["Name", "Department"])

# Fill missing numerical values.
model_data["Salary"] = model_data["Salary"].fillna(model_data["Salary"].mean())

# Create a simple numerical feature.
model_data["SalaryAfterBonus"] = model_data["Salary"] * 1.10

print("\n18. Model-ready example:")
print(model_data)


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Read CSV:
# pd.read_csv("file.csv")

# Read selected columns:
# pd.read_csv(
#     "file.csv",
#     usecols=["Name", "Salary"]
# )

# Limit rows:
# pd.read_csv(
#     "file.csv",
#     nrows=100
# )

# Treat custom values as missing:
# pd.read_csv(
#     "file.csv",
#     na_values=["NA", "Unknown"]
# )

# Parse dates while reading:
# pd.read_csv(
#     "file.csv",
#     parse_dates=["JoinDate"]
# )

# Save CSV:
# df.to_csv(
#     "output.csv",
#     index=False
# )

# Read Excel:
# pd.read_excel("file.xlsx")

# Read a specific sheet:
# pd.read_excel(
#     "file.xlsx",
#     sheet_name="Employees"
# )

# Save Excel:
# df.to_excel(
#     "output.xlsx",
#     index=False
# )

# Multiple Excel sheets:
# with pd.ExcelWriter("report.xlsx") as writer:
#     df1.to_excel(writer, sheet_name="Data", index=False)
#     df2.to_excel(writer, sheet_name="Summary", index=False)
