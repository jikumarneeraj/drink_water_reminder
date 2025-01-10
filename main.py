from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
import time
from plyer import notification
import pyttsx3

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water.",
            message="Water is very important for our body for maintaining proper hydration.",
            app_icon=r'water.ico",
            timeout=10
        )
        speak("Drink the water")
        time.sleep(2)
