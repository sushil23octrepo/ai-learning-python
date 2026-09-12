import pandas as pd

orders = pd.DataFrame(
    {
        "OrderId": [101, 102, 103, 104],
        "Customer": ["Amit", "Neha", "Rahul", "Priya"],
        "OrderDate": [
            "2026-09-01",
            "2026-09-03",
            "2026-09-05",
            "2026-09-07",
        ],
        "Amount": [1200, 1800, 900, 2200],
    }
)

print(orders)
# At this point, OrderDate is still usually treated as text/object data.
print(orders.dtypes)

# Convert text to datetime
print()
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
print(orders)
print(orders.dtypes)

# Extract year, month, and day
orders["Year"] = orders["OrderDate"].dt.year
orders["Month"] = orders["OrderDate"].dt.month
orders["Day"] = orders["OrderDate"].dt.day
orders["DayName"] = orders["OrderDate"].dt.day_name()
orders["MonthName"] = orders["OrderDate"].dt.month_name()
print(orders)

# Filtering
print()
filtered = orders[orders["OrderDate"] > "2026-09-03"]
print(filtered)

# Filter between two dates
filtered = orders[
    orders["OrderDate"].between(
        "2026-09-02",
        "2026-09-06",
    )
]
print(filtered)

# Sort by date
print(
    orders.sort_values(
        "OrderDate",
        ascending=False,
    )
)

# Calculate date differences
print()
orders["DeliveryDate"] = pd.to_datetime(
    [
        "2026-09-03",
        "2026-09-05",
        "2026-09-08",
        "2026-09-10",
    ]
)
# substract
orders["DeliveryTime"] = orders["DeliveryDate"] - orders["OrderDate"]

print(orders)

# Get number of days
print()
orders["DeliveryDays"] = orders["DeliveryTime"].dt.days

print(orders)

print(pd.Timestamp.now())  # Current date/time


# Invalid date handling
print()
data = pd.DataFrame(
    {
        "Date": [
            "2026-09-01",
            "invalid-date",
            "2026-09-05",
        ]
    }
)

data["Date"] = pd.to_datetime(
    data["Date"],
    errors="coerce",
)
print(data)


# Date formatting
print()
orders["FormattedDate"] = orders["OrderDate"].dt.strftime("%d-%m-%Y")

print(orders)

# Datetime with time
print()
logs = pd.DataFrame(
    {
        "Timestamp": [
            "2026-09-01 09:30:00",
            "2026-09-01 12:45:00",
            "2026-09-02 16:20:00",
        ]
    }
)

logs["Timestamp"] = pd.to_datetime(logs["Timestamp"])

logs["Hour"] = logs["Timestamp"].dt.hour

print(logs)
