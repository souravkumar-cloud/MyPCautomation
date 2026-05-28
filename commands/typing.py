import pyautogui
import pyperclip
import time


# ==========================================
# TYPE TEXT
# ==========================================
def type_text(text):

    pyautogui.write(text, interval=0.05)

    return f"Typed: {text}"


# ==========================================
# COPY SELECTED TEXT
# ==========================================
def copy_text():

    pyautogui.hotkey("ctrl", "c")

    return "Copied selected text"


# ==========================================
# PASTE TEXT
# ==========================================
def paste_text():

    pyautogui.hotkey("ctrl", "v")

    return "Pasted text"


# ==========================================
# COPY DIRECT TEXT TO CLIPBOARD
# ==========================================
def copy_to_clipboard(text):

    pyperclip.copy(text)

    return f"Copied '{text}' to clipboard"


# ==========================================
# SELECT ALL TEXT
# ==========================================
def select_all():

    pyautogui.hotkey("ctrl", "a")

    return "Selected all text"


# ==========================================
# BACKSPACE
# ==========================================
def backspace(count=1):

    for _ in range(count):

        pyautogui.press("backspace")

        time.sleep(0.05)

    return f"Pressed backspace {count} times"


# ==========================================
# DELETE KEY
# ==========================================
def delete_key(count=1):

    for _ in range(count):

        pyautogui.press("delete")

        time.sleep(0.05)

    return f"Pressed delete {count} times"


# ==========================================
# PRESS ENTER
# ==========================================
def press_enter():

    pyautogui.press("enter")

    return "Pressed Enter"


# ==========================================
# PRESS TAB
# ==========================================
def press_tab():

    pyautogui.press("tab")

    return "Pressed Tab"


# ==========================================
# PRESS ESC
# ==========================================
def press_escape():

    pyautogui.press("esc")

    return "Pressed Escape"


# ==========================================
# PRESS SPACE
# ==========================================
def press_space():

    pyautogui.press("space")

    return "Pressed Space"


# ==========================================
# HOTKEY FUNCTION
# ==========================================
def hotkey(*keys):

    pyautogui.hotkey(*keys)

    return f"Pressed hotkey: {' + '.join(keys)}"