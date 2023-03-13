#Zadatak 2.4.4

import numpy as np
import matplotlib.pyplot as plt

zeros = np.zeros((50, 50))
ones = np.ones((50, 50))

left = np.vstack([zeros, ones])
right = np.flip(left, axis = 0)
img = np.hstack([left, right])
plt.imshow(img, cmap = "gray")
plt.show()