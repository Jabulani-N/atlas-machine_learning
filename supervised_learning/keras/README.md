# Keras

<details>
  <summary>test code structure</summary>
<details>
  <summary>test code</summary>

  ```python
content
```
</details>
<details>
  <summary>expected output</summary>

  ```python
content
```
</details>
</details>

## Task 0 Sequential

<details>
  <summary>test code</summary>
  
  ```python
  #!/usr/bin/env python3

  # Force Seed - fix for Keras
  SEED = 0

  import os
  os.environ['PYTHONHASHSEED'] = str(SEED)
  import random
  random.seed(SEED)
  import numpy as np
  np.random.seed(SEED)
  import tensorflow as tf
  tf.random.set_seed(SEED)
  import tensorflow.keras as K

  build_model = __import__('0-sequential').build_model

  if __name__ == '__main__':
      network = build_model(784, [256, 256, 10], ['tanh', 'tanh', 'softmax'], 0.001, 0.95)
      network.summary()
      print(network.losses)

```
</details>
<details>
  <summary>expected output</summary>

  ```python
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense (Dense)                (None, 256)               200960
_________________________________________________________________
dropout (Dropout)            (None, 256)               0
_________________________________________________________________
dense_1 (Dense)              (None, 256)               65792
_________________________________________________________________
dropout_1 (Dropout)          (None, 256)               0
_________________________________________________________________
dense_2 (Dense)              (None, 10)                2570
=================================================================
Total params: 269,322
Trainable params: 269,322
Non-trainable params: 0
_________________________________________________________________
[<tf.Tensor: shape=(), dtype=float32, numpy=0.5120259>, <tf.Tensor: shape=(), dtype=float32, numpy=0.5118243>, <tf.Tensor: shape=(), dtype=float32, numpy=0.020181004>]

```
</details>

&nbsp;

