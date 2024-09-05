#!/usr/bin/env python
"""plays a game via full ecxploit"""

import numpy as np
load_frozen_lake = __import__('0-load_env').load_frozen_lake
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def play(env, Q, max_steps=100):
    """
    plays a game of frozenlake
        always exploits
    """
    # guarantees exploitation
    epsilon = 0
    # clarity
    qtable = Q
    state, _ = env.reset()
    episode_reward = 0
    for step in range(max_steps):
        print(env.render())
        act_idx = epsilon_greedy(qtable, state, epsilon)
        new_state, step_reward, done, _, _ = env.step(act_idx)
        # display
        episode_reward += step_reward
    # the below is almost exactly pasted from task3
    # When the agent falls in a hole,  reward updated to -1
        # because gameover despite no loot
        if episode_reward == 0 and done:
            episode_reward = -1
        state = new_state
        if done:
            # step = max_steps
            break
    print(env.render())
    return episode_reward
