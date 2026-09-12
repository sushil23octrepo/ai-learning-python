import pandas as pd

# ============================================================
# PANDAS EXERCISE 08 — DATE AND TIME HANDLING
# Reference solution.
# ============================================================

orders = pd.DataFrame(
    {
        "OrderId": [101, 102, 103, 104, 105],
        "Customer": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "OrderDate": [
            "2026-08-28",
            "2026-09-01",
            "2026-09-03",
            "invalid-date",
            "2026-09-08",
        ],
        "DeliveryDate": [
            "2026-08-30",
            "2026-09-04",
            "2026-09-05",
            "2026-09-09",
            "2026-09-12",
        ],
        "Amount": [1200, 1800, 900, 2200, 1500],
    }
)


# ------------------------------------------------------------
# 1. Convert OrderDate using errors="coerce".
# ------------------------------------------------------------

# Invalid dates become NaT instead of raising an error.
orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"],
    errors="coerce",
)


# ------------------------------------------------------------
# 2. Convert DeliveryDate to datetime.
# ------------------------------------------------------------

orders["DeliveryDate"] = pd.to_datetime(orders["DeliveryDate"])


# ------------------------------------------------------------
# 3. Count invalid/missing OrderDate values.
# ------------------------------------------------------------

invalid_order_dates = orders["OrderDate"].isna().sum()

print("\n3. Invalid OrderDate count:")
print(invalid_order_dates)


# ------------------------------------------------------------
# 4. Create OrderYear.
# ------------------------------------------------------------

orders["OrderYear"] = orders["OrderDate"].dt.year


# ------------------------------------------------------------
# 5. Create OrderMonth.
# ------------------------------------------------------------

orders["OrderMonth"] = orders["OrderDate"].dt.month


# ------------------------------------------------------------
# 6. Create OrderDayName.
# ------------------------------------------------------------

orders["OrderDayName"] = orders["OrderDate"].dt.day_name()


# ------------------------------------------------------------
# 7. Select orders placed on or after 2026-09-01.
# ------------------------------------------------------------

recent_orders = orders[orders["OrderDate"] >= "2026-09-01"]

print("\n7. Orders on or after 2026-09-01:")
print(recent_orders)


# ------------------------------------------------------------
# 8. Sort OrderDate newest to oldest.
# ------------------------------------------------------------

sorted_orders = orders.sort_values(
    "OrderDate",
    ascending=False,
)

print("\n8. Orders newest to oldest:")
print(sorted_orders)


# ------------------------------------------------------------
# 9. Create DeliveryDays.
# ------------------------------------------------------------

# Date subtraction produces a Timedelta.
# .dt.days extracts the number of whole days.
orders["DeliveryDays"] = (orders["DeliveryDate"] - orders["OrderDate"]).dt.days


# ------------------------------------------------------------
# 10. Create formatted DD-MM-YYYY date.
# ------------------------------------------------------------

orders["FormattedOrderDate"] = orders["OrderDate"].dt.strftime("%d-%m-%Y")

# NaT remains a missing value in the formatted result.


# ------------------------------------------------------------
# 11. Create DaysSinceOrder.
# ------------------------------------------------------------

reference_date = pd.Timestamp("2026-09-12")

orders["DaysSinceOrder"] = (reference_date - orders["OrderDate"]).dt.days


# ------------------------------------------------------------
# 12. Print final DataFrame.
# ------------------------------------------------------------

print("\n12. Final DataFrame:")
print(orders)


# ------------------------------------------------------------
# OPTIONAL CHECK
# ------------------------------------------------------------

print("\nFinal data types:")
print(orders.dtypes)
