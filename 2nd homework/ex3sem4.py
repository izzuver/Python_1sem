import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')
pl = list(df['PetalLengthCm'])
min12 = 0
m12 = 0
m1215 = 0
m15 = 0
max15 = 0
for i in pl:
    if i > 1.5:
        max15 += 1
    else:
        if i < 1.5:
            if i > 1.2:
                m1215 += 1
            else:
                if i < 1.2:
                    min12 += 1
                else:
                    m12 += 1
        else:
            m15 += 1
summ = min12 + m12 + m1215 + m15 + max15

fig = plt.figure(figsize = (16, 9))
plt.pie([min12/summ, m12/summ, m1215/summ, m15/summ, max15/summ], labels = ['<1.2','=1.2','>1.2 && <1.5', '=1.5', '>1.5'])
plt.title('sizes')


plt.show()