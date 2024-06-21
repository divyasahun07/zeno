import pyttsx3
def text_to_speech(spoken_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 0.5)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(spoken_text)
    engine.runAndWait()
    if spoken_text in ["bye", "goodbye", "thanks"]:
        text_to_speech("Glad I could help!")
        return