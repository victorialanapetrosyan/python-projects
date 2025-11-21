from customtkinter import *
from tkinter import filedialog
from gtts import gTTS
import os

app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")

def text_to_speech():
    text = entry.get()
    language='en'
    output = gTTS(text=text,lang=language,slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")

def file_to_speech():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file to convert to speech")
    text = open(f'{filename}','r').read()
    language='en'
    output = gTTS(text=text,lang=language,slow=False)
    output.save('fileoutput.mp3')
    os.system("start fileoutput.mp3")



button = CTkButton(master=app, text="Convert text to speech",corner_radius=32, command=text_to_speech, fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2)
button.place(relx=0.5,rely=0.5,anchor="center")
file_button = CTkButton(master=app, text="upload file",corner_radius=32, command=file_to_speech, fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2)
file_button.place(relx=0.5,rely=0.7,anchor="center")

entry = CTkEntry(master=app, placeholder_text="Start typing to convert text to speech...", width=300,
                text_color="#FFCC70")

entry.place(relx=0.5, rely=0.4, anchor="center") 

label = CTkLabel(master=app, text="Text to Speech Converter", font=("Arial", 20), text_color="#FFCC70")

label.place(relx=0.5, rely=0.3, anchor="center") 

app.mainloop()