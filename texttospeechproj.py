import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            commands = listener.recognize_google(voice)
            commands = commands.lower()
            if 'alexa' in commands:
                commands = commands.replace('alexa', '')
                print(commands)
    except:
        return 0
        pass
    return commands

from googletrans import Translator


def run_alexa():
    command = take_command()
    print(command)
    if "stop" in command:
        talk('Have a Nice Day.')
        return 2
    elif "telugu" in command:
        telugu_translation = translate_english_to_telugu(command)
        print(telugu_translation)
        talk(telugu_translation)
        return 1

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        return 1
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        return 1
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        return 1
    elif 'date' in command:

        talk('sorry, I have a headache')
        return 1
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        return 1
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        return 1
    else:
        talk('Please say the command again.')
        return 1
    return 1


while True:
    k=run_alexa()
    if k==2:
        
        break