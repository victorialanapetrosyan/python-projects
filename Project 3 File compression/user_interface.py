import tkinter as tk
from compress_decompress_module import compress,decompress


def compression(i,o):
    compress(i,o)
def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title("Compression engine!")
window.geometry("600x400")

compression_input_entry = tk.Entry(window)
compression_output_entry = tk.Entry(window)
compression_input_label = tk.Label(window,text="file to be compressed")
compression_output_label = tk.Label(window,text="name of compressed file")

# convert the compression(i,o) function to a lambda because the command= option must receive a callable that takes no arguments. 
# It should not run immediately, but rather be stored so Tkinter can call it later—when the button is clicked.
# if you just write command=compression(), Python evaluates the function call immediately, right when the button is created. That means it runs compression(...) before the button even appears.
compress_button = tk.Button(window,text="Compress",command=lambda:compression(compression_input_entry.get(),compression_output_entry.get()))

compression_input_entry.grid(row=0,column=1)
compression_input_label.grid(row=0,column=0)
compression_output_entry.grid(row=1,column=1)
compression_output_label.grid(row=1,column=0)
compress_button.grid(row=2,column=1)

# Now let's create decompression buttons

decompression_input_entry = tk.Entry(window)
decompression_output_entry = tk.Entry(window)
decompression_input_label = tk.Label(window,text="file to be decompressed")
decompression_output_label = tk.Label(window,text="name of decompressed file")
decompress_button = tk.Button(window,text="Decompress",command=lambda:decompression(decompression_input_entry.get(),decompression_output_entry.get()))

decompression_input_entry.grid(row=3,column=1)
decompression_input_label.grid(row=3,column=0)
decompression_output_entry.grid(row=4,column=1)
decompression_output_label.grid(row=4,column=0)
decompress_button.grid(row=5,column=1)

window.mainloop()












