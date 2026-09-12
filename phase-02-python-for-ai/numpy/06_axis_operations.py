import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.sum())
print(matrix.sum(axis=0))  # Sum down the rows, result per column
print(matrix.sum(axis=1))  # Sum across columns, result per row

scores = np.array([[80, 70, 90], [60, 85, 75], [95, 90, 92]])
print(scores.mean(axis=1))  # Average across columns for each row
print(scores.mean(axis=0))  # Average down rows for each column
print(scores.max(axis=1))  # Max value in each row
print(scores.max(axis=0))  # Max value in each column
