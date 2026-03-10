# check_install.py
# Run this to confirm all packages installed correctly.

print("Checking installations...\n")

try:
    import vizdoom
    print(f"✅ ViZDoom:            {vizdoom.__version__}")
except Exception as e:
    print(f"❌ ViZDoom FAILED:     {e}")

try:
    import torch
    cuda = torch.cuda.is_available()
    device = torch.cuda.get_device_name(0) if cuda else "CPU only"
    print(f"✅ PyTorch:            {torch.__version__}")
    print(f"   CUDA available:    {cuda}")
    print(f"   Device:            {device}")
except Exception as e:
    print(f"❌ PyTorch FAILED:     {e}")

try:
    import stable_baselines3 as sb3
    print(f"✅ Stable-Baselines3: {sb3.__version__}")
except Exception as e:
    print(f"❌ Stable-Baselines3 FAILED: {e}")

try:
    import gymnasium
    print(f"✅ Gymnasium:         {gymnasium.__version__}")
except Exception as e:
    print(f"❌ Gymnasium FAILED:  {e}")

try:
    import cv2
    print(f"✅ OpenCV:            {cv2.__version__}")
except Exception as e:
    print(f"❌ OpenCV FAILED:     {e}")

print("\nDone. Fix any ❌ errors before continuing.")
