from pathlib import Path

import pandas as pd

current_folder = Path(__file__).parent
csv_file = current_folder.parent / "docs" / "employees.csv"
print(csv_file)


employees = pd.read_csv(csv_file)
print(employees)

# inspecting
print()
print(employees.head())
print(employees.shape)
print(employees.dtypes)
employees.info()

# Read only selected columns
print()
employees = pd.read_csv(csv_file, usecols=["Name", "Department", "Salary"])
print(employees)


# Read only a limited number of rows
print()
employees = pd.read_csv(csv_file, nrows=2)
print(employees)

# Handle missing values while reading,You can tell Pandas to treat them as missing:
print()
employees = pd.read_csv(csv_file, na_values=["NA", "N/A", "Unknown", "-"])
print(employees)


# Convert dates while reading
print()
employees = pd.read_csv(csv_file, parse_dates=["JoinDate"])
print(employees)

employees.to_csv("cleaned_employees.csv", index=False)
