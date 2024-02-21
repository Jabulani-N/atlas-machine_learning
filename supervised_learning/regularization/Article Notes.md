# L2 Regularization

Regularization is used to prevent a prediction model from overfitting: becoming so extremely good at predicting a given data set that it becomes less useful when applied to others.

L2 Regularization proportoinately alters the weights to prevent them from ever perfectly fitting a given dataset.
The basic idea is
* `L2_cost = sum of (all individual weights squared)`
* `L2_regularization = (lambtha / (2 * m)) * l2_cost`
