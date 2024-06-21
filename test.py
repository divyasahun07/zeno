
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from googlesearch import search
def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for user input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:
        return "Could not understand audio"

# Example usage:

def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 200)  # Speed of speech
    engine.setProperty('volume', 0.5)  # Volume level (0.0 to 1.0)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    # Convert text to speech
    engine.say(text)

    engine.runAndWait()

def SearchFunc(Spoken_text):
    
    user_query = Spoken_text
    print(user_query)
    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    if user_query=="Could not understand audio":
        text_to_speech(user_query)
    else:
        try:
            page = requests.get(URL,headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            result = soup.find('div', class_='Z0LcW').get_text()
            text_to_speech(result)
        except Exception as e:
            search_results = search(user_query, num_results=10)
            text_to_speech("here these are the top results")
            for result in search_results:
                print(result)

while True:
    spoken_text=speech_to_text()
    if spoken_text.lower()=="bye" or spoken_text.lower()=="goodbye" or spoken_text.lower()=="thanks":
        text_to_speech("Glad i could help")
        break
    else:
        SearchFunc(spoken_text)
        

# year of first fifa world cup
# age of ronaldo
# height of burj khalifa
# when was leonardo di vinci born
# prime minister of uk
# what is the weight of earth
        