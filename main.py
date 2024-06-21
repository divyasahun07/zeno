import TexttoSpeech
import SpeechtoText
import web_scrapping
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

def Main():
    while True:
        display_text.insert(str(tk.END), "Listening" + '\n')
        spoken_text = SpeechtoText.speech_to_text()
        display_text.insert(str(tk.END), "Recognizing" + '\n')
        if spoken_text == "goodbye" or spoken_text == "thanks" or spoken_text == "welcome" or spoken_text == "thank you":
            display_text.insert(str(tk.END),spoken_text+'\n')
            display_text.insert(str(tk.END),"Glad to help"+'\n')
            break
        else:
            if spoken_text=="Could not understand audio":
                display_text.insert(str(tk.END), spoken_text + '\n')
                TexttoSpeech.text_to_speech(spoken_text)
            else:
                result = web_scrapping.search_and_display(spoken_text)
                if type(result)==list:
                    for re in result:
                        display_text.insert(str(tk.END), re + '\n')
                else:
                    display_text.insert(str(tk.END), spoken_text + '\n')
                    display_text.insert(str(tk.END), result + '\n')
                    TexttoSpeech.text_to_speech(result)
                    display_text.see(tk.END)

def start_listening():
    thread = Thread(target=Main)
    thread.start()

root = tk.Tk()
root.title("Voice Assistant")

display_text = scrolledtext.ScrolledText(root, width=60, height=20)
display_text.pack(padx=10, pady=10)

listen_button = tk.Button(root, text="Listen", command=start_listening)
listen_button.pack(pady=10)

root.mainloop()
