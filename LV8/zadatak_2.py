import numpy as np
from tensorflow import keras
from keras import layers
from keras.models import load_model
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

num_classes = 10
input_shape = (28, 28, 1)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)
model = load_model("MNIST/")
predictions = model.predict(x_test_s)
y_test_s = np.argmax(y_test_s, axis = 1)
predictions = np.argmax(predictions, axis = 1)
bad = x_test_s[y_test_s != predictions]
print(len(bad))
bad_y_test_s = y_test_s[y_test_s != predictions]
bad_predictions = predictions[y_test_s != predictions]
for i in range(5):
    plt.figure()
    plt.title("Stvarno: " + str(bad_y_test_s[i]) + ", predvideno: " + str(bad_predictions[i]))
    plt.imshow(bad[i])
plt.show()