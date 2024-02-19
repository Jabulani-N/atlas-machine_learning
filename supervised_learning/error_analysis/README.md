# Error Analysis


## Task 0 Create Confusion

![example confusion matrix](https://www.dataschool.io/content/images/2015/01/confusion_matrix_simple2.png)

We'll be creating a [Confusion Matrix](https://machinelearningmastery.com/confusion-matrix-machine-learning/).

These are used evaluate performance. "That's what accuracy is for?" That's what I thought too, before I read that article and learned that merely looking at accuracy won't necassarily tell *where* the problems are located. That's like knowing a student's GPA, but not knowing which classes they excelled in and which were less successful. Furthermore, in the case of classification/prediction models, it may simply be a matter of "guessing C" so often it gets a reasonably high score merely by the frequency of C being correct, and actually has no idea how to compute the answer.

<p align="center"><b>"The confusion matrix shows the ways in which your classification model is confused when it makes predictions."</b></p>

[Confusion Matrix Terminology](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)

[Example confusion matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

`confusion` is matrix shaped `(classcount, classcount)`.

* confusion[0] = list of what happened when it was actually class 0

[numpy argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html) will compare the contents of an array, elementwise, perpendicular to the axis you specify.
```
>>> a = np.arange(6).reshape(2,3) + 10
>>> a
array([[10, 11, 12],
       [13, 14, 15]])
>>> np.argmax(a)
    //no array specified, compares for the largest overall item position
5
>>> np.argmax(a, axis=0)
array([1, 1, 1])
>>> np.argmax(a, axis=1)
array([2, 2])
```
we can use this by only looking at one "row" of `labels` at a time, to use argmax to find which index of that row has the 1.
That's the 0th dimension in our confusion array. The 1st dimension is the same thing bbut with `logits`.

# Task 1 Sensitivity

[Sensitivity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity): ability to predict `true positives` (as opposed to false positive.) If the correct answer is "A," Sensitivity is the chances the model will predict "A."