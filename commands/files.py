import os
import shutil


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