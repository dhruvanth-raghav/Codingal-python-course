class Calculator:
    def __init__(self):
        self.a=0
        self.b=0

    #"Self" means the object that calls this method
    def get_input(self):
        self.a=int(input("Enter the first number:"))
        self.b=int(input("Enter the second number:"))


    def add(self):
        print(f"The sum of the numbers {self.a} and {self.b} = {self.a + self.b}")

    def subtract(self):
        return self.a - self.b

#====================================================================================
calc= Calculator()
print("Initial values of calc.a and calc.b =",calc.a, calc.b)

calc.get_input()
calc.add()

print(f"The diffefrence between {calc.a} and {calc.b} ={calc.subtract()}")

