# Word Embeddings

Notes on Embedding [here](./embedding_notes.md)

## Prerequisite installs

### Download Gensim latest

`pip install --user gensim==3.8`

* note that some task instructions may have hte typo "genism." This is incorrect and should be `gensim`.

### Check that Keras version is 2.6.0

```
>>> import keras; keras.__version__
'2.6.0'
```

## Task 0 - Bag Of Words

<details>
    <summary>instructions</summary>


Write a function def bag_of_words(sentences, vocab=None): that creates a bag of words embedding matrix:

sentences is a list of sentences to analyze
vocab is a list of the vocabulary words to use for the analysis
If None, all words within sentences should be used
Returns: embeddings, features

embeddings is a numpy.ndarray of shape (s, f) containing the embeddings
s is the number of sentences in sentences
f is the number of features analyzed
features is a list of the features used for embeddings
You are not allowed to use genism library.

</details>

<details>
    <summary>test code</summary>

```

$ cat 0-main.py
#!/usr/bin/env python3

bag_of_words = __import__('0-bag_of_words').bag_of_words

sentences = ["Holberton school is Awesome!",
             "Machine learning is awesome",
             "NLP is the future!",
             "The children are our future",
             "Our children's children are our grandchildren",
             "The cake was not very good",
             "No one said that the cake was not very good",
             "Life is beautiful"]
E, F = bag_of_words(sentences)
print(E)
print(F)
$ ./0-main.py
[[0 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 1 0 0]
 [1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0]
 [1 0 0 0 2 0 0 1 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0]
 [0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 1 1]
 [0 0 0 1 0 0 1 0 0 0 0 0 0 0 1 1 1 0 1 0 1 1 1 1]
 [0 0 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0]]
['are', 'awesome', 'beautiful', 'cake', 'children', 'future', 'good', 'grandchildren', 'holberton', 'is', 'learning', 'life', 'machine', 'nlp', 'no', 'not', 'one', 'our', 'said', 'school', 'that', 'the', 'very', 'was']
$

```

</details>


<details>
    <summary>plan</summary>

 - [x] convert all words to lowercase



 - [x] if list, tuple, dict, then use " ".join(string to be concatenated)

   - [x]  else, skip that step

 - [x] make a list of " " delimitered words

 - [x] alphabetize the list

 - [x] create zeros arrray to be used in one-hot
    * yes it is sparse, yes it will feel bad; that is the point of this assignment.
    * zeros array will be shape (no_sentences, no_words_in_bag-of-words)

 - [ ] for each word_index in words, if the word is in sentance, put that inhdex of the onehot as 1
 - [ ] return that one-hot & alphebetized list of words
</details>

## Task 1 - TF-IDF

<details>
    <summary>instrucitons</summary>

Write a function def tf_idf(sentences, vocab=None): that creates a TF-IDF embedding:

sentences is a list of sentences to analyze
vocab is a list of the vocabulary words to use for the analysis
If None, all words within sentences should be used
Returns: embeddings, features
embeddings is a numpy.ndarray of shape (s, f) containing the embeddings
s is the number of sentences in sentences
f is the number of features analyzed
features is a list of the features used for embeddings


</details>

<details>
    <summary>test code</summary>

```
$ cat 1-main.py
#!/usr/bin/env python3

tf_idf = __import__('1-tf_idf').tf_idf

sentences = ["Holberton school is Awesome!",
             "Machine learning is awesome",
             "NLP is the future!",
             "The children are our future",
             "Our children's children are our grandchildren",
             "The cake was not very good",
             "No one said that the cake was not very good",
             "Life is beautiful"]
vocab = ["awesome", "learning", "children", "cake", "good", "none", "machine"]
E, F = tf_idf(sentences, vocab)
print(E)
print(F)
$ ./1-main.py
[[1.         0.         0.         0.         0.         0.
  0.        ]
 [0.5098139  0.60831315 0.         0.         0.         0.
  0.60831315]
 [0.         0.         0.         0.         0.         0.
  0.        ]
 [0.         0.         1.         0.         0.         0.
  0.        ]
 [0.         0.         1.         0.         0.         0.
  0.        ]
 [0.         0.         0.         0.70710678 0.70710678 0.
  0.        ]
 [0.         0.         0.         0.70710678 0.70710678 0.
  0.        ]
 [0.         0.         0.         0.         0.         0.
  1.        ]]
['awesome', 'learning', 'children', 'cake', 'good', 'none', 'machine']
$
```

</details>

