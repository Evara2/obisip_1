import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.WaitTimeoutError:
        print("No speech detected within the timeout period.")
        return ""
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
        
    elif "weather" in command:
        speak("What is your city name?")
        city = listen()
        if city:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            url = f"https://www.google.com/search?q=weather in {city} on {current_date}"
            webbrowser.open(url)
            speak(f"Here is the weather forecast for {city} on {current_date}")
        
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What would you like to search for?")
        search_query = listen()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm sorry, I don't understand that command.")
    return True

def main():
    speak("Hello! I'm your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        if command and not process_command(command):
            break

if __name__ == "__main__":
    main()