import os
import time
import pyautogui
import pyperclip
import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import InvalidSessionIdException

driver = None


def get_driver():

    global driver

    try:

        # Check if existing driver still works
        if driver is not None:

            driver.current_url

            return driver

    except InvalidSessionIdException:

        driver = None

    except Exception:

        driver = None

    # Create new driver
    options = Options()
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")


    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver

# ==========================================
# OPEN APPS
# ==========================================
def open_chrome():
    os.system("start chrome")
    return "Opening Chrome"

def open_chatgpt():

    driver = get_driver()

    driver.get("https://chat.openai.com")

    return "Opening ChatGPT"

def open_gmail():

    driver = get_driver()

    driver.get("https://mail.google.com")

    return "Opening Gmail"


def open_brave():
    os.system("start brave")
    return "Opening Brave"


def open_edge():
    os.system("start msedge")
    return "Opening Edge"


def open_vscode():
    os.system("code")
    return "Opening VS Code"


def open_notepad():
    os.system("notepad")
    return "Opening Notepad"


def open_calculator():
    os.system("calc")
    return "Opening Calculator"


def open_paint():
    os.system("mspaint")
    return "Opening Paint"


def open_cmd():
    os.system("start cmd")
    return "Opening Command Prompt"


def open_powershell():
    os.system("start powershell")
    return "Opening PowerShell"


def open_file_explorer():
    os.system("explorer")
    return "Opening File Explorer"


def open_task_manager():
    os.system("taskmgr")
    return "Opening Task Manager"


def open_camera():
    os.system("start microsoft.windows.camera:")
    return "Opening Camera"


def open_settings():
    os.system("start ms-settings:")
    return "Opening Settings"


# ==========================================
# CREATE FOLDER
# ==========================================
def create_folder(name):

    desktop = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    path = os.path.join(desktop, name)

    os.makedirs(path, exist_ok=True)

    return f"Folder '{name}' created"


# ==========================================
# DELETE FOLDER
# ==========================================
def delete_folder(name):

    desktop = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    path = os.path.join(desktop, name)

    if os.path.exists(path):

        shutil.rmtree(path)

        return f"Folder '{name}' deleted"

    return "Folder not found"

# ==========================================
# SCREENSHOT
# ==========================================
def take_screenshot():

    filename = f"screenshot_{int(time.time())}.png"

    pyautogui.screenshot(filename)

    return f"Screenshot saved as {filename}"


# ==========================================
# TYPE TEXT
# ==========================================
def type_text(text):

    pyautogui.write(text, interval=0.05)

    return f"Typed: {text}"


# ==========================================
# COPY TEXT
# ==========================================
def copy_text(text):

    pyperclip.copy(text)

    return "Text copied to clipboard"


# ==========================================
# PASTE TEXT
# ==========================================
def paste_text():

    pyautogui.hotkey("ctrl", "v")

    return "Pasted text"

# ==========================================
# YOUTUBE SEARCH
# ==========================================
def youtube_search(query):

    driver = get_driver()

    # Reuse current tab
    # driver.switch_to.window(driver.current_window_handle)

    driver.get("https://youtube.com")

    time.sleep(2)

    search_box = driver.find_element(
        By.NAME,
        "search_query"
    )

    search_box.clear()

    search_box.send_keys(query)

    search_box.send_keys(Keys.RETURN)

    return f"Searching YouTube for {query}"

# ==========================================
# GOOGLE SEARCH
# ==========================================
def google_search(query):

    driver = get_driver()
    
    # Reuse current tab
    # driver.switch_to.window(driver.current_window_handle)

    driver.get("https://google.com")

    time.sleep(2)

    search_box = driver.find_element(
        By.NAME,
        "q"
    )
    
    search_box.clear()

    search_box.send_keys(query)

    search_box.send_keys(Keys.RETURN)

    return f"Searching Google for {query}"


# ==========================================
# GITHUB SEARCH
# ==========================================
def github_search(query):

    driver = get_driver()
    
    # driver.switch_to.window(driver.current_window_handle)

    driver.get("https://github.com")

    time.sleep(2)

    search_box = driver.find_element(
        By.NAME,
        "q"
    )
    
    search_box.clear()

    search_box.send_keys(query)

    search_box.send_keys(Keys.RETURN)

    return f"Searching GitHub for {query}"


# ==========================================
# LEETCODE SEARCH
# ==========================================
def leetcode_search(query):

    driver = get_driver()

    driver.get(
        f"https://leetcode.com/problemset/?search={query}"
    )

    return f"Searching LeetCode for {query}"


# ==========================================
# AMAZON SEARCH
# ==========================================
def amazon_search(query):

    driver = get_driver()
    
    # driver.switch_to.window(driver.current_window_handle)

    driver.get("https://amazon.in")

    time.sleep(2)

    search_box = driver.find_element(
        By.ID,
        "twotabsearchtextbox"
    )
    
    search_box.clear()

    search_box.send_keys(query)

    search_box.send_keys(Keys.RETURN)

    return f"Searching Amazon for {query}"


# ==========================================
# WIKIPEDIA SEARCH
# ==========================================
def wikipedia_search(query):

    driver = get_driver()

    driver.get(
        f"https://en.wikipedia.org/wiki/{query}"
    )

    return f"Searching Wikipedia for {query}"

def close_browser():

    global driver

    if driver is not None:

        driver.quit()

        driver = None

        return "Browser closed"

    return "Browser already closed"