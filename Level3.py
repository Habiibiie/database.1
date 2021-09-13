from tkinter import *
import sqlite3

data = Tk()
data.title('STORAGE')
data.geometry("600x600")

# database
database = sqlite3.connect('details_storage.db')
c = database.cursor()


# fn for database

def submit():
    database = sqlite3.connect('details_storage.db')
    c = database.cursor()

    c.execute("INSERT INTO address VALUES(:name, :email, :contact)",
              {
                  'name': name.get(),
                  'email': email.get(),
                  'contact': contact.get()
              })
    database.commit()
    database.close()
    name.delete(0, END)
    email.delete(0, END)
    contact.delete(0, END)


# creating table

'''
c.execute("""CREATE TABLE address (
            name text,
            email text,
            contact integer)""")
'''


# Query function

def que():
    database = sqlite3.connect('details_storage.db')
    c = database.cursor()
    c.execute("SELECT *,oid FROM address")
    record = c.fetchall()
    print(record)
    for records in record:
        record += str(records[0]) + '\n'

    que_labels = Label(data, text=record)
    que_labels.grid(row=7, column=0, columnspan=2)

    database.commit()
    database.close()


# Text Lables

name_labels = Label(data, text='NAME')
name_labels.grid(row=2, column=0)

email_labels = Label(data, text='EMAIL')
email_labels.grid(row=3, column=0)

contact_labels = Label(data, text='NUMBER')
contact_labels.grid(row=4, column=0)

# Text Boxes

name = Entry(data, width=40)
name.grid(row=2, column=3, padx=25)

email = Entry(data, width=40)
email.grid(row=3, column=3)

contact = Entry(data, width=40)
contact.grid(row=4, column=3)

# Buttons

submit_btn = Button(data, text="ADD DATA", command=submit)
submit_btn.grid(row=5, column=0, columnspan=3, pady=30, padx=30, ipadx=50)

que_btn = Button(data, text="VIEW DATA", command=que)
que_btn.grid(row=6, column=0, columnspan=3, pady=20, padx=20, ipadx=50)

database.commit()
database.close()
data.mainloop()
