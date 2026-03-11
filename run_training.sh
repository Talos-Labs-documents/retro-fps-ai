#!/usr/bin/env bash

set -e

PROJECT_DIR="$HOME/doom-ai-bot"
LOG_DIR="$PROJECT_DIR/logs"
RUN_LOG="$LOG_DIR/overnight_train.log"

mkdir -p "$LOG_DIR"

cd "$PROJECT_DIR"
source venv/bin/activate

echo "========================================" | tee -a "$RUN_LOG"
echo "Starting training: $(date)" | tee -a "$RUN_LOG"
echo "Project dir: $PROJECT_DIR" | tee -a "$RUN_LOG"
echo "Log file: $RUN_LOG" | tee -a "$RUN_LOG"
echo "========================================" | tee -a "$RUN_LOG"

python train.py 2>&1 | tee -a "$RUN_LOG"
