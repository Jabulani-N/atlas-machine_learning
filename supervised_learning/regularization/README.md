# Regularization


## Task 0 L2 Regularization Cost

Basic idea:
1. `L2_cost = sum of (all individual weights squared)`
2. `L2_regularization = (lambtha / (2 * m)) * l2_cost`
3. `new_cost = cost + l2_regularization`

## Task 1 Gradient Descent with L2 Regularization

Remember from the [Classification Project](https://github.com/Jabulani-N/atlas-machine_learning/blob/main/supervised_learning/classification/13-neural_network.py) and other previous weeeks that `dz = cost of last activation slot`
*  `cache[A0]`, so each layer is naturally enumerated (layer 1 activation = `cache[A1]`)

# Task 2 L2 Regularization Cost
The reason this task gives so much less information is because we are using `Tensorflow`, not numpy