from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title('Administration')
root.geometry('1200x1200')
root['bg']='black'
var = StringVar()

# Registration Treeview and Functions and Button
'''update_headig = Label(root, text='Update a field', bg='white', width=25)
update_headig.place(x=780, y=315)
people_loged_in = Label(root, text='logged in:')
people_loged_in.place(x=890, y=10)
number = Label(root, text='', textvariable=var, bg='white', width=3)
number.place(x=960,y=10)
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute('SELECT COUNT(DISTINCT Logins FROM Logins')
for i in mycursor:
        var.set(i[0])'''



# Registration Function
def registration():
    global tv # making my tv to be global so that is can be accessible
    tv = ttk.Treeview(root, selectmode="browse")
    tv.grid(row=1, column=1, padx=20, pady=20)
    tv['columns'] = ('Rank', 'Name', 'Surname', 'Phone_No', 'Password', 'Next_of_kin_fullname', 'Next_of_kin_Cell_No'
                     , 'ID_number', 'Register_DateTime')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Rank', anchor=CENTER, width=80)
    tv.column('Name', anchor=CENTER, width=100)
    tv.column('Surname', anchor=CENTER, width=100)
    tv.column('Phone_No', anchor=CENTER, width=100)
    tv.column('Password', anchor=CENTER, width=100)
    tv.column('Next_of_kin_fullname', anchor=CENTER, width=190)
    tv.column('Next_of_kin_Cell_No', anchor=CENTER, width=190)
    tv.column('ID_number', anchor=CENTER, width=190)
    tv.column('Register_DateTime', anchor=CENTER, width=220)
# tv headings
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Rank', text='Rank', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Surname', text='Surname', anchor=CENTER)
    tv.heading('Phone_No', text='Phone_No', anchor=CENTER)
    tv.heading('Password', text='Password', anchor=CENTER)
    tv.heading('Next_of_kin_fullname', text='Next_of_kin_fullname', anchor=CENTER)
    tv.heading('Next_of_kin_Cell_No', text='Next_of_kin_Cell_No', anchor=CENTER)
    tv.heading('ID_number', text='ID_number', anchor=CENTER)
    tv.heading('Register_DateTime', text='Register_DateTime', anchor=CENTER)

    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Register")
    for dt in mycursor:
        tv.insert('', 'end', iid=dt[0], text=dt[0],
                  values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8]))


# Registration Button
registration_btn = Button(root, text="Register List", borderwidth="10", command=registration, font=("Consolas 13 bold"), bg="yellow",
                       fg="black")
registration_btn.place(x=750, y=650)


# Delete Function
def delete():
    selected = tv.focus()
    values = tv.item(selected, 'values')
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "DELETE FROM Register WHERE Id_No = %s"
    val = (values[0],)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Delete', 'Record deleted! ')


# Delete Button
delete_btn = Button(root, text="Delete Records", borderwidth="10", command=delete, font=("Consolas 13 bold"),
                          bg="yellow", fg="black")
delete_btn.place(x=750, y=550)


# Login tv, function and button
def login():
    tv = ttk.Treeview(root, selectmode="browse")
    tv.place(x=20, y=260)
    tv['columns'] = ('Rank', 'Name', 'Password', 'Login_DateTime')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Rank', anchor=CENTER, width=80)
    tv.column('Name', anchor=CENTER, width=200)
    tv.column('Password', anchor=CENTER, width=200)
    tv.column('Login_DateTime', anchor=CENTER, width=220)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Rank', text='Id', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Password', text='Password', anchor=CENTER)
    tv.heading('Login_DateTime', text='Login_DateTime', anchor=CENTER)

    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mydb.commit()
    mycursor.execute("SELECT * FROM Logins")
    for dt in mycursor:
        tv.insert('', 'end', iid=dt[0], text=dt[0],
                  values=(dt[0], dt[1], dt[2], dt[3]))


# button
logins_btn = Button(root, text="Login List", borderwidth="10", command=login, font=("Consolas 13 bold"), bg="yellow",
                       fg="black")
logins_btn.place(x=950, y=650)


# Logout tv, function and button
def logout():
    tv = ttk.Treeview(root, selectmode="browse")
    tv.place(x=20, y=500)
    tv['columns'] = ('Rank', 'Name', 'Password', 'Logout_DateTime')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Rank', anchor=CENTER, width=80)
    tv.column('Name', anchor=CENTER, width=200)
    tv.column('Password', anchor=CENTER, width=200)
    tv.column('Logout_DateTime', anchor=CENTER, width=220)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Rank', text='Id', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Password', text='Password', anchor=CENTER)
    tv.heading('Logout_DateTime', text='Logout_DateTime', anchor=CENTER)

    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mydb.commit()
    mycursor.execute("SELECT * FROM Logouts")
    for dt in mycursor:
        tv.insert('', 'end', iid=dt[0], text=dt[0],
                  values=(dt[0], dt[1], dt[2], dt[3]))


logout_btn = Button(root, text="Logout List", borderwidth="10", command=logout, font=("Consolas 13 bold"), bg="yellow",
                       fg="black")
logout_btn.place(x=1130, y=650)


