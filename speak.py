# imports pyaudio and google speech recgonition
import pyttsx3
import speech_recognition as sr
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
rate = config['assistant']['speechRate']
rate = int(rate)


engine = pyttsx3.init()
engine.setProperty('voice', "com.apple.speech.synthesis.voice.kate.premium")
engine.setProperty('rate', rate)


voices = engine.getProperty('voices')

# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello, my name is Atlas!")