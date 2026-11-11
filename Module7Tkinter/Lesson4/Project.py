
import tkinter as tk
from tkinter import messagebox

# Step 1: Create the main window
root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("450x400")
root.configure(bg="lightblue")

# Step 2: Add heading and instructions
heading = tk.Label(
    root,
    text="After-School Routine Checker",
    font=("Arial", 18, "bold"),
    bg="darkblue",
    fg="white",
    pady=10
)
heading.pack(fill="x", pady=10)

instruction = tk.Label(
    root,
    text="Enter your next after-school task:",
    font=("Arial", 12),
    bg="lightblue"
)
instruction.pack(pady=10)

# Step 3: Create Entry and Key Label
task_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30
)
task_entry.pack(pady=10)

key_label = tk.Label(
    root,
    text="Last character typed: None",
    font=("Arial", 11),
    bg="lightyellow"
)
key_label.pack(pady=10)

# Step 4: Bind a Keypress Event
def handle_keypress(event):
    character = event.char
    key_label.config(text="Last character typed: " + character)

task_entry.bind("<Key>", handle_keypress)

# Step 5: Bind a Mouse-Click Event
def handle_click(event):
    routine_label.config(
        text="Routine area clicked!"
    )

routine_label = tk.Label(
    root,
    text="Click here to check your routine",
    font=("Arial", 12, "bold"),
    bg="lightgreen",
    width=35,
    height=2
)
routine_label.pack(pady=15)

routine_label.bind("<Button-1>", handle_click)

# Step 6: Create the Routine-Checking Function
def check_routine():
    task = task_entry.get()

    if task.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter your after-school task!"
        )
    else:
        messagebox.showinfo(
            "Routine Checker",
            "Your next task is: " + task
        )

# Step 7: Connect the Button Command
check_button = tk.Button(
    root,
    text="Check My Routine",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=check_routine
)
check_button.pack(pady=15)

# Step 8: Run the application
root.mainloop()
