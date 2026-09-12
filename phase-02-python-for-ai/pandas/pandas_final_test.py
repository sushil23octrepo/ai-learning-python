import pandas as pd

# ============================================================
# PANDAS FINAL TEST
# Covers Modules 01-10
#
# Try to solve each question before checking your notes.
# Avoid hardcoding expected outputs where Pandas can calculate them.
# ============================================================


# ------------------------------------------------------------
# PART A — DATAFRAME BASICS AND SELECTION
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
        "Salary": [85000, 65000, 95000, 72000, 60000, 88000],
        "Experience": [5, 3, 8, 4, 2, 6],
    }
)

# 1. Print shape, size, ndim, and dtypes.
# 2. Select Salary as a Series.
# 3. Select Name and Salary as a DataFrame.
# 4. Using iloc, select rows 1 through 3 and columns Name through Salary.
# 5. Set Name as the index, then use loc to select Rahul's Salary.


# ------------------------------------------------------------
# PART B — FILTERING, SORTING, AND QUERYING
# ------------------------------------------------------------

# Start again with a fresh DataFrame if you changed the index above.

# 6. Select employees whose Salary is greater than 75000.
# 7. Select employees in IT with Experience >= 6.
# 8. Select employees from HR or Finance using isin().
# 9. Select salaries between 65000 and 90000 using between().
# 10. Sort Department ascending and Salary descending.
# 11. Show the two employees with the highest Salary.
# 12. Using query(), select Salary > 70000 and Experience >= 5.


# ------------------------------------------------------------
# PART C — MISSING DATA
# ------------------------------------------------------------

missing_data = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya"],
        "Department": ["IT", None, "IT", "Finance"],
        "Salary": [85000, None, 95000, 72000],
        "Experience": [5, 3, None, 4],
    }
)

# 13. Count missing values in every column.
# 14. Print rows containing at least one missing value.
# 15. Create a copy called cleaned_data.
# 16. Fill Department with "Unknown".
# 17. Fill Salary using mean Salary.
# 18. Fill Experience using median Experience.
# 19. Confirm whether any missing values remain.


# ------------------------------------------------------------
# PART D — GROUPBY AND AGGREGATION
# ------------------------------------------------------------

sales = pd.DataFrame(
    {
        "Employee": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sonal"],
        "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
        "Sales": [120000, 80000, 150000, 95000, 70000, 130000],
        "Deals": [12, 8, 15, 10, 7, 13],
    }
)

# 20. Calculate average Sales by Department.
# 21. Count employees per Department.
# 22. Create a named aggregation with:
#     AverageSales, HighestSales, TotalDeals
# 23. reset_index() so Department becomes a normal column.
# 24. Sort departments by AverageSales descending.


# ------------------------------------------------------------
# PART E — COLUMN TRANSFORMATIONS
# ------------------------------------------------------------

staff = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya"],
        "Department": ["IT", "HR", "IT", "Finance"],
        "Salary": [85000, 65000, 95000, 72000],
        "Experience": [5, 3, 8, 4],
    }
)

# 25. Create Bonus = 10% of Salary.
# 26. Create TotalCompensation = Salary + Bonus.
# 27. Create ExperienceLevel:
#     Experienced when Experience >= 5, otherwise Junior.
# 28. Create DepartmentFullName using map().
# 29. Rename Name to EmployeeName.
# 30. Insert EmployeeId values [101, 102, 103, 104] at column position 0.
# 31. Convert EmployeeId to string.
# 32. Create EmployeeNameUpper using .str.upper().


# ------------------------------------------------------------
# PART F — COMBINING DATAFRAMES
# ------------------------------------------------------------

employees = pd.DataFrame(
    {
        "EmployeeId": [101, 102, 103, 104],
        "Name": ["Amit", "Neha", "Rahul", "Priya"],
        "DepartmentId": [1, 2, 1, 3],
    }
)

departments = pd.DataFrame(
    {
        "DepartmentId": [1, 2, 3, 4],
        "DepartmentName": ["IT", "HR", "Finance", "Operations"],
    }
)

salaries = pd.DataFrame(
    {
        "EmployeeId": [101, 102, 103, 105],
        "Salary": [85000, 65000, 95000, 70000],
    }
)

# 33. Left join employees with departments.
# 34. Left join that result with salaries.
# 35. Keep only Name, DepartmentName, Salary.
# 36. Explain in a comment what would change if the second merge used outer.


# ------------------------------------------------------------
# PART G — DATE AND TIME
# ------------------------------------------------------------

orders = pd.DataFrame(
    {
        "OrderId": [1, 2, 3, 4],
        "OrderDate": [
            "2026-09-01",
            "2026-09-03",
            "invalid-date",
            "2026-09-08",
        ],
        "DeliveryDate": [
            "2026-09-03",
            "2026-09-06",
            "2026-09-09",
            "2026-09-12",
        ],
    }
)

# 37. Convert OrderDate using errors="coerce".
# 38. Convert DeliveryDate to datetime.
# 39. Count invalid OrderDate values.
# 40. Create OrderDayName.
# 41. Create DeliveryDays.
# 42. Using reference date 2026-09-12, create DaysSinceOrder.


# ------------------------------------------------------------
# PART H — READING / WRITING FILES
# ------------------------------------------------------------

# 43. Write code that reads:
#     ../docs/employees.csv
#     relative to this Python file using pathlib Path(__file__).
#
# 44. While reading, parse JoinDate as datetime.
# 45. Write code to save a cleaned DataFrame as:
#     ../docs/employees_cleaned.csv
#     without writing the Pandas index.


# ------------------------------------------------------------
# PART I — PRACTICAL CLEANING / ML FEATURE PREPARATION
# ------------------------------------------------------------

customers = pd.DataFrame(
    {
        "CustomerId": [101, 102, 102, 103, 104],
        "Name": [" amit ", "NEHA", "NEHA", "Rahul", " Priya"],
        "City": ["hyderabad", "HYDERABAD", "HYDERABAD", "Pune", None],
        "Income": ["75000", "45000", "45000", "95000", None],
        "Debt": [15000, 30000, 30000, 10000, 28000],
        "SignupDate": [
            "2025-01-10",
            "2025-04-15",
            "2025-04-15",
            "invalid",
            "2025-08-01",
        ],
    }
)

# 46. Remove duplicate CustomerId rows.
# 47. Clean Name with strip() and title().
# 48. Clean City with strip() and title(), then fill missing with "Unknown".
# 49. Convert Income using pd.to_numeric(..., errors="coerce").
# 50. Fill missing Income using median.
# 51. Convert SignupDate safely with errors="coerce".
# 52. Create DebtRatio = Debt / Income.
# 53. Create HighDebt as 1 when DebtRatio > 0.50, otherwise 0.
# 54. Create DaysSinceSignup using reference date 2026-09-12.
# 55. Create final_features containing:
#     Income, Debt, DebtRatio, HighDebt, DaysSinceSignup.
# 56. Create model_ready_features by removing rows with missing final features.


# ============================================================
# FINAL SELF-CHECK QUESTIONS
# ============================================================

# 57. loc vs iloc — what is the difference?
# 58. size() vs count() after groupby — what is the difference?
# 59. map() vs replace() — what important difference should you remember?
# 60. Why should missing values not automatically be replaced with zero?
# 61. Why can a raw date be converted into DaysSinceEvent for ML?
# 62. Why is a cleaned business DataFrame not always immediately model-ready?
