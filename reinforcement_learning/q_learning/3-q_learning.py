#!/usr/bin/env python
"""performs q-learning"""

import numpy as np
load_frozen_lake = __import__('0-load_env').load_frozen_lake
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q, episodes=5000, max_steps=100,
          alpha=0.1, gamma=0.99, epsilon=1,
          min_epsilon=0.1, epsilon_decay=0.05):
    """
    env = forzenlake instance
    Q = q table
        np.ndarray
    episodes = # of episodes to train over
        int
    max_steps = step cap per episode
        int
    alpha = learning rate
    gamma = discount rate
    epsilon = INITIAL epsilon greedy epsilon
        float
    min_epsilon = minimum permitted epsilon greedy epsilon
    epsilon_decay = between-episode epsilon decrease
    """
    total_rewards = []
    qtable = Q
    current_epsilon = epsilon
    for episode in range(episodes):
        state, _ = env.reset()
        print("state is: ", state, type(state))
        # episode_reward = 0
        done = False

        for step in range(max_steps):
            act_idx = epsilon_greedy(qtable, state, current_epsilon)
            print("step results: ", env.step(act_idx))
            new_state, episode_reward, done, _, _ = env.step(act_idx)
            print("episode_reward is: ", episode_reward)

            # update qtable via learning rate
            qtable[state][act_idx] = qtable[state][act_idx] +\
                alpha * (episode_reward + gamma * np.max(qtable[new_state, :]) -
                         qtable[state, act_idx])
            # print("qtable updated to: ", qtable)

            # When the agent falls in a hole,  reward updated to -1
            # because gameover despite no loot
            if episode_reward == 0 and done:
                episode_reward = -1
            state = new_state

            if done:
                break
        # epsilon decay between episodes
        decayed_epsilon = current_epsilon - epsilon_decay
        if decayed_epsilon >= min_epsilon:
            current_epsilon = decayed_epsilon
        else:
            current_epsilon = min_epsilon
        np.append(episode_reward, total_rewards)
        print("total rewards = ", total_rewards)
        return qtable, total_rewards
