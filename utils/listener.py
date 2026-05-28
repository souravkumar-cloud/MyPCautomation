import speech_recognition as sr

recognizer = sr.Recognizer()

# Better sensitivity
recognizer.energy_threshold = 300

# Dynamic adjustment
recognizer.dynamic_energy_threshold = True

def listen():

    try:

        with sr.Microphone() as source:

            print("Listening...")

            # Reduce noise calibration
            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")

        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text.lower()

    except sr.WaitTimeoutError:

        print("Timeout")

        return ""

    except sr.UnknownValueError:

        print("Could not understand")

        return ""

    except Exception as e:

        print(e)

        return ""