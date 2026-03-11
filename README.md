# Retro FPS AI
### Reinforcement Learning Enemy AI for Classic FPS Games

For decades the question was:

> **"Can it run Doom?"**

This project asks a different question:

> **"Can Doom learn?"**

Retro FPS AI explores using **reinforcement learning (RL)** to train enemy behavior in classic first-person shooter engines. Instead of static scripted logic written decades ago, enemies learn strategies through repeated gameplay.

The project begins with **DOOM** as a sandbox environment for experimenting with modern AI techniques inside a classic game engine.

---

# Project Goals

Classic FPS games relied on **hardcoded AI behavior** due to hardware limitations of the time. Today we can experiment with:

- Reinforcement learning driven enemy behavior
- Dynamic combat strategies
- Self-improving NPC logic
- Training AI agents through simulated gameplay
- Community-driven model improvements

This repository provides a **working framework for training AI agents inside Doom environments.**

---

# Current Features

- Reinforcement Learning training pipeline
- Custom Doom environment wrapper
- PPO-based training
- GPU acceleration (CUDA supported)
- Training dashboards and monitoring tools
- Scripted training and launch tools
- TensorBoard support for learning visualization

The AI continuously interacts with the game environment and adjusts its strategy based on reward signals.

---

# Why Doom?

Doom is an ideal platform for reinforcement learning experiments:

- Lightweight engine
- Extremely fast game loop
- Deterministic environments
- Mature open-source tooling
- Easy simulation at large scale

This allows AI agents to train **millions of gameplay iterations quickly.**

---

# Repository Structure

retro-fps-ai/
│
├── environment/
│ └── doom_env.py # Custom Gymnasium environment
│
├── config/
│ └── basic.cfg # Doom scenario configuration
│
├── models/ # Trained model storage
├── checkpoints/ # Training checkpoints
├── logs/ # TensorBoard logs
│
├── train.py # RL training script
├── watch_ai.py # Run the trained agent
├── test_env.py # Environment testing
├── check_install.py # Dependency test
│
├── requirements.txt
├── README.md
└── .gitignore
---

# Quick Start

Clone the repository:

```bash
git clone https://github.com/Talos-Labs-documents/retro-fps-ai.git
cd retro-fps-ai
Create a virtual environment:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt

----

Start Training

Run the reinforcement learning agent:
python3 train.py
Or use the helper script:
chmod +x start_ai_training.sh
./start_ai_training.sh
Training will begin immediately and the AI agent will start interacting with the Doom environment.

---

Monitoring Training

You can monitor training progress using:

Live Dashboard
python3 monitor_dashboard.py
TensorBoard
./start_tensorboard.sh
This allows visualization of:

reward progression

episode performance

training stability

learning curves

---

Hardware

Current development hardware:

GPU: RTX 2070 Super

CPU: Ryzen 5

RAM: 16GB

OS: Linux Mint / Ubuntu

The system will also run on:

CPU-only machines

cloud GPU instances

smaller local systems

Training speed simply scales with hardware performance.

---

Training Philosophy

Traditional game AI uses scripted decision trees.

Reinforcement learning instead allows agents to:

explore environments

fail repeatedly

discover better strategies

adapt behavior over time

The goal is to create enemy behavior that was never explicitly programmed.

---

Future Roadmap

This project is just the starting point.

Planned expansions include:

Advanced Enemy Behavior

tactical movement

smarter pathfinding

threat prioritization

cover seeking

Training Visualization

gameplay recording

reward graph dashboards

automated performance reports

Multi-Game Support

Future engine targets may include:

Quake

Quake II

Half-Life

Thief

Hexen

Heretic

Distributed Training

Potential support for:

community training runs

shared model checkpoints

distributed RL experimentation

---

Why This Matters

Classic game engines are incredibly efficient simulation environments.

By combining them with modern AI systems we can explore:

emergent gameplay behavior

adaptive enemy logic

AI training environments for research

modernizing classic games without rewriting them

Retro FPS AI explores what happens when old engines meet modern machine learning.

---

Contributing

Contributions are welcome.

Possible contribution areas include:

reward function improvements

training stability

performance optimization

new environment integrations

monitoring tools

Fork the repository and experiment.

---

License

MIT License

This project is open source and free to use, modify, and distribute.

---

Author

Brandon Lemon

Exploring the intersection of classic game engines and modern artificial intelligence.

---

0694302 (Update training environment, add monitoring tools and scripts)
