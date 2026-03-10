import os
import glob
from stable_baselines3 import PPO
from environment.doom_env import DoomEnv


def find_latest_checkpoint():
    checkpoints = glob.glob("checkpoints/doom_ppo_*_steps.zip")

    if not checkpoints:
        raise FileNotFoundError("No checkpoints found.")

    latest = max(checkpoints, key=os.path.getmtime)
    return latest


if __name__ == "__main__":

    model_path = find_latest_checkpoint()

    print(f"Loading latest model: {model_path}")

    env = DoomEnv(render_mode="human")

    model = PPO.load(model_path)

    obs, info = env.reset()

    while True:
        action, _ = model.predict(obs, deterministic=True)

        obs, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            obs, info = env.reset()
