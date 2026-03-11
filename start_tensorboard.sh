#!/bin/bash

cd /home/linux-work/doom-ai-bot || exit
source venv/bin/activate
tensorboard --logdir /home/linux-work/doom-ai-bot/logs/doom_ppo_run_0 --host 0.0.0.0 --port 6006
