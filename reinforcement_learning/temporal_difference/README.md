# Temporal Difference

## Resources

[RL Course by David Silver - Lecture 4: Model-Free Prediction](https://www.youtube.com/watch?v=PnHCvfgC_ZA)

[RL Course by David Silver - Lecture 5: Model Free Control](https://www.youtube.com/watch?v=0g4j2k_Ggc4&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ&index=6)

[Simple Reinforcement Learning: Temporal Difference Learning
](https://medium.com/@violante.andre/simple-reinforcement-learning-temporal-difference-learning-e883ea0d65b0) (medium member only)

[On-Policy TD control methods](https://paperswithcode.com/methods/category/on-policy-td-control)

### [Monte Carlo Policy evaluation](https://www.geeksforgeeks.org/monte-carlo-policy-evaluation/)

Evaluation Paent formula

* ![evaluation parent formula](https://quicklatex.com/cache3/30/ql_456afe0ff1ee40f5503c31f1dfb79030_l3.svg)
  * `V` is "value" of state `s` under policy `π`.
  * `G` = average return of that state `s` using that policy.
  * `N(s)` = number of times state `s` is visited during episode.
  * return is `V(s)` value of that state `s`

That is the general logic we'll be following to create the monte carlo policy evaluation.

![images of respective Q and V tables](./img/Q_and_V-tables-cropped.jpg)

## General background and terms

`V` = value estimate = value estimate table

`policy` = π = policy function.
* the contents of `policy` are not relevant for the calculations we'll be performing here, as our job is to evaluate the ersults that policy created.

## Task 1 - TD(λ)

<details>
    <summary>Instructions</summary>

Write the function `def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):` that performs the TD(λ) algorithm:


* `env` is the openAI environment instance

* `V` is a `numpy.ndarray` of shape `(s,)` containing the value estimate

* `policy` is a function that takes in a state and returns the next action to take

* `lambtha` is the eligibility trace factor

* `episodes` is the total number of episodes to train over

* `max_steps` is the maximum number of steps per episode

* `alpha` is the learning rate

* `gamma` is the discount rate

* Returns: `V`, the updated value estimate

</details>

<details>
    <summary>Test Code</summary>


```

$ cat 1-main.py
#!/usr/bin/env python3

import gym
import numpy as np
td_lambtha = __import__('1-td_lambtha').td_lambtha

np.random.seed(0)

env = gym.make('FrozenLake8x8-v0')
LEFT, DOWN, RIGHT, UP = 0, 1, 2, 3

def policy(s):
    p = np.random.uniform()
    if p > 0.5:
        if s % 8 != 7 and env.desc[s // 8, s % 8 + 1] != b'H':
            return RIGHT
        elif s // 8 != 7 and env.desc[s // 8 + 1, s % 8] != b'H':
            return DOWN
        elif s // 8 != 0 and env.desc[s // 8 - 1, s % 8] != b'H':
            return UP
        else:
            return LEFT
    else:
        if s // 8 != 7 and env.desc[s // 8 + 1, s % 8] != b'H':
            return DOWN
        elif s % 8 != 7 and env.desc[s // 8, s % 8 + 1] != b'H':
            return RIGHT
        elif s % 8 != 0 and env.desc[s // 8, s % 8 - 1] != b'H':
            return LEFT
        else:
            return UP

V = np.where(env.desc == b'H', -1, 1).reshape(64).astype('float64')
np.set_printoptions(precision=4)
env.seed(0)
print(td_lambtha(env, V, policy, 0.9).reshape((8, 8)))

$ ./1-main.py
[[-0.774  -0.8288 -0.8065 -0.7214 -0.6344 -0.548  -0.4152 -0.4393]
 [-0.7643 -0.7553 -0.776  -0.6273 -0.4213 -0.4698 -0.3294 -0.4009]
 [-0.8883 -0.8796 -0.9215 -1.     -0.669  -0.37   -0.2522 -0.4788]
 [-0.9091 -0.907  -0.9199 -0.9078 -0.8009 -1.     -0.3478 -0.1532]
 [-0.8774 -0.9579 -0.9336 -1.     -0.7624 -0.8244 -0.6629 -0.1192]
 [-0.9308 -1.     -1.      0.6361 -0.7978 -0.715  -1.      0.3673]
 [-0.9145 -1.     -0.5743 -0.0703 -1.     -0.3774 -1.      0.9231]
 [-0.8599 -0.8444 -0.7795 -1.      1.      0.4657  0.5018  1.    ]]
$


```

</details>

Value Function Update: The value function estimate `V(s)` is updated for all states s according to the following rule:

`V(s) = V(s) + α * δ * e(s)`
* `e(s)` = eligibility trace
  * initialized at 0 for each state
  * shares a shape with V(s) because they are both graphs of values assigned to each state
  * Eligibility Trace Update: The eligibility trace `e(s)` is updated for all states `s` according to the following rule:


        If s = s_t (the current state), then e(s) = e(s) + 1

        Else, e(s) = γ * λ * e(s)


       * where `γ` is the discount factor and `λ` is the trace decay parameter.
       * `γ` = gamma = discount factor = discount rate
       * `λ` = lambda AKA lambtha (because lambda is a protected class in Python)
       * I'm currently using the current state condition in my code, so lambtha bay or may not be used
         * ... although, I could theoretically run a different loop to just calculate all of these
         * I may actually do both of them in series, since all e's start at 0 until we add the 1.
           * this is what I did.

This blog post has a fun (~~formula~~)filled section going over eligibility traces.
* search `Eligibility traces and who the hell is to blame for this reward`

where `α` is the learning rate, and `δ` is the TD error, defined as:

`δ = r + γ * V(s') - V(s)`

* `δ` = delta = TD error
* `r` = reward
* `γ` = gamma = discount factor
* `V(s')` = estimated value of next state
  * this is what we already have stored at the time.
  * I believe this is before we've actually updated that section of the V table
* `V(s)` = estimated value of current state
  * is this simply using the value we already have too?
    * and then we update it based on error function?


## Task 2 - SARSA(λ)

<details>
    <summary>Instructions</summary>

Write the function `def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):` that performs SARSA(λ):


* `env` is the openAI environment instance

* `Q` is a `numpy.ndarray` of shape `(s,a)` containing the Q table

* `lambtha` is the eligibility trace factor

* `episodes` is the total number of episodes to train over

* `max_steps` is the maximum number of steps per episode

* `alpha` is the learning rate

* `gamma` is the discount rate

* `epsilon` is the initial threshold for epsilon greedy

* `epsilon_decay` is the decay rate for updating epsilon between episodes

* `min_epsilon` is the minimum value that epsilon should decay to

* Returns: `Q`, the updated Q table

</details>

<details>
    <summary>Test Code</summary>

```

$ cat 2-main.py
#!/usr/bin/env python3

import gym
import numpy as np
sarsa_lambtha = __import__('2-sarsa_lambtha').sarsa_lambtha

np.random.seed(0)
env = gym.make('FrozenLake8x8-v0')
Q = np.random.uniform(size=(64, 4))
np.set_printoptions(precision=4)
env.seed(0)
print(sarsa_lambtha(env, Q, 0.9))
$ ./2-main.py
[[0.5758 0.5842 0.5899 0.6206]
 [0.5937 0.5902 0.6322 0.5816]
 [0.5466 0.6339 0.5825 0.5711]
 [0.5686 0.6361 0.5396 0.5723]
 [0.5782 0.6011 0.7    0.5844]
 [0.5974 0.5891 0.757  0.5919]
 [0.5033 0.7233 0.5643 0.5999]
 [0.5459 0.7341 0.5168 0.6089]
 [0.6082 0.6041 0.5821 0.5878]
 [0.6096 0.5729 0.5975 0.6009]
 [0.5806 0.6021 0.5897 0.5885]
 [0.5037 0.4874 0.4872 0.6189]
 [0.5125 0.5903 0.575  0.6992]
 [0.6521 0.7526 0.6523 0.5856]
 [0.7358 0.4134 0.6052 0.5389]
 [0.3303 0.4083 0.7277 0.3076]
 [0.6098 0.6291 0.634  0.6343]
 [0.6194 0.5935 0.6114 0.6201]
 [0.5926 0.5317 0.5195 0.5672]
 [0.2828 0.1202 0.2961 0.1187]
 [0.4376 0.3981 0.3933 0.5932]
 [0.6894 0.6587 0.79   0.5926]
 [0.6692 0.7851 0.6575 0.6771]
 [0.4706 0.7876 0.5482 0.4909]
 [0.664  0.6424 0.6637 0.6378]
 [0.6345 0.5687 0.6038 0.638 ]
 [0.6831 0.664  0.6374 0.6621]
 [0.6189 0.704  0.6147 0.5325]
 [0.6945 0.6243 0.6423 0.6109]
 [0.8811 0.5813 0.8817 0.6925]
 [0.7535 0.6997 0.825  0.7131]
 [0.6585 0.8962 0.447  0.5378]
 [0.6998 0.6437 0.6951 0.7129]
 [0.7405 0.6738 0.6397 0.7039]
 [0.7222 0.7166 0.7424 0.6897]
 [0.8965 0.3676 0.4359 0.8919]
 [0.8405 0.7678 0.2192 0.7594]
 [0.7136 0.9139 0.3553 0.7366]
 [0.2221 0.743  0.4957 1.0541]
 [1.0156 0.6719 0.7078 0.3995]
 [0.6121 0.6495 0.7227 0.7908]
 [0.9755 0.8558 0.0117 0.36  ]
 [0.73   0.1716 0.521  0.0543]
 [0.2    0.0185 0.8387 0.2239]
 [0.3915 0.9155 0.7215 0.0318]
 [0.2311 0.8802 0.6549 0.2991]
 [0.9342 0.614  0.5356 0.5899]
 [1.0533 0.3119 0.5305 0.3138]
 [0.4295 0.3969 0.4392 0.4893]
 [0.2274 0.2544 0.058  0.4344]
 [0.3118 0.5476 0.3778 0.2648]
 [0.0582 0.0672 0.7587 0.4519]
 [0.5366 0.8967 0.9903 0.2169]
 [0.6631 0.3552 0.1426 0.8345]
 [0.32   0.3835 0.5883 0.831 ]
 [0.7522 1.3151 0.4288 0.88  ]
 [0.3564 0.3988 0.3986 0.3472]
 [0.4117 0.4306 0.3115 0.2766]
 [0.4533 0.0257 0.2221 0.4247]
 [0.3742 0.4636 0.2776 0.5868]
 [0.8157 0.1175 0.5174 0.1321]
 [0.6973 0.3961 0.5654 0.1833]
 [0.1448 0.4881 0.3556 0.9404]
 [0.7653 0.7487 0.9037 0.0834]]
$

```

</details>

[this person](https://github.com/farkoo/N-Step-SARSA-Lambda-SARSA/blob/master/WindyGridworld.py) has an application that seems to utilize the same logic we'll want to use in the funciton `def n_step_sarsa(env, n, alpha, gamma, epsilon, num_episodes):`.