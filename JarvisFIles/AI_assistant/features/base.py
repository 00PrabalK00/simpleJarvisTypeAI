import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import wikipedia
import pyjokes
import pyautogui
import wikipediaapi

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
voicespeed = 140
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    mic_index = 0
    with sr.Microphone(device_index=mic_index) as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('User:', query)

    except:
        query = '--'
        print('User:', query)

    return query


def time():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(current_time)
    print(current_time)


def open_chrome():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    url = 'http://youtube.com/'
    webbrowser.get(chrome_path).open(url)


def wishes():
    speak("Welcome back Sir")
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    elif 18 <= hour < 24:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("How can I help you today?")


