# This document has notes for what I may say in the article

about half of the tasks are demonstrating the way Tensorflow streamlines operations one can manuualy perform using numpy (which is itself a massive streamling improvement from base python for matrix operations.)

Due to this, we will discuss the tasks in pairs: treating each duo of tasks as a single opreration to perform.

## Batch Normalization

Batch normalization is an operation performed to help prevent predictions from varying too wildly. This allows changes to be more "smooth," in their approach to local loss minima, rather than making iterations that are not necessarily better than the previous ones.

[Explanation for why normliaze data](https://www.jeremyjordan.me/batch-normalization/)

[What is RMSProp?](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a)
* the purpose is to solve the problem of "sometimes the gradient is huge, and other times it is small. how do we get a learning rate that works for both?"