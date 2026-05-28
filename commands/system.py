import os
import pyautogui
import time


# ==========================================
# SCREENSHOT
# ==========================================
def take_screenshot():

    filename = f"screenshot_{int(time.time())}.png"

    pyautogui.screenshot(filename)

    return f"Screenshot saved as {filename}"


# ==========================================
# SHUTDOWN PC
# ==========================================
def shutdown_pc():

    os.system("shutdown /s /t 5")

    return "PC will shutdown in 5 seconds"


# ==========================================
# RESTART PC
# ==========================================
def restart_pc():

    os.system("shutdown /r /t 5")

    return "PC will restart in 5 seconds"


# ==========================================
# LOCK PC
# ==========================================
def lock_pc():

    os.system("rundll32.exe user32.dll,LockWorkStation")

    return "PC locked"