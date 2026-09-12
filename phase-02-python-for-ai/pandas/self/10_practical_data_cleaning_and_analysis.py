import pandas as pd

customers = pd.DataFrame(
    {
        "CustomerId": [1, 2, 2, 3, 4, 5],
        "Name": [" Amit ", "Neha", "Neha", "RAHUL", "Priya", "Karan"],
        "City": ["Hyderabad", "hyderabad", "hyderabad", "Pune", None, "Mumbai"],
        "Income": ["72000", "40000", "40000", "91000", None, "60000"],
        "Debt": [15000, 32000, 32000, 9000, 27000, None],
        "SignupDate": [
            "2025-01-10",
            "2025-03-15",
            "2025-03-15",
            "invalid-date",
            "2025-06-20",
            "2025-08-01",
        ],
        "TemporaryColumn": ["x", "x", "x", "x", "x", "x"],
    }
)

print(customers)

# Inspect the data
print()
print(customers.head())
print(customers.dtypes)
print(customers.isna().sum())

# Remove duplicate rows
print()
customers = customers.drop_duplicates()
print(customers)

# If duplicates should be identified by only certain columns:
customers = customers.drop_duplicates(subset=["CustomerId"])

customers["Name"] = customers["Name"].str.strip().str.title()
print()
print(customers)

customers["Income"] = pd.to_numeric(customers["Income"], errors="coerce")
customers["SignupDate"] = pd.to_datetime(customers["SignupDate"], errors="coerce")
customers = customers.drop(columns=["TemporaryColumn"])
