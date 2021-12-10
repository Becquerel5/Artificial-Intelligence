import pyttsx3
from pyttsx3 import engine
import speech_recognition as sr
import datetime
from typing import Text
import wikipedia
import pywhatkit 
import pyjokes
import smtplib
import webbrowser
import os





listener = sr.Recognizer()

MASTER = " Master Fresnel"

#engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time =datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)   
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)    
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year) 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('my email', 'password')
    server.sendmail(" email", to,content)
    server.close()
def wishme():  
    speak("Welcome back sir!") 
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour= datetime.datetime.now().hour
    if hour>=0 and hour <12:
        speak("Good Morning" +MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" +MASTER)
    elif hour>=18 and hour<24:
        speak("Good Evening" +MASTER)    

    else:
        speak("Good Night " +MASTER)
    speak("intellect at your service.. What can i do for you sir!!")    
def takeCommand():
    """ r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Listening...")
        query = r.recognize_google(audio, language = 'en-in')
        print(query) """
    try:
        with sr.Microphone() as source:
            print('i am ready, Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice) 
            command =command.lower()
            if 'intellect' in command:
                command = command.replace('intellect', '')
                print(command)
        """ except Exception as e:
            print(e)
            speak("say that again please...")
            
        return command        """
    except:
        pass
    return command
def run_intellect():
    command = takeCommand()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)  
        pywhatkit.playonyt(song)

    elif 'wikipedia' in command:
        speak('Searching Wikipedia...')
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences =2)
        print(results) 
        speak(results)

    elif 'play music' in command:
        songs_dir ="C:\\AI\\song"
        songs = os.listdir(songs_dir)
        print(songs) 
        os.startfile(os.path.join(songs_dir,songs[0]))

    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        print(time)
        speak('The Current time is' + time)  

    elif 'family' in command:
        speak('the total familly is composed of 8 members.')
    elif 'parents' in command:
        speak('Your parents names are Donfack ' +MASTER)    
    elif 'elder' in command:
        speak('Your elder is Becquerel' +MASTER)    
    elif 'junior' in command:
        speak('Your junior is Papito alias Stein' +MASTER)        
    elif 'who is'  in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    elif 'open youtube' in command:
        url = "youtube.com"
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url) 

    elif 'your father is' in command:
        speak('My father is dfd')

    elif 'the time' in command():
        strTime = datetime.now.strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in command():  
        codepath = ""
        os.startfile(codepath) 

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'email to me' in command:
        try:
            speak("what should i send")
            content = takeCommand()
            to = "Donfackfresnel4@gmail.com"
            sendEmail(to, content)
            speak("Email send succesful")
        except Exception as e:
            print(e)
    else:
        speak('Please say it again sir. I didnot understood ')
while True:
    wishme()
    run_intellect()

