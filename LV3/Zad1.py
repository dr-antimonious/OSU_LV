import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

#a
print(len(data))
print(data.info())
print(data.isnull().sum())

data = data.dropna(axis = 0).dropna(axis = 1).drop_duplicates().reset_index()

data['Make'] = data['Make'].astype('category')
data['Vehicle Class'] = data['Vehicle Class'].astype('category')
data['Transmission'] = data['Transmission'].astype('category')
data['Fuel Type'] = data['Fuel Type'].astype('category')

#b
print(data.sort_values(by = 'Fuel Consumption City (L/100km)').tail(3)[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print(data.sort_values(by = 'Fuel Consumption City (L/100km)').head(3)[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

#c
byengine = data[(data['Engine Size (L)'] > 2.5) & (data['Engine Size (L)'] < 3.5)]
print(len(byengine))
print(byengine['CO2 Emissions (g/km)'].mean())

#d
audi = data[data['Make'] == 'Audi']
print(len(audi))
print(audi[audi['Cylinders'] == 4]['CO2 Emissions (g/km)'].mean())

#e
print(data[(data['Cylinders'] >= 4) & (data['Cylinders'] % 2 == 0)]['index'].count())
bycylinder = data.groupby('Cylinders')
print(bycylinder[['CO2 Emissions (g/km)']].mean())

#f
print(data[data['Fuel Type'] == 'D']['Fuel Consumption City (L/100km)'].mean())
print(data[data['Fuel Type'] == 'X']['Fuel Consumption City (L/100km)'].mean())
print(data[data['Fuel Type'] == 'D']['Fuel Consumption City (L/100km)'].median())
print(data[data['Fuel Type'] == 'X']['Fuel Consumption City (L/100km)'].median())

#g
diesel4c = data[(data['Cylinders'] == 4) & (data['Fuel Type'] == 'D')]
print(diesel4c.sort_values(by = 'Fuel Consumption City (L/100km)').tail(1)[['Make', 'Model']])

#h
print(data[data['Transmission'].str.startswith('M')]['index'].count())

#i
print(data.corr(numeric_only = True))