class WhatsappChat:
    def __init__(self):
        print("Creating the object in Constructor")

    def __del__(self):
        print("Deleting the object in Destructor")

print("Will now create an object")
chat=WhatsappChat()

del chat 

print("Program ends here....")
