# Natural Language Processing

## Word Embedding

[genism python library](https://radimrehurek.com/gensim/index.html) is the word2vector library that has the google model that trained on this stuff from the springboard article.

https://www.springboard.com/blog/data-science/introduction-word-embeddings/

`king-man+woman≈queen`

Machines can learn the relationship between words of a language in the form of real vector relationships. For example, these vectors are the relationship between country names and the names of their capitals:

![vector relationships of words: country and capital visual](https://www.springboard.com/blog/wp-content/uploads/2017/08/country-Copy.png)

They can even learn the "direction" of gendered terms:

![gendered terms represented via vector](https://www.springboard.com/blog/wp-content/uploads/2017/08/relations-Copy.png)

![word embedding visual aid](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/7/a2fa719214e8c81107842b9fcd97defd08ba3d82.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240722%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240722T185534Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6a7db32f9f28b707f5d6c4f6acac163e58bdf43df3badfcdba96515e17cfa7d5)

This even applies across languages:

![bilingual graph comparison](https://www.springboard.com/blog/wp-content/uploads/2017/08/mt-Copy.png)

[**Bag of Words Intuition**](https://www.youtube.com/watch?v=IKgBLTeQQL8&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm&index=6) is essentially recording the important words as a chart (or one-hot matrix) that tells how many instances of each "feature" (important term) are in the sentences. It is less good for analysis on large sentences/paragraphs, but can be used for sentiment analysis on smaller samples. You'll probably prefer word2vec.

## [**TF-IDF Intuition**](https://www.youtube.com/watch?v=D2V1okCEsiE&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm&index=8), Term-frequency, Inverse document frequency:

* This could be understood as literally `TF * IDF`. ~~`term frequency * (document frequency)^-1`, because you divide the frequency of a given term in the sentence by the number of word in the doucument's sentence (just the one sentence at a time).~~

**Term Frequency**, `TF`, which is *not* the entire thing:

`term frequency = number of times word appears in sentence in question / number of words in sentence`
* "word" only includes the important words keywords; it's the sentence without the "[stop keywords](#things-to-always-do)."

[![tf-idf with "good" in sentence 1](./image/TF%20Good.PNG)](https://youtu.be/D2V1okCEsiE?si=9CAa3D6Um9rsupSk&t=145)

in the image above, you can see that it's a matrix of each word/feature vs which sentence is being investigated.

**Inverse Document Frequency** `IDF`

`IDF = ln(document sentence count / number of sentences including the word in question)`

[![IDF calculation image](./image/IDF%20girl.PNG)](https://youtu.be/D2V1okCEsiE?si=7p2MgBEe-Tiql1k2&t=236)

Here we can see it Inverse Document Frequency for "girl" calculated as `ln(3/2)` for ln(3 sentences total / 2 sentences with "girl")

`TF-IDF` of a given word *in a given sentence* will be the `TF` of the word times the `IDF` of that word for that sentence. word = feature.

## [Word Embedding](https://www.youtube.com/watch?v=pO_6Jk0QtKw)

with bag of words being method 1, and TF-IDF being method 2, Word Embedding is the method 3, in a list of increasing smeantic understanding.
* semantic meaning "similar words," like how "man" is similar to "woman" and to "adult".

Word Embedding has 2 techniques:
* word2vec
* Glove

from what I can tell, this is info common to both until the presenter specifies he is doing one or the other.

say you have a list `wordswordswords` of words (he says "dictionary", but describes in the form of an ordered list object) and the word you're interested in is "man" and it is in index 5000; you can one-hot-matrix this for "man" as a list the same length as `wordswordswords` that has `0` for every index except position 5000, which has a `1`, representing "man".
* nevermind, it is not part of embedding at all.
* matrix with this many zeros vs so many ones is called a "sparse matrix"

**Word Embedding** instead makes a matrix of features vs words to develop associasions between the two.

[![word-feature matrix visual](./image/embedding%20feature%20matrix%20-%20labelled.PNG)](https://youtu.be/pO_6Jk0QtKw?si=WlT3lOZ03cVP_LQf&t=385)

In this example, the feature "gender" is highly related to the words "boy", "girl", "king", and "queen". feature "royal", however, is only related to words "king" and "queen".
* this example is for having a 300 dimensional matrix. think of each "feature" as a dimension, like how we can say each "word" has an `x` value, `y` value, `z` diension value... instead we have a `gender` value, `royal` value, `food` dimension value... each feature is a dimension.
* This is still significantly **lower dimension** and a **dense matrix** (as opposed to high dimension sparse matrix we'd get froma one-hot representation.)

## Misc.

skip-grams use negative sampling, selecting "negative" irrelevant words to skip, to accelerate training.

<details>
    <summary>summary I grabbed from an ai</summary>

Character N-grams: Character n-grams involve breaking words into smaller units, such as individual characters or sequences of characters, to capture morphological and orthographic information. By considering character-level information, this method can handle out-of-vocabulary words and capture subword information, making it useful for morphologically rich languages and handling misspellings. However, it may result in higher dimensionality due to the increased number of unique character n-grams.
Skip-grams and Continuous Bag of Words (CBOW): Both skip-gram and CBOW are architectures used in Word2Vec to produce distributed representations of words. The skip-gram model predicts the surrounding context words given the current word, while CBOW predicts the current word given context words within a specific window. These models consider both individual words and a sliding context window as they iterate over the corpus, capturing the relationships between words based on their co-occurrence within the context window. The skip-gram model is designed to predict the context, while CBOW can be viewed as a fill-in-the-blank task, where the word embedding represents the way the word influences the relative probabilities of other words in the context window[1](https://en.wikipedia.org/wiki/Word2vec).

Co-occurrence Matrices: Co-occurrence matrices are used to capture the statistical relationships between words based on their co-occurrence within a specific context. By analyzing the frequency of word co-occurrences within a given window size, co-occurrence matrices can be constructed to represent the relationships between words in a corpus. This method is based on the distributional hypothesis, which states that words appearing in similar contexts are likely to have similar meanings. However, co-occurrence matrices may suffer from high dimensionality and sparsity, especially for large vocabularies.

Negative Sampling: Negative sampling is a technique used to address the computational inefficiency of traditional softmax-based training in word embedding models. Instead of considering all words in the vocabulary for each training sample, negative sampling randomly samples a small number of "negative" words (i.e., words not in the context of the current word) to update the model parameters. This approach speeds up the training process and reduces the computational cost, making it more efficient for large vocabularies. Negative sampling is a refined model that improves the quality of representation and speed of computation, particularly in the skip-gram model.[2](https://medium.com/towards-datascience/word2vec-negative-sampling-made-easy-7a1a647e07a4)[3](https://analyticsindiamag.com/how-to-use-negative-sampling-with-word2vec-model/)

In summary, word embedding methods leverage various techniques, such as character n-grams, skip-grams, CBOW, co-occurrence matrices, and negative sampling, to capture the semantic and syntactic relationships between words. Each method offers unique advantages and considerations, contributing to the rich landscape of word embedding techniques.


FastText utilizes the character n-grams method to provide embeddings. It extends the Word2Vec model by representing words as a bag of character n-grams, allowing it to capture subword information and handle out-of-vocabulary words effectively. This approach enriches word vectors with subword information, leading to improved performance on syntactic word analogy tasks, especially for morphologically rich languages like Czech and German. Additionally, FastText is capable of representing out-of-vocabulary words by summing their sub-words, further enhancing its performance compared to other embedding techniques like CBOW and skip-gram baselines on word-similarity tasks[4](https://www.analyticsvidhya.com/blog/2023/01/introduction-to-fasttext-embeddings-and-its-implication/)
</details>

## Preprocessing


### things to always do

* convert text to lowercase
  * This keeps the first words of sentences from being processed differently from non capitalized versions
  * some terms, like `US` are worthwhile exceptions.
* filter out "stop keywords," uniportant words from the sentence. [this](https://www.youtube.com/watch?v=iu2-G_5YkEo&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm&index=7&pp=iAQB) vid should demonstrate how, but if not, just do a general search.
