import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 140, 180, 210]

plt.plot(months, sales)
plt.show()

# Add markers and title
# marker="o" places a circle on every data point.
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")

# Add X and Y axis labels
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
