import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')
sl = list(df['SepalLengthCm'])
sw = list(df['SepalWidthCm'])
pl = list(df['PetalLengthCm'])
pw = list(df['PetalWidthCm'])
fig = plt.figure(figsize = (16, 9))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)
ax1.scatter(sl, sw, marker='x')
ax2.scatter(sl, pl, marker='x')
ax3.scatter(sl, pw, marker='x')
ax4.scatter(sw, pl, marker='x')
ax5.scatter(sw, pw, marker='x')
ax6.scatter(pl, pw, marker='x')


num_pl = np.array(pl)
num_pw = np.array(pw)

b = ((np.mean(num_pl*num_pw) - np.mean(pl)*np.mean(pw))/(np.mean(num_pl ** 2) - (np.mean(pl)) ** 2))
a = np.mean(pw) - b * np.mean(pl)
print(a, b)
ax6.plot(num_pl, b * num_pl + a, 'r')

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()
plt.show()