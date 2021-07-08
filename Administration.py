from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title('Administration')
root.geometry('800x800')
root['bg']='#fb0'

tv = ttk.Treeview(root, selectmode="browse")
tv.grid(row=1, column=1, padx=20, pady=20)
tv['columns'] = ('Rank', 'Name', 'Surname', 'Phone_No', 'Password')
tv.column('#0', width=0, stretch=NO)
tv.column('Rank', anchor=CENTER, width=80)
tv.column('Name', anchor=CENTER, width=80)
tv.column('Surname', anchor=CENTER, width=80)
tv.column('Phone_No', anchor=CENTER, width=80)
tv.column('Password', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Rank', text='Id', anchor=CENTER)
tv.heading('Name', text='name', anchor=CENTER)
tv.heading('Surname', text='surname', anchor=CENTER)
tv.heading('Phone_No', text='Phone_No', anchor=CENTER)
tv.heading('Password', text='Password', anchor=CENTER)

mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                               database='sql4423138', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Register")
for dt in mycursor:
    tv.insert('', 'end', iid=dt[0], text=dt[0],
              values=(dt[0], dt[1], dt[2], dt[3], dt[4]))


def delete():
    selected = tv.focus()
    values = tv.item(selected, 'values')
    mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                                   database='sql4423138', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "DELETE FROM Register WHERE id = %s"
    val = (values[0],)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Delete', 'Record deleted! ')

login_btn = Button(root, text="Login", borderwidth="10", command=delete, font=("Consolas 13 bold"), bg="yellow",
                   fg="black")
login_btn.place(x=60, y=350)


root.mainloop()