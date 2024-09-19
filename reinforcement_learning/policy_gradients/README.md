# Policy Gradients

## Resrouces

[Policy Gradients in a Nutshell](https://towardsdatascience.com/policy-gradients-in-a-nutshell-8b72f9743c5d)

## Task 0 - Simple Policy function


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

### Resources

[this](https://www.sharpsightlabs.com/blog/numpy-softmax/#stable-softmax-syntax) explains numerically stable softmax

## Task 1 - Compute the Monte-Carlo policy gradient

<details>
    <summary>Instructions</summary>

By using the previous function created `policy`, write a function that computes the Monte-Carlo policy gradient based on a state and a weight matrix.

Prototype: `def policy_gradient(state, weight):`
* `state`: matrix representing the current observation of the environment
* `weight`: matrix of random weight

Return: the action and the gradient (in this order)

</details>

<details>
    <summary>Test Code</summary>

```

$ cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""
import gym
import numpy as np
from policy_gradient import policy_gradient

env = gym.make('CartPole-v1')
np.random.seed(1)

weight = np.random.rand(4, 2)
state = env.reset()[None,:]
print(weight)
print(state)

action, grad = policy_gradient(state, weight)
print(action)
print(grad)

env.close()

$
$ ./1-main.py
[[4.17022005e-01 7.20324493e-01]
 [1.14374817e-04 3.02332573e-01]
 [1.46755891e-01 9.23385948e-02]
 [1.86260211e-01 3.45560727e-01]]
[[ 0.04228739 -0.04522399  0.01190918 -0.03496226]]
0
[[ 0.02106907 -0.02106907]
 [-0.02253219  0.02253219]
 [ 0.00593357 -0.00593357]
 [-0.01741943  0.01741943]]
$

```

</details>

* Results can be different since `weight` is randomized

The [Temporal Difference](../temporal_difference/) directory also has a [Monte Carlo](../temporal_difference/0-monte_carlo.py) function, so we can probably base what we do on that.
* It may not be related. Investigating.

`policy` is the function, so I just have to take the gradient of the function `policy` with respect to

### resources

https://colab.research.google.com/github/jorditorresBCN/Deep-Reinforcement-Learning-Explained/blob/master/DRL_13_14_Monte_Carlo.ipynb

[GPT Transcript](https://you.com/search?q=given+policy+function+%60policy%60%2C+how+do+I+write+a+f&cid=c1_f3c4aeef-3f2e-4ceb-85de-bc9e7eaf1fc0&tbm=youchat)
* This is just the code-relevant discussion. conceptual learning searches are not included.
