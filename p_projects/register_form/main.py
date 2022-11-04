from tkinter import *

# COLORS

LIGHTBLUE = "#213141"
LIGHTGREEN = "#56CD63"

appWind = Tk()
appWind.geometry("650x550")
appWind.title("Registration Form | Welcome to InBy!")
appWind.resizable(False, False)
appWind.config(background = LIGHTBLUE)
main_title = Label(text="| InBy Registration Form |", font=("Cambria", 13), bg=LIGHTGREEN, fg="white", width="550", height="2")
main_title.pack()


######################## LABEL CREATION ########################
username_label = Label(text="Username", bg=LIGHTBLUE).place(x=22, y=70)
password_label = Label(text="Password", bg=LIGHTBLUE).place(x=22, y=130)
fullname_label = Label(text="Full Name", bg=LIGHTBLUE).place(x=22, y=190)
age_label = Label(text="Age", bg=LIGHTBLUE).place(x=22, y=250)

appWind.mainloop()
