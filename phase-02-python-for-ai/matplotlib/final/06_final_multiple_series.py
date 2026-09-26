import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ============================================================
# MODULE 06 — MULTIPLE SERIES
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. TWO LINE SERIES
# ------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]

product_a = [120, 140, 150, 170, 190]
product_b = [100, 130, 145, 160, 180]

plt.plot(
    months,
    product_a,
    marker="o",
    label="Product A",
)

plt.plot(
    months,
    product_b,
    marker="o",
    label="Product B",
)

plt.legend()

plt.show()


# ------------------------------------------------------------
# 2. COMPLETE COMPARISON CHART
# ------------------------------------------------------------

plt.plot(
    months,
    product_a,
    marker="o",
    label="Product A",
)

plt.plot(
    months,
    product_b,
    marker="o",
    label="Product B",
)

plt.title("Product Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend()
plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 3. THREE SERIES
# ------------------------------------------------------------

product_c = [90, 120, 135, 155, 165]

plt.plot(
    months,
    product_a,
    marker="o",
    label="Product A",
)

plt.plot(
    months,
    product_b,
    marker="o",
    label="Product B",
)

plt.plot(
    months,
    product_c,
    marker="o",
    label="Product C",
)

plt.title("Product Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend()
plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 4. ACTUAL VS TARGET
# ------------------------------------------------------------

actual_sales = [
    120,
    145,
    155,
    170,
    185,
]

target_sales = [
    130,
    140,
    150,
    165,
    180,
]

plt.plot(
    months,
    actual_sales,
    marker="o",
    label="Actual",
)

plt.plot(
    months,
    target_sales,
    marker="o",
    label="Target",
)

plt.title("Actual vs Target Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 5. MULTIPLE SERIES USING PANDAS
# ------------------------------------------------------------

sales = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Online": [120, 145, 160, 175, 190],
        "Store": [150, 155, 158, 170, 180],
    }
)

plt.plot(
    sales["Month"],
    sales["Online"],
    marker="o",
    label="Online",
)

plt.plot(
    sales["Month"],
    sales["Store"],
    marker="o",
    label="Store",
)

plt.title("Online vs Store Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 6. PRACTICAL AI / ML EXAMPLE
# TRAINING LOSS VS VALIDATION LOSS
# ------------------------------------------------------------

epochs = [1, 2, 3, 4, 5]

training_loss = [
    0.90,
    0.70,
    0.52,
    0.40,
    0.30,
]

validation_loss = [
    0.95,
    0.76,
    0.60,
    0.55,
    0.58,
]

plt.figure(
    figsize=(8, 5),
)

plt.plot(
    epochs,
    training_loss,
    marker="o",
    label="Training Loss",
)

plt.plot(
    epochs,
    validation_loss,
    marker="o",
    label="Validation Loss",
)

plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 7. SIDE-BY-SIDE BAR SERIES
# ------------------------------------------------------------

departments = [
    "IT",
    "HR",
    "Finance",
]

salary_2025 = [
    80000,
    60000,
    70000,
]

salary_2026 = [
    90000,
    65000,
    75000,
]

# Create numeric positions for each category.
positions = np.arange(len(departments))

# Width of each bar.
width = 0.35

plt.bar(
    positions - width / 2,
    salary_2025,
    width=width,
    label="2025",
)

plt.bar(
    positions + width / 2,
    salary_2026,
    width=width,
    label="2026",
)

# Replace numeric positions with department names.
plt.xticks(
    positions,
    departments,
)

plt.title("Department Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.legend()
plt.grid(axis="y")

plt.tight_layout()
plt.show()


# ============================================================
# IMPORTANT REVISION
# ============================================================

# One series:
# plt.plot(x, y)

# Multiple series:
# plt.plot(x, y1, label="Series 1")
# plt.plot(x, y2, label="Series 2")
# plt.legend()

# Important:
#
# Call plt.plot() multiple times BEFORE plt.show()
# if you want the lines on the same chart.

# Good use cases:
#
# Actual vs Target
# Online vs Store
# Product A vs Product B
# Training vs Validation Loss
# Model comparisons over time


# ============================================================
# AI / ML CONNECTION
# ============================================================

# Training loss decreasing:
# often means the model is learning the training data.
#
# Validation loss increasing while training loss decreases:
# can be an indication of overfitting.
#
# We will study overfitting properly later
# during machine-learning lessons.
