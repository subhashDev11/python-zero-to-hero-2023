#Interpolation

import numpy as np
from scipy.interpolate import splrep, splev
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.sin(x)

tck = splrep(x, y, s=0)
x_new = np.linspace(0, 10, num=101, endpoint=True)
y_new = splev(x_new, tck, der=0)

plt.plot(x, y, 'o', label='data')
plt.plot(x_new, y_new, label='spline')
plt.legend()
plt.show()
