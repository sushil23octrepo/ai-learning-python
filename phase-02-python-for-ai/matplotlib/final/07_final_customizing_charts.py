import matplotlib.pyplot as plt

# ============================================================
# MODULE 07 — CUSTOMIZING CHARTS
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. CHANGE LINE STYLE
# ------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 145, 138, 170, 190]

# linestyle controls the line appearance.
plt.plot(
    months,
    sales,
    linestyle="--",
)

plt.show()


# ------------------------------------------------------------
# 2. CHANGE MARKER STYLE
# ------------------------------------------------------------

plt.plot(
    months,
    sales,
    marker="s",
)

plt.show()


# ------------------------------------------------------------
# 3. CONTROL LINE WIDTH
# ------------------------------------------------------------

plt.plot(
    months,
    sales,
    linewidth=3,
)

plt.show()


# ------------------------------------------------------------
# 4. CONTROL MARKER SIZE
# ------------------------------------------------------------

plt.plot(
    months,
    sales,
    marker="o",
    markersize=8,
)

plt.show()


# ------------------------------------------------------------
# 5. CONTROL TRANSPARENCY
# ------------------------------------------------------------

# alpha:
# 0.0 -> fully transparent
# 1.0 -> fully visible
plt.plot(
    months,
    sales,
    marker="o",
    alpha=0.6,
)

plt.show()


# ------------------------------------------------------------
# 6. CONTROL AXIS LIMITS
# ------------------------------------------------------------

models = [
    "Model A",
    "Model B",
    "Model C",
]

accuracy = [
    0.82,
    0.88,
    0.91,
]

plt.bar(
    models,
    accuracy,
)

# Display Y-axis from 0 to 1.
plt.ylim(
    0,
    1,
)

plt.title("Model Accuracy")
plt.ylabel("Accuracy")

plt.show()


# ------------------------------------------------------------
# 7. BASIC ANNOTATION
# ------------------------------------------------------------

plt.plot(
    months,
    sales,
    marker="o",
)

# xy identifies the point being described.
plt.annotate(
    "Highest Sales",
    xy=("May", 190),
)

plt.title("Monthly Sales")

plt.show()


# ------------------------------------------------------------
# 8. ANNOTATION WITH ARROW
# ------------------------------------------------------------

plt.plot(
    months,
    sales,
    marker="o",
)

plt.annotate(
    "Highest Sales",
    # Point being highlighted.
    xy=("May", 190),
    # Position where annotation text is displayed.
    xytext=("Mar", 200),
    # Draw arrow from text to the point.
    arrowprops={
        "arrowstyle": "->",
    },
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 9. COMPLETE CUSTOMIZED LINE CHART
# ------------------------------------------------------------

plt.figure(
    figsize=(8, 5),
)

plt.plot(
    months,
    sales,
    # Circle at every point.
    marker="o",
    # Dashed line.
    linestyle="--",
    # Thickness of line.
    linewidth=2,
    # Size of markers.
    markersize=8,
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.annotate(
    "Highest Sales",
    xy=("May", 190),
    xytext=("Mar", 200),
    arrowprops={
        "arrowstyle": "->",
    },
)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 10. PRACTICAL AI / ML EXAMPLE
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
    # Slight transparency.
    alpha=0.8,
)

plt.title("Model Accuracy")
plt.xlabel("Model")
plt.ylabel("Accuracy")

# Accuracy is between 0 and 1.
plt.ylim(
    0,
    1,
)

# Show numeric value above each bar.
plt.bar_label(bars)

# Rotate long model names.
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

# Line styles:
#
# "-"   -> solid
# "--"  -> dashed
# ":"   -> dotted
# "-."  -> dash-dot


# Common marker styles:
#
# "o" -> circle
# "s" -> square
# "^" -> triangle
# "x" -> x marker
# "*" -> star


# Change line thickness:
# linewidth=2


# Change marker size:
# markersize=8


# Control transparency:
# alpha=0.8


# Control X-axis range:
# plt.xlim(minimum, maximum)


# Control Y-axis range:
# plt.ylim(minimum, maximum)


# Add annotation:
#
# plt.annotate(
#     "Text",
#     xy=(x, y),
# )


# Add annotation with arrow:
#
# plt.annotate(
#     "Text",
#     xy=(x, y),
#     xytext=(text_x, text_y),
#     arrowprops={
#         "arrowstyle": "->"
#     },
# )


# ============================================================
# IMPORTANT IDEA
# ============================================================

# Chart customization changes how the data is presented.
#
# It does NOT change the underlying data.

# Use customization to improve:
#
# readability
# comparison
# emphasis
# presentation
#
# But avoid misleading viewers with inappropriate axis limits.
