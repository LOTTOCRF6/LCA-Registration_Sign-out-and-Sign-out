from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title("My_random_tkinter")
root.geometry("600x600")
root.config(bg="Black")
# start of label name
lab_name = Label(root, text="Enter your Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=20)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=310, y=20, width=220, height=30)
# end of label name
# start of label password
lab_password = Label(root, text="Enter your Password: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=70)
entry_password = Entry(root, show="*", bg="lightblue", fg="black")
entry_password.place(x=310, y=70, width=220, height=30)
# end of password label

name = "Zipho"
password = "2919"


# login function
def login():
    mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com', database='sql4423138',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from register')
    for i in mycursor:
        if i[1] == entry_password.get() and i[0] == entry_name.get():
            messagebox.showinfo("Output", "Login")
    if i[1] != entry_password.get() or i[0] != entry_name.get():
            messagebox.showinfo("Output", "Enter correct information")
            entry_password.delete(0, END)
            entry_name.delete(0, END)


# login button
login_btn = Button(root, text="Login", borderwidth="10", command=login, font=("Consolas 13 bold"), bg="black",
                   fg="lightblue")
login_btn.place(x=80, y=150)


# clear function
def clear():
    entry_name.delete(0, END)
    entry_password.delete(0, END)


# clear button
clear_button = Button(root, text="Clear", borderwidth="10", command=clear, font=("Consolas 13 bold"), bg="black",
                      fg="lightblue")
clear_button.place(x=240, y=150)


# exit function
def register():
    messagebox.showinfo("Message", "fill in all the empty spaces!")
    root.destroy()
    import Register


# exit button
exit_button = Button(root, text="Register", borderwidth="10", command=register, font=("Consolas 13 bold"), bg="black",
                     fg="lightblue")
exit_button.place(x=390, y=150)


root.mainloop()