# RNN

Recurrant Neural Network

These are good at processing sequences/sequential data

uses a loop that allows information to persist.
* updates internal state `h_sub_t` at the same step of generating output vector
* the block doing this is called the 'recurrent cell.'
* h_sub_t = f_sub_w (h_sub_[t-1], x_sub_t)

[in a normal feedforward neural network, the steps are all independant of each other](https://www.geeksforgeeks.org/introduction-to-recurrent-neural-network/), rather than output of one step influencing input of next step

[example](https://www.geeksforgeeks.org/introduction-to-recurrent-neural-network/):

```
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# generate some example data using text
text = "This is GeeksforGeeks a software training institute"
chars = sorted(list(set(text)))
char_to_index = {char: i for i, char in enumerate(chars)}
index_to_char = {i: char for i, char in enumerate(chars)}

# created input sequencces and corresponding labels for further implementation
seq_length = 3
sequences = []
labels = []

for i in range(len(text) - seq_length):
    seq = text[i:i+seq_length]
    label = text[i+seq_length]
    sequences.append([char_to_index[char] for char in seq])
    labels.append(char_to_index[label])

# converted sequences and labels into numpy arrays
# and used one-hot encoding to convert text to vector
X = np.array(sequences)
y = np.array(labels)

X_one_hot = tf.one_hot(X, len(chars))
y_one_hot = tf.one_hot(y, len(chars))


# model building
# build RNN model using relu and softmax activation functoins
model = Sequential()
model.add(SimpleRNN(50, input_shape=(seq_length, len(chars)), activation='relu'))
model.add(Dense(len(chars), activation='softmax'))

# model compilation
# builds neural network for training by specfying
#   optimizer
#   loss function
#   training metric
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# model training
model.fit(X_one_hot, y_one_hot, epochs=100)
```
