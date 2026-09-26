import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Sales"]
employees = [25, 12, 10, 18]

plt.bar(departments, employees)
# plt.show()

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.grid(axis="y")
plt.show()


products = [
    "Laptop",
    "Phone",
    "Tablet",
    "Monitor",
]

revenue = [
    450000,
    380000,
    210000,
    170000,
]

bars = plt.bar(
    products,
    revenue,
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.bar_label(bars)

plt.show()
