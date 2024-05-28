# Hidden Markov Models

## Task 0

<details>
    <summary> Instructions</summary>

Write the function `def markov_chain(P, s, t=1):` that determines the probability of a markov chain being in a particular state after a specified number of iterations:

`P` is a square 2D numpy.ndarray of shape `(n, n)` representing the transition matrix

`P[i, j]` is the probability of transitioning from state i to state j
`n` is the number of states in the markov chain

* `s` is a numpy.ndarray of shape `(1, n)` representing the probability of starting in each state

* `t` is the number of iterations that the markov chain has been through

Returns: a `numpy.ndarray` of shape `(1, n)` representing the probability of being in a specific state after `t` iterations, or `None` on failure


</details>

You'll be able to find the chance of any given position via dot product of `s` and `P`.



## Task 1

<details>
    <summary> Instructions </summary>

    Write the function def regular(P): that determines the steady state probabilities of a regular markov chain:

P is a is a square 2D numpy.ndarray of shape (n, n) representing the transition matrix
P[i, j] is the probability of transitioning from state i to state j
n is the number of states in the markov chain
Returns: a numpy.ndarray of shape (1, n) containing the steady state probabilities, or None on failure

</details>


### Resources

Steady State is the term used in the curriculum, but [it seems to be the same as](https://math.stackexchange.com/questions/9325/equilibrium-distribution-steady-state-distribution-stationary-distribution-and) "equilibrium" and "stationary" states.

Steady state (stationary [in this text](https://towardsdatascience.com/markov-chain-analysis-and-simulation-using-python-4507cee0b06e)) is referred to as `pi` or `π` and equals:

![steady state formula](https://miro.medium.com/v2/resize:fit:396/format:webp/1*zbWBjSC1Xba9zODUDMkftA.png)

[This](https://stackoverflow.com/questions/52137856/steady-state-probabilities-markov-chain-python-implementation) is one python code application example I found.

## Task 2

### Resources

Absorbing:

[![absorbing chain example](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Drunkard%E2%80%99s_walk.svg/1920px-Drunkard%E2%80%99s_walk.svg.png)](https://en.wikipedia.org/wiki/Absorbing_Markov_chain)

* [it is absorbing if every given position has a chance of leading to situation where you cannot escape a select set of positions](https://en.wikipedia.org/wiki/Absorbing_Markov_chain)

* "[Absorbing **State**: a state `i` is called absorbing if it is impossible to leave this state. Therefore, the state [position on the matrix] '`i`' is absorbing if `p`<sub>`ii`</sub>` = 1` and `p`<sub>`ij`</sub>` = 0` for `i ≠ j`. If every state can reach an absorbing state, then the Markov chain is an absorbing Markov chain.
](https://www.datacamp.com/tutorial/markov-chains-python-tutorial)"

  * This basically means the matrix has at least one position `p`<sub>`ii`</sub>` = 1`, and every position has a chance of eventually landing there.

    * [`numpy.diagonal(matrix)`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html) can tell you the value of the diagonal of `matrix` if 2D
    * [`numpy.diag(matrix, positions)`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html) can help us judge every single other value by doing every possible value of `positions` except `0`(diagonal that is supposed to be 1)
      * alternatively, we can do diag for everything possible, and make it check for `0`s everywhere except when positions=0, in which case we check for the return to be filled with `1`s

we can tell a matrix is absorbing, first and foremost, if *any* diagonal value is at 1, as that represents being forced back into itself, or being forced to never arrive there, which is also absorbing.

* **this gets cancelled** if any position cannot land  at that position (or another absorbing position) within a finite number of steps.

  * essentially, this seems to mean that every position just needs to have access to a `1` on a diagonal. Must either be a 1, or 