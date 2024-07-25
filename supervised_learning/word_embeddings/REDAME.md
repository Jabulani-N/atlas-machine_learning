# Word Embeddings

Notes on Embedding [here](./embedding_notes.md)

## Task 0

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

## Task 1

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
  0.        ]]
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