#!/usr/bin/env python3
"""computes the policy with a weight of a matrix"""

import numpy as np


def policy(matrix, weight):
    """
    computes the policy with a weight of a matrix
        softmaxes the dot of matrix with weight

    input info pulled from the subsequent task
    matrix = input matrix
    weight = matrix input policy
    """
    policy = matrix_softmax(weight, matrix)
    return policy


def softmax(z):
    """
    based on a previous project
    calculate softmax of an array
    """
    # Subtract the maximum value for numerical stability
    exp_z = np.exp(z - np.max(z, axis=-1, keepdims=True))
    return exp_z / exp_z.sum(axis=-1, keepdims=True)


def matrix_softmax(the_list, the_matrix, bias=0):
    """
    helps softmax function
        lets us just directly plug in a matrix and list
    bias exists as a 'just in case'
    """
    return softmax(np.dot(the_matrix, the_list) + bias)


def policy_gradient(state, weight):
    """
    computes monte-carlo policy gradient
    state = matrix of current observation of env
        shape = (1,4)
    weight = matrix of random weight

    return
        action
        gradient
    """
    # Get action probabilities from the policy function
    action_probs = policy(state, weight)
    action_probs = action_probs[0]
    # print("action probs[0]: ", action_probs[0])
    # Sample an action based on the probabilities
    action = np.random.choice(
        np.arange(len(action_probs)), p=action_probs)
    print("action: ", action)
    # the below seems irrrelevant as we don't have a reward
    # Assume we have a function to get the reward for the action taken
    # reward = get_reward(state, action)  # Placeholder for actual reward
    # function

    # Compute the gradient
    gradient = np.zeros_like(weight)
    for i in range(len(action_probs)):
        # The gradient is the reward times the derivative of the log
        # probability
        # gradient[:, i] = (reward - np.mean(reward)) * \
        #     (action_probs[i] * (1 - action_probs[i])) * state
        # print("contents:")
        # print("gradient[:, i]:", gradient[:, i])
        # print("state:", state)
        # print("action_probs[i]:", action_probs[i])
        # print("(1 - action_probs[i]):", (1 - action_probs[i]))
        # print("state * (1 - action_probs[i]):", state * (1 - action_probs[i]))
        # print("-state * action_probs[i]:", -state * action_probs[i])
        if i == action:
            gradient[:, i] = state.flatten() * (1 - action_probs[i]
                                                )  # For the selected action
        else:
            # For the non-selected actions
            gradient[:, i] = -state.flatten() * action_probs[i]

    return action, gradient
