# Jarvis - Intelligent Virtual Assistant

## 📖 Overview
Jarvis is an AI-powered virtual assistant built with Python. It features both a Command-Line Interface (CLI) and a Tkinter Graphical User Interface (GUI). Jarvis utilizes OpenAI's GPT-4o-mini for intelligent conversational responses, Google Speech Recognition for voice commands, and gTTS (Google Text-to-Speech) for audio feedback. 

## ✨ Key Features
*   Voice & GUI Interaction: Control Jarvis via voice commands or through an interactive Tkinter GUI.
*   AI Chatbot (GPT-4o-mini): Utilizes the OpenAI API to answer questions and process complex prompts intelligently.
*   Web Automation: Opens popular websites (Google, YouTube, GitHub, LinkedIn, etc.) via voice commands.
*   Music Player: Plays predefined songs from YouTube links using the pygame library.
*   News Fetching: Uses the NewsAPI to fetch and read out the top 5 news headlines.
*   Voice Feedback: Provides audio responses using gTTS (Google Text-to-Speech) and pyttsx3.

## 🛠️ Tech Stack
*   Language: Python
*   GUI: Tkinter
*   APIs: OpenAI API, NewsAPI, Google Speech Recognition
*   Libraries: SpeechRecognition, gTTS, pyttsx3, pygame, requests, threading.

## 🚀 How to Run This Project Locally

1. Clone the repository:
   `bash
   git clone https://github.com/Madhav30100/jarvis-assistant.git
   cd jarvis-assistant

   python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

python main.py

python gui_app.py

<img width="374" height="284" alt="Screenshot 2026-09-29 092813" src="https://github.com/user-attachments/assets/99b648ee-03d7-4a09-a5f4-a8d0dd095fb2" />
