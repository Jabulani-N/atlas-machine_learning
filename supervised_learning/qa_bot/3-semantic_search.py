#!/usr/bin/env python3
"""
finds a snippet of text within reference document
    to answer a question
        uses task 0
    the question is user given
        uses task 1
"""


from sentence_transformers import SentenceTransformer, util
import os


def semantic_search(corpus_path, sentence):
    # Load the pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Load the corpus from the specified path
    corpus = []
    for filename in os.listdir(corpus_path):
        with open(os.path.join(corpus_path, filename), 'r', encoding='utf-8') as file:
            corpus.append(file.read())

    # Compute embeddings for the corpus and the input sentence
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    sentence_embedding = model.encode(sentence, convert_to_tensor=True)

    # Compute cosine similarities
    similarities = util.pytorch_cos_sim(sentence_embedding, corpus_embeddings)

    # Get the index of the most similar document
    most_similar_idx = similarities.argmax()

    # Return the most similar document
    return corpus[most_similar_idx]
