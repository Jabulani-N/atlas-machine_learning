#!/usr/bin/env python3
"""creates an environment"""

import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """
    creates a frozen lake environment object
    from OpenAI's gym
    """
    return gym.make('FrozenLake-v1',
                    desc=desc,
                    map_name=map_name,
                    is_slippery=is_slippery)
