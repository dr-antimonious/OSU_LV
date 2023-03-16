import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

data = pd.read_csv('data_C02_emission.csv')

print(len(data))
print(data.info())
print(data.isnull().sum())

data = data.dropna(axis = 0).dropna(axis = 1).drop_duplicates().reset_index()

#a
data['CO2 Emissions (g/km)'].plot(kind = 'hist')
plt.xlabel('CO2 Emissions (g/km)')
plt.grid(visible = True)

#b
scatter = data.copy()
for i in range(len(scatter)):
    if scatter['Fuel Type'][i] == 'D':
        scatter['Fuel Type'][i] = 1
    elif scatter['Fuel Type'][i] == 'E':
        scatter['Fuel Type'][i] = 2
    elif scatter['Fuel Type'][i] == 'N':
        scatter['Fuel Type'][i] = 3
    elif scatter['Fuel Type'][i] == 'X':
        scatter['Fuel Type'][i] = 4
    elif scatter['Fuel Type'][i] == 'Z':
        scatter['Fuel Type'][i] = 5
fig, ax = plt.subplots(figsize = (7,5))
hexbins = ax.scatter(x = scatter['Fuel Consumption City (L/100km)'],
                    y = scatter['CO2 Emissions (g/km)'],
                    s = 10,
                    c = scatter['Fuel Type'],
                    cmap = cm.get_cmap('viridis'))
ax.set_xlabel('Fuel Consumption City (L/100km)')
ax.set_ylabel('CO2 Emissions (g/km)')
tickvals = [1, 2, 3, 4, 5]
cb = fig.colorbar(hexbins, ax = ax, ticks = tickvals)
cb.ax.set_yticklabels(['D', 'E', 'N', 'X',  'Z'])
cb.set_label('Fuel Type')

#c
data.boxplot(column = ['Fuel Consumption Hwy (L/100km)'], by = 'Fuel Type')
plt.figure()

#d
data.groupby('Fuel Type').size().plot(kind = 'bar')
plt.figure()

#e
data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean().plot(kind = 'bar')
plt.show()