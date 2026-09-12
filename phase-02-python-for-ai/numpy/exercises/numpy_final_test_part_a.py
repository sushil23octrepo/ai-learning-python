import numpy as np

data = np.arange(1, 25).reshape(2, 3, 4)
print(data)
print(data.ndim, data.shape, data.size)
print(data[1, 1, 1])
print(data[:, 1])

print(data[0, :, -2:])

print(data.reshape(4, 6))
