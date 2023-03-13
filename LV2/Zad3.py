#Zadatak 2.4.3

import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('road.jpg')
orig = img[:, :, 0].copy()
plt.imshow(orig, cmap = "gray")
plt.figure()

#a
aCopy = orig.copy()
for i in range(int(str(aCopy.shape).split(',')[0].lstrip('('))):
    for j in range(int(str(aCopy.shape).split(',')[1].rstrip(')'))):
        aCopy[i, j] += 100
        if aCopy[i, j] <= 100:
            aCopy[i, j] = 255

plt.imshow(aCopy, cmap = "gray")
plt.figure()

#b
bCopy = np.hsplit(orig.copy(), 4)[1]
plt.imshow(bCopy, cmap = "gray")
plt.figure()

#c
cCopy = np.rot90(np.rot90(np.rot90(orig.copy())))
plt.imshow(cCopy, cmap = "gray")
plt.figure()

#d
dCopy = np.flip(orig.copy(), axis = 1)
plt.imshow(dCopy, cmap = "gray")
plt.show()