# Keras


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
* `inputs = tf.keras.Input(shape=(3,))` We want our input to work for the "number of input features," `nx`, so the shape of `shape=(nx,)` will be perfect.
* `x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)` `x` is going to be a single layer.
  * `4` is the number of nodes
    * our project will have this number stored in the list `layers` we are given as input
  * `activation=tf.nn.relu` is making the activation function reLu.
    * our project will have this value stored in the list `layers` we are given as input