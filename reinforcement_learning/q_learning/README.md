# q learning

## Installing OpenAI’s Gym

`pip install --user gym`


## Task 0

<details>
    <summary>Instructions</summary>

Write a function `def load_frozen_lake(desc=None, map_name=None, is_slippery=False):` that loads the pre-made `FrozenLakeEnv` evnironment from OpenAI’s `gym`:


* `desc` is either None or a list of lists containing a custom description of the map to load for the environment

* `map_name` is either None or a string containing the pre-made map to load

* Note: If both `desc` and `map_name` are `None`, the environment will load a randomly generated 8x8 map

* `is_slippery` is a boolean to determine if the ice is slippery

* Returns: the environment

</details>

<details>
    <summary>Test Code</summary>

```
$ cat 0-main.py
#!/usr/bin/env python3

load_frozen_lake = __import__('0-load_env').load_frozen_lake
import numpy as np

np.random.seed(0)
env = load_frozen_lake()
print(env.desc)
print(env.P[0][0])
env = load_frozen_lake(is_slippery=True)
print(env.desc)
print(env.P[0][0])
desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
print(env.desc)
env = load_frozen_lake(map_name='4x4')
print(env.desc)
$ ./0-main.py
[[b'S' b'F' b'F' b'F' b'F' b'F' b'F' b'H']
 [b'H' b'F' b'F' b'F' b'F' b'H' b'F' b'F']
 [b'F' b'H' b'F' b'H' b'H' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'H' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'H' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'H' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'F' b'G']]
[(1.0, 0, 0.0, False)]
[[b'S' b'F' b'H' b'F' b'H' b'F' b'H' b'F']
 [b'H' b'F' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'H' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'H' b'F' b'F' b'F' b'F' b'H']
 [b'F' b'F' b'F' b'F' b'F' b'H' b'F' b'H']
 [b'F' b'F' b'H' b'F' b'H' b'F' b'H' b'F']
 [b'F' b'F' b'H' b'F' b'F' b'F' b'F' b'G']]
[(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 8, 0.0, True)]
[[b'S' b'F' b'F']
 [b'F' b'H' b'H']
 [b'F' b'F' b'G']]
[[b'S' b'F' b'F' b'F']
 [b'F' b'H' b'F' b'H']
 [b'F' b'F' b'F' b'H']
 [b'H' b'F' b'F' b'G']]
$
```


</details>

[documentation for the frozen lake](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/).

* arguments: `gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True)`

## Task 1

<details>
    <summary>Instructions</summary>

Write a function `def q_init(env):` that initializes the Q-table:

* `env` is the `FrozenLakeEnv` instance

Returns: the Q-table as a `numpy.ndarray` of zeros

</details>

<details>
    <summary>Test Code</summary>

```
$ cat 1-main.py
#!/usr/bin/env python3

load_frozen_lake = __import__('0-load_env').load_frozen_lake
q_init = __import__('1-q_init').q_init

env = load_frozen_lake()
Q = q_init(env)
print(Q.shape)
env = load_frozen_lake(is_slippery=True)
Q = q_init(env)
print(Q.shape)
desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
Q = q_init(env)
print(Q.shape)
env = load_frozen_lake(map_name='4x4')
Q = q_init(env)
print(Q.shape)
$ ./1-main.py
(64, 4)
(64, 4)
(9, 4)
(16, 4)
$
```

</details>

<details>
    <summary>According to AI, this is a list of the possible attributes in a gym environment:</summary>


```
print("Observation Space:")
print("Type:", type(env.observation_space))
print("Number of States (n):", env.observation_space.n if hasattr(env.observation_space, 'n') else None)
print("Shape:", env.observation_space.shape if hasattr(env.observation_space, 'shape') else None)
print("Low:", env.observation_space.low if hasattr(env.observation_space, 'low') else None)
print("High:", env.observation_space.high if hasattr(env.observation_space, 'high') else None)
print("Data Type:", env.observation_space.dtype if hasattr(env.observation_space, 'dtype') else None)

# Accessing action space attributes
print("\nAction Space:")
print("Type:", type(env.action_space))
print("Number of Actions (n):", env.action_space.n if hasattr(env.action_space, 'n') else None)
print("Shape:", env.action_space.shape if hasattr(env.action_space, 'shape') else None)
print("Low:", env.action_space.low if hasattr(env.action_space, 'low') else None)
print("High:", env.action_space.high if hasattr(env.action_space, 'high') else None)
print("Data Type:", env.action_space.dtype if hasattr(env.action_space, 'dtype') else None)


```

</details>

