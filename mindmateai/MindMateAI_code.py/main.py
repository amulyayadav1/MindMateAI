# MindMate AI - Emotion Aware Reminder Assistant
# Author: Bairaboina Amulya
# Description: An intelligent reminder assistant that adapts notifications based on emotion and mode.

import datetime
import time
import pyttsx3
import speech_recognition as sr
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)   # Speed of voice
engine.setProperty('volume', 1.0) # Volume

# Modes available
modes = ["Library Mode", "Work Mode", "Relax Mode"]
current_mode = "Work Mode"

# Sample emotion states (mock)
emotions = ["happy", "sad", "tired", "stressed", "neutral"]

# Function to speak
def speak(text):
    print(f"MindMate AI: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to detect emotion (simulated for demo)
def detect_emotion():
    emotion = random.choice(emotions)
    print(f"[Emotion Detected: {emotion}]")
    return emotion

# Function to take voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your reminder...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    try:
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    except:
        speak("Sorry, I couldn't hear you properly. Please type your reminder instead.")
        return input("Type your reminder: ")

# Function to set reminder
def set_reminder(task, remind_time):
    speak(f"Reminder set for {task} at {remind_time}.")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == remind_time:
            emotion = detect_emotion()
            if current_mode == "Library Mode":
                speak(f"Hey, it’s time for your reminder: {task}. (Silent alert mode)")
            elif current_mode == "Work Mode":
                speak(f"Reminder Alert! {task}. Stay focused.")
            else:
                speak(f"Hey there! Time for {task}. You’ve got this!")
            break
        time.sleep(30)  # check every 30 seconds

# ----------------- MAIN PROGRAM -----------------

speak("Hello! I'm MindMate AI, your personal reminder assistant.")
speak(f"Currently, I’m in {current_mode}.")
speak("Would you like to set a new reminder? (yes/no)")

choice = input("Enter your choice: ").lower()

if choice == "yes":
    task = take_command()
    remind_time = input("Enter time in HH:MM format (24-hour): ")
    speak(f"Setting reminder for {task} at {remind_time}.")
    set_reminder(task, remind_time)
else:
    speak("Alright! Have a productive day.")