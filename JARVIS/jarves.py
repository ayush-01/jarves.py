import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import requests
import subprocess
import time
import winshell
import wolframalpha   #nlb-natural language processing.

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WisMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir! ")

    elif hour >= 19 and hour < 23:
        speak("Good evening sir!")

    speak("I am your Assistant Jarvis 1 point o, please tell me sir how may i help you") 
    


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        speak("say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rshkumar697@gmail.com', 'rishu@45')
    server.sendmail('iamamit.kumar267@gmail.com', to, content)
    server.close() 


app = wolframalpha.Client("9EXQHV-KL98LAJX6X")
if __name__ == "__main__":
    WisMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query or 'start youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube sir!")

        elif 'open google' in query or 'start google' in query:
            webbrowser.open("google.com")
            speak("opening google sir!")

        elif 'open stack overflow' in query or 'start stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow sir!")

        elif 'open facebook' in query or 'start facebook' in query:
            webbrowser.open("Facebook.com")
            speak("opening facebook sir!")

        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music sir!") 
            music_dir = "C:\\Users\\HP\\Desktop\\my music"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1]))    

        elif 'what is the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

 

        elif 'open code' in query or 'open visual studio code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening code sir!")

        elif 'open zoom' in query or 'start zoom' in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
            speak("opening zoom sir!")

        elif 'open my CBSE guide' in query or 'start mycbseguide' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\Application"
            os.startfile(codePath)
            speak("opening my CBSE guide sir!")    


        elif 'open whatsapp' in query or 'start whatsapp' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\Application"
            os.startfile(codePath)
            speak(" opening whatsapp sir!")

        elif 'open internet explorer' in query or 'open explorer' in query:
            codePath = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
            os.startfile(codePath)
            speak(" opening internet explorer sir")

        elif 'open wo mic' in query or 'open mic' in query:
            codepath = "C:\\Program Files (x86)\\WOMic\\WOMicClient.exe"
            os.startfile(codepath)
            speak("opening wo mic sir")



        elif 'open opera' in query or 'open opera gx' in query:
            codepath ="C:\\Users\\HP\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(codepath)
            speak("opening opera gx sir!")           
        elif 'open anaconda navigator' in query or 'open anaconda' in query:
            codepath ="C:\\Users\\HP\\anaconda3\\pythonw.exe C:\\Users\\HP\\anaconda3\\cwp.py C:\\Users\\HP\\anaconda3 C:\\Users\\HP\\anaconda3\\pythonw.exe"
            os.startfile(codepath)
            speak("opening anaconda navigator sir!")          

        elif 'open python ' in query or 'open python 3.9' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
            os.startfile(codepath)
            speak("opening python sir!") 

        elif 'open covid-19 meter ' in query or 'open covid-19.org' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\Application\\chrome_proxy.exe  --profile-directory=Default --app-id=fcccjaecoeiiilchcaljkepeadfgnhla"
            os.startfile(codepath)
            speak("opening covid19.org sir!")

        elif 'open excel' in query or 'ms excel' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)
            speak("opening excel sir!")

        elif 'open powerpoint' in query or 'ms powerpoint' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)
            speak("opening powerpoint sir!")

        elif 'open word' in query or 'ms word' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
            speak("opening word sir!")

        elif 'open access' in query or 'ms access' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
            os.startfile(codePath)
            speak("opening access sir!")

        elif 'open publisher' in query or 'ms publisher' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE"
            os.startfile(codePath)
            speak("opening publisher sir!")



        elif '.in' in query or '.com' in query:
            webbrowser.open(f"https://www.google.com/search?&q={query}")
            speak("opening the website for you sir!")

        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "iamamit.kumar267@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send this email at this time ")

        elif 'jarves quit' in query or 'exit' in query or 'close' in query or 'quit jarvis' in query:
            speak("Thanks for using jarvis")
            print("Thanks for using jarvis")
            exit()
   

        elif 'hey jarvis' in query:
            speak("yes sir what can i do for you")
            speak("you can assign me work like opening apps for you telling you time etcetera ")
            print("yes sir what can i do for you")
            print("you can assign me work like opening apps for you telling you time etc. ")

        elif 'awesome' in query or 'amazing' in query or 'wonderful' in query:
            speak("Thank you sir, i am here to help you") 

        elif 'who is' in query or 'what is' in query or 'can you' in query or 'where is' in query:
            (f"https://www.google.com/search?&q={query}")
            speak(wikipedia.summary(query,sentences=2)) 
            print(wikipedia.summary(query,sentences=2)) 

        elif 'who are you' in query:
            speak("I am jarvis, An AI which is made by Mister Aayush kumar")

        elif 'made you' in query:
            speak("I have been  made by mister Aayush kumar")    

        elif 'why are you made' in query:
            speak("i am maked for making the work easier of the humanbeings as we know that an AI makes it possible for machines to learn from experiance, adjust to new inputs and perform human like task, I am same as alexa and google assistant.")

        elif ' better' in query:
            speak("we all are good at our work, but i think that the voice of alexa is better than me")

        elif 'where do you live' in query:
            speak("I live in the the laptop of the person who made me, his name is Aayush kumar")

        elif 'how are you' in query:
            speak("i am fine sir")
            speak("how are you")

        elif 'which language is used to make you' in query or 'language is used' in query  or 'you are made' in query:
            speak("I am made with python language, which is high level language, and it is an object oriented programing language ")  

        
        elif "good morning" in query:
            speak("A warm" +query) 
            speak("How are you Mister") 
            speak("i am jarvis your desktop aasistant") 

        elif "good nignt" in query:
            speak("good night sir")
            speak(" have a good sleep")
            speak("we will meet tommorow")        
            
        elif 'fine' in query or 'good' in query:
            speak("its good to know that you are fine!") 

        elif 'tell me a joke' in query or 'joke in query' in query:
            speak(pyjokes.get_jokes())

        elif 'clear the recycle bin' in query or 'empty the recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("your recycle bin has been recycled")

        elif "dont listen" in query or "stop listening" in query:
            speak("for how much time you want me to stop listen")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'weather' in query or 'temperature'in query:
            res = app.query(query)
            speak(next(res.results).text)
            print(next(res.results).text)

        elif 'calculate' in query:
            speak("what should i calculate?")
            print("what should i calculate?")
            gh = takeCommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)
            print(next(res.results).text)

                   



