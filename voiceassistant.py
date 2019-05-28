# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:52:08 2019

@author: harshvardhan
"""
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def ask():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(src)
        
    try:
        print("Recognizing....")
        qr = r.recognize_google(audio,language='en-in')
        print(f"User Said : {qr}\n")
        
    except Exception:
        speak("Say that again please")
        return "NONE"
    return qr    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hr= int(datetime.datetime.now().hour)
    if(hr>=0 and hr<12):
        speak("Good Morning")
    elif(hr>=12 and hr<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("I am Your Personal Voice Assistance How May I help You")
    
if __name__=="__main__":
    greeting()
    while True:
        query=ask().lower()
        
        if 'wikipedia' in query:
            speak("Opening Wikipedia..")
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open browser' in query:
            os.system(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open spotify' in query:
            speak("Do you want to open the application or on browser")
            reply=ask().lower()
            if 'application' in reply:
                os.startfile(r"C:\Users\harshvardhan\AppData\Roaming\Spotify\Spotify.exe")
                
            else:
                webbrowser.open("spotify.com")
          
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open whatsapp' in query:
            os.startfile(r"C:\Users\harshvardhan\AppData\Local\WhatsApp\WhatsApp.exe")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = "C:\\Users\\harshvardhan\\Music\\"
            songs = [each for each in os.listdir(music_dir) if each.endswith('.mp3')]
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"It is {time}")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        
        elif 'exit' in query:
            raise SystemExit
            
        
    
    
    