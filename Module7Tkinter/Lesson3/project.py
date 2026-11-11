
from tkinter import *

# Step 1: Create the main window
root = Tk()
root.title("ATM PIN Setup Interface")
root.geometry("400x500")
root.configure(bg="lightblue")

# Step 2: Create the details frame
details_frame = Frame(
    root,
    bg="lightyellow",
    width=350,
    height=120
)
details_frame.place(x=25, y=20)

# Step 3: Add labels and entry widgets
account_label = Label(
    details_frame,
    text="Account Name:",
    bg="lightyellow",
    font=("Arial", 11)
)
account_label.place(x=10, y=15)

account_entry = Entry(details_frame, width=25)
account_entry.place(x=140, y=15)

pin_label = Label(
    details_frame,
    text="Enter PIN:",
    bg="lightyellow",
    font=("Arial", 11)
)
pin_label.place(x=10, y=60)

pin_entry = Entry(details_frame, width=25, show="*")
pin_entry.place(x=140, y=60)

# Step 4: Create the button function
def confirm_pin():
    account = account_entry.get()
    pin = pin_entry.get()

    message_box.delete("1.0", END)

    if account == "" or pin == "":
        message_box.insert(END, "Please enter account name and PIN.")
    else:
        message_box.insert(
            END,
            "ATM PIN Setup Successful!\n"
            f"Account Name: {account}\n"
            "Your PIN has been set."
        )

# Step 5: Create a bordered keypad frame
keypad_frame = Frame(
    root,
    relief=SUNKEN,
    borderwidth=2,
    bg="white",
    width=250,
    height=190
)
keypad_frame.place(x=75, y=160)

# Step 6: Prepare the keypad values
keypad_values = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

# Step 7: Build the grid of cells
for i in range(4):
    for j in range(3):
        cell = Frame(
            keypad_frame,
            relief=RAISED,
            borderwidth=2,
            bg="lightgray",
            width=70,
            height=40
        )
        cell.grid(row=i, column=j, padx=5, pady=5)

        label = Label(
            cell,
            text=keypad_values[i][j],
            font=("Arial", 14, "bold"),
            bg="lightgray"
        )
        label.pack(expand=True)

# Step 8: Add the button and message box
set_button = Button(
    root,
    text="Set ATM PIN",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=confirm_pin
)
set_button.place(x=135, y=370)

message_box = Text(
    root,
    width=40,
    height=4,
    font=("Arial", 10)
)
message_box.place(x=25, y=415, width=350, height=70)

# Step 10: Run the application
root.mainloop()
