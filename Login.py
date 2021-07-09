from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.title("My_random_tkinter")
root.geometry("800x600")
root.config(bg="Black")

now = datetime.now()
formatted_data = now.strftime('%Y-%m-%d %H:%M:%s')
# Heading
lab_name = Label(root, text="WELCOME TO LIFECHOICES ACADEMY ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=100, y=20)
lab_name = Label(root, text="Please go to Register button to register! ", bg="black", fg="lightblue", font=("Consolas 10 bold"))
lab_name.place(x=130, y=70)
lab_name = Label(root, text="You can login and logout here also!", bg="black", fg="lightblue", font=("Consolas 10 bold"))
lab_name.place(x=130, y=120)

# start of label name
lab_name = Label(root, text="Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=200)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=250, y=200, width=220, height=30)
# end of label name
# start of label password
lab_id_no = Label(root, text="Enter ID No: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_id_no.place(x=60, y=250)
entry_id_no = Entry(root, bg="lightblue", fg="black")
entry_id_no.place(x=250, y=250, width=220, height=30)
# end of password label
# start of label password
lab_password = Label(root, text="Password: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=300)
entry_password = Entry(root, bg="lightblue", fg="black")
entry_password.place(x=250, y=300, width=220, height=30)
# end of password label


# login function
def login():
    mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com', database='sql4423138',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Register')
    for i in mycursor:
        if i[1] == entry_name.get() and i[4] == entry_password.get():
            mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                                           database='sql4423138',
                                           auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()
            sql = "INSERT INTO Logins (Name, Password, Login_DateTime ) Value(%s, %s, %s)"
            val = (entry_name.get(), entry_password.get(), formatted_data)
            mycursor.execute(sql, val)
            messagebox.showinfo("Output", "Login")
            mydb.commit()

    if i[1] != entry_password.get() or i[0] != entry_id_no.get():
            messagebox.showinfo("Output", "Enter correct information")
            entry_password.delete(0, END)
            entry_id_no.delete(0, END)


# login button
login_btn = Button(root, text="Login", borderwidth="10", command=login, font=("Consolas 13 bold"), bg="black",
                   fg="lightblue")
login_btn.place(x=60, y=350)


# clear function
def logout():
    mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com', database='sql4423138',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Register')
    for i in mycursor:
        if i[1] == entry_name.get() and i[4] == entry_password.get():
            mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                                           database='sql4423138',
                                           auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()
            sql = "INSERT INTO Logouts (Name, Password, Logout_DateTime ) Value(%s, %s, %s)"
            val = (entry_name.get(), entry_password.get(), formatted_data)
            mycursor.execute(sql, val)
            messagebox.showinfo("Output", "Successful Logout. See you next time")
            mydb.commit()

    if i[1] != entry_password.get() or i[0] != entry_id_no.get():
            messagebox.showinfo("Output", "Enter correct information")
            entry_password.delete(0, END)
            entry_id_no.delete(0, END)


# logout button
logout_button = Button(root, text="Logout", borderwidth="10", command=logout, font=("Consolas 13 bold"), bg="black",
                      fg="lightblue")
logout_button.place(x=200, y=350)


# exit function
def register():
    messagebox.showinfo("Message", "fill in all the empty spaces!")
    root.destroy()
    import Register


# REGISTER button
register_button = Button(root, text="Register", borderwidth="10", command=register, font=("Consolas 13 bold"), bg="black",
                     fg="lightblue")
register_button.place(x=340, y=350)


def admin():
    messagebox.showinfo('Alert', 'Only Administration Team allowed Please!')
    root.destroy()
    import Administration


# Admin Button
admin_button = Button(root, text="Admin", borderwidth="10", command=admin, font=("Consolas 13 bold"), bg="black",
                     fg="lightblue")
admin_button.place(x=340, y=430)


root.mainloop()