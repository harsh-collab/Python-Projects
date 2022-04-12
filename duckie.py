import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your assistant, how may I help you?")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,  language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshsaraswat13@gmail.com', '9887781001H')
    server.sendmail('harshsaraswat13@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open amazon prime' in query:
            webbrowser.open('primevideo.com')

        elif 'open gmail' in query:
            webbrowser.open('mail.google.com')

        elif 'open amazon' in query:
            webbrowser.open('amazon.in')
            
        elif 'stop' in query:
            speak('quitting')
            quit()

        elif 'who am i' in query:
            speak('you are harsh, developer of this program')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'visual studio' in query:
            codePath = "E:\Visual Studio\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'send' in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = 'harshsaraswat13@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
            except exception as e:
                print(e)
                speak('Sorry, i could not send this email')

            
            
            





        
        
    
    