#!/usr/bin/env python3
"""
trains a deep qlearning model
to play breakout
"""

import gym
import keras
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory


def create_agent():
    """parent function for DQNAgent creation"""
    pass
