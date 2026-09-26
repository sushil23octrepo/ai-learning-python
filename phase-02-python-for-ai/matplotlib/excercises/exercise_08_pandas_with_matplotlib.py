import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# MATPLOTLIB EXERCISE 08
# PANDAS WITH MATPLOTLIB
# Reference solution.
# ============================================================

sales = pd.DataFrame(
    {
        "Product": [
            "Laptop",
            "Phone",
            "Tablet",
            "Laptop",
            "Phone",
            "Tablet",
        ],
        "Revenue": [
            120000,
            90000,
            60000,
            150000,
            110000,
            70000,
        ],
    }
)


# ------------------------------------------------------------
# 1. GROUP BY PRODUCT
# 2. CALCULATE TOTAL REVENUE
# 3. RESET INDEX
# ------------------------------------------------------------

product_revenue = sales.groupby("Product")["Revenue"].sum().reset_index()

print(product_revenue)


# ------------------------------------------------------------
# 4. SORT TOTAL REVENUE DESCENDING
# ------------------------------------------------------------

product_revenue = product_revenue.sort_values(
    "Revenue",
    ascending=False,
)

print(product_revenue)


# ------------------------------------------------------------
# 5. SET FIGURE SIZE
# ------------------------------------------------------------

plt.figure(
    figsize=(8, 5),
)


# ------------------------------------------------------------
# 6. CREATE BAR CHART
# ------------------------------------------------------------

bars = plt.bar(
    product_revenue["Product"],
    product_revenue["Revenue"],
)


# ------------------------------------------------------------
# 7. ADD TITLE
# ------------------------------------------------------------

plt.title("Total Revenue by Product")


# ------------------------------------------------------------
# 8. ADD AXIS LABELS
# ------------------------------------------------------------

plt.xlabel("Product")

plt.ylabel("Revenue")


# ------------------------------------------------------------
# 9. ADD VALUE LABELS TO BARS
# ------------------------------------------------------------

plt.bar_label(bars)


# ------------------------------------------------------------
# 10. ADD HORIZONTAL GRID
# ------------------------------------------------------------

plt.grid(axis="y")


# ------------------------------------------------------------
# 11. ADJUST LAYOUT
# ------------------------------------------------------------

plt.tight_layout()


# ------------------------------------------------------------
# 12. DISPLAY CHART
# ------------------------------------------------------------

plt.show()
