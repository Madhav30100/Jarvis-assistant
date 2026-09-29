import tkinter as tk
import threading
import speech_recognition as lg
from main import speak, processCommand

# Assuming you already have speak() and processCommand() from your main code

def jarvis_loop():
    r = lg.Recognizer()
    speak("Jarvis started")

    while True:
        try:
            with lg.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes sir")

                with lg.Microphone() as source:
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processCommand(command)

        except Exception as e:
            print("Error:", e)


def start_jarvis():
    thread = threading.Thread(target=jarvis_loop)
    thread.daemon = True
    thread.start()


# UI
root = tk.Tk()
root.title("Jarvis Assistant")
root.geometry("300x200")

label = tk.Label(root, text="Jarvis Voice Assistant", font=("Arial", 14))
label.pack(pady=20)

btn = tk.Button(root, text="Start Jarvis", command=start_jarvis)
btn.pack(pady=10)

root.mainloop()