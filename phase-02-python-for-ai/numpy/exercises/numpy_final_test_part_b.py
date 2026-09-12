# --------------------------------
# PART B — STUDENT ANALYTICS
# --------------------------------
import numpy as np

scores = np.array([[80, 70, 90], [60, 85, 75], [95, 90, 92], [50, 65, 70]])
print(scores.mean(axis=1))
print(scores.mean(axis=0))
print(scores[scores.mean(axis=1) > 80])
print(np.sum(np.all(scores >= 75, axis=1)))  # Count rows where every score >= 75
print(scores.max(axis=0))
