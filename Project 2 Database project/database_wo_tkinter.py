# import library
import psycopg2

# you can put this code into a function:
def create_table():
    # use connect method to connect to your database
    # you must pass in the database name, username, password, host and port number
    # save this connection object into a variable
    conn = psycopg2.connect(dbname='studentdb',user='postgres',password='1623',host='localhost',port='5432')

    #whenever you want to perform database operations you need to use the database cursor
    cur = conn.cursor()
    # using the execute method, you can then pass in the actual SQL query which you want to execute here. Don't forget the semicolon!
    cur.execute('create table students(student_id serial primary key, name text, address text, age int, number text);')
    print('student table created')
    # to execute the code, you have to commit those changes to the database
    conn.commit()
    # when you are finished, close the database
    conn.close()

# you can create a function that inserts data
def insert_data():
    # you again have to create a connection object, a cursor and execute it
    # code to accept data from the user
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")

    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="1623",host="localhost",port="5432")
    cur = conn.cursor()
    # in order to pass those values from above that we accepted you have to insert %s as placeholders then outside the string, take the variables and pass them in the way below
    cur.execute("insert into students(name,address,age,number) values (%s,%s,%s,%s)", (name,address,age,number))
    print("data inserted")
    conn.commit()
    conn.close()



def delete_data():
    student_id = input("Enter the ID of the student you want to delete: ")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="1623",host="localhost",port="5432")
    cur = conn.cursor()
    # we find the student row by executing the SQL query below
    cur.execute("select * from students where student_id=%s", (student_id,))
    # once we have found the student row which we want, we obtain it
    student = cur.fetchone()

    # check if the row exists and display information
    if student:
        print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}")
        # ask user for confirmation
        choice = input("Are you sure you want to delete the student? (yes/no)")
        if choice.lower() == "yes":
            cur.execute("delete from students where student_id=%s", (student_id,))
            print("Student record deleted")
        else:
            print("Deletion cancelled")
    else: 
        print("Student not found")
    conn.commit()
    conn.close()

def update_data():
    #accept student id
    student_id = input('Enter id of the student to be updated')
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="1623",host="localhost",port="5432")
    cur = conn.cursor()
    # create a dictionary with key value pairs of the options to change in our data
    fields = {
        "1": ("name", "Enter the new name"),
        "2": ("address", "Enter the new address"),
        "3": ("age", "Enter the new age"),
        "4": ("number", "Enter the new number"),
    }
    # we'll ask the user to choose between the options above
    print("Which field would you like to update")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice = input("Enter the number of the field you want to update: ")
    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_value = input(prompt)
        # we have to make this SQL query dynamic, so create a new string
        sql = f"update students set {field_name}=%s where student_id=%s"
        cur.execute(sql, (new_value,student_id))
        print(f"{field_name} updated successfully")
    else:
        print("Invalid choice")


    conn.commit()
    conn.close()


def read_data():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="1623",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("select * from students;")
    # the fetchone method fetches one row, fetchall gets all the rows 
    students = cur.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}")
    conn.close()


while True:
    print("\n Welcome to the student database management system")
    print("1. Create Table")
    print("2. Insert data")
    print("3. Read data")
    print("4. Update data")
    print("5. Delete Table")
    print("6. EXIT")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        create_table()
    elif choice == "2":
        insert_data()
    elif choice == "3":
        read_data()
    elif choice == "4":
        update_data()
    elif choice == "5":
        delete_data()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number from 1-6")
