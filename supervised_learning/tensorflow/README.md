# Tensorflow

This directory demonstrates the utilization of [Tensorflow](https://www.tensorflow.org/install/pip).

when assigning attributes to the tensorflow `placeholder` (it's a clas)

* name: `name='myName'` will give a printed result of `myName:0`
* dtype: simply put the dtype. you don't say "data type" or anything.
* size: `size=[None, x]` [will make the first dimension undefined](https://stackoverflow.com/questions/42606722/shape-of-placeholder-in-tensorflow), and able to be changed, rather than set in stone.
  * the "size=" is optional


tested via
```
#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

create_placeholders = __import__('0-create_placeholders').create_placeholders

x, y = create_placeholders(784, 10)
print(x)
print(y)
```
which should output
```
Tensor("x:0", shape=(?, 784), dtype=float32)
Tensor("y:0", shape=(?, 10), dtype=float32)
```
# Task 1 Create Layer

[Layer creation](https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/low_level_intro.md#layers)

[Initializing](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling)

[Densing layers](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)

* The `kernel_initializer=` segment can be fed an initializer you've already made as a variable via the initializing section above.

tested by
```
#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

create_placeholders = __import__('0-create_placeholders').create_placeholders
create_layer = __import__('1-create_layer').create_layer

x, y = create_placeholders(784, 10)
l = create_layer(x, 256, tf.nn.tanh)
print(l)
```
And should output
```
Tensor("layer/Tanh:0", shape=(?, 256), dtype=float32)
```
# Task 2 Forward Propagation

This task is running layer creation multiple times in series.
Each layer will be helping create the subsequent layer.
* if we are creating layer `n`, we will feed `create layer` layer `n-1`.
  * `x`, the placeholder, will be the very "first" layer.
* Prediction will be the final layer created.

The basic idea of what is going on is explained [here](https://aadimator.github.io/deep-learning-specialization/1.%20Neural%20Networks%20and%20Deep%20Learning/Week%204/Building+your+Deep+Neural+Network+-+Step+by+Step+v3.html) (search `L_model_forward`), but as long as you remember the concept of forward propagation from the previous project, understanding that concept will be much more helpful than another reading.

# Task 3 Calculate Accuracy

[tensorflow.divide is a funciton of Tensorflow](https://indianaiproduction.com/tensorflow-division-function/)

accuracy = correct_predictions / all_predictions
* apparently, this means it is the number of correct predictions divided by total number of predictions

This can be calculated via counting how many times prediction = correct answer, and dividing by length.

[`tf.math.equal`](https://www.tensorflow.org/api_docs/python/tf/math/equal) will allow elementwise comparison. After this, one can simply divide the sum of all elements by the length.
* in order to avoid counting every single "it is not x" as a correct prediction, we only want to check how many times they both return `1` in the same spot. We can do this with [`tf.math.argmax`](https://www.tensorflow.org/api_docs/python/tf/math/argmax). (the following  satement needs is my extrapolation and needs testing)This will spit out a list of indices that had the max value: `1`. Wherever the prediciotn and the input list are the same, indicating the guess was correct, it is correct.
After that, we can find the [mean](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean), which will divide the numebr  of correct predictions by the number of total predictions, granting the accuracy decimal.


## Potential Pitfall:

Cast the inputs of `tf.math.reduce_mean` as float32.  Because if our input tensors will be ints, that fact will override mean's default float output
