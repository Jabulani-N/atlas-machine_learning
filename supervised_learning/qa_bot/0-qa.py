#!/usr/bin/env python3
"""
finds a snippet of text within reference document
    to answer a question
"""

import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer


def question_answer(question, reference):
    """
    question = string
        containing question to answer
    reference = string
        containing reference document from which to find the answer
    Returns: a string containing answer
        If no answer is found, return None
    """
    tokenizer = BertTokenizer.from_pretrained(
        'bert-large-uncased-whole-word-masking-finetuned-squad')
    # model from tf hub
    model_address = "https://www.kaggle.com/models"
    model_address += "/seesee/bert/TensorFlow2/uncased-tf2-qa/1"
    model = hub.load(model_address)
    # token creation
    quest_tokens = tokenizer.tokenize(question)
    ref_tokens = tokenizer.tokenize(reference)
    # important for id assignment
    all_tokens = ['[CLS]'] + quest_tokens +\
                 ['[SEP]'] + ref_tokens +\
                 ['[SEP]']
    token_ids = tokenizer.convert_tokens_to_ids(all_tokens)
    all_mask = [1] * len(token_ids)
    # record the tokens that identify types
    type_ids = [0] * (1 + len(quest_tokens) + 1) +\
               [1] * (len(ref_tokens) + 1)
    # convert to tensor
    token_ids, all_mask, type_ids = map(
        lambda t: tf.expand_dims(
            tf.convert_to_tensor(
                t, dtype=tf.int32), 0), (token_ids, all_mask, type_ids))
    # ask the model our question
    models_answer = model([token_ids, all_mask, type_ids])
    # identify start and end points of quoted snippet
    answer_start, answer_end = bert_answer_coord(models_answer)
    answer_end = answer_end + 1  # to include idx of last tok
    answer_tokens = all_tokens[answer_start:answer_end]
    answer = tokenizer.convert_tokens_to_string(answer_tokens)
    return answer


def bert_answer_coord(models_answer):
    """returns a model's answer's start and end"""
    hajimari = tf.argmax(models_answer[0][0][1:]) + 1
    owari = tf.argmax(models_answer[1][0][1:]) + 1
    return hajimari, owari
