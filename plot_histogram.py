import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.loadtxt("histogram.txt")

h = data[:,0]
s = data[:,1]
v = data[:,2]
values = data[:,3]

# remove zero bins
mask = values > 0
h = h[mask]
s = s[mask]
v = v[mask]
values = values[mask]

values = values / np.max(values)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(h, s, np.zeros_like(values), 0.5, 0.5, values)

ax.set_xlabel('Hue Bin')
ax.set_ylabel('Saturation Bin')
ax.set_zlabel('Frequency')

plt.show()