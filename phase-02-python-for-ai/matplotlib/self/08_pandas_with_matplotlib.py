import pandas as pd
import matplotlib.pyplot as plt

sales = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Revenue": [120000, 135000, 128000, 150000, 165000],
    }
)

plt.plot(
    sales["Month"],
    sales["Revenue"],
    marker="o",
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)
# plt.show()


employees = pd.DataFrame(
    {
        "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [85000, 65000, 95000, 72000, 60000],
    }
)
high_salary = employees[employees["Salary"] > 70000]

plt.plot(high_salary["Name"], high_salary["Salary"], marker="o")
plt.title("Employees with Salary Above 70000")
plt.xlabel("Employee")
plt.ylabel("Salary")
# plt.show()

orders = pd.DataFrame(
    {
        "OrderDate": [
            "2026-09-01",
            "2026-09-02",
            "2026-09-03",
            "2026-09-04",
        ],
        "Orders": [
            100,
            125,
            118,
            140,
        ],
    }
)

plt.title("Daily Orders")
plt.xlabel("Date")
plt.ylabel("Order Count")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
