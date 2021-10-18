from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Coding With Doc")
root.geometry("400x400")


# create or connect to database

conn = sqlite3.connect('address_book.db')

# Create Cursor
c = conn.cursor()

# Create table
'''
c.execute(""" CREATE TABLE addresses (
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )

""")
'''

# Create Submit Function for Database


def submit():
    # create or connect to database

    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

# Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name), :address, :city, :state, :zipcode",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()

              })

    # Commit changes
    conn.commit()

    # Close Connection

    conn.close()

    # Clear TextBox
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create TextBoxes

f_name = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)


# Create Textbox labels

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address Name")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City Name")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State Name")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode Name")
zipcode_label.grid(row=5, column=0)


# Create Submit Button

submit_btn = Button(root, text= "Add To DataBase", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#  Commit changes
conn.commit()

# Close Connection

conn.close()


root.mainloop()