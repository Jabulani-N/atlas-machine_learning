# Transfer Learning

![Your meme is my meme now?](https://cdn.imgchest.com/files/345xcw8ne87.jpg)
* [it's more likely than you think](https://www.youtube.com/watch?v=FQM13HkEfBk&index=20&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF)


## [Introdtion to Transfer Learning](https://www.youtube.com/watch?v=FQM13HkEfBk&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=20:)

* you basically go to someone's github and download an open source implimentation of a neural network. both code and weights. look for something doesn't have to be the same as what you're loking to categotrize on.

You can get rid of the current output layer at the end, and replace it with your own, that'll output categories relevant to what you want

freeze the parameters of the network you downloaded, and only train the output layer that you inserted to replace the one that came with it.

Many deep learning frameworks support this, so just search around for one that allows you to do this. Ideally, find one that has "trainable parameter = 0" or "freeze = 1" so you can mess with whether or not you train the earlier layers, and you just train your custom output layer.


### "Precompute" AKA "Save-to-Disk" Method
 one trick that can be used on this situation is to save the computed output of the earlier layers, since they won't be getting trained. One can directly calculate what they'll behave like a function with an input and output.

- preferred for if you have a small training dataset

- if you have a larger ddata set (like a lot for a normal person's topic,) you can freeze fewer layers, and train off more thatn just the final layer.
- you can also make your own layers to replace multiple layers

The more pictures you have for training, the more layers you can afford to let get trained.
- at most, you can still even use the entire database as it's own initial weight.


## [Nuts and Bolts of AI Applications using Deep Learning by Andrew Ng](https://youtu.be/wjqaz6m42wU)
* [Slides](https://media.nips.cc/Conferences/2016/Slides/6203-Slides.pdf)

## [Comprehensive Hands-on Guide to Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
 Reading notes:

### Motivation for Transfer Learning

The idea behind transfer learning it to have a network utilize old knowledge when new training is performed. Similar to how humans and other logical beings can transfer knowledge from one lesson to the next, and dissimilar to deep learning training being done in isolation. It is not a new concept. It is synonymous with "Learning to Learn", "Knowledge Consolidation", and "Inductive Transfer", and "Generalization."


### Understading Transfer Learning

![Transfer Learning visual aid from the same article](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9GTEzcO8KxxrfutmtsPs3Q.png)

As no knowledge is retained in traditional learning, traditionally, it all starts from the ground up, and is only trained in the specific way intended for at the time. Work done today is of no help tomorrow, so to speak.

#### For example

Task `T1` is identifying features present in a restaurant; Task `T2` is identifying features in a park. There may be some overlap, but if we pull all of `T1`, it'll be biased towards identifying things as being resetaraunt-associated features. That said, some low level things like edges and corners might be transferrable. We can preserve the earlier layers that are likely to identify such low levels of patterns, and then our park `T2` will have a launching point to work with.

![mathematic description of the above](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*J5GsN8izqdRR4sdxt6mwEg.png)

![more of the mathematic description of the above](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*KgkqmR18XoFUkzmy-UjjKw.png)

Domain Vs Task

![Visual aid](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*vE8VO6isG0fSVYzgci3DuQ.png)

### Understanding Transfer LEarning Key Takeaways

What to transfer:
* how much of the source will be useful to the target task?

When to transfer:
* There may be situations where transferring acatually degrades performance, rather than imrpoving results.

How to transfer:
* Whne transfer has been confirmed, there are a selection of usable algorithms and techniquese to choose from. they are described later in the article.


### Transfer Learning Strategies

`placeholder for content`