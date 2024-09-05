#!/usr/bin/env python3
"""returns a gym environment attirbute"""

import numpy as np


def q_init(env):
    """
    env = FrozenLakeEnv instance
    Returns:  Q-table as numpy.ndarray of zeros
    """
    # these are dimensions of the q-table
    obs_count = env.observation_space.n
    act_count = env.action_space.n
    empty_q = np.zeros((obs_count, act_count))
    return empty_q
