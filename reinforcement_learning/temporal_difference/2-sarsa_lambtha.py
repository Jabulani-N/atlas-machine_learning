#!/usr/bin/env python3
"""performs the SARSA(λ) algorithm"""

import numpy as np


def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100,
                  alpha=0.1, gamma=0.99, epsilon=1,
                  min_epsilon=0.1, epsilon_decay=0.05):
    """
    env = openai environment instance
    Q = qtable
        np.ndarray
            shape = (s,a)
                s = number of states
                a = number of actions
    lambtha = eligibility trace factor
    episodes = num episodes for training
    max_steps = steps per episode
    alpha = learning rate
    gamma = discount rate
    epsilon = initial threshold for epsilon greedy
        float
    epsilon_decay = how much to decrease epsilon between episodes
    min_epsilon = epsilon must go below this value

    return Q (updated)
    """
    pass
