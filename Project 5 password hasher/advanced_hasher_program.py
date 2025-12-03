from tkinter import *
from tkinter import messagebox
import bcrypt
import psycopg2
# using PostgreSQL
APP_DB_NAME = "myusers"
def database():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1623", host="localhost",port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    # checking if database already exists
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (APP_DB_NAME,))
    exists = cur.fetchone()
    if not exists:
        cur.execute(f"CREATE DATABASE {APP_DB_NAME};")
        print("Created database", APP_DB_NAME)

    cur.close()
    conn.close()

def get_app_connection():
    database()
    conn = psycopg2.connect(
        dbname=APP_DB_NAME,
        user="postgres",
        password="1623",
        host="localhost",
        port=5432
    )
    return conn

def run_query(query, parameters=()):
    conn = psycopg2.connect(dbname=APP_DB_NAME,user='postgres',password='1623',host='localhost',port='5432')
    cur = conn.cursor()
    query_result = None
    try:
        cur.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result = cur.fetchall()
        conn.commit()
    
    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        cur.close()
        conn.close()
    return query_result

def ensure_users_table():
    conn = get_app_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash BYTEA NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def signup(created_username,created_password):
    next_button = None
    rows = run_query(
    "SELECT 1 FROM users WHERE username = %s",
    (created_username,))

    if rows:
        # At least one row returned → username already exists
        messagebox.showinfo("Information", "Account already exists, please enter a different username")
        return
    else:
        ensure_users_table()
        encoded_password = bytes(created_password,encoding='utf-8')
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        query = "insert into users(username,password_hash) values (%s,%s)"
        parameters = (created_username,hashed_password)
        run_query(query,parameters)
        messagebox.showinfo("Information","Account created successfully")
        label = Label(signin,text="Click here to move on to the Log In page")
        if next_button is None:
            next_button = Button(signin,text="Next",command=move)
            next_button.pack()
    


def move():
    signin.pack_forget()
    login.pack()
    label_2.pack()
    enter_username.pack()
    enter_password.pack()
    login_button.pack()
    


def validate(username,password):
    conn = get_app_connection()
    cur = conn.cursor()
    encoded_entered_password = bytes(password,encoding='utf-8')
    cur.execute("select password_hash from users where username=%s", (username,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row is None:
        messagebox.showinfo("Information","user not found, please enter the username correctly") 
        return

    stored_hash = bytes(row[0]) 
    if bcrypt.checkpw(encoded_entered_password, stored_hash):
        messagebox.showinfo("Information","Log in Successful")
    else:
        messagebox.showinfo("Information","Invalid password")
        


root = Tk()
root.geometry("300x300")
database()
signin = Frame(root)
signin.pack()
login = Frame(root)
label = Label(signin,text="Sign up")
label.pack()
create_username_entry = Entry(signin,text="enter a username")
create_username_entry.pack()
create_password_entry = Entry(signin,text="enter a password")
create_password_entry.pack()
signup_button = Button(signin,text="Sign up",command=lambda: signup(create_username_entry.get(),create_password_entry.get()))
signup_button.pack()


# after login frame is packed
label_2 = Label(login,text="Sign up")
enter_username = Entry(login,text="enter your username")
enter_password = Entry(login,text="enter your password")
login_button = Button(text="Log in",command=lambda: validate(enter_username.get(),enter_password.get()))




root.mainloop()