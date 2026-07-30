#THIS IS A FUNCTION DEFINTION (OR CREATION)
def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("fresh lemonade available for you!")
 
#CALLING A FUNCTION
greet_customer()      

PricePerCup=int(input("Enter the price of a cup of lemonade:"))
TotalCupSold=int(input("Enter the number of cup you want:"))

def calculate_total(price, cups):
    total= price * cups
    return total

bill= calculate_total(PricePerCup, TotalCupSold)
print("Your total bill:", bill)

def TQ_message(cups):
    if cups >=5:
        return "WOW! Big order! Thanks for the support!"
    else:
        return "Thanks for coming"

#Call function

msg=TQ_message(TotalCupSold)
print(msg)