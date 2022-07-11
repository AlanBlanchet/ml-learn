import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler

import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
import tensorflow as tf
import matplotlib.pyplot as plt

from data import *

gpus = K.tensorflow_backend._get_available_gpus()


train_labels = np.array(train_labels)
train_samples = np.array(train_samples)
test_samples = np.array(test_samples)
test_labels = np.array(test_labels)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train_samples = scaler.fit_transform((train_samples).reshape(-1, 1))
scaled_test_samples = scaler.fit_transform((test_samples).reshape(-1, 1))

model = Sequential(
    [
        Dense(16, input_shape=(1,), activation="relu"),
        Dense(32, activation="relu"),
        Dense(2, activation="softmax"),
    ]
)

model.summary()
model.compile(
    Adam(lr=0.001), loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.fit(
    scaled_train_samples,
    train_labels,
    batch_size=10,
    epochs=20,
    verbose=2,
    validation_split=0.1,
    shuffle=True,
)

predictions = model.predict(scaled_test_samples, batch_size=10, verbose=0)

for i in predictions:
    print(i)

rounded_predictions = model.predict_classes(
    scaled_test_samples, batch_size=10, verbose=0
)

cm = confusion_matrix(test_labels, rounded_predictions)
