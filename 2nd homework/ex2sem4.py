import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

values1 = np.random.normal(0, 10, 100)
values2 = np.random.normal(0, 10, 1000)
values3 = np.random.normal(0, 10, 10000)

fig = plt.figure(figsize = (16, 9))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
ax1.hist(values1, 50)
ax2.hist(values2, 50)
ax3.hist(values3, 50)

ax1.grid()
ax2.grid()
ax3.grid()
plt.show()