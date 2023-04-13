import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#a
X_train_tsposed = np.transpose(X_train)
X_test_tsposed = np.transpose(X_test)
plt.scatter(x = X_train_tsposed[0],
            y = X_train_tsposed[1],
            s = 20,
            c = y_train,
            cmap = 'viridis',
            label = 'Training')
plt.scatter(x = X_test_tsposed[0],
            y = X_test_tsposed[1],
            s = 20,
            c = y_test,
            marker = 'x',
            cmap = 'viridis',
            label = 'Test')
plt.legend()
plt.colorbar()
plt.xlabel('x1')
plt.ylabel('x2')

#b
lrm = LogisticRegression()
lrm.fit(X_train, y_train)

#c
t0 = lrm.intercept_[0]
t1, t2 = lrm.coef_.T
plt.figure()
plt.scatter(x = X_train_tsposed[0],
            y = X_train_tsposed[1],
            s = 20,
            c = y_train,
            cmap = 'viridis',
            label = 'Training')
plt.colorbar()
plt.xlabel('x1')
plt.ylabel('x2')
decision_values = - ((t0 / t2) + X_train_tsposed[0] * (t1 / t2))
plt.plot(X_train_tsposed[0], decision_values)

#d
y_test_p = lrm.predict(X_test)
cm = confusion_matrix(y_test, y_test_p)
cmd = ConfusionMatrixDisplay(cm)
cmd.plot()
print(classification_report(y_test, y_test_p))

#e
plt.figure()
true = np.where(y_test == y_test_p)
false = np.where(y_test != y_test_p)
plt.scatter(x = X_test_tsposed[0, true],
            y = X_test_tsposed[1, true],
            s = 20,
            c = 'green')
plt.scatter(x = X_test_tsposed[0, false],
            y = X_test_tsposed[1, false],
            s = 20,
            c = 'black')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()