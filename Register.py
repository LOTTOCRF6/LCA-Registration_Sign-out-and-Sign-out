from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime

root = Tk()
root.config(bg="Black")
root.geometry("800x600")
root.title("Registration")

now = datetime.now()
formatted_data = now.strftime('%Y-%m-%d %H:%M:%s')
img = PhotoImage(file="resize-LogoLifeChoices300x80.png")
canvas = Canvas(root, width=1200, height=600)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

# Head
'''lab_name = Label(root, text="LIFE CHOICES ACADEMY ", bg="black", fg="lightblue", font=("Consolas 18 bold"))
lab_name.place(x=150, y=20)'''
lab_name = Label(root, text="Please Register and fill in all empty spaces! ", bg="black", fg="lightblue", font=("Consolas 12 bold"))
lab_name.place(x=70, y=150)

# start of label name and entry
lab_name = Label(root, text="Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=200)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=200, y=200, width=220, height=30)
# end of label name and entry

# start of label Surname and Entry
lab_surname = Label(root, text="Surname: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_surname.place(x=60, y=250)
entry_surname = Entry(root, bg="lightblue", fg="black")
entry_surname.place(x=200, y=250, width=220, height=30)
# end of Surname and Entry

# Start of ID number Label and Entry
lab_id_no = Label(root, text="ID No.: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_id_no.place(x=60, y=300)
entry_id_no = Entry(root, bg="lightblue", fg="black")
entry_id_no.place(x=200, y=300, width=220, height=30)
#  end of id number label and entry

# start of label Phone No and Entry
lab_phone_no = Label(root, text="Phone No.: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_phone_no.place(x=60, y=350)
entry_phone_no = Entry(root, bg="lightblue", fg="black")
entry_phone_no.place(x=200, y=350, width=220, height=30)
# end of Phone No label and Entry

# start of Password label and Entry
lab_password = Label(root, text="Password: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=400)
entry_password = Entry(root, show="*", bg="lightblue", fg="black")
entry_password.place(x=200, y=400, width=220, height=30)
# end of Password label and Entry

# start of Next of kin Fullname label and Entry
lab_fullname = Label(root, text="Next of kin Fullname:", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_fullname.place(x=60, y=450)
entry_fullname = Entry(root, bg="lightblue", fg="black")
entry_fullname.place(x=330, y=450, width=220, height=30)
# end of Next of kin Fullname label and Entry

# start of Next of kin Cell No label and entry
lab_cell_no = Label(root, text="Next of kin Cell No.:", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_cell_no.place(x=60, y=500)
entry_cell_no = Entry(root, bg="lightblue", fg="black")
entry_cell_no.place(x=330, y=500, width=220, height=30)
# end of Next of kin Cell No label and entry

# functions
# Register function
def register():
    mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                                   database='sql4423138', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "INSERT INTO Register (name,surname,phone_no,password,next_of_kin_Fullname,Next_of_kin_Phone_No, Register_DateTime, ID_number ) Value(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (entry_name.get(), entry_surname.get(), entry_phone_no.get(), entry_password.get(), entry_fullname.get(), entry_cell_no.get(), formatted_data, entry_id_no.get())
    mycursor.execute(sql, val)
    messagebox.showinfo("Output", "Registration Done.You can login.")
    mydb.commit()
    root.destroy()
    import Login

# button
register_button = Button(root, text="Register", borderwidth="10", command=register, font=("Consolas 13 bold"), bg="black", fg="lightblue")
register_button.place(x=350, y=540)

# Update record
def update_record():
    mydb = mysql.connector.connect(user='sql4423138', password='dwD2bh8UpN', host='sql4.freesqldatabase.com',
                                   database='sql4423138', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("""UPDATE Register SET
    		name = :first,
    		surname = :last,
    		id_ = :address,
    		city = :city,
    		state = :state,
    		zipcode = :zipcode

    		WHERE oid = :oid""",
                     {
                         'first': entry_name.get(),
                         'last': entry_surname.get(),
                         'address': entry_id_no.get(),
                         'city': entry_phone_no.get(),
                         'state': entry_password.get(),
                         'zipcode': entry_fullname.get(),
                         'oid': entry_cell_no.get(),
                     })
    messagebox.showinfo("Output", "Registration Done.You can login.")
    mydb.commit()

    '''tv.item(selected, text="", values=(entry_name.get(), entry_surname.get(), entry_phone_no.get(), entry_password.get(), entry_fullname.get(), entry_cell_no.get(), formatted_data, entry_id_no.get())

    mycursor.execute("""UPDATE customers SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""",
              {
                  'first': entry_name.get(),
                  'last': entry_surname.get(),
                  'address': entry_id_no.get(),
                  'city': entry_phone_no.get(),
                  'state': entry_password.get(),
                  'zipcode': entry_fullname.get(),
                  'oid': entry_cell_no.get(),
              })
    # Commit changes
    mydb.commit()'''




root.mainloop()