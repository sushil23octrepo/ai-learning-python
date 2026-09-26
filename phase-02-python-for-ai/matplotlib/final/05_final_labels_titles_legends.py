import matplotlib.pyplot as plt

# ============================================================
# MODULE 05 — TITLES, LABELS, LEGENDS, AND PRESENTATION
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. BASIC TITLE AND AXIS LABELS
# ------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 140, 180]

plt.plot(
    months,
    sales,
    marker="o",
)

# Describe what the chart shows.
plt.title("Monthly Sales")

# Describe the X-axis.
plt.xlabel("Month")

# Describe the Y-axis.
plt.ylabel("Sales")

plt.show()


# ------------------------------------------------------------
# 2. MULTIPLE LINES WITH LABELS
# ------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr"]

product_a = [120, 150, 140, 180]
product_b = [100, 130, 160, 170]

# label= gives each plotted series a name.
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

# legend() displays the labels.
plt.legend()

plt.show()


# ------------------------------------------------------------
# 3. COMPLETE COMPARISON CHART
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

plt.title("Monthly Product Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend()

plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 4. LEGEND POSITION
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

# loc controls the legend position.
plt.legend(
    loc="upper left",
)

plt.title("Monthly Product Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.show()


# ------------------------------------------------------------
# 5. ROTATE X-AXIS LABELS
# ------------------------------------------------------------

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "Gradient Boosting",
]

accuracy = [
    0.82,
    0.79,
    0.88,
    0.90,
]

plt.bar(
    models,
    accuracy,
)

plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")

# Rotate long category names so they do not overlap.
plt.xticks(
    rotation=45,
)

plt.show()


# ------------------------------------------------------------
# 6. CONTROL FIGURE SIZE
# ------------------------------------------------------------

# figsize=(width, height), measured in inches.
plt.figure(
    figsize=(8, 5),
)

plt.bar(
    models,
    accuracy,
)

plt.title("Model Accuracy Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy")

plt.xticks(
    rotation=45,
)

plt.show()


# ------------------------------------------------------------
# 7. TIGHT LAYOUT
# ------------------------------------------------------------

plt.figure(
    figsize=(8, 5),
)

plt.bar(
    models,
    accuracy,
)

plt.title("Model Accuracy Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy")

plt.xticks(
    rotation=45,
)

# Automatically adjusts spacing so labels are not cut off.
plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 8. BAR LABELS WITH PRESENTATION SETTINGS
# ------------------------------------------------------------

plt.figure(
    figsize=(8, 5),
)

bars = plt.bar(
    models,
    accuracy,
)

plt.title("Model Accuracy Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy")

# Display value above every bar.
plt.bar_label(bars)

plt.xticks(
    rotation=45,
)

plt.grid(
    axis="y",
)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 9. PRACTICAL AI / ML EXAMPLE
# ------------------------------------------------------------

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
]

accuracy = [
    0.82,
    0.79,
    0.88,
]

plt.figure(
    figsize=(8, 5),
)

bars = plt.bar(
    models,
    accuracy,
)

plt.title("Model Accuracy Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy")

plt.bar_label(bars)

plt.xticks(
    rotation=30,
)

plt.grid(
    axis="y",
)

plt.tight_layout()

plt.show()


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Chart title:
# plt.title("Chart Title")

# X-axis label:
# plt.xlabel("X Label")

# Y-axis label:
# plt.ylabel("Y Label")

# Name a plotted series:
# plt.plot(x, y, label="Series Name")

# Display labels:
# plt.legend()

# Set legend position:
# plt.legend(loc="upper left")

# Control figure size:
# plt.figure(figsize=(8, 5))

# Rotate X-axis labels:
# plt.xticks(rotation=45)

# Prevent chart content from being cut off:
# plt.tight_layout()

# Add values above bars:
# bars = plt.bar(x, y)
# plt.bar_label(bars)


# ============================================================
# IMPORTANT IDEA
# ============================================================

# A chart should clearly answer:
#
# What am I looking at?
# -> title
#
# What does the X-axis represent?
# -> xlabel
#
# What does the Y-axis represent?
# -> ylabel
#
# What does each line or series represent?
# -> label + legend
#
# Are long labels readable?
# -> xticks(rotation=...)
#
# Is the layout properly spaced?
# -> tight_layout()
