from tkinter import *
from datetime import date, datetime
#Create Window
window = Tk()

window.title("Module 7 lesson-1")
window.geometry("400x300")
lbl = Label(text="Hi There!", fg="white", bg="#072F5F", height=2, width=300)

name_lbl = Label(text="Full Name", bg = "#3895D3")

name_entry = Entry()

def display():
    name = name_entry.get()
    greeting = f"Hello, {name}\n"
    msg = "Welcome to your first Tkinter GUI App!\n Today's date is:"
    text_block.delete("1.0", "end")
    text_block.insert(END, greeting)
    text_block.insert(END, msg)
    text_block.insert(END, datetime.now())

btn = Button(text="Begin", command=display,height=1, bg="#1261A0", fg="white")

text_block = Text(height=3)

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_block.pack()

window.mainloop()

