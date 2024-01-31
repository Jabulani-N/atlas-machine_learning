# Classification

<details>
  <summary>The code contained within is classified. </summary>
   Just kidding.
</details>


* For a refresher on basic Pythonic classes, see [my previous repository explaining the subject](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/tree/main/python-classes).

The `Neuron` class simulates a single neuron recieving weighted inputs to learn. The `NeuralNetwork` class simulates a nework of 2 layers of neurons with weighted inputs.

# Task 0

This is essentially a refresher on basic Pythonic techniques.

For a no-spoilers sight of properly documented modules and classses, one can reference [one of my previous tutorial projects](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/blob/main/python-more_classes/1-rectangle.py)


# Task 1

Changes Task0 attributes from public to private.

Create getters for affected attributes.

* [Example](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/blob/main/python-more_classes/7-rectangle.py)

# Task 2 Neuron Forward Propagation

Use sigmoid function on the *weighted* input array.

* multiply weights array with input array.

Incredible as always, [numpy has a tool](https://numpy.org/doc/stable/reference/generated/numpy.exp.html) to find `e` of an array

# Task 3 - Cost Function

function `def cost(self, Y, A):`

* calculates cost~~/loss~~ function.

  * uses logistic regression formula
    * [video on logistic regression](https://www.youtube.com/watch?v=hjrYrynGWGA&list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0&index=9)
      * logistic regression of array x = `ŷ = sigmoid(W(transpose)x + b)`
        * array(transpose), aka array^T, is a mathematic operation that [numpy has built in](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
    * [subsequent video on using logistic regression for loss calculation and cost calculation](https://www.youtube.com/watch?v=SHEPb1JHw5o&list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0&index=9).
      * **loss** function = `(ŷ - y(correct)) ^ 2 / 2`
      *  when `yi = y superscript i` and `ŷi = ŷ superscript i`, **cost** function = cost = `J(w, b) = - 1 / m * (sum{i = 1 to m}(yi * log(ŷi) + (1 - yi) * (log(1 - ŷi)))`
         *  m = shape of Y = `numpy.shape(Y) = m`
    * Note to self: when reaching the gradiant descent task, use this [resource video](https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&index=1) (long.)

* recieves correct answers, and predicted answers (an array same shape as `self.__A`,) but **does not pull it's own self.__A**

use 1.0000001 - A instead of 1 - A

return cost

# Task 4 - Evaluate Neuron

Create pubic method `def evaluate(self, X, Y):`.

* Returns both prediction and cost

~~Because we want 0.5 to equal 1, and anything below to be 0, we can double everything in the cell, and then truncate. everything 0.5 and up will be 1 or more, truncating to 1. everything else is 0.999999999 or less, truncating to 0.~~
Numpy has an "[is greater than or equal to](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html)" built-in function, and it's boolean result [can be converted to an array of integers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html).

# Task 5

create public method `def gradient_descent(self, X, Y, A, alpha=0.05):` to [calculate Gradiant Descent](https://www.youtube.com/watch?v=uJryes5Vk1o&list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0&index=12). This does not return anyting.

* alpha = α = learning rate.
* Instad of returning, this method updates self.__W and self.__b by a single step of gadiant descent.
  * each step of gradiant descent does
    * note: `x :=` means "the updated value of x ="...
    * `w := w - α * d/dW(J(W))`
      * J(W,b) = cost function, so just derive it with te respect to W
    * `b := b - α * d/db(J(b))`
  * Thankfully, [**numpy has a gradient method built in**](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html)

I wasn't able to use the above, though it provides useful background knowledge, so I ended up using the exact calculations provided [here](https://www.analyticsvidhya.com/blog/2018/10/introduction-neural-networks-deep-learning/). search "derivative of the parameters," and it'll list the calculations you need.

* I did not fully understand this part, so further research and reading of that above source may be appropriate.

# Task 6

create public method `def train(self, X, Y, iterations=5000, alpha=0.05):`, which does the same thing as 5, except you can tell it how many times to repeat.

You'll have to use your own A, though.

# Task 7

updates the `train` method created in task 6
* from `def train(self, X, Y, iterations=5000, alpha=0.05):`
* to `def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):`

`Verbose`, `Step`
* boolean
* decides wether we print some words after every `step` counts of training.
* Easy

`Graph`, `Step`
* boolean
* decides wether we display a graphical representation of every `step` counts of training.
* **note to self**: details go here in subsequent bullet points

`Step`
* only verify the `step` input if either `verbose` or `graph` is true.
* needs to be between `0` and `iterations`

To ensure the completion of a minimum viable product, the `graph` functionality of this class has been left incomplete, until other, more vital tasks are completed.

# Task 8 Neural Network

attributes ending with 1 are related to the hidden layer
attributes ending with 2 are related to the output layer
    if you really wanted, you could make more hiddedn layers before output layer.
        this would be done via making a new set of attributes with 3 for output layer, and 2 would be hidden layer 2.

The output layer recieves the hidden layer as it's input, so there are `nodes` number of inputs for the output layer. in the same way, however many layers you have, each layer will have as many inputs as the previous layer has outputs.

# Task 9

Privatizes the attributes created in task 8
```

self.pub = "im a public attribute!"
self.__priv = "im a private attribute!"

...

@property
def priv(self):
    """I'm a getter"""
    return self.__priv
```

# task 10

creates public method `def forward_prop(self, X):`.

This is for the entire network to propagate once.

Numpy can recieve arrays just as well as it recieves integers, so one can use the same input-output logic as used in Task 2.

# Task 11 NeuralNetwork Cost

Adds public method `def cost(self, Y, A):`. This calculates the cost of a single forward propagation.

* Y = correct answer
* A = forward prop's answer.

See Task 3 for formulae and detials.

* Currently identical to Task 3, as there is no change in formulae nor implimentation

# Task 12 Evaluate Neural Network

Effectively identical to Task 4, creataing `def evaluate(self, X, Y):`.
Be sure to remember that forward prop in our Neural Network tasks returns two items. You only want the final `A2` output to be evaluated. We don't care about the first one, A1

# Task 13 NeuralNetwork Gradient Descent

performs Gradient Descent via `def gradient_descent(self, X, Y, A1, A2, alpha=0.05):`.

* alpha is learning rate.

The idea will be the same as Task 5
* pay attention to what is relevant input for eacah layer, and what is output. This is important for how layer 2's input comes from layer 1's outputs.

Because we are updating two layers, we'll need to update both sets of weights and biases.

# Tasks 14 Train Neural Network

Same idea as Task 6.

creates public method `def train(self, X, Y, iterations=5000, alpha=0.05):`, performing `iterations` `forward propogation`s and `gradient descent`s. Finally, returns evaluation afterwards.

This requires task 13 to work in order to work, being  dependant on `gradient descent`.

# Task 15 Upgrade Train NeuralNetwork

improves Tas k14 with `def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):`.

This improved method has the option to display a report every `step` iterations. See Task 7.

# Task 16 DeepNeuralNetwork

Creates class `DeepNeuralNetwork` iniitialized via `def __init__(self, nx, layers):`.

elementwise type checking: https://stackoverflow.com/questions/6009589/how-to-test-if-every-item-in-a-list-of-type-int

Of note:

`weights`: A dictionary to hold all weights and biased[sic] of the network. Upon instantiation:
* The weights of the network should be initialized using the `He et al.` method and saved in the `weights` dictionary using the key `W{l}` where `{l}` is the hidden layer the weight belongs to
  * [He et al. initialization demonstrated](https://github.com/fanghao6666/neural-networks-and-deep-learning/blob/master/py/Initialization.py). what it has as `parameters` is what we call `weights` in this project. **This will not work if copy-pasted**. You must instead understand the logic of what it's doing.
    * Inside the for loop, you can see the way it's using random with the number of nodes in current layer `l`, and the number of nodes in *the layer before* the current layer, `l - 1`.
      * This provided setup **does not** consider layer 0. We need to fix that.
      * layer 0 ALSO needs an input layer. it's input layer is the input itself, which has `nx` elements. We use `nx` for the number of how many elements are in the layer before it.
* The biases of the network should be initialized to 0’s and saved in the weights dictionary using the key `b{l}` where `{l}` is the hidden layer the bias belongs to

### Potential pitfalls

**You will not 1-1 copy the reference linked above**

When the logic of my loop had the ability to double-assign a value to dictionary term `W1`, that resulted in a wong answer. When reordering my code to use an if/else for whether it was the first slot or not, this actually change my output to the correct value.

# Task 17

This merely changes the public attributes to private, and creates relevant getters.

# Task 18 DeepNeuralNetwork Forward Propagation
