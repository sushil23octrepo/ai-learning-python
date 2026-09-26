import matplotlib.pyplot as plt
import pandas as pd

# ============================================================
# MODULE 01 — LINE CHART BASICS
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. BASIC LINE CHART
# ------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 140, 180, 210]

# plot(x_values, y_values)
# months -> X-axis
# sales  -> Y-axis
plt.plot(months, sales)

# show() displays the chart window.
plt.show()


# ------------------------------------------------------------
# 2. LINE CHART WITH MARKERS
# ------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 140, 180, 210]

# marker="o" places a circle at every data point.
plt.plot(
    months,
    sales,
    marker="o",
)

plt.show()


# ------------------------------------------------------------
# 3. TITLE AND AXIS LABELS
# ------------------------------------------------------------

plt.plot(
    months,
    sales,
    marker="o",
)

# title() sets the chart title.
plt.title("Monthly Sales")

# xlabel() and ylabel() describe the axes.
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# ------------------------------------------------------------
# 4. ADD GRID LINES
# ------------------------------------------------------------

plt.plot(
    months,
    sales,
    marker="o",
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# grid(True) displays grid lines.
plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 5. NUMERIC X-AXIS
# ------------------------------------------------------------

days = [1, 2, 3, 4, 5]
temperature = [30, 32, 31, 35, 36]

plt.plot(
    days,
    temperature,
    marker="o",
)

plt.title("Daily Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 6. LINE CHART USING A PANDAS DATAFRAME
# ------------------------------------------------------------

sales_data = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [120, 150, 140, 180, 210],
    }
)

# A Pandas Series can be passed directly to Matplotlib.
plt.plot(
    sales_data["Month"],
    sales_data["Sales"],
    marker="o",
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 7. PRACTICAL AI EXAMPLE — TRAINING LOSS
# ------------------------------------------------------------

epochs = [1, 2, 3, 4, 5]
loss = [0.90, 0.72, 0.55, 0.43, 0.35]

# Ordered progression such as epochs is well suited
# to a line chart.
plt.plot(
    epochs,
    loss,
    marker="o",
)

plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.grid(True)
plt.show()


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Import Matplotlib:
# import matplotlib.pyplot as plt

# Create a line:
# plt.plot(x_values, y_values)

# Add markers:
# plt.plot(x_values, y_values, marker="o")

# Add chart title:
# plt.title("Chart Title")

# IMPORTANT:
# plt.title(...) is a function call.
#
# Do NOT write:
# plt.title = "Chart Title"
#
# That would replace the title function with a string.

# X-axis label:
# plt.xlabel("X Label")

# Y-axis label:
# plt.ylabel("Y Label")

# Show grid:
# plt.grid(True)

# Display chart:
# plt.show()

# Basic flow:
#
# Prepare data
#     ↓
# plt.plot()
#     ↓
# title / labels / grid
#     ↓
# plt.show()
