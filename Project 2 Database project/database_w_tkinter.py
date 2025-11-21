from tkinter import *
# we have to import another module for tree view
from tkinter import ttk
from tkinter import messagebox
# don't forget psycopg2
import psycopg2

#create a new function to run our SQL query
# for our run_query function, we need to accept the SQL query and parameters in tuple form
def run_query(query, parameters=()):
    conn = psycopg2.connect(dbname='studentdb',user='postgres',password='1623',host='localhost',port='5432')
    cur = conn.cursor()
    query_result = None
    try:
        cur.execute(query,parameters)
        # the startswith method checks if a particular string starts with some other string
        # if the query starts with select then we want to go ahead and fetch all the rows from that result
        if query.lower().startswith("select"):
            query_result = cur.fetchall()
        conn.commit()
    
    # when there's an issue with the query, it would be a psycopg2 error
    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        cur.close()
        conn.close()
    return query_result

# the refresh tree view function fetches all the new data from the database and populates the tree view which we have 
def refresh_treeview():
    # we do not want to insert duplicate rows, so clear the current items if they are present in the tree view when executing this function
    for item in tree.get_children():
        tree.delete(item)
    # obtaining the rows of student data
    records = run_query("select * from students;")
    # loop through each row and insert into the tree view
    for record in records:
        tree.insert('',END,values=record)

def insert_data():
    query = "insert into students(name,address,age,number) values (%s,%s,%s,%s)"
    # now we need to get access to the data in our entry fields
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),number_entry.get())
    # pass in the query and parameters in our run_query function
    run_query(query,parameters)
    messagebox.showinfo("Information","Data inserted successfully")
    # use refresh_treeview function to display the data on the tree view
    refresh_treeview()

def delete_data():
    # in the tree view, the user will select the row which they want to delete, so we will need to obtain that selected row, obtain the id of the person in the selected row, use SQL to delete it, then refresh the tree view
    selected_item = tree.selection()[0]
    # item() is used to retrieve info about a specific row
    # item() takes the items identifier as an argument
    student_id = tree.item(selected_item)['values'][0]
    query = "delete from students where student_id=%s"
    parameters = (student_id,)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data deleted successfully")
    refresh_treeview()

def update_data():
    # if you want to update a row, you should select it, fill the newly updated data which you want, and then click on the update data button
    selected_item = tree.selection()[0]
    student_id = tree.item(selected_item)['values'][0]
    query = "update students set name=%s, address=%s, age=%s, number=%s where student_id=%s"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),number_entry.get(),student_id)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data updated successfully")
    refresh_treeview()

def create_table():
    # create a query that will only create a table if it doesn't already exist
    query = "create table if not exists students(student_id serial primary key, name text, address text, age int, number text);"
    run_query(query)
    messagebox.showinfo("Information","Table created")
    refresh_treeview()



# now for out interface:

root = Tk()
root.title("Student management system")

#we first create a frame to place our labels and inputs on
frame = LabelFrame(root, text="Student Data")
frame.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

# since we are placing this label on the frame, you don't need to pass in root as a parameter
Label(frame,text="Name:").grid(row=0,column=0,padx=2,sticky="w")
name_entry = Entry(frame)
name_entry.grid(row=0,column=1,pady=2,sticky="ew")

Label(frame,text="Address:").grid(row=1,column=0,padx=2,sticky="w")
address_entry = Entry(frame)
address_entry.grid(row=1,column=1,pady=2,sticky="ew")

Label(frame,text="Age:").grid(row=2,column=0,padx=2,sticky="w")
age_entry = Entry(frame)
age_entry.grid(row=2,column=1,pady=2,sticky="ew")

Label(frame,text="Number:").grid(row=3,column=0,padx=2,sticky="w")
number_entry = Entry(frame)
number_entry.grid(row=3,column=1,pady=2,sticky="ew")

# let's create a separate button frame 
button_frame = Frame(root)
button_frame.grid(row=1,column=0,pady=5,sticky="ew")

#creating buttons
Button(button_frame,text="Create table", command=create_table).grid(row=0,column=0,padx=5)
Button(button_frame,text="Add Data",command=insert_data).grid(row=0,column=1,padx=5)
Button(button_frame,text="Update Data", command=update_data).grid(row=0,column=2,padx=5)
Button(button_frame,text="Delete Data",command=delete_data).grid(row=0,column=3,padx=5)

# adding a tree view in out tkinter window to display our database data in rows and columns
tree_frame = Frame(root)
tree_frame.grid(row=2,column=0,padx=10,sticky="nsew")

# creating a scroll bar for our table
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)
# using yscrollcommand=tree_scroll.set we link our table with the scroll bar
tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="browse")
tree.pack()
tree_scroll.config(command=tree.yview)

# defining the columns/heading of our table
tree['columns']=("student_id", "name", "address", "age", "number")
tree.column("#0", width=0,stretch=NO)
tree.column("student_id", anchor=CENTER, width=80)
tree.column("name", anchor=CENTER, width=120)
tree.column("address", anchor=CENTER, width=120)
tree.column("age", anchor=CENTER, width=50)
tree.column("number", anchor=CENTER, width=120)

tree.heading("student_id", text="ID", anchor=CENTER)
tree.heading("name", text="Name", anchor=CENTER)
tree.heading("address", text="Address", anchor=CENTER)
tree.heading("age", text="Age", anchor=CENTER)
tree.heading("number", text="Number", anchor=CENTER)





refresh_treeview()
root.mainloop()