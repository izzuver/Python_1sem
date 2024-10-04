import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 7, 8, 10])

b = ((np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x ** 2) - (np.mean(x)) ** 2))
a = np.mean(y) - b * np.mean(x)

print(b, a)