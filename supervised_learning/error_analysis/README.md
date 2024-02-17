# Error Analysis


## Task 0 Create Confusion

We'll be creating a [Confusion Matrix](https://machinelearningmastery.com/confusion-matrix-machine-learning/).

These are used evaluate performance. "That's what accuracy is for?" That's what I thought too, before I read that article and learned that merely looking at accuracy won't necassarily tell *where* the problems are located. That's like knowing a student's GPA, but not knowing which classes they excelled in and which were less successful. Furthermore, in the case of classification/prediction models, it may simply be a matter of "guessing C" so often it gets a reasonably high score merely by the frequency of C being correct, and actually has no idea how to compute the answer.

<p align="center"><b>"The confusion matrix shows the ways in which your classification model is confused when it makes predictions."</b></p>

[Confusion Matrix Terminology](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)