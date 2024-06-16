# Autoencoders

# Task 0 - "Vanilla" Autoencoder

<details>
    <summary>Instructions</summary>

Write a function `def autoencoder(input_dims, hidden_layers, latent_dims):` that creates an autoencoder:


* `input_dims` is an integer containing the dimensions of the model input

* `hidden_layers` is a list containing the number of nodes for each hidden layer in the encoder, respectively

  * the hidden layers should be reversed for the decoder

* `latent_dims` is an integer containing the dimensions of the latent space representation

Returns: `encoder`, `decoder`, `auto`

* `encoder` is the encoder model

* `decoder` is the decoder model

* `auto` is the full autoencoder model

The autoencoder model should be compiled using adam optimization and binary cross-entropy loss

All layers should use a `relu` activation except for the last layer in the decoder, which should use `sigmoid`

</details>

<details>
    <summary>Test Data</summary>

```
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

autoencoder = __import__('0-vanilla').autoencoder

(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((-1, 784))
x_test = x_test.reshape((-1, 784))
np.random.seed(0)
tf.random.set_seed(0)
encoder, decoder, auto = autoencoder(784, [128, 64], 32)
auto.fit(x_train, x_train, epochs=50,batch_size=256, shuffle=True,
                validation_data=(x_test, x_test))
encoded = encoder.predict(x_test[:10])
print(np.mean(encoded))
reconstructed = decoder.predict(encoded)

for i in range(10):
    ax = plt.subplot(2, 10, i + 1)
    ax.axis('off')
    plt.imshow(x_test[i].reshape((28, 28)))
    ax = plt.subplot(2, 10, i + 11)
    ax.axis('off')
    plt.imshow(reconstructed[i].reshape((28, 28)))
plt.show()
```

should output

```
Epoch 1/50
60000/60000 [==============================] - 5s 85us/step - loss: 0.2504 - val_loss: 0.1667
Epoch 2/50
60000/60000 [==============================] - 5s 84us/step - loss: 0.1498 - val_loss: 0.1361
Epoch 3/50
60000/60000 [==============================] - 5s 83us/step - loss: 0.1312 - val_loss: 0.1242
Epoch 4/50
60000/60000 [==============================] - 5s 79us/step - loss: 0.1220 - val_loss: 0.1173
Epoch 5/50
60000/60000 [==============================] - 5s 79us/step - loss: 0.1170 - val_loss: 0.1132

...

Epoch 46/50
60000/60000 [==============================] - 5s 80us/step - loss: 0.0852 - val_loss: 0.0850
Epoch 47/50
60000/60000 [==============================] - 5s 81us/step - loss: 0.0851 - val_loss: 0.0846
Epoch 48/50
60000/60000 [==============================] - 5s 84us/step - loss: 0.0850 - val_loss: 0.0848
Epoch 49/50
60000/60000 [==============================] - 5s 80us/step - loss: 0.0849 - val_loss: 0.0845
Epoch 50/50
60000/60000 [==============================] - 5s 85us/step - loss: 0.0848 - val_loss: 0.0844
6.5280433
```

</details>

# Task 1 - Sparse Autoencoder

<details>
    <summary>Instructions</summary>

Write a function def autoencoder(input_dims, hidden_layers, latent_dims, lambtha): that creates a sparse autoencoder:

input_dims is an integer containing the dimensions of the model input
hidden_layers is a list containing the number of nodes for each hidden layer in the encoder, respectively
the hidden layers should be reversed for the decoder
latent_dims is an integer containing the dimensions of the latent space representation
lambtha is the regularization parameter used for L1 regularization on the encoded output
Returns: encoder, decoder, auto
encoder is the encoder model
decoder is the decoder model
auto is the sparse autoencoder model
The sparse autoencoder model should be compiled using adam optimization and binary cross-entropy loss
All layers should use a relu activation except for the last layer in the decoder, which should use sigmoid
</details>


<details>
    <summary>Test Code</summary>

```

$ cat 1-main.py
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

autoencoder = __import__('1-sparse').autoencoder

(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((-1, 784))
x_test = x_test.reshape((-1, 784))
np.random.seed(0)
tf.set_random_seed(0)
encoder, decoder, auto = autoencoder(784, [128, 64], 32, 10e-6)
auto.fit(x_train, x_train, epochs=100,batch_size=256, shuffle=True,
                validation_data=(x_test, x_test))
encoded = encoder.predict(x_test[:10])
print(np.mean(encoded))
reconstructed = decoder.predict(encoded)

for i in range(10):
    ax = plt.subplot(2, 10, i + 1)
    ax.axis('off')
    plt.imshow(x_test[i].reshape((28, 28)))
    ax = plt.subplot(2, 10, i + 11)
    ax.axis('off')
    plt.imshow(reconstructed[i].reshape((28, 28)))
plt.show()
$ ./1-main.py
Epoch 1/50
60000/60000 [==============================] - 6s 102us/step - loss: 0.3123 - val_loss: 0.2538
Epoch 2/100
60000/60000 [==============================] - 6s 96us/step - loss: 0.2463 - val_loss: 0.2410
Epoch 3/100
60000/60000 [==============================] - 5s 90us/step - loss: 0.2400 - val_loss: 0.2381
Epoch 4/100
60000/60000 [==============================] - 5s 80us/step - loss: 0.2379 - val_loss: 0.2360
Epoch 5/100
60000/60000 [==============================] - 5s 82us/step - loss: 0.2360 - val_loss: 0.2339

...

Epoch 96/100
60000/60000 [==============================] - 5s 80us/step - loss: 0.1602 - val_loss: 0.1609
Epoch 97/100
60000/60000 [==============================] - 5s 84us/step - loss: 0.1601 - val_loss: 0.1608
Epoch 98/100
60000/60000 [==============================] - 5s 87us/step - loss: 0.1601 - val_loss: 0.1601
Epoch 99/100
60000/60000 [==============================] - 5s 89us/step - loss: 0.1601 - val_loss: 0.1604
Epoch 100/100
60000/60000 [==============================] - 5s 82us/step - loss: 0.1597 - val_loss: 0.1601
0.016292876

```
</details>
