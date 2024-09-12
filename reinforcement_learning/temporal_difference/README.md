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
