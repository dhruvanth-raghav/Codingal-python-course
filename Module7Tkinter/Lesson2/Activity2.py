from tkinter import *

window= Tk()
window.title("User Registration")
window.geometry("400x400")

frame= Frame(master=window,height=200, width=340, bg="#d0efff")

lbl1 = Label(frame, text="Full Name", bg="#3895d3", fg="white", width=12)
lbl2 = Label(frame, text="Email ID", bg="#3895d3", fg="white", width=12)
lbl3 = Label(frame, text="Password", bg="#3895d3", fg="white", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")


def display():
    name= name_entry.get()
    greeeting= f"Hello, {name} !"
    msg = "\n Congratilations on your new account!"
    textbox.insert(END, greeeting)
    textbox.insert(END, msg)


textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text="Create account", command=display)



frame.place(x=20, y=0)

lbl1.place(x= 20, y=20)
name_entry.place(x=150, y=20)

lbl2.place(x= 20, y=80)
email_entry.place(x=150, y=80)

lbl3.place(x= 20, y=140)
password_entry.place(x=150, y=140)

btn.place(y=200, x=130)
textbox.place(y=250)


window.mainloop()