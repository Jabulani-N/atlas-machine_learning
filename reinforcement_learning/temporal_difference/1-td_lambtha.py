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
    num_states = env.observation_space.n
    for ep_num in range(episodes):
        # eligibility trace init at 0 for each state
        elig_trace = np.zeros(V.shape)
        current_state = env.reset()

        for step_num in range(max_steps):
            # this bit is the same as monte carlo
            action = policy(current_state)
            next_state, reward, terminal, _ = env.step(action)
            # TD Error
            delta = reward + gamma * V[next_state] - V[current_state]
            # eligibility only assigned to sates actually visited
            elig_trace[current_state] += 1
            for statenum in range(num_states):
                # update V
                V[statenum] += alpha * delta * elig_trace[statenum]
                # this can be compressed into a single line by
                #   directly assigning current state to this value
                #   only if this happens before updating V
                elig_trace[statenum] *= gamma * lambtha
            current_state = next_state
            if terminal:
                break
    return V
