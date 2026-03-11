HEAD
# Retro FPS AI
### Reinforcement Learning for Classic Shooter Enemy Behavior

This project explores how **modern reinforcement learning techniques can evolve enemy behavior inside classic FPS games**.

Instead of relying on the traditional scripted AI found in older shooters, this system trains an agent to **learn combat behavior through experience**.

Using **VizDoom and PPO (Proximal Policy Optimization)**, the agent learns how to move, orient itself, and fire in response to enemies within the game environment.

The long-term goal of this project is to demonstrate how **classic FPS games can be upgraded with modern AI systems**, transforming static enemies into **adaptive combat agents**.

---

# Why This Project Exists

Many classic FPS games have incredible gameplay mechanics but rely on **very simple scripted AI**.

Enemies often behave as:

- bullet sponges
- predictable movement patterns
- scripted attack loops
- limited tactical awareness

Reinforcement learning allows enemies to **develop behavior instead of executing scripts**.

This project explores the idea that we can:

**retrofit classic shooters with modern AI behavior systems.**

If successful, this approach could allow older games to gain:

- adaptive enemy movement
- better target tracking
- dynamic combat responses
- evolving difficulty curves

---

# Features

• Reinforcement Learning using **Stable-Baselines3 PPO**  
• Doom simulation through **VizDoom**  
• Frame-based perception pipeline  
• Parallel training environments  
• TensorBoard monitoring  
• Model checkpoint saving  
• Trained combat agent demonstration  

---

# Project Structure
Great — this is the moment where we turn your repo from “code dump” into a project people understand immediately.

Right now your README works, but we can make it much stronger and more compelling by explaining the why, not just the how.

Below is a full upgraded README you can paste directly into your repo.

Replace your README.md with this
# Retro FPS AI
### Reinforcement Learning for Classic Shooter Enemy Behavior

This project explores how **modern reinforcement learning techniques can evolve enemy behavior inside classic FPS games**.

Instead of relying on the traditional scripted AI found in older shooters, this system trains an agent to **learn combat behavior through experience**.

Using **VizDoom and PPO (Proximal Policy Optimization)**, the agent learns how to move, orient itself, and fire in response to enemies within the game environment.

The long-term goal of this project is to demonstrate how **classic FPS games can be upgraded with modern AI systems**, transforming static enemies into **adaptive combat agents**.

---

# Why This Project Exists

Many classic FPS games have incredible gameplay mechanics but rely on **very simple scripted AI**.

Enemies often behave as:

- bullet sponges
- predictable movement patterns
- scripted attack loops
- limited tactical awareness

Reinforcement learning allows enemies to **develop behavior instead of executing scripts**.

This project explores the idea that we can:

**retrofit classic shooters with modern AI behavior systems.**

If successful, this approach could allow older games to gain:

- adaptive enemy movement
- better target tracking
- dynamic combat responses
- evolving difficulty curves

---

# Features

• Reinforcement Learning using **Stable-Baselines3 PPO**  
• Doom simulation through **VizDoom**  
• Frame-based perception pipeline  
• Parallel training environments  
• TensorBoard monitoring  
• Model checkpoint saving  
• Trained combat agent demonstration  

---

# Project Structure


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

# Installation

Clone the repository:
git clone https://github.com/Talos-Labs-documents/retro-fps-ai

cd retro-fps-ai


Install dependencies:


=======
# Doom AI Bot
### Reinforcement Learning NPC Training for Classic FPS Engines

This project explores using **reinforcement learning (RL)** to train enemy behavior in the classic game **DOOM**. Instead of relying on the original hard-coded enemy logic written in the early 1990s, this project trains an AI agent to learn gameplay behaviors directly from interaction with the environment.

The goal is to create a **modern AI layer for classic games**, allowing them to evolve beyond their original scripted behavior.

---

# Project Vision

Classic games like **Doom, Quake, Thief, and Half-Life** were built with static enemy logic due to the hardware limitations of their time.

Modern hardware and machine learning now allow us to experiment with:

- Reinforcement learning based enemy decision making
- Dynamic combat behavior
- Self-improving NPC tactics
- Community trained AI models
- Long-running background training

This project acts as a **proof of concept** showing how classic engines can be upgraded with modern AI techniques.

---

# Current Features

- Reinforcement Learning training loop
- Custom Doom environment wrapper
- PPO (Proximal Policy Optimization) training
- GPU acceleration using CUDA when available
- Training logs and metrics
- Reproducible environment setup

