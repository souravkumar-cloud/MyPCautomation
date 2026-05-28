import os 
from config.settings import SUPPORTED_APPS

def open_app(app_name):
    if app_name in SUPPORTED_APPS:
        os.system(SUPPORTED_APPS[app_name])
        return f"{app_name} opened"
    
    return "Application not supported"