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