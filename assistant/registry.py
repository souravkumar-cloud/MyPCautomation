from commands.apps import open_app
from commands.system import (
    take_screenshot,
    shutdown_pc,
    restart_pc,
    lock_pc,
)
from commands.files import (
    create_folder,
    delete_folder,
)
from commands.browser import (
    youtube_search,
    google_search,
    github_search,
    leetcode_search,
    amazon_search,
    wikipedia_search,
)

from commands.typing import (
    type_text,
    copy_text,
    paste_text,
)


TOOLS = {

    # =====================================
    # APPS
    # =====================================
    "open chrome": lambda: open_app("chrome"),

    "open brave": lambda: open_app("brave"),

    "open edge": lambda: open_app("edge"),

    "open vscode": lambda: open_app("vscode"),

    "open notepad": lambda: open_app("notepad"),

    "open calculator": lambda: open_app("calculator"),

    "open paint": lambda: open_app("paint"),

    "open cmd": lambda: open_app("cmd"),

    "open powershell": lambda: open_app("powershell"),

    "open explorer": lambda: open_app("explorer"),

    "open task manager": lambda: open_app("taskmanager"),

    "open camera": lambda: open_app("camera"),

    "open settings": lambda: open_app("settings"),

    "open spotify": lambda: open_app("spotify"),

    "open whatsapp": lambda: open_app("whatsapp"),

    "open telegram": lambda: open_app("telegram"),

    "open discord": lambda: open_app("discord"),

    # =====================================
    # SYSTEM
    # =====================================
    "take screenshot": take_screenshot,

    "shutdown pc": shutdown_pc,

    "restart pc": restart_pc,

    "lock pc": lock_pc,

    # =====================================
    # TYPING
    # =====================================
    "copy text": lambda: copy_text(),

    "paste text": lambda: paste_text(),

}