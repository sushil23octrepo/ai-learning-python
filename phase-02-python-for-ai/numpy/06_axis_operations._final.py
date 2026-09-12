import numpy as np

# --------------------------------
# BASIC MATRIX
# --------------------------------

matrix = np.array([[1, 2, 3], [4, 5, 6]])


# No axis = sum every value
total = matrix.sum()

print("Total:")
print(total)


# axis=0 collapses rows
# Result = one sum for each column
column_sums = matrix.sum(axis=0)

print("\nColumn sums:")
print(column_sums)


# axis=1 collapses columns
# Result = one sum for each row
row_sums = matrix.sum(axis=1)

print("\nRow sums:")
print(row_sums)


# --------------------------------
# STUDENT SCORE EXAMPLE
# --------------------------------

# Rows = students
# Columns = subjects
scores = np.array([[80, 70, 90], [60, 85, 75], [95, 90, 92]])


# axis=1 -> average across subjects for each student
student_averages = scores.mean(axis=1)

print("\nAverage for each student:")
print(student_averages)


# axis=0 -> average down students for each subject
subject_averages = scores.mean(axis=0)

print("\nAverage for each subject:")
print(subject_averages)


# axis=1 -> maximum value in each student's row
student_highest = scores.max(axis=1)

print("\nHighest score for each student:")
print(student_highest)


# axis=0 -> maximum value in each subject column
subject_highest = scores.max(axis=0)

print("\nHighest score for each subject:")
print(subject_highest)


# --------------------------------
# ML DATASET EXAMPLE
# --------------------------------

# Rows = customers/samples
# Columns = Income, Credit Score, Debt
customers = np.array(
    [[0.72, 0.85, 0.25], [0.40, 0.55, 0.80], [0.91, 0.90, 0.10], [0.60, 0.70, 0.45]]
)


# Average of each feature/column
feature_means = customers.mean(axis=0)

print("\nFeature averages:")
print(feature_means)


# Average across features for each customer/row
customer_means = customers.mean(axis=1)

print("\nCustomer averages:")
print(customer_means)