# Add function and button
def add():
    messagebox.showinfo('Outlet', 'Be Ready')
    root.destroy()
    import Register


add_btn = Button(root, text="Add Rocords", borderwidth="10", command=add, font=("Consolas 13 bold"), bg="yellow",
                       fg="black")
add_btn.place(x=950, y=550)

# Insert function and button


# Update record
def update_record():
    if entry_update.get() == 'Name':
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LCA',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE Register SET Name = %s  WHERE Name = %s "
        val = (entry_into_update.get(), entry_into_what_update.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('Updated', 'Records Updated! ')
    elif entry_update.get() == 'surname':
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LCA',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE Register SET surname = %s  WHERE surname = %s "
        val = (entry_into_update.get(), entry_into_what_update.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('Updated', 'Records Updated! ')
    elif entry_update.get() == 'Phone_No':
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LCA',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE Register SET Phone_No = %s  WHERE Phone_No = %s "
        val = (entry_into_update.get(), entry_into_what_update.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('Updated', 'Records Updated! ')
    elif entry_update.get() == 'Password':
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LCA',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE Register SET Password = %s  WHERE Password = %s "
        val = (entry_into_update.get(), entry_into_what_update.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('Updated', 'Records Updated! ')
    elif entry_update.get() == 'Next_of_kin_Fullname':
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LCA',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE Register SET Next_of_kin_Fullname = %s  WHERE Next_of_kin_Fullname = %s "
        val = (entry_into_update.get(), entry_into_what_update.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('Updated', 'Records Updated! ')
    elif entry_update.get() == 'Next_of_kin_Phone_No':
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LCA',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE Register SET Next_of_kin_Phone_No = %s  WHERE Next_of_kin_Phone_No = %s "
        val = (entry_into_update.get(), entry_into_what_update.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('Updated', 'Records Updated! ')
    elif entry_update.get() == 'ID_number':
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LCA',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE Register SET ID_number = %s  ID_number = %s "
        val = (entry_into_update.get(), entry_into_what_update.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('Updated', 'Records Updated! ')


# update label and entry
lab_update = Label(root, text="Update: ", bg="black", fg="lightblue", font=("Consolas 10 bold"))
lab_update.place(x=750, y=470)
entry_update = Entry(root, bg="lightblue", fg="black")
entry_update.place(x=830, y=470, width=220, height=30)

lab_into_update = Label(root, text="Which Update3: ", bg="black", fg="lightblue", font=("Consolas 10 bold"))
lab_into_update.place(x=750, y=400)
entry_into_update = Entry(root, bg="lightblue", fg="black")
entry_into_update.place(x=870, y=400, width=220, height=30)

lab_into_what_update = Label(root, text="Into Update2: ", bg="black", fg="lightblue", font=("Consolas 10 bold"))
lab_into_what_update.place(x=750, y=330)
entry_into_what_update = Entry(root, bg="lightblue", fg="black")
entry_into_what_update.place(x=860, y=330, width=220, height=30)

# update button
update_btn = Button(root, text="Update Records", borderwidth="5", command=update_record, font=("Consolas 13 bold"), bg="yellow",
                       fg="black")
update_btn.place(x=1070, y=470)

def admin_registration():
    global tv # making my tv to be global so that is can be accessible
    tv = ttk.Treeview(root, selectmode="browse")
    tv.grid(row=1, column=1, padx=20, pady=20)
    tv['columns'] = ('Rank', 'Name', 'Surname', 'Phone_No', 'Password', 'Next_of_kin_fullname', 'Next_of_kin_Cell_No'
                     , 'ID_number', 'Register_DateTime')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Rank', anchor=CENTER, width=80)
    tv.column('Name', anchor=CENTER, width=100)
    tv.column('Surname', anchor=CENTER, width=100)
    tv.column('Phone_No', anchor=CENTER, width=100)
    tv.column('Password', anchor=CENTER, width=100)
    tv.column('Next_of_kin_fullname', anchor=CENTER, width=190)
    tv.column('Next_of_kin_Cell_No', anchor=CENTER, width=190)
    tv.column('ID_number', anchor=CENTER, width=190)
    tv.column('Register_DateTime', anchor=CENTER, width=220)
# tv headings
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Rank', text='Rank', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Surname', text='Surname', anchor=CENTER)
    tv.heading('Phone_No', text='Phone_No', anchor=CENTER)
    tv.heading('Password', text='Password', anchor=CENTER)
    tv.heading('Next_of_kin_fullname', text='Next_of_kin_fullname', anchor=CENTER)
    tv.heading('Next_of_kin_Cell_No', text='Next_of_kin_Cell_No', anchor=CENTER)
    tv.heading('ID_number', text='ID_number', anchor=CENTER)
    tv.heading('Register_DateTime', text='Register_DateTime', anchor=CENTER)

    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LCA',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Admin_Register")
    for dt in mycursor:
        tv.insert('', 'end', iid=dt[0], text=dt[0],
                  values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8]))


# Registration Button
registration_btn = Button(root, text="Admin List", borderwidth="10", command=admin_registration, font=("Consolas 13 bold"), bg="yellow",
                       fg="black")
registration_btn.place(x=1130, y=550)

root.mainloop()