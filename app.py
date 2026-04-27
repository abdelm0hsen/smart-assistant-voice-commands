import datetime
import os
import platform
import subprocess
import webbrowser

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()


def speak(text: str) -> None:
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen_command(recognizer: sr.Recognizer):
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except Exception:
        # Fallback helps run the project even on machines without microphone setup.
        return input("Type command (mic unavailable): ").strip().lower()


def open_local_app(app_name: str) -> bool:
    system = platform.system().lower()

    try:
        if app_name == "notepad":
            if system == "windows":
                subprocess.Popen(["notepad.exe"])
            elif system == "darwin":
                subprocess.Popen(["open", "-a", "TextEdit"])
            else:
                subprocess.Popen(["gedit"])
            return True

        if app_name == "calculator":
            if system == "windows":
                subprocess.Popen(["calc.exe"])
            elif system == "darwin":
                subprocess.Popen(["open", "-a", "Calculator"])
            else:
                subprocess.Popen(["gnome-calculator"])
            return True
    except FileNotFoundError:
        return False

    return False


def handle_command(command: str) -> bool:
    if not command:
        return True

    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Current time is {now}")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open notepad" in command:
        if open_local_app("notepad"):
            speak("Opening notepad")
        else:
            speak("Could not open notepad on this system")
    elif "open calculator" in command:
        if open_local_app("calculator"):
            speak("Opening calculator")
        else:
            speak("Could not open calculator on this system")
    elif command in {"quit", "exit", "stop"}:
        speak("Goodbye")
        return False
    else:
        speak("Sorry, I did not understand that command")

    return True


def main() -> None:
    recognizer = sr.Recognizer()
    speak("Smart assistant is ready. Say a command or type one.")

    running = True
    while running:
        command = listen_command(recognizer)
        running = handle_command(command)


if __name__ == "__main__":
    main()
