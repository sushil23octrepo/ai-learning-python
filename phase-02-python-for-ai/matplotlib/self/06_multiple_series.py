import matplotlib.pyplot as plt
import pandas as pd

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

plt.title("Product Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend()
plt.grid(True)

plt.show()

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
