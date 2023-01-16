
# create an interface to calculate derivates.

import tkinter as tk
from tkinter import *
from tkinter import simpledialog

class Derivates:
    def __init__(self, window):
        self.wind = window
        window.geometry("400x300")
        self.wind.title('Derivates')

        # frame container --------------------------------------------|
        frame = LabelFrame(self.wind, text='Enter your expression: ') #
        frame.grid(row=0, column=0, columnspan=3, pady=20, sticky=W+E)#
                                                                      #
        # expression input                                            #
        Label(frame, text='Expresion: ').grid(row=1, column=0, sticky=W+E)        #
        self.expression = Entry(frame)
        self.expression.focus()
        self.expression.grid(row=1, column=1)
        




if __name__ == '__main__':
    window = Tk()
    app = Derivates(window)
    window.mainloop()
