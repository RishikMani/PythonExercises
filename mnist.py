import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Dropout

'''load the data'''
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
 
 '''let us check the shape of various datasets'''
 print('Training dataset:')
 print('Features shape is {}'.format(X_train.shape))
 print('Labels shape is {}'.format(y_train.shape))
 
 print('Testing dataset:')
 print('Features shape is {}'.format(X_test.shape))
 print('Labels shape is {}'.format(y_test.shape))
 
 '''let us display an image here and verify it with its label'''
plt.imshow(X_train[0], cmap=plt.cm.binary)
plt.show()
print('Label is {}'.format(y_train[0])

'''
The images are in the shape of (28, 28).
Normalize the images and convert them to shape (28, 28, 1).
The 1 at the last signifies that the inages are of one color. i.e gray scale
'''
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_train = X_train / 255.0
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_test = X_test / 255.0

'''create a Sequential keras model'''
model = Sequential()

'''for the very first layer in the model, input_shape attribute should be mentioned'''
model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, kernel_size=3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

'''tf.train.AdamOptimizer has been deprecated'''
model.compile(optimizer=tf.compat.v1.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=10)

'''create a pandas dataset with all the keys stored in the history object'''
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch


def plot_history():
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy vs validation accuracy')
    plt.plot(hist['epoch'], hist['acc'], label='Train accuracy')
    plt.plot(hist['epoch'], hist['val_acc'], label='Val accuracy')
    plt.legend()
    plt.show()
    
plot_history()

test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)

'''save the model locally'''
model.save('epic_num_reader.model')

'''load the saved model'''
new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict(X_test)

print(np.argmax(predictions[0]))

X_test = X_test.reshape(X_test.shape[0], 28, 28)
plt.imshow(X_test[0],cmap=plt.cm.binary)
plt.show()
