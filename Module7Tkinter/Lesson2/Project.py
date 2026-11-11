
from tkinter import *
from datetime import date

# Step 2: Create the main window
root = Tk()
root.title("Workshop Welcome Desk")
root.geometry("450x450")
root.configure(bg="lightblue")

# Step 3: Add the heading label
heading = Label(
    root,
    text="Workshop Welcome Desk",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="darkblue",
    pady=15
)
heading.pack(fill=X, pady=15)

# Step 4: Add the name input
name_label = Label(
    root,
    text="Participant Name:",
    font=("Arial", 12),
    bg="lightblue"
)
name_label.pack(pady=5)

name_entry = Entry(
    root,
    font=("Arial", 12),
    width=30
)
name_entry.pack(pady=5)

# Step 5: Create the display function
def display_welcome():
    name = name_entry.get()

    if name.strip() == "":
        name = "Participant"

    greeting = f"Hello, {name}!"
    welcome = "Welcome to our workshop."
    today = date.today()

    # Step 6: Display multi-line output
    text_box.delete("1.0", END)

    text_box.insert(END, greeting + "\n")
    text_box.insert(END, welcome + "\n")
    text_box.insert(END, f"Today's Date: {today}\n")

# Step 7: Create the Check In button
check_button = Button(
    root,
    text="Check In",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=display_welcome
)
check_button.pack(pady=15)

# Step 6: Create the Text widget
text_box = Text(
    root,
    height=5,
    width=40,
    font=("Arial", 12)
)
text_box.pack(pady=10)

# Step 9: Run the application
root.mainloop()