This involves [building a Keras model](https://keras.io/guides/sequential_model/):
```

# Define Sequential model with 3 layers
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ]
)
# Call model on a test input
x = ops.ones((3, 3))
y = model(x)
```

You can `add()` a layer this way:
* `model = keras.Sequential()`
* `model.add(layers.Dense(2, activation="relu"))`
* `model.add(layers.Dense(3, activation="relu"))`
* `model.add(layers.Dense(4))`

[Dropout Layers](https://keras.io/api/layers/regularization_layers/dropout/) follow this format:
* `keras.layers.Dropout(rate, noise_shape=None, seed=None, **kwargs)`

## Task 1 Input


<details>
  <summary>test code</summary>

  ```python
#!/usr/bin/env python3

# Force Seed - fix for Keras
SEED = 0

import os
os.environ['PYTHONHASHSEED'] = str(SEED)
import random
random.seed(SEED)
import numpy as np
np.random.seed(SEED)
import tensorflow as tf
tf.random.set_seed(SEED)
import tensorflow.keras as K
build_model = __import__('1-input').build_model

if __name__ == '__main__':
    network = build_model(784, [256, 256, 10], ['tanh', 'tanh', 'softmax'], 0.001, 0.95)
    network.summary()
    print(network.losses)

```
</details>
<details>
  <summary>expected output</summary>

  ```python
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 784)]             0
_________________________________________________________________
dense (Dense)                (None, 256)               200960
_________________________________________________________________
dropout (Dropout)            (None, 256)               0
_________________________________________________________________
dense_1 (Dense)              (None, 256)               65792
_________________________________________________________________
dropout_1 (Dropout)          (None, 256)               0
_________________________________________________________________
dense_2 (Dense)              (None, 10)                2570
=================================================================
Total params: 269,322
Trainable params: 269,322
Non-trainable params: 0
_________________________________________________________________
[<tf.Tensor: shape=(), dtype=float32, numpy=0.5120259>, <tf.Tensor: shape=(), dtype=float32, numpy=0.5118243>, <tf.Tensor: shape=(), dtype=float32, numpy=0.020181004>]

```
</details>

To make this [keras model](https://www.tensorflow.org/api_docs/python/tf/keras/Model), we'll need to put together all the [input](https://www.tensorflow.org/api_docs/python/tf/keras/Input) and output objects it needs.

For example:
```
import tensorflow as tf

inputs = tf.keras.Input(shape=(3,))
x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)
outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

* note that in our work, we'll be immporting keras as `K`, so we'll have that instead of "tf.keras"

Let's break this down.
* `inputs = tf.keras.Input(shape=(3,))`: We want our input to work for the "number of input features," `nx`, so the shape of `shape=(nx,)` will be perfect.
* `x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)`: `x` is going to be a single layer with `inputs` assigned as the input layer.
  * `4` is the number of nodes
    * our project will have this number provided in the list `layers` we are given as input
  * `activation=tf.nn.relu` is making the activation function reLu.
    * our project will have this value provided in the list `activations` we are given as input
  * `(inputs)`
    * the input layer for the layer `x` is the layer `(inputs)`
* `outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x)`: creates the layer  `outputs` and assigns `x` to it as the input layer.
    * `5` is the number of nodes
    * `activation=tf.nn.softmax`: this layer uses softmax activaiton
      * our project will have this value provided in the list `activations` we are given as input.
    * the input layer for the layer `outputs` is the layer `x`
* `model = tf.keras.Model(inputs=inputs, outputs=outputs)`: creates model `model` with the inputs layer `inputs` and the output layer `outputs`.
  * If we wanted, we could make any layer the output layer to see what that layer did.

Hint for how you can design/assign your layers:
```
layer = 1
layer = layer + 1
```
Layers can do the same idea as integers in that they can have a layer defined by saying "the layer i used to be assigned to is now my input." Just like integers can say "the value i used to have? add 1 to that and that is now my value."

## Task 2 Optimize

<details>
  <summary>test code</summary>

  ```python
#!/usr/bin/env python3

import tensorflow as tf

build_model = __import__('1-input').build_model
optimize_model = __import__('2-optimize').optimize_model

if __name__ == '__main__':
    model = build_model(784, [256, 256, 10], ['tanh', 'tanh', 'softmax'], 0.001, 0.95)
    optimize_model(model, 0.01, 0.99, 0.9)
    print(model.loss)
    opt = model.optimizer
    print(opt.__class__)
    print(tuple(map(lambda x: x.numpy(),(opt.lr, opt.beta_1, opt.beta_2))))

```
</details>
<details>
  <summary>expected output</summary>

  ```python
categorical_crossentropy
<class 'keras.optimizer_v2.adam.Adam'>
(0.01, 0.99, 0.9)


```
</details>

[This is how you make an Adam Optimizer](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam).
* we are given the necesary inputs.
* it returns an Optimizer object.

[This is how you run the optimizer in your model](https://keras.io/api/models/model_training_apis/)
* you don't have to return anything. This changes the model itself.

### Potential Pitfalls

`crossentropy` is different from `categorical_crossentropy`


## Task 2 One Hot

<details>
  <summary>test code</summary>

  ```python
#!/usr/bin/env python3

import numpy as np
one_hot = __import__('3-one_hot').one_hot

if __name__ == '__main__':
    labels = np.load('../data/MNIST.npz')['Y_train'][:10]
    print(labels)
    print(one_hot(labels))


```
</details>
<details>
  <summary>expected output</summary>

  ```python
[5 0 4 1 9 2 1 3 1 4]
[[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]]
```
</details>

[There is a Keras method for this](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical).

## Task 4 Train, 5 Validate, 6 Early Stopping

<details>
  <summary> task 4 test code</summary>

  ```python
#!/usr/bin/env python3
"""
Main file
"""

# Force Seed - fix for Keras
SEED = 0

import os
os.environ['PYTHONHASHSEED'] = str(SEED)
import random
random.seed(SEED)
import numpy as np
np.random.seed(SEED)
import tensorflow as tf
tf.random.set_seed(SEED)
import tensorflow.keras as K

# Imports
build_model = __import__('1-input').build_model
optimize_model = __import__('2-optimize').optimize_model
one_hot = __import__('3-one_hot').one_hot
train_model = __import__('4-train').train_model


if __name__ == '__main__':
    datasets = np.load('../data/MNIST.npz')
    X_train = datasets['X_train']
    X_train = X_train.reshape(X_train.shape[0], -1)
    Y_train = datasets['Y_train']
    Y_train_oh = one_hot(Y_train)

    lambtha = 0.0001
    keep_prob = 0.95
    network = build_model(784, [256, 256, 10], ['relu', 'relu', 'softmax'], lambtha, keep_prob)
    alpha = 0.001
    beta1 = 0.9
    beta2 = 0.999
    optimize_model(network, alpha, beta1, beta2)
    batch_size = 64
    epochs = 5
    train_model(network, X_train, Y_train_oh, batch_size, epochs)
```
</details>
<details>
  <summary> task 4 expected output</summary>

  ```python
Epoch 1/5
782/782 [==============================] - 5s 4ms/step - loss: 0.3536 - acc: 0.9205
Epoch 2/5
782/782 [==============================] - 3s 3ms/step - loss: 0.1948 - acc: 0.9654
Epoch 3/5
782/782 [==============================] - 3s 3ms/step - loss: 0.1568 - acc: 0.9752
Epoch 4/5
782/782 [==============================] - 3s 3ms/step - loss: 0.1365 - acc: 0.9803
Epoch 5/5
782/782 [==============================] - 3s 3ms/step - loss: 0.1269 - acc: 0.9829
```
</details>

<details>
  <summary>task 5 test code</summary>

  ```python
#!/usr/bin/env python3
"""
Main file
"""

# Force Seed - fix for Keras
SEED = 0

import os
os.environ['PYTHONHASHSEED'] = str(SEED)
import random
random.seed(SEED)
import numpy as np
np.random.seed(SEED)
import tensorflow as tf
tf.random.set_seed(SEED)
import tensorflow.keras as K

# Imports
build_model = __import__('1-input').build_model
optimize_model = __import__('2-optimize').optimize_model
one_hot = __import__('3-one_hot').one_hot
train_model = __import__('5-train').train_model

if __name__ == '__main__':
    datasets = np.load('../data/MNIST.npz')
    X_train = datasets['X_train']
    X_train = X_train.reshape(X_train.shape[0], -1)
    Y_train = datasets['Y_train']
    Y_train_oh = one_hot(Y_train)
    X_valid = datasets['X_valid']
    X_valid = X_valid.reshape(X_valid.shape[0], -1)
    Y_valid = datasets['Y_valid']
    Y_valid_oh = one_hot(Y_valid)

    lambtha = 0.0001
    keep_prob = 0.95
    network = build_model(784, [256, 256, 10], ['relu', 'relu', 'softmax'], lambtha, keep_prob)
    alpha = 0.001
    beta1 = 0.9
    beta2 = 0.999
    optimize_model(network, alpha, beta1, beta2)
    batch_size = 64
    epochs = 5
    train_model(network, X_train, Y_train_oh, batch_size, epochs, validation_data=(X_valid, Y_valid_oh))
```
</details>
<details>
  <summary>task 5 expected output</summary>

  ```python
Train on 50000 samples, validate on 10000 samples
Epoch 1/5
50000/50000 [==============================] - 7s 145us/step - loss: 0.3508 - acc: 0.9202 - val_loss: 0.2174 - val_acc: 0.9602
Epoch 2/5
50000/50000 [==============================] - 7s 135us/step - loss: 0.1964 - acc: 0.9660 - val_loss: 0.1772 - val_acc: 0.9702
Epoch 3/5
50000/50000 [==============================] - 7s 131us/step - loss: 0.1587 - acc: 0.9760 - val_loss: 0.1626 - val_acc: 0.9740
Epoch 4/5
50000/50000 [==============================] - 6s 129us/step - loss: 0.1374 - acc: 0.9810 - val_loss: 0.1783 - val_acc: 0.9703
Epoch 5/5
50000/50000 [==============================] - 7s 137us/step - loss: 0.1242 - acc: 0.9837 - val_loss: 0.1547 - val_acc: 0.9757

```
</details>

<details>
  <summary>task 6 test code</summary>

  ```python
#!/usr/bin/env python3
"""
Main file
"""

# Force Seed - fix for Keras
SEED = 0

import os
os.environ['PYTHONHASHSEED'] = str(SEED)
import random
random.seed(SEED)
import numpy as np
np.random.seed(SEED)
import tensorflow as tf
tf.random.set_seed(SEED)
import tensorflow.keras as K

# Imports
build_model = __import__('1-input').build_model
optimize_model = __import__('2-optimize').optimize_model
one_hot = __import__('3-one_hot').one_hot
train_model = __import__('6-train').train_model


if __name__ == '__main__':
    datasets = np.load('../data/MNIST.npz')
    X_train = datasets['X_train']
    X_train = X_train.reshape(X_train.shape[0], -1)
    Y_train = datasets['Y_train']
    Y_train_oh = one_hot(Y_train)
    X_valid = datasets['X_valid']
    X_valid = X_valid.reshape(X_valid.shape[0], -1)
    Y_valid = datasets['Y_valid']
    Y_valid_oh = one_hot(Y_valid)

    lambtha = 0.0001
    keep_prob = 0.95
    network = build_model(784, [256, 256, 10], ['relu', 'relu', 'softmax'], lambtha, keep_prob)
    alpha = 0.001
    beta1 = 0.9
    beta2 = 0.999
    optimize_model(network, alpha, beta1, beta2)
    batch_size = 64
    epochs = 30
    train_model(network, X_train, Y_train_oh, batch_size, epochs,
                validation_data=(X_valid, Y_valid_oh), early_stopping=True,
                patience=3)
```
</details>
<details>
  <summary>task 6 expected output</summary>

  ```python
Epoch 1/30
782/782 [==============================] - 5s 4ms/step - loss: 0.3536 - acc: 0.9205 - val_loss: 0.2088 - val_acc: 0.9639
Epoch 2/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1949 - acc: 0.9658 - val_loss: 0.1681 - val_acc: 0.9726
Epoch 3/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1574 - acc: 0.9758 - val_loss: 0.1637 - val_acc: 0.9741
Epoch 4/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1369 - acc: 0.9804 - val_loss: 0.1562 - val_acc: 0.9760
Epoch 5/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1257 - acc: 0.9834 - val_loss: 0.1585 - val_acc: 0.9751
Epoch 6/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1151 - acc: 0.9857 - val_loss: 0.1503 - val_acc: 0.9773
Epoch 7/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1100 - acc: 0.9866 - val_loss: 0.1500 - val_acc: 0.9760
Epoch 8/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1071 - acc: 0.9875 - val_loss: 0.1395 - val_acc: 0.9790
Epoch 9/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1015 - acc: 0.9889 - val_loss: 0.1406 - val_acc: 0.9787
Epoch 10/30
782/782 [==============================] - 3s 3ms/step - loss: 0.1004 - acc: 0.9883 - val_loss: 0.1459 - val_acc: 0.9773
Epoch 11/30
782/782 [==============================] - 3s 3ms/step - loss: 0.0943 - acc: 0.9907 - val_loss: 0.1477 - val_acc: 0.9786

```
</details>


Just put all the provided parameters into the inputted model via [`Keras.model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model). They're even provided in order.

