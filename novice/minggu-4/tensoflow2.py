from keras.datasets import reuters
(train_data,train_labels),(test_data,test_labels)=reuters.load_data(num_words=10000)

len(train_data)

len(test_data)

train_data[10]

##convert news example sample text
word_index = reuters.get_word_index()
reverse_word_index = dict([(value,key)for (key,value)in word_index.items()])
decoded_newswire = ' '.join(
    [reverse_word_index.get(i -3,'?')for i in train_data[0]]
)
decoded_newswire

import numpy as np

def vectorize_sequences(sequences,dimension=10000):
    results = np.zeros((len(sequences),dimension), dtype='uint16')
    for i,sequence in enumerate(sequences):
        results[i,sequence]=1
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

from keras.utils.np_utils import to_categorical

one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels=to_categorical(test_labels)
one_hot_test_labels[10]

from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(64,activation='relu',input_shape=(10000,)))
model.add(layers.Dense(128,activation='relu'))
model.add(layers.Dense(46,activation='softmax'))

##compile the model

model.compile(optimizer ='rmsprop',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val=one_hot_train_labels[:1000]
partial_y_train=one_hot_train_labels[1000:]

# train the model

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val,y_val))

results = model.evaluate(x_test,one_hot_test_labels)

import matplotlib.pyplot as plt

loss =history.history['loss']
val_loss=history.history['val_loss']

epochs=range(1,len(loss)+1)

plt.plot(epochs,loss,'bo',label='Training los')
plt.plot(epochs,val_loss,'b',label='validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()



plt.clf()

accs = history.history['acc']
val_accs = history.history['val_acc']

plt.plot(epochs, accs, 'bo', label='Training acc')
plt.plot(epochs, val_accs, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

