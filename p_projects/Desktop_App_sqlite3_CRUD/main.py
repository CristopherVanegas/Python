from cmath import e
from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    def __init__ (self, window):
        self.wind = window
        self.wind.title('Products App')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Register A new Product')
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Name Input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name=Entry(frame)
        self.name.focus()   # To when the app starts the cursor sets in the first fill field.
        self.name.grid(row=1, column=1)

        # Price Input
        Label(frame, text = 'Price: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Button Add Product
        ttk.Button(frame, text='Save Product').grid(row=3, columnspan=2, sticky = W+E)  # sticky property defines from where to where it's going to be stretched (in this case WESTERN TO EAST) a button or smthg else.

        # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)  # calls a function to create a table using .Treeview() and saving it into 'tree' class property to handle it in the future.
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text = 'Price', anchor=CENTER)


if __name__ == '__main__':
    window = Tk()
    app = Product(window)
    window.mainloop()
