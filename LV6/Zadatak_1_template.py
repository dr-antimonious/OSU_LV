import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

def plot_decision_regions(X, y, classifier, resolution=0.02):
    plt.figure()
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl)

# ucitaj podatke
data = pd.read_csv("Social_Network_Ads.csv")
print(data.info())

data.hist()

# dataframe u numpy
X = data[["Age","EstimatedSalary"]].to_numpy()
y = data["Purchased"].to_numpy()

# podijeli podatke u omjeru 80-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify=y, random_state = 10)

# skaliraj ulazne velicine
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform((X_test))

# Model logisticke regresije
LogReg_model = LogisticRegression(penalty=None) 
LogReg_model.fit(X_train_n, y_train)

# Evaluacija modela logisticke regresije
y_train_p = LogReg_model.predict(X_train_n)
y_test_p = LogReg_model.predict(X_test_n)

print("Logisticka regresija: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

# granica odluke pomocu logisticke regresije
plot_decision_regions(X_train_n, y_train, classifier=LogReg_model)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Tocnost: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
plt.tight_layout()

#6.5.1.1.
KNN = KNeighborsClassifier(n_neighbors = 5)
KNN.fit(X_train_n, y_train)

y_train_p = KNN.predict(X_train_n)
y_test_p = KNN.predict(X_test_n)

print("KNN model: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

#6.5.1.2.
KNN_1 = KNeighborsClassifier(n_neighbors = 1)
KNN_1.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, KNN_1)
plt.title('K=1')

KNN_100 = KNeighborsClassifier(n_neighbors = 100)
KNN_100.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, KNN_100)
plt.title('K=100')

#6.5.2.
param_grid = {'n_neighbors': [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
knn_gscv = GridSearchCV(estimator = KNeighborsClassifier().fit(X_train_n, y_train), param_grid = param_grid, cv = 5, scoring = 'accuracy')
knn_gscv.fit(X_train_n, y_train)
print(knn_gscv.best_params_)
print(knn_gscv.best_score_)

#6.5.3.
rbf_svm = svm.SVC(kernel = 'rbf', C = 1, gamma = 1, random_state = 42)
rbf_svm.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, rbf_svm)

for i in range(4):
    for j in range (4):
        for k in range(4):
            C = [0.01, 0.1, 1, 10]
            gamma = [0.01, 0.1, 1, 10]
            kernel = ['linear', 'poly', 'rbf', 'sigmoid']
            test = svm.SVC(kernel = kernel[i], C = C[j], gamma = gamma[k], random_state = 42)
            test.fit(X_train_n, y_train)
            plot_decision_regions(X_train_n, y_train, test)
            plt.title("C: " + str(C[j]) + ", gamma: " + str(gamma[k]) + ", kernel: " + kernel[i])
        plt.show()

#6.5.4.
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
              'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
svm_gscv = GridSearchCV(estimator = svm.SVC().fit(X_train_n, y_train), param_grid = param_grid, cv = 5, scoring = 'accuracy')
svm_gscv.fit(X_train_n, y_train)
print(svm_gscv.best_params_)
print(svm_gscv.best_score_)
plt.show()