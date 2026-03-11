import os
import re
import time
import shutil
import subprocess
from datetime import datetime
from collections import deque

import psutil
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

LOG_FILE = os.path.expanduser("~/doom-ai-bot/training_log.txt")

# Keep a rolling history for mini graphs
HISTORY_LEN = 40
speed_history = deque(maxlen=HISTORY_LEN)
fps_history = deque(maxlen=HISTORY_LEN)
value_loss_history = deque(maxlen=HISTORY_LEN)


def get_gpu_info():
    try:
        result = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=name,utilization.gpu,memory.used,memory.total,temperature.gpu",
                "--format=csv,noheader,nounits",
            ],
            text=True,
        ).strip()

        if not result:
            return "No NVIDIA GPU detected"

        gpu_rows = []
        for line in result.splitlines():
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 5:
                name, util, mem_used, mem_total, temp = parts
                gpu_rows.append(
                    {
                        "name": name,
                        "util": util,
                        "mem_used": mem_used,
                        "mem_total": mem_total,
                        "temp": temp,
                    }
                )
        return gpu_rows
    except Exception:
        return None


def tail_file(path, lines=100):
    if not os.path.exists(path):
        return f"Log file not found yet:\n{path}"

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.readlines()
        return "".join(content[-lines:]) if content else "Log file exists but is empty."
    except Exception as e:
        return f"Could not read log file:\n{e}"


def parse_progress_line(log_text):
    progress_pattern = re.compile(
        r"\[progress\]\s+timesteps=([\d,]+)\s+\|\s+elapsed=([0-9:]+)\s+\|\s+steps_per_sec=([0-9.]+)\s+\|\s+eta=([0-9:]+)"
    )

    matches = progress_pattern.findall(log_text)
    if not matches:
        return None

    timesteps, elapsed, steps_per_sec, eta = matches[-1]
    return {
        "timesteps": timesteps,
        "elapsed": elapsed,
        "steps_per_sec": steps_per_sec,
        "eta": eta,
    }


def parse_last_sb3_block(log_text):
    lines = log_text.splitlines()
    blocks = []
    current_block = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("--------------------------------"):
            if current_block:
                blocks.append(current_block[:])
                current_block = []
            continue

        if "|" in line:
            current_block.append(line)

    if current_block:
        blocks.append(current_block)

    parsed = {}

    for block in reversed(blocks):
        block_data = {}
        for line in block:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 2:
                key = parts[0]
                value = parts[1]
                block_data[key] = value

        if "total_timesteps" in block_data or "fps" in block_data or "iterations" in block_data:
            parsed = block_data
            break

    return parsed


def parse_training_stats(log_text):
    progress = parse_progress_line(log_text)
    sb3 = parse_last_sb3_block(log_text)

    stats = {
        "timesteps": progress["timesteps"] if progress else "N/A",
        "elapsed": progress["elapsed"] if progress else "N/A",
        "steps_per_sec": progress["steps_per_sec"] if progress else "N/A",
        "eta": progress["eta"] if progress else "N/A",
        "sb3_fps": sb3.get("fps", "N/A"),
        "sb3_iterations": sb3.get("iterations", "N/A"),
        "sb3_total_timesteps": sb3.get("total_timesteps", "N/A"),
        "approx_kl": sb3.get("approx_kl", "N/A"),
        "clip_fraction": sb3.get("clip_fraction", "N/A"),
        "explained_variance": sb3.get("explained_variance", "N/A"),
        "learning_rate": sb3.get("learning_rate", "N/A"),
        "loss": sb3.get("loss", "N/A"),
        "policy_gradient_loss": sb3.get("policy_gradient_loss", "N/A"),
        "value_loss": sb3.get("value_loss", "N/A"),
    }

    update_histories(stats)
    return stats


def safe_float(value):
    try:
        return float(str(value).replace(",", ""))
    except Exception:
        return None


def update_histories(stats):
    speed = safe_float(stats["steps_per_sec"])
    fps = safe_float(stats["sb3_fps"])
    value_loss = safe_float(stats["value_loss"])

    if speed is not None:
        speed_history.append(speed)
    if fps is not None:
        fps_history.append(fps)
    if value_loss is not None:
        value_loss_history.append(value_loss)


