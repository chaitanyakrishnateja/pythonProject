import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

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
            print("M.O.N.D.A.Y is Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'monday' in command:
                command = command.replace('monday'+' ')
                print(command)
    except:
        pass
    return command

def run_monday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('current time is' + time)
        print(time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d,%B,%Y')
        talk(date)
        print(date)
    elif 'tell me about' in command :
        person = command.replace('tell me about' , ' ')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'search' in command:
        new=2
        tabUrl ="https://google.com/?#q="
        term = command.replace('monday search', ' ')
        talk("opening"  + term)
        webbrowser.open(tabUrl + term,new=new)

run_monday()




