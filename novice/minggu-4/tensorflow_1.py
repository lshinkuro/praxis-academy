import tensorflow as tf

# import  numpy as np
# a = np.arange(15).reshape(3,5)  
# print(a.shape)
# print(a.ndim)
# print(a.dtype.name)
# print(a.itemsize)
# print(a.size)
# print(type(a))

# b = np.array([8,34,4,2])
# print(b)
# print(b.dtype)

# b1 =np.array([(1,2,3,4),(5,6,7,8)])
# print(b1)

# c = np.array([[2,3],[4,5]],dtype=complex)
# print(c)

# print(np.zeros((3,5)))

'''
First step to Keras

This is modified version of fchollet/deep-learning-with-python-notebooks
Original copyright: Copyright (c) 2017 François Chollet
https://github.com/fchollet/deep-learning-with-python-notebooks
'''

from keras.datasets import imdb

import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    # Create an all-zero matrix of shape (len(sequences), dimension)
    print("shape=%s" % sequences.shape)
    results = np.zeros((len(sequences), dimension), dtype='uint16')
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.  # set specific indices of results[i] to 1s
    return results


# load data
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# vectorize train data
x_train = vectorize_sequences(train_data)

# vectorize test data
x_test = vectorize_sequences(test_data)

# vectorize train label
y_train = np.asarray(train_labels).astype('float32')

# vectorize test label
y_test = np.asarray(test_labels).astype('float32')


x_train[0]

y_train[0]


from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
             loss='binary_crossentropy',
             metrics=['accuracy'])

x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val)
                   )

history_dict = history.history
history_dict.keys()

import matplotlib.pyplot as plt

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len(loss_values) + 1)

# 'bo' means 'blue dot'
plt.plot(epochs, loss_values, 'bo', label='Training loss')
# 'b' means 'solid blue line'
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# clear the image
plt.clf()

accs = history_dict['acc']
val_accs = history_dict['val_acc']

plt.plot(epochs, accs, 'bo', label='Training acc')
plt.plot(epochs, val_accs, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()



results = model.evaluate(x_test, y_test)
results

