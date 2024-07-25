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

 - [ ] create zeros arrray to be used in one-hot
    * yes it is sparse, yes it will feel bad; that is the point
    * zeros array will be shape (no_sentences, no_words_in_bag-of-words)

 - [ ] for each word_index in words, if the word is in sentance, put that inhdex of the onehot as 1
</details>
