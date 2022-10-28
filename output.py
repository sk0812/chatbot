from speak import speak
import configparser

config = configparser.ConfigParser()



def stop_talking():

    config.read('config.ini')
    speech = config['assistant']['speech']

    if speech == "False":
        print("I am already not talking!")
    else:
        config['assistant']['speech'] = "False"
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        print("Okay I will stop talking now.")

def start_talking():

    config.read('config.ini')
    speech = config['assistant']['speech']

    if speech == "True":
        print("I am already talking!")
    else:
        config['assistant']['speech'] = "True"
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        print("Okay I will start talking now.")

def output(text):

    config.read('config.ini')
    speech = config['assistant']['speech']

    print(text)
    if speech == "True":
        speak(text)
    else:
        pass