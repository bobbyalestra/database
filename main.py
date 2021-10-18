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

c.execute(""" CREATE TABLE addresses (
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )

""")



# commit changes
conn.commit()

# Close Connection

conn.close()


root.mainloop()