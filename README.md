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


pip install -r requirements.txt


---

# Train the AI

Start reinforcement learning training:


python train.py


This will train the AI using the PPO algorithm and periodically save checkpoints.

TensorBoard logs will also be generated for training analysis.

---

# Watch the AI Play

After training, run:


python watch_ai.py


This loads the trained model and runs the AI inside the Doom environment.

You should see the bot:

- move
- orient toward enemies
- fire weapons
- engage targets

---

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
