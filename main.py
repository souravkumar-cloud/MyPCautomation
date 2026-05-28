from assistant.router import route_command
from utils.logger import log
from utils.speech import speak

def main():
    speak("Nexus Assistant Started")
    
    while(True):
        command=input("Enter command: ")
        log(command)
        
        if command.lower()=='exit':
            speak("Bye Bye !")
            
            break
        
        try:
            res=route_command(command)
            speak(res)
        except Exception as e:
            speak("Error occurred")
            print(e)
            
            
if __name__=="__main__":
    main()