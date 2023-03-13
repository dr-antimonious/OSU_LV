#Zadatak 2.4.2

import numpy as np
import matplotlib.pyplot as plt

file = open('data.csv')
for line in file:
    try:
        line = line.rstrip().split(',')
        temp = np.array([[float(line[0]), float(line[1]), float(line[2])]])
        if 'data' not in globals():
            data = temp
        else:
            data = np.concatenate((data, temp))
    except ValueError:
        continue
file.close()

# a
print('Broj mjerenja: ', str(data.shape).lstrip('(').split(',')[0])

# b
plt.scatter(data[:, 2], data[:, 1])
plt.xlabel('masa/kg')
plt.ylabel('visina/cm')
plt.title('Odnos visine i mase osobe')

# c
plt.figure()
plt.scatter(data[0:-1:50, 2], data[0:-1:50, 1])
plt.xlabel('masa/kg')
plt.ylabel('visina/cm')
plt.title('Odnos visine i mase svake 50-te osobe')

# d
print('Minimalna visina: ', np.min(data[:, 1]))
print('Maksimalna visina: ', np.max(data[:, 1]))
print('Srednja visina: ', np.mean(data[:, 1]))

# e
men = data[:, :][(data[:, 0]) == 1]
print('Broj muskaraca: ', str(men.shape).lstrip('(').split(',')[0])
print('Minimalna visina: ', np.min(men[:, 1]))
print('Maksimalna visina: ', np.max(men[:, 1]))
print('Srednja visina: ', np.mean(men[:, 1]))

women = data[:, :][(data[:, 0]) == 0]
print('Broj zena: ', str(women.shape).lstrip('(').split(',')[0])
print('Minimalna visina: ', np.min(women[:, 1]))
print('Maksimalna visina: ', np.max(women[:, 1]))
print('Srednja visina: ', np.mean(women[:, 1]))

plt.show()