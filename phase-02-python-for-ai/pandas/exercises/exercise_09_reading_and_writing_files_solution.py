from pathlib import Path
import pandas as pd

# ============================================================
# PANDAS EXERCISE 09 — READING AND WRITING FILES
# Reference solution.
# ============================================================

# Python file:
# pandas/self/exercise_09_reading_and_writing_files.py
#
# CSV file:
# pandas/docs/employees.csv

current_folder = Path(__file__).parent

# If your exercise file is inside pandas/self/,
# move one level up to pandas/, then enter docs/.
csv_file = current_folder.parent / "docs" / "employees.csv"


# ------------------------------------------------------------
# 1. Load employees.csv.
# ------------------------------------------------------------

employees = pd.read_csv(csv_file)

print("\n1. Employees:")
print(employees)


# ------------------------------------------------------------
# 2. Print first three rows.
# ------------------------------------------------------------

print("\n2. First three rows:")
print(employees.head(3))


# ------------------------------------------------------------
# 3. Print shape and data types.
# ------------------------------------------------------------

print("\n3. Shape:")
print(employees.shape)

print("\nData types:")
print(employees.dtypes)


# ------------------------------------------------------------
# 4. Load again and parse JoinDate as datetime.
# ------------------------------------------------------------

employees = pd.read_csv(
    csv_file,
    parse_dates=["JoinDate"],
)

print("\n4. After parsing JoinDate:")
print(employees.dtypes)


# ------------------------------------------------------------
# 5. Count missing values.
# ------------------------------------------------------------

print("\n5. Missing values:")
print(employees.isna().sum())


# ------------------------------------------------------------
# 6. Fill missing Salary using average Salary.
# ------------------------------------------------------------

average_salary = employees["Salary"].mean()

employees["Salary"] = employees["Salary"].fillna(average_salary)

print("\n6. After filling Salary:")
print(employees)


# ------------------------------------------------------------
# 7. Create SalaryAfterBonus with 10% bonus.
# ------------------------------------------------------------

employees["SalaryAfterBonus"] = employees["Salary"] * 1.10

print("\n7. SalaryAfterBonus:")
print(employees)


# ------------------------------------------------------------
# 8. Save cleaned CSV.
# ------------------------------------------------------------

cleaned_csv_file = current_folder.parent / "docs" / "employees_cleaned.csv"

employees.to_csv(
    cleaned_csv_file,
    index=False,
)

print("\n8. Cleaned CSV saved:")
print(cleaned_csv_file)


# ------------------------------------------------------------
# 9. Save cleaned data as Excel.
# ------------------------------------------------------------

cleaned_excel_file = current_folder.parent / "docs" / "employees_cleaned.xlsx"

employees.to_excel(
    cleaned_excel_file,
    index=False,
)

print("\n9. Cleaned Excel saved:")
print(cleaned_excel_file)


# ------------------------------------------------------------
# 10. Read cleaned CSV again to verify.
# ------------------------------------------------------------

verified_employees = pd.read_csv(
    cleaned_csv_file,
    parse_dates=["JoinDate"],
)

print("\n10. Verified cleaned data:")
print(verified_employees)
