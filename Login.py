from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("My_random_tkinter")
root.geometry("600x600")
root.config(bg="Black")
# start of label name
lab_name = Label(root, text="Enter your Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=20)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=260, y=20, width=220, height=30)
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
    if entry_name.get() != name or entry_password.get() != password:
        messagebox.showinfo(title="Output", message="Sorry try again")
        root.destroy()


    else:
        messagebox.showinfo(title="Output", message="Go through")
        root.destroy()
        import random_tkinter



# login button
login_btn = Button(root, text="Login", borderwidth="10", command=login, font=("Consolas 13 bold"), bg="black", fg="lightblue")
login_btn.place(x=80, y=150)


# clear function
def clear():
    entry_name.delete(0, END)
    entry_password.delete(0, END)


# clear button
clear_button = Button(root, text="Clear", borderwidth="10", command=clear, font=("Consolas 13 bold"), bg="black", fg="lightblue")
clear_button.place(x=240, y=150)


# exit function
def exit_program():
    return root.destroy()


# exit button
exit_button = Button(root, text="exit", borderwidth="10", command=exit, font=("Consolas 13 bold"), bg="black", fg="lightblue")
exit_button.place(x=390, y=150)








root.mainloop()