def sparkbar(values, width=40):
    if not values:
        return "No data yet"

    ticks = "▁▂▃▄▅▆▇█"
    vmin = min(values)
    vmax = max(values)

    if vmax == vmin:
        return ticks[3] * min(len(values), width)

    if len(values) > width:
        values = list(values)[-width:]

    chars = []
    for v in values:
        idx = int((v - vmin) / (vmax - vmin) * (len(ticks) - 1))
        chars.append(ticks[idx])

    return "".join(chars)


def build_system_table():
    cpu = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory()
    disk = shutil.disk_usage("/")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Metric")
    table.add_column("Value")

    table.add_row("CPU Usage", f"{cpu}%")
    table.add_row("RAM Usage", f"{mem.percent}% ({mem.used // (1024**3)} GB / {mem.total // (1024**3)} GB)")
    table.add_row("Disk Usage", f"{disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB")
    table.add_row("Updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return table


def build_gpu_table():
    gpu_info = get_gpu_info()

    if gpu_info is None:
        return Panel("nvidia-smi not available or GPU query failed.", title="GPU")

    if isinstance(gpu_info, str):
        return Panel(gpu_info, title="GPU")

    table = Table(show_header=True, header_style="bold green")
    table.add_column("GPU")
    table.add_column("Util %")
    table.add_column("VRAM")
    table.add_column("Temp °C")

    for gpu in gpu_info:
        table.add_row(
            gpu["name"],
            gpu["util"],
            f'{gpu["mem_used"]}/{gpu["mem_total"]} MB',
            gpu["temp"],
        )

    return table


def build_progress_table(stats):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Run Progress")
    table.add_column("Value")

    table.add_row("Timesteps", stats["timesteps"])
    table.add_row("Elapsed", stats["elapsed"])
    table.add_row("Speed", f'{stats["steps_per_sec"]} steps/sec')
    table.add_row("ETA", stats["eta"])
    table.add_row("PPO FPS", stats["sb3_fps"])
    table.add_row("SB3 Iterations", stats["sb3_iterations"])
    table.add_row("SB3 Total Steps", stats["sb3_total_timesteps"])

    return table


def build_metrics_table(stats):
    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("PPO Metric")
    table.add_column("Value")

    table.add_row("Approx KL", stats["approx_kl"])
    table.add_row("Clip Fraction", stats["clip_fraction"])
    table.add_row("Explained Var", stats["explained_variance"])
    table.add_row("Learning Rate", stats["learning_rate"])
    table.add_row("Loss", stats["loss"])
    table.add_row("Policy Grad Loss", stats["policy_gradient_loss"])
    table.add_row("Value Loss", stats["value_loss"])

    return table


def build_graphs_panel():
    lines = [
        f"Steps/sec  : {sparkbar(speed_history)}",
        f"PPO FPS    : {sparkbar(fps_history)}",
        f"Value Loss : {sparkbar(value_loss_history)}",
    ]
    return Panel("\n".join(lines), title="Live Mini-Graphs", border_style="cyan")


def build_middle_panels(log_text):
    stats = parse_training_stats(log_text)

    left = Panel(build_progress_table(stats), title="Run Progress", border_style="magenta")
    middle = Panel(build_metrics_table(stats), title="PPO Metrics", border_style="yellow")
    right = build_graphs_panel()

    return left, middle, right


def build_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="top", size=10),
        Layout(name="middle", size=18),
        Layout(name="bottom"),
    )

    layout["top"].split_row(
        Layout(name="system"),
        Layout(name="gpu"),
    )

    layout["middle"].split_row(
        Layout(name="progress"),
        Layout(name="metrics"),
        Layout(name="graphs"),
    )

    layout["bottom"].update(Panel("", title="Training Log Tail"))
    return layout


def render_dashboard():
    log_text = tail_file(LOG_FILE, lines=100)
    layout = build_layout()

    layout["system"].update(Panel(build_system_table(), title="System"))
    layout["gpu"].update(Panel(build_gpu_table(), title="GPU"))

    progress_panel, metrics_panel, graphs_panel = build_middle_panels(log_text)
    layout["progress"].update(progress_panel)
    layout["metrics"].update(metrics_panel)
    layout["graphs"].update(graphs_panel)

    layout["bottom"].update(Panel(log_text, title=f"Training Log Tail: {LOG_FILE}"))
    return layout


def main():
    console = Console()
    with Live(render_dashboard(), console=console, refresh_per_second=1, screen=True) as live:
        while True:
            live.update(render_dashboard())
            time.sleep(1)


if __name__ == "__main__":
    main()
