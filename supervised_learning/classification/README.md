# Classification

<details>
  <summary>The code contained within is classified. </summary>
   Just kidding.
</details>


* For a refresher on basic Pythonic classes, see [my previous repository explaining the subject](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/tree/main/python-classes).

# Task 0

This is essentially a refresher on basic Pythonic techniques.

For a no-spoilers sight of properly documented modules and classses, one can reference [one of my previous tutorial projects](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/blob/main/python-more_classes/1-rectangle.py)


# Task 1

Changes Task0 attributes from public to private.

Create getters for affected attributes.

* [Example](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/blob/main/python-more_classes/7-rectangle.py)

# Taask 2

Use sigmoid function on the *weighted* input array.

* multiply weights array with input array.

Incredible as always, [numpy has a tool](https://numpy.org/doc/stable/reference/generated/numpy.exp.html) to find `e` of an array

# Task 3

function `def cost(self, Y, A):`

* calculates cost/loss function.

* * uses logistic regression formula.

* recieves correct answers, and predicted answers (an array same shape as `self.__A`,) but **does not pull it's own self.__A**

use 1.0000001 - A instead of 1 - A

return cost
