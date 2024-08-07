# Transfer Learning

![Your meme is my meme now?](https://cdn.imgchest.com/files/345xcw8ne87.jpg)
* [it's more likely than you think](https://www.youtube.com/watch?v=FQM13HkEfBk&index=20&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF)

# Table of Contents

- [Introdtion to Transfer Learning](#introdtion-to-transfer-learning)
- [Nuts and Bolts of AI Applications](#nuts-and-bolts-of-ai-applications-using-deep-learning-by-andrew-ng)
- [Comprehensive Hands on Guide](#comprehensive-hands-on-guide-to-transfer-learning)
- [Potential Pitfalls](#potential-pitfalls)
- [Large File Removal](#large-file-removal)


## [Introdtion to Transfer Learning](https://www.youtube.com/watch?v=FQM13HkEfBk&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=20:)

![Trasfer Learning: idea image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Ww3AMxZeoiB84GVSRBr4Bw.png)

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

![Domain vs Task Visual aid](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*vE8VO6isG0fSVYzgci3DuQ.png)

### Understanding Transfer Learning Key Takeaways

What to transfer:
* how much of the source will be useful to the target task?

When to transfer:
* There may be situations where transferring acatually degrades performance, rather than imrpoving results.

How to transfer:
* Whne transfer has been confirmed, there are a selection of usable algorithms and techniquese to choose from. they are described later in the article.


### Transfer Learning Strategies

Ideal strategies vary with the domain, task, and data availablity. This is one example of the logic one might take after deciding to utilize transfer learning:

![Strategy Selection Floawchart](https://miro.medium.com/v2/resize:fit:1222/format:webp/1*mEHO0-LifV7MgwXSpY9wyQ.png)
* [source](https://www.cse.ust.hk/~qyang/Docs/2009/tkde_transfer_learning.pdf)

* **Inductive Transfer Learning** is used when source and target domains are the same, meaining same sort of data will be looked at, but the tasks (what we we want to do with the data,) will be different.
  * Use the bias of the source (towards things being in the reelvant domain) to improve target task's performance.

* **Unsupervised Transfer Learning** is similar to the previous: same domain, different task.
  * Used when there is little training data in both source and target tasks.
*  **Transductive Transfer Learning** is for similar tasks, but different domains.
*  If the source domain has much labled data and the target domain has none.

This table summarizes this logic:

![Transfer Learning Strategy logic table](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*ZEJeJS06czdyPwov5EbCuQ.png)

#### What to transfer

**Instance transfer**: Usually, the ideal would be to reuse source domain knowledge. This is not always feasible; instead certian instanes from the source domain can be reused, alongside data from target.

* modifications like AdaBoost by Dai, etc. help use training instances from source domain into target task.

**Feature-representation transfer** minimizes domain divergence and error rates by identifying feature representations that can be utilized from source domain in target domain. May be supervised or unsupervised based on availability of labeled data.

**Parameter Transfer** assumes related tasks wil share some parmeters or hyperparameters, and has us give additional weight to target domain.

**Rational-knowledge Transfer** attempts to handle non-IID data, meaning data where each datum is related to other data. Social network data utilizes this.

The "transfer learning strategies" and "what to transfer" relate as according to this table:

![TL strategies vs what to transfer table](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xK81ohzG-tLRKVexowUvgw.png)

### Transfer Learning for Deep Learning

![DL banner image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nMEcHwB18CTqfY0mTd-s1g.png)

Deep Learning models represent "inductive learning." Inductive learning algorithms infer a mapping from a set of training examples. With classification, it maps input features that result in class labels. They make assumptions based on the training data called "inductive bias" in order to apply the lessons of training to unseen entities.

These inductive biases can be characterized by factors, including "the hypothesis space it restricts to and the search process ythrough the hypothesis space." They impact how and what is learned by the model.


Inductive transfer tecniquesa use these inductive biases via a number of ways, such narrowing hypothesis space, making adjustments to search process itself.

![image example of the above](https://miro.medium.com/v2/resize:fit:1210/format:webp/1*yjBaWnApTg_4Mz1xrHBJZg.png)

#### Deep Transfer Learning Strategies

There is a need for speed among deep models. Pre-trained networkds/models are part of the solution, the basis of "deep transfer learning."

One method of using these models is described as "**Off-the-shelf Pre-trained Models as Feature Extractors**." Essentially, we take an entire model, and then don't use it's final (labelling) layer.

![visual example of off the shelf model as feature extractor](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qfQ3hmHLwApXZBN-A85r8g.png)

* "The key idea here is to just leverage the pre-trained model’s weighted layers to extract features but not to update the weights of the model’s layers during training with new data for the new task."

AlexNet without it's final classifiation layer can transform images from a new domain and get its features for a new task. Doing this is popular.

They're "surprisingly effective":

![efficacy of off-the-shelf models as feature extractors](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cdqFwsX3ol0WPfkqDEfKiA.png)

![closeup of above](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*d__1oSbHOSEq6m4bFflE5g.png)

Another approach is **Fine-tuning Off-the-shelf Pre-trained Models**, a more involved technique were we select previous layers to retrain, alongiside replacing the model's final layer. Deep neural networks generally have iintial layers to capture generic features, and later layers are specified to the identification task they were trained for. This method freezes the early layers, which will be sufficiently trained for the current new task, and retrains the rest.

![freezing image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*AUI4rH8_tbb7x4xkBsHu2Q.png)

**Pre-trained Models** are mercifully available, with open source models of high quality being commonly available in the form of the parameters/weights they were trained into having. Keras even has an interface for downloading some more popular models.

Some computer vision models are

* [VGG-16](https://www.kaggle.com/keras/vgg16/home)
* [VGG-19](https://www.kaggle.com/keras/vgg19/home)
* [Inception V3](https://arxiv.org/abs/1512.00567)
* [XCeption](https://arxiv.org/abs/1610.02357)
* [ResNet-50](https://www.kaggle.com/keras/resnet50/home)


Some word embedding models, which may help for some natural language processing (nlp) related tasks are

* [Word2Vec](https://en.wikipedia.org/wiki/Word2vec)
* [GloVe](https://nlp.stanford.edu/projects/glove/)
* [FastText](https://fasttext.cc/)

these represent progress towarfds nlp transfer learning

* [Universal Sentence Encoder by Google](https://arxiv.org/abs/1803.11175)
* [Bidirectional Encoder Representations from Transformers (BERT) by Google](https://arxiv.org/abs/1810.04805)

### Types of Deep Transfer Learning

## Potential Pitfalls

Be sure you have `scipy` installed: `pip install scipy`

## Large File Removal

If you accidentally attempt to push a created model to Git, causing `Large files detected` becuase `this exceeds GitHub's file size limit of 100.00 MB`, follow [these instrucitons](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) **if you have not made any more commits** yet.

**If you have made other commits** since the oversized file commit, you'll use [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/).
* I was not able to have it work when following the instructions provided on the BFG website. To clean my repo, I instead had to put (a copy of) the executable BFG ".jar" file to the top directory of the local repository, and then do [`bfg --delete-files YOUR-FILE-WITH-SENSITIVE-DATA`](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
  * replace `bfg` with whatever the name of the actual item has
    * for example, mine was `java -jar bfg-1.14.0.jar --delete-files NAME_OF_HUGE_FILE`
* If BFG cannot find any file and asks if the repo needs to be packed, consider [`git gc`](https://stackoverflow.com/questions/61769785/warning-no-large-blobs-matching-criteria-found-in-packfiles-does-the-repo-ne)
