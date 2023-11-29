"""import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import wikipedia
import pyjokes
import pyautogui

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


if __name__ == "__main__":
    # wishes()
    while True:
        query = takecommand().lower()

        if "good morning" in query:
            speak("Good morning bro")
        elif "time" in query:
            time()
        elif "will AI takeover" in query:
            speak("Kill Yourself")
        elif "chrome" in query:  # quit to end the program
            speak("opening the Chrome")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            url = 'http://youtube.com/'
            webbrowser.get(chrome_path).open(url)
        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want tot opem

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()  # terminate
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "joke" in query:
            speak(pyjokes.get_joke())
            speak("Ha                Ha                 Ha")
        elif "funny" in query:
            speak("Thanks")
            speak("Would You like to hear another one")
            query = takecommand().lower()

            if "yes" in query:
                speak(pyjokes.get_joke())
                speak("Ha                Ha                 Ha")
            elif "no" in query:
                speak("Okay")
        elif "lock" in query:
            pyautogui.hotkey('winleft', 'k')
        elif "task manager" in query:
            pyautogui.hotkey('ctrl', 'shift', 'esc')
        elif "close app" in query:
            pyautogui.hotkey('alt', 'f4')
        elif "take screenshot" in query:
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")
"""