from tkinter import *

import mysql.connector


root = Tk()
root.config(bg="Black")
root.geometry("800x800")
root.title("Registration")

# start of label name
lab_name = Label(root, text="Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=20)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=200, y=20, width=220, height=30)
# end of label name
# start of label password
lab_password = Label(root, text="Surname: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=70)
entry_password = Entry(root, bg="lightblue", fg="black")
entry_password.place(x=200, y=70, width=220, height=30)
# end of password label# start of label password
# Start of ID number Label and Entry
lab_password = Label(root, text="ID No.: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=120)
entry_password = Entry(root, bg="lightblue", fg="black")
entry_password.place(x=200, y=120, width=220, height=30)
#  end of id number label
# start of label password
lab_password = Label(root, text="Phone No.: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=170)
entry_password = Entry(root, bg="lightblue", fg="black")
entry_password.place(x=200, y=170, width=220, height=30)
# end of password label
# start of label password
lab_password = Label(root, text="Password: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=220)
entry_password = Entry(root, show="*", bg="lightblue", fg="black")
entry_password.place(x=200, y=220, width=220, height=30)
# end of password label
# start of label password
lab_password = Label(root, text="Next of kin Fullname:", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=270)
entry_password = Entry(root, bg="lightblue", fg="black")
entry_password.place(x=330, y=270, width=220, height=30)
# end of password label
# start of label password
lab_password = Label(root, text="Next of kin Cell No.:", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=320)
entry_password = Entry(root, bg="lightblue", fg="black")
entry_password.place(x=330, y=320, width=220, height=30)
# end of password label


'''
mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                               database='sql4423138',auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
sql = "INSERT INTO  (username, password) Value(%s, %s)"
mycursor.execute("CREATE TABLE register(name VARCHAR(225), surname VARCHAR(225), id number VARCHAR(225),"
                 " phone number VARCHAR(225), next of kin ) ")
mydb.commit()'''

root.mainloop()