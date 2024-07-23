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

[![woird-feature matrix visual](./image/embedding%20feature%20matrix%20-%20labelled.PNG)](https://youtu.be/pO_6Jk0QtKw?si=WlT3lOZ03cVP_LQf&t=385)

In this example, the feature "gender" is highly related to the words "boy", "girl", "king", and "queen". feature "royal", however, is only related to words "king" and "queen".
* this example is for having a 300 dimensional matrix. think of each "feature" as a dimension, like how we can say each "word" has an `x` value, `y` value, `z` diension value... instead we have a `gender` value, `royal` value, `food` dimension value... each feature is a dimension.

## Preprocessing


### things to always do

* convert text to lowercase
  * This keeps the first words of sentences from being processed differently from non capitalized versions
  * some terms, like `US` are worthwhile exceptions.
* filter out "stop keywords," uniportant words from the sentence. [this](https://www.youtube.com/watch?v=iu2-G_5YkEo&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm&index=7&pp=iAQB) vid should demonstrate how, but if not, just do a general search.
