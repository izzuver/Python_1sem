import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.array([1, 2, 3, 4, 5, 7, 9, 12, 34])
y = np.array([1, 4, 7, 8, 10, 14, 17, 25, 70])

fig = plt.figure(figsize = (16, 9))
ax1 = fig.add_subplot(111)
ax1.scatter(x, y, marker='x')


b = ((np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x ** 2) - (np.mean(x)) ** 2))
a = np.mean(y) - b * np.mean(x)

ax1.plot(x, b * x + a, 'r')
print(a, b)

ax1.grid()
plt.show()