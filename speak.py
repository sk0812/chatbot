# imports pyaudio and google speech recgonition
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
