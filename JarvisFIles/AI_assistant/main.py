import subprocess
import webbrowser

import pyautogui
from pyjokes import pyjokes
from wikipedia import wikipedia
from AI_assistant.features.base import takecommand, speak, time, wishes

import tkinter
import urllib.request

root_url = "http://192.168.52.24"
window = tkinter.Tk()
window.title("GUI")


def sendRequest(url):
    n = urllib.request.urlopen(url)  # send request to ESP


def a():
    sendRequest(root_url + "/ledon")
    # print("Led is on")


def b():
    sendRequest(root_url + "/ledoff")
    # print("Led is off")


def c():
    sendRequest(root_url + "/purple")
    # print("Led is on")


if __name__ == "__main__":
    wishes()
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
            speak("What should I search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takecommand().lower()
            webbrowser.get(chromepath).open_new_tab("https://www.google.com/search?q=" + search)
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
        elif "dark" in query:
            a()
            speak("the led is turned off")
        elif "light" in query:
            b()
            speak("the led is turned on")



