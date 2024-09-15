import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said :" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return take_command()
    return query


if __name__ == '__main__':

    speak("Jarvis activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'your name' in query:
            speak("I am Jarvis, a voice assistant developed by Shivam Gangal.")
        elif 'how are you' in query:
            speak("I am doing great sir. What can i do for you?")
        elif 'hi' in query:
            speak("Hello sir. What can i do for you?")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\Shivam Gangal\\AppData\\Local\\WhatsApp"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            speak("Good bye sir. Its been an honour to serve you.")
            exit(0)
        elif 'what' in query or 'who' in query or 'why' in query or 'when' in query or 'where' in query or 'how' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There were multiple results for your query. Please be more specific.")
            except Exception as e:
                speak("I couldn't find any results on Wikipedia. Please try again with a different query.")