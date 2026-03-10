# test_env.py
#
# Runs the DOOM environment for one episode using purely RANDOM actions.
# No AI yet — we're just confirming the environment starts, steps,
# and returns observations correctly.

import numpy as np
from environment import DoomEnv

print("Initializing DOOM environment...")
env = DoomEnv()

print("Running one episode with random actions...\n")

obs, info = env.reset()
print(f"Observation shape: {obs.shape}")   # Should be (4, 84, 84)
print(f"Action space:      {env.action_space}")   # Should be Discrete(4)

total_reward = 0
steps = 0

while True:
    # Pick a random action (0, 1, 2, or 3)
    action = env.action_space.sample()

    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    steps += 1

    if steps % 50 == 0:
        print(f"  Step {steps:4d} | Reward this step: {reward:+.2f} | "
              f"Total reward: {total_reward:+.2f}")

    if terminated or truncated:
        break

print(f"\nEpisode finished.")
print(f"  Total steps:  {steps}")
print(f"  Total reward: {total_reward:.2f}")

env.close()
print("\nEnvironment closed cleanly. ✅")
