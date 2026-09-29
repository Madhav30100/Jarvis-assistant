import speech_recognition as lg
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = lg.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR_API_KEY"


# 🔊 Offline TTS
def speak_old(text):
    engine.say(text)
    engine.runAndWait()


# 🔊 Online TTS
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


# 🎯 Command Processing
def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open github" in c:
        webbrowser.open("https://github.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open chatgpt" in c:
        webbrowser.open("https://chatgpt.com")

    elif "open anime" in c:
        webbrowser.open("https://hianime.sx/home")

    elif "open pokemon" in c:
        webbrowser.open("https://hianime.sx/pokemon-2097")

    # 🎵 Music
    elif "play" in c:
        song = c.split(" ")[-1]
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found")

    # 📰 News
    elif "news" in c:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Failed to fetch news")


# 🚀 Main Program
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = lg.Recognizer()
        print("Listening...")

        try:
            with lg.Microphone() as source:
                print("Recognizing...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes sir")

                with lg.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processCommand(command)

        except Exception as e:
            print(f"Error: {e}")