<details>
    <summary>plan</summary>

 - [ ]check the `genism` library for TF-IDF function

   - [ ] if none, check for logarithm function.

     - [ ]if none, use numpy's logarithm

 - [ ] `sentences_using_this_word = np.zeros(length of words list)`
    * each index will be filled with an integer representing how many sentences have the word repesented by that position.
 - [ ] for sentence in sentences, count number of sentences each word in `words` is used in.
   - [ ] store in `sentences_using_this_word` by adding one to `sentences_using_this_word[word_num]`
   - [ ] `for word_num in range len(words)`
   - [ ] for sentence in sentences
     - [ ] if word in sentence

 - [ ] With that established, copy the code for the zeros matrix from the previous task
 - [ ] each cell will be filled with `TF * IDF` of the `word_in_question` for the sentence in question
   - [ ] `word_in_question = words[word_num]`
   - [ ] TF = number of times `word_in_question` is in sentence number sentenceindex
   - [ ] IDF = log(number of sentences / number of sentences that have `word_in_question`)
</details>

## Task 2, 4 - Word2Vec, FastText

These two tasks are adjascent beacuase they are functionally identical, aside from the manner of model to be crafted.

<details>
    <summary>Task 2 Instructions</summary>

Write a function `def word2vec_model(sentences, size=100, min_count=5, window=5, negative=5, cbow=True, iterations=5, seed=0, workers=1):` that creates and trains a `gensim` `word2vec` model:


* `sentences` is a list of sentences to be trained on

* `size` is the dimensionality of the embedding layer

* `min_count` is the minimum number of occurrences of a word for use in training

* `window` is the maximum distance between the current and predicted word within a sentence

* `negative` is the size of negative sampling

* `cbow` is a boolean to determine the training type; `True` is for `CBOW`; `False` is for `Skip-gram`

* `iterations` is the number of iterations to train over

* `seed` is the seed for the random number generator

* `workers` is the number of worker threads to train the model
Returns: the trained model


</details>


<details>
    <summary>Task 2 Test Code</summary>

*Note: gensim is not inherently deterministic and therefore your outputs may vary*

```


$ cat 2-main.py
#!/usr/bin/env python3

from gensim.test.utils import common_texts
word2vec_model = __import__('2-word2vec').word2vec_model

print(common_texts[:2])
w2v = word2vec_model(common_texts, min_count=1)
print(w2v.wv["computer"])
$ ./2-main.py
[['human', 'interface', 'computer'], ['survey', 'user', 'computer', 'system', 'response', 'time']]
[-3.0043968e-03  1.5343886e-03  4.0832465e-03  3.7239199e-03
  4.9583608e-04  4.8461729e-03 -1.0620747e-03  8.2803884e-04
  9.7367732e-04 -6.7797926e-05 -1.5526683e-03  1.8058836e-03
 -4.3851901e-03  4.7258494e-04  2.8616134e-03 -2.2246949e-03
  2.7494587e-03 -3.5267104e-03  3.0259083e-03  2.7240592e-03
  2.6110576e-03 -4.5409841e-03  4.9135066e-03  8.2884904e-04
  2.7018311e-03  1.5654180e-03 -1.5859824e-03  9.3057036e-04
  3.7275942e-03 -3.6502020e-03  2.8285771e-03 -4.2384453e-03
  3.2712172e-03 -1.9101484e-03 -1.8624340e-03 -5.6956144e-04
 -1.5617535e-03 -2.3851227e-03 -1.4313431e-05 -4.3398165e-03
  3.9115595e-03 -3.0616210e-03  1.7589398e-03 -3.4103722e-03
  4.7280011e-03  1.9380470e-03 -3.3873315e-03  8.4065803e-04
  2.6089977e-03  1.7012059e-03 -2.7421617e-03 -2.2240754e-03
 -5.3690566e-04  2.9577864e-03  2.3726511e-03  3.2704175e-03
  2.0853498e-03 -1.1927494e-03 -2.1565862e-03 -9.0970926e-04
 -2.8641665e-04 -3.4961947e-03  1.1104723e-03  1.2320089e-03
 -5.9017556e-04 -3.0594901e-03  3.6974431e-03 -1.8557351e-03
 -3.8218759e-03  9.2711346e-04 -4.3113795e-03 -4.4118706e-03
  4.7748778e-03 -4.5557776e-03 -2.2665847e-03 -8.2379003e-04
 -7.9581753e-04 -1.3048936e-03  1.9261248e-03  3.1299898e-03
 -1.9034051e-03 -2.0335305e-03 -2.6451424e-03  1.7377195e-03
  6.7217485e-04 -2.4134698e-03  4.3735080e-03 -3.2599240e-03
 -2.2431149e-03  4.4288361e-03  1.4923669e-04 -2.2144278e-03
 -8.9370424e-04 -2.7281314e-04 -1.7176758e-03  1.2485087e-03
  1.3230384e-03  1.7001784e-04  3.5425189e-03 -1.7469387e-04]
$
```
*Note: gensim is not inherently deterministic and therefore your outputs may vary*
</details>

