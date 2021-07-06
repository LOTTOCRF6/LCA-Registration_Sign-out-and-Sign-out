from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.config(bg="Black")
root.geometry("800x800")
root.title("Registration")

# start of label name and entry
lab_name = Label(root, text="Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=20)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=200, y=20, width=220, height=30)
# end of label name and entry

# start of label Surname and Entry
lab_surname = Label(root, text="Surname: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_surname.place(x=60, y=70)
entry_surname = Entry(root, bg="lightblue", fg="black")
entry_surname.place(x=200, y=70, width=220, height=30)
# end of Surname and Entry

# Start of ID number Label and Entry
lab_id_no = Label(root, text="ID No.: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_id_no.place(x=60, y=120)
entry_id_no = Entry(root, bg="lightblue", fg="black")
entry_id_no.place(x=200, y=120, width=220, height=30)
#  end of id number label and entry

# start of label Phone No and Entry
lab_phone_no = Label(root, text="Phone No.: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_phone_no.place(x=60, y=170)
entry_phone_no = Entry(root, bg="lightblue", fg="black")
entry_phone_no.place(x=200, y=170, width=220, height=30)
# end of Phone No label and Entry

# start of Password label and Entry
lab_password = Label(root, text="Password: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=220)
entry_password = Entry(root, show="*", bg="lightblue", fg="black")
entry_password.place(x=200, y=220, width=220, height=30)
# end of Password label and Entry

# start of Next of kin Fullname label and Entry
lab_fullname = Label(root, text="Next of kin Fullname:", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_fullname.place(x=60, y=270)
entry_fullname = Entry(root, bg="lightblue", fg="black")
entry_fullname.place(x=330, y=270, width=220, height=30)
# end of Next of kin Fullname label and Entry

# start of Next of kin Cell No label and entry
lab_cell_no = Label(root, text="Next of kin Cell No.:", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_cell_no.place(x=60, y=320)
entry_cell_no = Entry(root, bg="lightblue", fg="black")
entry_cell_no.place(x=330, y=320, width=220, height=30)
# end of Next of kin Cell No label and entry

# functions
# Register function
def register():
    mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                                   database='sql4423138', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "INSERT INTO Register (name,surname,phone_no,password,next_of_kin_Fullname,Next_of_kin_Phone_No ) Value(%s, %s, %s, %s, %s, %s)"
    val = (entry_name.get(), entry_surname.get(), entry_phone_no.get(), entry_password.get(), entry_fullname.get(), entry_cell_no.get() )
    mycursor.execute(sql, val)
    messagebox.showinfo("Output", "Registration Done.You can login.")
    entry_password.delete(0, END)
    entry_name.delete(0, END)
    mydb.commit()

# button
register_button = Button(root, text="Register", borderwidth="10", command=register, font=("Consolas 13 bold"), bg="black", fg="lightblue")
register_button.place(x=390, y=360)

'''
mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                               database='sql4423138',auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
sql = "INSERT INTO  (username, password) Value(%s, %s)"
mycursor.execute("CREATE TABLE register(name VARCHAR(225), surname VARCHAR(225), id number VARCHAR(225),"
                 " phone number VARCHAR(225), next of kin ) ")
mydb.commit()'''

root.mainloop()