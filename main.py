import speech_recognition as sr
import  pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
def talk(text):
    alexa.say(text)
    alexa.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
            else:
                print("I am Alexa, Not the one you called!")
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I: %M %p")
        print(time)
        talk('Current time is: '+time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "date" in command:
        date = 'Sorry I am not available for this'
        print(date)
        talk(date)
    else:
        el ="Sorry I can't understand. Say it again"
        print(el)
        talk(el)
while True:
    run_alexa()