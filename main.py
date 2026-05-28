from assistant.router import route_command
from utils.logger import log
from utils.speech import speak
from utils.listener import listen

def main():

    speak("Nexus Assistant Started")

    while True:

        # Listen for voice command
        command = listen()

        # Skip empty recognition
        if not command:
            continue

        # Debug print
        print("RAW COMMAND:", command)

        # Save command in logs
        log(command)

        # Exit command
        if "exit" in command:

            speak("Goodbye")

            break

        try:

            # Execute command
            result = route_command(command)

            print("RESULT:", result)

            # Speak response
            speak(result)

        except Exception as e:

            speak("Error occurred")

            print("ERROR:", e)

if __name__ == "__main__":
    main()