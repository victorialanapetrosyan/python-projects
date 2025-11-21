from gtts import gTTS 
import os
from tkinter import *
from tkinter import filedialog
root = Tk()
canvas = Canvas(root,width=400,height=300)
canvas.pack()

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



entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text="Start",command=text_to_speech)
canvas.create_window(200,230, window=button)
file_button = Button(text="from file",command=file_to_speech)
canvas.create_window(200,280, window=file_button)





root.mainloop()




