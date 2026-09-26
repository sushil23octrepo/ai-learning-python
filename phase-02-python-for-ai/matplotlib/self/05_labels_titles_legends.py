import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 140, 180]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


product_a = [120, 150, 140, 180]
product_b = [100, 130, 160, 170]

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
