import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn.linear_model as lm
import sklearn.metrics as skmetrics

#a
input = pd.read_csv("data_C02_emission.csv")
X_labels = ['Engine Size (L)',
            'Cylinders',
            'Fuel Consumption City (L/100km)',
            'Fuel Consumption Hwy (L/100km)',
            'Fuel Consumption Comb (L/100km)',
            'Fuel Consumption Comb (mpg)']
y_label = ['CO2 Emissions (g/km)']
X = input[X_labels].to_numpy()
y = input[y_label].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

#b
X_train_tsposed = np.transpose(X_train)
X_test_tsposed = np.transpose(X_test)
for i in range(len(X_labels)):
    plt.scatter(x = X_train_tsposed[i],
                y = y_train,
                s = 20,
                c = '#0000ff',
                label = 'Training')
    plt.scatter(x = X_test_tsposed[i],
                y = y_test,
                s = 20,
                c = '#ff0000',
                label = 'Test')
    plt.xlabel(X_labels[i])
    plt.ylabel(y_label[0])
    plt.legend()
    plt.figure()

#c
ss = StandardScaler()
X_train_s = ss.fit_transform(X_train)
X_train_s_tsposed = np.transpose(X_train_s)
for i in range(len(X_labels)):
    plt.subplot(211)
    plt.hist(X_train_tsposed[i])
    plt.title(X_labels[i] + " before fit")
    plt.subplot(212)
    plt.hist(X_train_s_tsposed[i])
    plt.title(X_labels[i] + " after fit")
    plt.figure()
X_test_s = ss.transform(X_test)

#d
linearModel = lm.LinearRegression()
linearModel.fit(X_train_s, y_train)
print(linearModel.coef_)

#e
y_test_p = linearModel.predict(X_test_s)
plt.scatter(x = y_test,
            y = y_test_p,
            s = 20,
            c = '#0000ff')
plt.plot(y_test, y_test, color = 'black', linestyle = 'dashed')
plt.xlabel("Test values")
plt.ylabel("Predicted values")

#f
MSE = skmetrics.mean_squared_error(y_test, y_test_p)
print("Test size: 0.2")
print("MSE: ", MSE)
print("RMSE: ", math.sqrt(MSE))
print("MAE: ", skmetrics.mean_absolute_error(y_test, y_test_p))
print("MAPE: ", skmetrics.mean_absolute_percentage_error(y_test, y_test_p))
print("Rsquared: ", skmetrics.r2_score(y_test, y_test_p))

#g
sample = 0.2
for i in range(10):
    sample += 0.05
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = sample, random_state = 1)
    ss = StandardScaler()
    X_train_s = ss.fit_transform(X_train)
    X_test_s = ss.transform(X_test)
    linearModel = lm.LinearRegression()
    linearModel.fit(X_train_s, y_train)
    y_test_p = linearModel.predict(X_test_s)
    MSE = skmetrics.mean_squared_error(y_test, y_test_p)
    print("Test size: ", sample)
    print("MSE: ", MSE)
    print("RMSE: ", math.sqrt(MSE))
    print("MAE: ", skmetrics.mean_absolute_error(y_test, y_test_p))
    print("MAPE: ", skmetrics.mean_absolute_percentage_error(y_test, y_test_p))
    print("Rsquared: ", skmetrics.r2_score(y_test, y_test_p))

plt.show()