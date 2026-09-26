import matplotlib.pyplot as plt

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
]

revenue = [
    120000,
    135000,
    128000,
    150000,
    165000,
    180000,
]

plt.plot(months, revenue)
plt.plot(months, revenue, marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
