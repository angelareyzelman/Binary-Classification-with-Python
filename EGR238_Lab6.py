import numpy as np
import matplotlib.pyplot as plt

x0_xcoords = []
x0_ycoords = []
x1_xcoords = []
x1_ycoords = []
for k in range(100):
    x0_xcoords.append(0)
    x0_ycoords.append(np.random.uniform(0,1))
    x1_xcoords.append(5)
    x1_ycoords.append(np.random.uniform(0,1))
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
ax.scatter(x0_xcoords, x0_ycoords)
#plt.xlabel('x0 coordinates')
#plt.ylabel('x1 coordinates')
plt.show
