#!/usr/bin/env python3
"""performs the TD(λ) algorithm"""

import numpy as np


def td_lambtha(
        env,
        V,
        policy,
        lambtha,
        episodes=5000,
        max_steps=100,
        alpha=0.1,
        gamma=0.99):
    """
    env = openai gym environment
    V = initial value estimate
        np.ndarray
            shape = (s,)
    policy = policy function
    lambtha = eligibility trace factor
    episodes = num episodes for training
    max_steps = steps per episode
    alpha = learning rate
    gamma = discount rate

    returns:
        V = value estimate (updated)
    """
    for ep_num in range(episodes):
        elig_trace = np.zeros(V.shape)
        state = env.reset()

        for step in range(max_steps):
            # this bit is hte same as monte carlo
            action = policy(state)
            next_state, reward, terminal, _ = env.step(action)
