from tkinter import * 
from tkinter import messagebox
import random 

root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showerror("Alert", "Stop! Virus Detected")

button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)
def confirm():
    response= messagebox.askyesno("Exit Confirmation","Are You Sure You Want To Quit?")
    if response:
        root.destroy()
    else:
        print("Exit Canceled!")
button2 = Button(root, text="Close", command=confirm)
button2.place(x=60, y=140)

def generate():
    emojis=["✅","✈️","⚡","🪟","🔊","🤑","🧭","🥶"]
    emojiChoice = random.choice(emojis)
    button.config(text=f"{emojiChoice} Scan for Virus! {emojiChoice}")
button3 = Button(root, text="Give me an emoji",command=generate)
button3.place(x=80, y=180)


root.mainloop()