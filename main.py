import pyttsx4
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import email_send_passwd


# first connect internet connection 
engine = pyttsx4.init("sapi5")          # Sapi5 - Microsoft Speech API(SAPI5) is the technogoly for voice recognition & synthesis product by Microsoft.
voice = engine.getProperty("voices")
# print(voice[0].id)                         # types of voices 0-david/ 1- zera
engine.setProperty("voice", voice[1].id)     # u can change the voice 0/1


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good Morning!!!")

    elif hour >=12 and hour <=18:
        speak("Good Afternoon!!!")

    else:
        speak("Good Evening!!!")

    print("I am Calci, How may I help you")          # u can change the name
    speak("I am Calci, How may I help you")          # u can change the name
    

def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:                            # when error comes
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said - {query}\n")

    except Exception as e:
        # print(e)
        print("Say That Again...")
        return "None"
    return query


def sendEmail(to_reciver, msg):
    
    from_sender = email_send_passwd.mail                    # sender mail id in separate file for security purpose
    pwd =  email_send_passwd.password                       # sender mail id passward(gmail 2 steps security) in separate file for sequrity purpose
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(user = from_sender, password = pwd)
    s.sendmail(from_sender, to_reciver, msg)
    s.quit()


if __name__ == "__main__":
    greet()
    while True:
    # if 1:
        query = takeCommand().lower()                       
        # logic for enecuting task based on query

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            speak("you tube is open sir")

        elif "open google" in query:
            webbrowser.open("google.com")
            speak("google is open sir")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")
            speak("gmail is open sir")
        
        elif "open whatsapp" in query:
            webbrowser.open("whatsapp.com")
            speak("whatsapp is open sir")

        elif "open notepad" in query:
            Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(Path)
            speak("notepad is open sir")

        elif "open chrome" in query:
            # webbrowser.open("google chrome.com")
            Path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"   # desktop right click - property - target(copy) give \\
            os.startfile(Path)                                                    # use os module to open 
            speak("chrome is open sir")

        elif 'play music' in query:
            music_dir = "D:\\All Songs\\2020 - 21- 22 New songs"    # give folder path and give double slash (\\)
            songs = os.listdir(music_dir)
            Random = random.choice(songs)                           # play random song from given path folder
            os.startfile(os.path.join(music_dir,Random))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is {strTime}")

        elif 'send email' in query:
            try:
                speak('What shall I say?')
                msg = takeCommand().lower()              # for speak and send mail
                speak("Write a message")         
                print(msg)
                speak("enter reciver emailID")
                to_reciver = input("Enter Reciver EmailID = ")
                sendEmail(to_reciver, msg) 
                speak('email has been sent')

            except Exception as e:
                print(e)


        elif "exit" in query:
            speak("Exit sir, Thank You")
            print("Exit sir, Thank You")
            exit()