[Early Stopping](https://keras.io/api/callbacks/early_stopping/) is a `callback` object created and fed to the model via `callbacks=callback_object` in the model's `fit` kwargs.

## Task 7 Learning Rate Decay

[Inverse Time Decay](https://keras.io/api/optimizers/learning_rate_schedules/inverse_time_decay/) learning rate decay returns an optimizer. That optimizer can be fed to the model via [`model.compile(optimizer, loss='mse', steps_per_execution=10)`](https://www.tensorflow.org/api_docs/python/tf/keras/Model) before using `model.fit`.

You'll need to use the [Learning Rate Scheduler](https://keras.io/api/callbacks/learning_rate_scheduler/) to create a new `callback` to append to whatever it currently has.
* we feed it a "schedule," and [Inverse Time Decay Schedule](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay)

<details>
<summary>if <code>K.optimizers.schedules.InverseTimeDecay</code> is incompatible, click me for an alternative format!</summary>

```python
callback.append(K.callbacks.LearningRateScheduler(lambda epoch: alpha / (1 + decay_rate * epoch), verbose=1))
```
</details>

## Task 8 Save only the Best

[This is the callback for saving best as a checkpoint](https://keras.io/api/callbacks/model_checkpoint/).

## Task 9 Save and Load Model

[Saving and Loading documentation](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/)
* `keras.saving.load_model` will not work. Use `keras.models.load_model` instead.


## Task 10 Save and Load Weights

[Saving and Loading weights documentation](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading/)

## Task 11 Save and Load Configuration

This is a subfunction of [saving and loading](https://keras.io/guides/serialization_and_saving/)
* basic structure `json_config = model.to_json()`, which can be found in the above page