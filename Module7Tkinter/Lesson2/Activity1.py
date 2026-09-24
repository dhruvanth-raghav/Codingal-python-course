from tkinter import *

window= Tk()
window.title("Number Pad")
window.geometry("250x300")

numbers=[
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    ["#", 0, "*"]
]

for i in range(4):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure (i, weight=1, minsize=50)

    for j in range(3):
        frame = Frame(master=window, relief=SUNKEN, borderwidth=4)
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=numbers[i][j], bg="#d0efff")
        label.pack(padx = 5, pady=5)











window.mainloop()