import tkinter as tk
from compress_decompress_module import compress,decompress
# the file dialogue allows you to open up a file which is present on your computer
from tkinter import filedialog

def open_file_compression():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file to compress")
    return filename
def open_file_decompression():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file to decompress")
    return filename
def compression(i,o):
    compress(i,o)
def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title("Compression engine!")
window.geometry("600x400")


# convert the compression(i,o) function to a lambda because the command= option must receive a callable that takes no arguments. 
# It should not run immediately, but rather be stored so Tkinter can call it later—when the button is clicked.
# if you just write command=compression(), Python evaluates the function call immediately, right when the button is created. That means it runs compression(...) before the button even appears.
compress_button = tk.Button(window,text="Compress",command=lambda:compression(open_file_compression(),"compressed_output.txt"))
compress_button.grid(row=2,column=1)

decompress_button = tk.Button(window,text="Decompress",command=lambda:decompression(open_file_decompression(),"decompressed_output.txt"))
decompress_button.grid(row=5,column=1)

window.mainloop()












