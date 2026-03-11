#!/bin/bash

cd /home/linux-work/doom-ai-bot || exit

source venv/bin/activate

echo "[$(date)] Starting Doom AI training..." >> training_log.txt
python train.py \
  --iterations 100000000 \
  --num-envs 4 \
  --checkpoint-freq 10000 \
  --log-freq 10000 \
  --device cuda >> training_log.txt 2>&1
echo "[$(date)] Training process exited." >> training_log.txt
