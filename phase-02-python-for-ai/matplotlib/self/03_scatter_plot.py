import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5, 6]
salary = [40000, 45000, 52000, 60000, 70000, 82000]


plt.scatter(experience, salary)

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
