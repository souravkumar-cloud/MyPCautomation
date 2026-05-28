from assistant.registry import TOOLS
from commands.files import create_folder
from commands.browser import youtube_search,type_text,delete_folder,google_search,github_search,leetcode_search,amazon_search,wikipedia_search

def route_command(command):
    command=command.lower()
    if command in TOOLS:
        return TOOLS[command]()
    
    elif command.startswith("create folder"):
        name=command.replace("create folder","").strip()
        
        return create_folder(name)
    
    elif command.startswith("search youtube for"):
        query=command.replace("search youtube for","").strip()
        
        if not query:
            return "Please provide a search query"
        
        return youtube_search(query)
    
    elif command.startswith("type "):

        text = command.replace("type ", "")

        return type_text(text)


    elif command.startswith("create folder"):

        name = command.replace(
            "create folder",
            ""
        ).strip()

        return create_folder(name)


    elif command.startswith("delete folder"):

        name = command.replace(
            "delete folder",
            ""
        ).strip()

        return delete_folder(name)


    # elif command.startswith("search youtube for"):

    #     query = command.replace(
    #         "search youtube for",
    #         ""
    #     ).strip()

    #     return youtube_search(query)


    elif command.startswith("search google for"):

        query = command.replace(
            "search google for",
            ""
        ).strip()

        return google_search(query)


    elif command.startswith("search github for"):

        query = command.replace(
            "search github for",
            ""
        ).strip()

        return github_search(query)


    elif command.startswith("search leetcode for"):

        query = command.replace(
            "search leetcode for",
            ""
        ).strip()

        return leetcode_search(query)


    elif command.startswith("search amazon for"):

        query = command.replace(
            "search amazon for",
            ""
        ).strip()

        return amazon_search(query)


    elif command.startswith("search wikipedia for"):

        query = command.replace(
            "search wikipedia for",
            ""
        ).strip()

        return wikipedia_search(query)
    
    return "Unknown command"
    