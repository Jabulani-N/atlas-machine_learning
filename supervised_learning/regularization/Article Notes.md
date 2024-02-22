# L2 Regularization

Regularization is used to prevent a prediction model from overfitting: becoming so extremely good at predicting a given data set that it becomes less useful when applied to others.

L2 Regularization proportoinately alters the weights to prevent them from ever perfectly fitting a given dataset.
The basic idea is
* `L2_cost = sum of (all individual weights squared)`
* `L2_regularization = (lambtha / (2 * m)) * l2_cost`

The resultant `L2 regularization` can then be added to each weight in a backpropagation step.
To create an `L2_regularization` for each weight in a backpropagation step, add `(lambtha / m) * weights["W" + str(layer_num)]` to `dW` and then backpropagate as normal.

# Dropout

[tensorflow dropout documentation](https://www.tensorflow.org/api_docs/python/tf/compat/v1/layers/Dropout)