<details>
    <summary>Task 4 Instructions</summary>

Write a function def `fasttext_model(sentences, size=100, min_count=5, negative=5, window=5, cbow=True, iterations=5, seed=0, workers=1):` that creates and trains a `genism` `fastText` model:


* `sentences` is a list of sentences to be trained on

* `size` is the dimensionality of the embedding layer

* `min_count` is the minimum number of occurrences of a word for use in training

* `window` is the maximum distance between the current and predicted word within a sentence

* `negative` is the size of negative sampling

* `cbow` is a boolean to determine the training type; `True` is for `CBOW`; `False` is for `Skip-gram`

* `iterations` is the number of iterations to train over

* `seed` is the seed for the random number generator

* `workers` is the number of worker threads to train the model

* Returns: the trained model

</details>

<details>
    <summary>Task 4 Test Code</summary>

*Note: gensim is not inherently deterministic and therefore your outputs may vary*

```
$ cat 4-main.py
#!/usr/bin/env python3

from gensim.test.utils import common_texts
fasttext_model = __import__('4-fasttext').fasttext_model

print(common_texts[:2])
ft = fasttext_model(common_texts, min_count=1)
print(ft.wv["computer"])
$ ./4-main.py
[['human', 'interface', 'computer'], ['survey', 'user', 'computer', 'system', 'response', 'time']]
[-2.3464665e-03 -1.4542247e-04 -3.9549544e-05 -1.5817649e-03
 -2.1579072e-03  4.5148263e-04  9.9494774e-04  3.2517681e-05
  1.7035202e-04  6.8571279e-04 -2.0803163e-04  5.3083687e-04
  1.2990861e-03  3.5418154e-04  2.1087916e-03  1.1022155e-03
  6.2364555e-04  1.8612258e-05  1.8982493e-05  1.3051173e-03
 -6.0260214e-04  1.6334689e-03 -1.0172457e-06  1.4247939e-04
  1.1081318e-04  1.8327738e-03 -3.3656979e-04 -3.7365756e-04
  8.0635358e-04 -1.2945861e-04 -1.1031038e-04  3.4695750e-04
 -2.1932719e-04  1.4800908e-03  7.7851227e-04  8.6328381e-04
 -9.7545242e-04  6.0775197e-05  7.1560958e-04  3.6474539e-04
  3.3428212e-05 -1.0499550e-03 -1.2412234e-03 -1.8492664e-04
 -4.8664736e-04  1.9178988e-04 -6.3863385e-04  3.3325219e-04
 -1.5724128e-03  1.0003068e-03  1.7905374e-04  7.8452297e-04
  1.2625050e-04  8.1183662e-04 -4.9907330e-04  1.0475471e-04
  1.4351985e-03  4.9145994e-05 -1.4620423e-03  3.1466845e-03
  2.0059240e-05  1.6659468e-03 -4.3319576e-04  1.3077060e-03
 -2.0228853e-03  5.7626975e-04 -1.4056480e-03 -4.2292831e-04
  6.4076332e-04 -8.5614284e-04  1.9028617e-04  6.0735084e-04
  2.6121829e-04 -1.0566596e-03  1.0602509e-03  1.2843860e-03
  7.9715136e-04  2.8305652e-04  1.9187009e-04 -1.0519206e-03
 -8.2213630e-04 -2.1762338e-04 -1.7580058e-04  1.2764390e-04
 -1.5695200e-03  1.3364316e-03 -1.5765150e-03  1.4802803e-03
  1.5476452e-03  2.1928034e-04 -9.3281898e-04  3.2964293e-04
 -1.0146293e-03 -1.3567278e-03  1.8070930e-03 -4.2649341e-04
 -1.9074128e-03  7.1639987e-04 -1.3686880e-03  3.7073060e-03]
$
```

*Note: gensim is not inherently deterministic and therefore your outputs may vary*
</details>



## Task 3 - Extract Word2Vec


### Resources

While this was [originally pretty easy](https://stackoverflow.com/questions/71044447/attributeerror-keyedvectors-object-has-no-attribute-get-keras-embedding), you can no longer do that, and should instead [replicate the one-functionality via this](https://github.com/piskvorky/gensim/wiki/Using-Gensim-Embeddings-with-Keras-and-Tensorflow)

I sucessfully (as far as I can tell) replicated this approach here: https://colab.research.google.com/drive/1P_uMUoSHx0YHAwb3VPEGINChbMhjQZl4?usp=sharing
