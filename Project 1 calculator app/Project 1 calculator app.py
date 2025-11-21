import tkinter as tk
import customtkinter as ctk
# this module has built-in functions that can evaluate our calculator display numbers
import ast

root= ctk.CTk()
root.geometry("500x300")
root.title("Calculator")
ctk.set_appearance_mode("dark")
for col in range(6):
    root.grid_columnconfigure(col,weight=1)
for row in range(6):
    root.grid_rowconfigure(row,weight=1)

# this function will display our clicked numbers into the entry field
i = 0
def getnumber(num):
    # to access i from the outside of the function, declare it as global
    global i
    # at index i, insert num (which was passed as our button text down there)
    display.insert(i,num)
    i+=1

# this function will display our clicked operations into the entry field
def get_operation(operator):
    global i
    length = len(operator)
    # at index i, insert our operator
    display.insert(i,operator)
    i+=length

# this will clear everything from the display
def clear_all():
    display.delete(0,tk.END)

# we use the ast module to calculate the numbers on the display
def calculate():
    entire_string = display.get()
    # use a try and except block to handle errors
    try:
        # parse the string into readable format
        node = ast.parse(entire_string,mode='eval')
        # evaluate our numbers
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        # inserting our result
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,'Error')

# create a new string which deletes the last number from the display (original) string
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,'')


display = ctk.CTkEntry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0,columnspan=6, sticky="nsew", padx=5, pady=5)

numbers = [1,2,3,4,5,6,7,8,9]
# this counter makes sure that every new button created has a new number
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = ctk.CTkButton(root, text=str(button_text), command= lambda text=button_text: getnumber(text), corner_radius=20,fg_color="#3c3b39",hover_color="#2b2a27")
        # we say we want to start from row x+2 because we want to put these numbers under the input field, starting from row 2
        button.grid(row=x+1, column=y, sticky="nsew", padx=2, pady=2)
        counter += 1

# don't forget the 0 button!
button = ctk.CTkButton(root, text="0", command = lambda: getnumber(0),corner_radius=20,fg_color="#3c3b39",hover_color="#2b2a27")
button.grid(row=4, column=1,sticky="nsew", padx=2, pady=2)

# we create a list of operations then loop through them to create buttons
operations = ['+','-','*','/','*3.14','%','(','**',')','**2']
# creating a 4x3 grid here with the for loop,
# but we only have 10 operations, so we must limit the loop and make it stop once we have enough
count = 0
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button = ctk.CTkButton(root, text=operations[count], command=lambda text=operations[count]: get_operation(text),corner_radius=20,fg_color="#3c3b39",hover_color="#2b2a27")
            count += 1
            button.grid(row=x+1, column=y+3,sticky="nsew", padx=2, pady=2)
        else:
            break

ctk.CTkButton(root, text='AC', command=clear_all,corner_radius=20,fg_color="#3c3b39",hover_color="#2b2a27").grid(row=4, column=0,sticky="nsew", padx=2, pady=2)
ctk.CTkButton(root, text='=', command=calculate,corner_radius=20,fg_color="#68c1c8",hover_color="#4f8f94").grid(row=4, column=2,sticky="nsew", padx=2, pady=2)
ctk.CTkButton(root,text='◀', command=lambda: undo(),corner_radius=20,fg_color="#3c3b39",hover_color="#2b2a27").grid(row=4, column=4,sticky="nsew", padx=2, pady=2)

root.mainloop()



