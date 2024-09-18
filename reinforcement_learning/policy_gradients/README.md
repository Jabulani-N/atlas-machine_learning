# Policy Gradients

## Resrouces

[Policy Gradients in a Nutshell](https://towardsdatascience.com/policy-gradients-in-a-nutshell-8b72f9743c5d)

## Task 0

<details>
    <summary>Instructions</summary>

Write a function that computes the policy with a weight of a matrix.

Prototype: `def policy(matrix, weight):`

</details>

<details>
    <summary>Test Code</summary>

```

$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""
import numpy as np
from policy_gradient import policy


weight = np.ndarray((4, 2), buffer=np.array([
    [4.17022005e-01, 7.20324493e-01],
    [1.14374817e-04, 3.02332573e-01],
    [1.46755891e-01, 9.23385948e-02],
    [1.86260211e-01, 3.45560727e-01]
    ]))
state = np.ndarray((1, 4), buffer=np.array([
    [-0.04428214,  0.01636746,  0.01196594, -0.03095031]
    ]))

res = policy(state, weight)
print(res)

$
$ ./0-main.py
[[0.50351642 0.49648358]]
$

```

</details>
* it **is** possible to get the exact same result as the test code.

The basic ask here is to make a softmax funciton that runs through using the matrix and weight, like our older neural network projects use for activation funcitons.

* softmax takes a vector (which could be a row or column of a matrix) and transforms it so that the elements sum to 1, making them interpretable as probabilities

I used my previous [implimentation of softmax](https://github.com/Jabulani-N/atlas-machine_learning/blob/43b46625e3b830b60704cec2f7c577ec5a8f5769/supervised_learning/regularization/4-dropout_forward_prop.py#L43) to do the math here, and (effectively) updated it to handle the matrixes and do hte dot products for me.