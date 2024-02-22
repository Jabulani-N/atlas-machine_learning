# Regularization

Regularization is used to prevent a prediction model from overfitting: becoming so extremely good at predicting a given data set that it becomes less useful when applied to others.

L2 Regularization proportoinately alters the weights to prevent them from ever perfectly fitting a given dataset.

## Task 0 L2 Regularization Cost

Basic idea:
1. `L2_cost = sum of (all individual weights squared)`
2. `L2_regularization = (lambtha / (2 * m)) * l2_cost`
3. `new_cost = cost + l2_regularization`

## Task 1 Gradient Descent with L2 Regularization

Remember from the [Classification Project](https://github.com/Jabulani-N/atlas-machine_learning/blob/main/supervised_learning/classification/13-neural_network.py) and other previous weeeks that `dz = cost of last activation slot`
*  `cache[A0]`, so each layer is naturally enumerated (layer 1 activation = `cache[A1]`)

# Task 2 L2 Regularization Cost
- currently incomplete
The reason this task gives so much less information is because we are using `Tensorflow`, not numpy

* [making a regularizer](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L2)
* [identifying all weights variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/trainable_variables)
  * `all_weights = [v for v in tf.trainable_variables() if "weights" in v.name]`
  * [add regularization penalty](https://www.typeerror.org/docs/tensorflow~1.15/contrib/layers/apply_regularization)

# Task 4 Forward Propagation with Dropout
**Dropout** is a means of ensuring no one node holds too much power in a neural network. If the whole thing falls apart when a given node is gone, that's not good. To counteract this, dropout removes random nodes when training the network. This way, every node is trained in a way such that it can function "well enough" when any given node(s) is removed.
