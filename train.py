import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.callbacks import CheckpointCallback
from environment.doom_env import DoomEnv

MODEL_DIR = "models"
LOG_DIR = "logs"
CHECKPOINT_DIR = "checkpoints"

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(CHECKPOINT_DIR, exist_ok=True)

NUM_ENVS = 4
TOTAL_TIMESTEPS = 1_000_000

FINAL_MODEL_CANDIDATES = [
    os.path.join("models", "doom_ppo_final.zip"),
    os.path.join("checkpoints", "doom_ppo_final.zip"),
]


def make_env(rank: int):
    def _init():
        env = DoomEnv()
        return env
    return _init


def find_existing_model():
    for path in FINAL_MODEL_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


if __name__ == "__main__":
    env = SubprocVecEnv([make_env(i) for i in range(NUM_ENVS)])

    checkpoint_callback = CheckpointCallback(
        save_freq=20_000,
        save_path=CHECKPOINT_DIR,
        name_prefix="doom_ppo"
    )

    existing_model = find_existing_model()

    if existing_model:
        print(f"Loading existing model: {existing_model}")
        model = PPO.load(existing_model, env=env, device="cuda")
        model.tensorboard_log = LOG_DIR
    else:
        print("No existing model found. Creating a new PPO model.")
        model = PPO(
            policy="CnnPolicy",
            env=env,
            verbose=1,
            tensorboard_log=LOG_DIR,
            device="cuda",
            learning_rate=2.5e-4,
            n_steps=1024,
            batch_size=256,
            n_epochs=4,
            gamma=0.99,
            gae_lambda=0.95,
            clip_range=0.1,
            ent_coef=0.01,
        )

    print("Starting parallel training...")

    model.learn(
        total_timesteps=TOTAL_TIMESTEPS,
        callback=checkpoint_callback,
        tb_log_name="PPO_parallel"
    )

    final_model_path = os.path.join(CHECKPOINT_DIR, "doom_ppo_final")
    model.save(final_model_path)

    print(f"Training complete. Final model saved to: {final_model_path}.zip")

    env.close()
