import pandas as pd

scores = pd.Series([80, 70, 90, 85])
print(scores)

scores = pd.Series([80, 70, 90], index=["Ram", "Shyam", "Mohan"])
print(scores)

customers = pd.DataFrame(
    {
        "Customer": ["Amit", "Neha", "Rahul", "Priya"],
        "Income": [72000, 40000, 91000, 60000],
        "CreditScore": [750, 650, 820, 700],
        "Debt": [15000, 32000, 9000, 27000],
    }
)

print(customers)
print(customers.shape)
print(customers.size)
print(customers.ndim)
print(customers.columns)
print(customers.index)
print(customers.dtypes)
print(customers.head(2))  # First two rows
print(customers.tail(2))  # Last two rows
customers.info()
print(customers.describe())
print(customers["Income"])
print(customers[["Customer", "Income"]])

print(customers["Income"])  # Series
print(customers[["Income"]])  # DataFrame
customers[["Income", "Debt"]]  # DataFrame with two columns

print(customers["Income"].mean())
print(customers["CreditScore"].max())  # Highest credit score
print(customers["Debt"].sum())  # Total debt
