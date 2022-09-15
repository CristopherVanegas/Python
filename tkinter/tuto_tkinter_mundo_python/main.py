import tkinter  # imports tkinter package
window = tkinter.Tk()   # creates new object tkinter
window.geometry("400x300")  # creates a new window using object 'window' and it's "geometry"/area it's 400px by 300px

label = tkinter.Label(window, text="Hello world!\nAnother line", bg="cyan", pady=10, fg="red")  # new label using class Label
label.pack()    # shows always in the center the label
label.pack(side=tkinter.BOTTOM) # shows in the BOTTOM side
label.pack(side=tkinter.RIGHT)  # shows in the RIGHT side
label.pack(side=tkinter.LEFT)   # shows in the LEFT side
label.pack(side=tkinter.TOP)    # shows in the TOP side


tkinter.Label(None, text='label', fg='green', bg='black').pack()    # creates a new label and shows it instantanely!
tkinter.Button(None, text='button', fg='green', bg='black').pack()  # creates a buttton with it's own parameters such as text, text-color(green) and bg(background-color)


window.mainloop()   # necesary to keep open the application / software
