import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 145, 138, 170, 190]

plt.plot(
    months,
    sales,
    linestyle="--",
    marker="o",
    linewidth=3,
    markersize=8,
    alpha=0.6,
)

plt.show()


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

plt.ylim(
    0,
    1,
)

plt.show()


months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 145, 138, 170, 190]

plt.plot(
    months,
    sales,
    marker="o",
)

# plt.annotate(
#     "Highest Sales",
#     xy=("May", 190),
# )

plt.annotate(
    "Highest Sales",
    xy=("May", 190),
    xytext=("Mar", 200),
    arrowprops={"arrowstyle": "->"},
)

plt.show()


import matplotlib.pyplot as plt

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
]

sales = [
    120,
    145,
    138,
    170,
    190,
]

plt.figure(
    figsize=(8, 5),
)

plt.plot(
    months,
    sales,
    marker="o",
    linestyle="--",
    linewidth=2,
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
    arrowprops={"arrowstyle": "->"},
)

plt.tight_layout()
plt.show()
