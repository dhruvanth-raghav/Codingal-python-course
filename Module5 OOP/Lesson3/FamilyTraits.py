class Parent :
    #Parent constructor method
    def __init__(self, eye_colour, bank_balance, height):#Constructor method
        self.eye_colour=eye_colour
        self.bank_balance=bank_balance
        self.height=height

    def show_traits(self):
        print("Eye colour:", self.eye_colour)
        print("Height:",self.height)
        print("Bank balance:",self.bank_balance)

#=======================================================================

class Kid(Parent): #The Kid class is inheriting from the Parent class
    def __init__(self, name, blood_type, eye_colour, bank_balance, height):
        #The following 2 are the Properties of  the Child Class
        self.name = name
        self.blood_type=blood_type
        #Call the Parent constructor below⬇️
        super().__init__(eye_colour, bank_balance, height)

    def show_traits(self):
        print("Name:",self.name)
        print("BLood Type:", self.blood_type)
        super().show_traits()

    def show_hobbies(self):
        self.hobbies = ["Playing Drums","Listeing to music"]
        print(self.hobbies)

#--------------------------------------------------------------------
dhruvanth = Kid("Dhruvanth","B+","Brown", 3000000000, 181)   

dhruvanth.show_traits()

print(f"I inherited Rs.{dhruvanth.bank_balance}")
print("IS kid inheriting from parent?", issubclass(Kid, Parent))

dhruvanth.show_hobbies()





