from tkinter import *
from os import system

######################## SEND DATA FUNCTION ########################

def send_data():
    username_data_collect = str(username.get())
    password_data_collect = str(password.get())
    fullname_data_collect = str(fullname.get())
    age_data_collect = str(age.get())
    print(username_data_collect, '\t', password_data_collect, '\t', fullname_data_collect, '\t', age_data_collect)  # print the data collected

    nFile = open('registration.txt', 'a')
    nFile.write(username_data_collect + '\t')
    nFile.write(password_data_collect + '\t')
    nFile.write(fullname_data_collect + '\t')
    nFile.write(age_data_collect + '\t')

    nFile.write('\n')
    system('open ./registration.txt')

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)


######################## CONSTANTS ########################

LIGHTBLUE = "#213141"
LIGHTGREEN = "#56CD63"


######################## WINDOW AND TITLE ########################

appWind = Tk()
appWind.geometry("600x900")
appWind.title("Registration Form | Welcome to InBy!")
appWind.resizable(False, False)
appWind.config(background = LIGHTBLUE)
main_title = Label(text="| InBy Registration Form |", font=("Cambria", 13), bg=LIGHTGREEN, fg="white", width="550", height="2")
main_title.pack()


######################## LABELS CREATION ########################
username_label = Label(text="Username", bg=LIGHTBLUE).place(x=22, y=70)
password_label = Label(text="Password", bg=LIGHTBLUE).place(x=22, y=130)
fullname_label = Label(text="Full Name", bg=LIGHTBLUE).place(x=22, y=190)
age_label = Label(text="Age", bg=LIGHTBLUE).place(x=22, y=250)


######################## GET DATA ########################
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

username_entry = Entry(textvariable=username, width="40")
username_entry.place(x=22, y=100)
password_entry = Entry(textvariable=password, width="40", show="*")
password_entry.place(x=22, y=160)
fullname_entry = Entry(textvariable=fullname, width="40")
fullname_entry.place(x=22, y=220)
age_entry = Entry(textvariable=age, width="40")
age_entry.place(x=22, y=280)

submit_btn = Button(appWind, text="| ¡Submit Data! |", command=send_data, width="30", height="2", bg="#00CD63").place(x=22, y=320)


appWind.mainloop()
