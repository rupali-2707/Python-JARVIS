import pyttsx3 #(For Speak)
#also pip install pyaudio (for recogniting)
import datetime 
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui #(For Screenshot)
import psutil 
import pyjokes 
import random
import operator
import json
import wolframalpha
import time
from urllib.request import urlopen
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    speak("the current time is")
    speak(Time)
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    speak(Time)


def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome !")
    speak("what is your name")
    global name
    name = TakeCommand()
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning "+name)
    elif hour >=12 and hour<18:
        speak("Good Afternoon !"+name)
    elif hour >=18 and hour <24:
        speak("Good Evening !"+name)
    else:
        speak("Good Night !"+name)
    speak("Jarvis at your service. Please tell me how can I help you?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png") #saves screenshot in file location


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


def Introduction():
    speak("I am PYTHON JARVIS , Personal AI assistant , "
    "I am created by , "+name+  "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")



    
if __name__ == '__main__':


    clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file
    clear()

    wishme()
    
    while True:
        query = TakeCommand().lower()
        # All the commands said by user will be 
		# stored here in 'query' and will be 
		# converted to lower case for easily 
		# recognition of command 

        if 'time' in query:
            time_()

        elif 'date' in query:
            date()

        elif 'how are you' in query:
            speak("I am fine, Thanks for asking")
            speak("How are you?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)

        elif 'search google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        
        #elif 'search' in query: 
            #query = query.replace("query","")
            #wb.open(query)
        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")

        elif "why you came to this world" in query:
            speak("Thanks to" +name+  "further it is a secret")

        elif 'word' in query:
            speak("opening MS Word")
            word = r'C:\Program Files\WindowsApps\Microsoft.Office.Desktop.Word_16051.13530.20316.0_x86__8wekyb3d8bbwe\Office16\WINWORD.EXE'
            os.startfile(word)


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")


        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        
        
        elif 'play songs' in query:
            video ='songs_path'  #add path
            audio = 'Songs_path'#add path
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                       #used while loop to keep the jarvis on the speak command untill req. command is given.
                speak("I could not understand you. Please Try again.")          #first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to reuirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block. 
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    #'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
            elif 'random' in rand:
                    rand = random.randint(1,219)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
                

            
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        
        
        elif 'write a note' in query:
            speak('what should i write ?')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak('rupali should i include date and time?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans :
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-\n')
                file.write(notes)
                speak('done taking notes')
            else:
                file.write(notes)

        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

       
        elif 'news' in query:
            
            try:

                jsonObj = urlopen('''http://newsapi.org/v2/everything?q=tesla&from=2021-01-04&sortBy=publishedAt&apiKey=793bf44e31e043d09e804ba6859d8121''')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 


                
        
        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")    


        elif 'cpu' in query:
            cpu()


        elif 'joke' in query:
            jokes()


        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()


        
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

     

        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        #quit
        elif 'offline' in query:
            speak("going Offline")
            quit()