The system continuously trains an AI agent by running simulated gameplay episodes and learning from reward signals.

---

# Why Doom?

Doom is an ideal AI experimentation platform because:

- The engine is lightweight
- Environments are deterministic
- The game loop is extremely fast
- Many open-source tools exist
- Reinforcement learning experiments run quickly

This makes Doom a perfect **sandbox for AI gameplay research**.

---

# Hardware Used

Current development system:
GPU: RTX 2070 Super
CPU: Ryzen 5
RAM: 16GB
OS: Linux Mint / Ubuntu

---


The project will still run on:

- CPU only systems
- older GPUs
- cloud instances

Training speed simply scales with hardware.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/doom-ai-bot.git
cd doom-ai-bot

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
>>>>>>> 0694302 (Update training environment, add monitoring tools and scripts)
pip install -r requirements.txt


---

<<<<<<< HEAD
# Train the AI

Start reinforcement learning training:

=======
Running Training
>>>>>>> 0694302 (Update training environment, add monitoring tools and scripts)

Start reinforcement learning training:
python3 train.py

The agent will begin interacting with the Doom environment and learning from experience.

Training can run for:

hours

days

weeks

millions or billions of frames

Longer training produces more intelligent behavior.


This will train the AI using the PPO algorithm and periodically save checkpoints.

TensorBoard logs will also be generated for training analysis.

---

<<<<<<< HEAD
# Watch the AI Play

After training, run:

=======
Training Philosophy
>>>>>>> 0694302 (Update training environment, add monitoring tools and scripts)

Unlike traditional scripted AI, reinforcement learning agents:

explore

fail

adapt

optimize behavior over time

This allows the AI to develop strategies that were never explicitly programmed.

Over long training runs the agent begins to learn:

movement optimization

threat avoidance

combat positioning

resource efficiency


This loads the trained model and runs the AI inside the Doom environment.

You should see the bot:

- move
- orient toward enemies
- fire weapons
- engage targets

---

<<<<<<< HEAD
# Example Training Metrics

Typical training runs produce:

- ~600 FPS training speed
- 1M+ training timesteps
- stable PPO convergence
- emergent combat behavior

---

# Long-Term Vision

This project is the beginning of a larger concept:

**Upgrading enemy AI in classic FPS games using reinforcement learning.**

Possible future directions include:

• More advanced reward shaping  
• Multi-enemy combat training  
• Improved action sets  
• Curriculum learning across maps  
• Cooperative AI agents  
• Cross-game AI experimentation  

The ultimate goal is to explore whether **community-driven AI training could modernize enemy behavior across classic games.**

---

# Technologies Used

- Python
- VizDoom
- Stable-Baselines3
- Gymnasium
- PyTorch
- OpenCV
- TensorBoard

---

# Contributing

Experimentation and contributions are welcome.

Possible contribution areas:

- reward design
- new training scenarios
- improved action sets
- visualization tools
- alternative RL algorithms

---

# License

This project is open-source.  
A license will be added in a future update.

---

# Project Author

Brandon Lemon

---

Monitoring Training

Training logs are written to:
logs/
These logs track:

reward scores

learning progression

episode length

performance metrics

Future versions will include a real-time dashboard for monitoring learning progress.

---

Future Roadmap

This project is only the beginning.

Planned expansions include:

Advanced Enemy AI

tactical movement

group coordination

ambush behavior

environment awareness

Visual Monitoring

training dashboards

gameplay playback

learning graphs

Cross Game Support

Potential engines to experiment with:

Quake

Quake II

Half-Life

Thief

Hexen

Heretic

Community Training

The long-term vision is to allow users to contribute training from their own machines.

Examples:

RTX gaming PCs

Raspberry Pi clusters

AI hardware

cloud GPUs

Training data could eventually be shared and merged into improved AI models.

---

Why This Matters

For decades people have asked:

"Can it run Doom?"

Now we ask a different question:

Can Doom learn?

This project explores what happens when classic game engines meet modern AI.

---

Contributing

Contributions are welcome.

Potential areas of improvement include:

environment wrappers

training stability

reward engineering

monitoring tools

performance optimization

Fork the repo and experiment.

---

License

MIT License

This project is open source and free to use, modify, and expand.

---

Author

Brandon Lemon

Exploring the intersection of classic games and modern artificial intelligence.

---

0694302 (Update training environment, add monitoring tools and scripts)
