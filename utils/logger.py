from datetime import datetime

LOG_FILE="logs/history.txt"

def log(message):
    with open(LOG_FILE,'a') as f:
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        f.write(f"[{time}] {message}\n")