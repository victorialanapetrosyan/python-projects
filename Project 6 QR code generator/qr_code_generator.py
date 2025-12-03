from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import png
# qr code generation works by turning a link into a qr code with the pyqrcode module
root = Tk()

def generate_qr(name,link):
    # generate image file
    file_name = name + ".png"
    # generate url for qr code
    url = pyqrcode.create(link)
    # then we generate the png image of this qr code
    url.png(file_name,scale=8)
    # create the image so it will display on our tkinter window
    image = ImageTk.PhotoImage(Image.open(file_name))
    # display the image onto this label
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,400,window=image_label)



canvas = Canvas(root,width=400,height=600)
canvas.pack()

app_label = Label(root,text="QR Code generator", fg='blue', font=("Arial", 30))
canvas.create_window(200,50, window=app_label)

name_label = Label(root,text="Link name")
name_entry = Entry(root)

link_label = Label(root,text="Link")
link_entry = Entry(root)

canvas.create_window(200,100, window=name_label)
canvas.create_window(200,160, window=link_label)
canvas.create_window(200,130, window=name_entry)
canvas.create_window(200,180, window=link_entry)

button = Button(text="Generate QR code", command=lambda: generate_qr(name_entry.get(),link_entry.get()))
canvas.create_window(200,230, window=button)

root.mainloop()