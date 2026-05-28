from assistant.registry import TOOLS

from commands.files import (
    create_folder,
    delete_folder
)

from commands.browser import (
    youtube_search,
    type_text,
    google_search,
    github_search,
    leetcode_search,
    amazon_search,
    wikipedia_search
)


def route_command(command):

    command = command.lower().strip()

    print("ROUTER RECEIVED:", command)

    # =====================================
    # STATIC TOOLS
    # =====================================

    if command in TOOLS:

        return TOOLS[command]()

    # =====================================
    # CREATE FOLDER
    # =====================================

    if "create folder" in command:

        name = command.replace(
            "create folder",
            ""
        ).strip()

        return create_folder(name)

    # =====================================
    # DELETE FOLDER
    # =====================================

    if "delete folder" in command:

        name = command.replace(
            "delete folder",
            ""
        ).strip()

        return delete_folder(name)

    # =====================================
    # TYPE TEXT
    # =====================================

    if command.startswith("type "):

        text = command.replace(
            "type ",
            ""
        ).strip()

        return type_text(text)

    # =====================================
    # YOUTUBE SEARCH
    # =====================================

    if "youtube" in command:

        query = extract_query(command)

        return youtube_search(query)

    # =====================================
    # GOOGLE SEARCH
    # =====================================

    if "google" in command:

        query = extract_query(command)

        return google_search(query)

    # =====================================
    # GITHUB SEARCH
    # =====================================

    if "github" in command:

        query = extract_query(command)

        return github_search(query)

    # =====================================
    # LEETCODE SEARCH
    # =====================================

    if "leetcode" in command:

        query = extract_query(command)

        return leetcode_search(query)

    # =====================================
    # AMAZON SEARCH
    # =====================================

    if "amazon" in command:

        query = extract_query(command)

        return amazon_search(query)

    # =====================================
    # WIKIPEDIA SEARCH
    # =====================================

    if "wikipedia" in command:

        query = extract_query(command)

        return wikipedia_search(query)

    return "Unknown command"


# ==========================================
# QUERY PARSER
# ==========================================

def extract_query(command):

    separators = [
        "for",
        "per",
        "about"
    ]

    for sep in separators:

        if sep in command:

            return command.split(
                sep,
                1
            )[1].strip()

    return ""