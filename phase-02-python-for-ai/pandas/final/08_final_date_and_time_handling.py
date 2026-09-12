import pandas as pd

# ============================================================
# MODULE 08 — DATE AND TIME HANDLING
# Complete reference implementation for later revision.
# ============================================================

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

print("\nOriginal DataFrame:")
print(orders)

print("\nOriginal data types:")
print(orders.dtypes)


# ------------------------------------------------------------
# 1. CONVERT TEXT TO DATETIME
# ------------------------------------------------------------

# pd.to_datetime() converts text/object values into
# Pandas datetime values.
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

print("\n1. After datetime conversion:")
print(orders.dtypes)


# ------------------------------------------------------------
# 2. EXTRACT DATE PARTS
# ------------------------------------------------------------

# .dt gives access to datetime-specific operations.
orders["Year"] = orders["OrderDate"].dt.year
orders["Month"] = orders["OrderDate"].dt.month
orders["Day"] = orders["OrderDate"].dt.day

print("\n2. Year, Month, and Day:")
print(orders)


# ------------------------------------------------------------
# 3. DAY NAME
# ------------------------------------------------------------

orders["DayName"] = orders["OrderDate"].dt.day_name()

print("\n3. Day names:")
print(orders[["OrderDate", "DayName"]])


# ------------------------------------------------------------
# 4. MONTH NAME
# ------------------------------------------------------------

orders["MonthName"] = orders["OrderDate"].dt.month_name()

print("\n4. Month names:")
print(orders[["OrderDate", "MonthName"]])


# ------------------------------------------------------------
# 5. FILTER BY DATE
# ------------------------------------------------------------

# Compare datetime values against a date threshold.
filtered_orders = orders[orders["OrderDate"] > "2026-09-03"]

print("\n5. Orders after 2026-09-03:")
print(filtered_orders)


# ------------------------------------------------------------
# 6. USE pd.Timestamp()
# ------------------------------------------------------------

# Timestamp represents a single Pandas datetime value.
cutoff_date = pd.Timestamp("2026-09-03")

filtered_orders = orders[orders["OrderDate"] > cutoff_date]

print("\n6. Filter using Timestamp:")
print(filtered_orders)


# ------------------------------------------------------------
# 7. FILTER BETWEEN TWO DATES
# ------------------------------------------------------------

# between() includes both boundaries by default.
date_range_orders = orders[
    orders["OrderDate"].between(
        "2026-09-02",
        "2026-09-06",
    )
]

print("\n7. Orders between two dates:")
print(date_range_orders)


# ------------------------------------------------------------
# 8. SORT BY DATE
# ------------------------------------------------------------

# descending order gives newest dates first.
sorted_orders = orders.sort_values(
    "OrderDate",
    ascending=False,
)

print("\n8. Orders sorted newest to oldest:")
print(sorted_orders)


# ------------------------------------------------------------
# 9. ADD DELIVERY DATE
# ------------------------------------------------------------

orders["DeliveryDate"] = pd.to_datetime(
    [
        "2026-09-03",
        "2026-09-05",
        "2026-09-08",
        "2026-09-10",
    ]
)

print("\n9. With DeliveryDate:")
print(orders)


# ------------------------------------------------------------
# 10. CALCULATE DATE DIFFERENCE
# ------------------------------------------------------------

# Subtracting two datetime columns returns a Timedelta.
orders["DeliveryTime"] = orders["DeliveryDate"] - orders["OrderDate"]

print("\n10. Delivery time:")
print(orders[["OrderDate", "DeliveryDate", "DeliveryTime"]])


# ------------------------------------------------------------
# 11. EXTRACT NUMBER OF DAYS FROM TIMEDELTA
# ------------------------------------------------------------

# .dt.days converts the Timedelta into integer days.
orders["DeliveryDays"] = orders["DeliveryTime"].dt.days

print("\n11. Delivery days:")
print(orders[["OrderDate", "DeliveryDate", "DeliveryDays"]])


# ------------------------------------------------------------
# 12. CURRENT DATE/TIME
# ------------------------------------------------------------

# Returns the current local timestamp.
current_time = pd.Timestamp.now()

print("\n12. Current timestamp:")
print(current_time)


# ------------------------------------------------------------
# 13. INVALID DATE HANDLING
# ------------------------------------------------------------

invalid_data = pd.DataFrame(
    {
        "Date": [
            "2026-09-01",
            "invalid-date",
            "2026-09-05",
        ]
    }
)

# errors="coerce" converts invalid dates into NaT.
invalid_data["Date"] = pd.to_datetime(
    invalid_data["Date"],
    errors="coerce",
)

print("\n13. Invalid date converted to NaT:")
print(invalid_data)

# NaT behaves like a missing datetime value.
print("\nMissing dates:")
print(invalid_data["Date"].isna())


# ------------------------------------------------------------
# 14. DATE FORMATTING
# ------------------------------------------------------------

# strftime() converts datetime values into formatted strings.
orders["FormattedDate"] = orders["OrderDate"].dt.strftime("%d-%m-%Y")

print("\n14. Formatted dates:")
print(orders[["OrderDate", "FormattedDate"]])


# ------------------------------------------------------------
# 15. DATETIME WITH TIME
# ------------------------------------------------------------

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

# Extract hour from timestamp.
logs["Hour"] = logs["Timestamp"].dt.hour

print("\n15. Log timestamps:")
print(logs)


# ------------------------------------------------------------
# 16. PRACTICAL AI / FEATURE ENGINEERING EXAMPLE
# ------------------------------------------------------------

transactions = pd.DataFrame(
    {
        "CustomerId": [1, 2, 3],
        "LastPurchaseDate": [
            "2026-08-20",
            "2026-09-01",
            "2026-07-15",
        ],
    }
)

transactions["LastPurchaseDate"] = pd.to_datetime(transactions["LastPurchaseDate"])

# Use a fixed date so the example is reproducible.
reference_date = pd.Timestamp("2026-09-12")

# Convert raw date information into a numeric ML feature.
transactions["DaysSinceLastPurchase"] = (
    reference_date - transactions["LastPurchaseDate"]
).dt.days

print("\n16. Feature engineering from dates:")
print(transactions)


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Convert to datetime:
# pd.to_datetime(df["Date"])

# Invalid values -> NaT:
# pd.to_datetime(
#     df["Date"],
#     errors="coerce"
# )

# Extract date components:
# df["Date"].dt.year
# df["Date"].dt.month
# df["Date"].dt.day
# df["Date"].dt.day_name()
# df["Date"].dt.month_name()

# Filter by date:
# df[df["Date"] >= "2026-09-01"]

# Filter a date range:
# df[df["Date"].between(start_date, end_date)]

# Sort dates:
# df.sort_values("Date", ascending=False)

# Date difference:
# df["EndDate"] - df["StartDate"]

# Convert Timedelta to integer days:
# (df["EndDate"] - df["StartDate"]).dt.days

# Format date for display:
# df["Date"].dt.strftime("%d-%m-%Y")

# Timestamp with time:
# df["Timestamp"].dt.hour

# AI feature engineering:
# DaysSinceEvent = reference_date - event_date
