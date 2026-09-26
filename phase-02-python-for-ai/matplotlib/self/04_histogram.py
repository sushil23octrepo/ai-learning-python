import matplotlib.pyplot as plt

ages = [
    22,
    25,
    27,
    29,
    31,
    33,
    35,
    36,
    38,
    40,
    42,
    45,
    47,
    50,
    52,
]

plt.hist(ages, bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis="y")

plt.show()
