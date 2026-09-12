import numpy as np

scores = np.array([[80, 70, 90], [60, 85, 75], [95, 90, 92], [50, 65, 70]])
total_score = scores.sum(axis=1)
print(total_score)

print(scores.mean(axis=1))
print(scores.mean(axis=0))
print(scores.max())
print(scores[scores.mean(axis=1) > 80])
print(np.sum(scores.mean(axis=1) > 80))
