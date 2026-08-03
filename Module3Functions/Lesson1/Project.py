def greet_customer():
    print("Welcome to Art supplies store!🎨")
    print("Enjoy your shopping!")

greet_customer()

PricePerItem=float(input("Enter the price of item💵:"))
total_items=int(input("Enter the no. of itmes bought:")) 

def calculate_total(price, items):
    total= price*items
    return total

bill=calculate_total(PricePerItem, total_items)
print("Your total bill is:",bill)
#Asks user to enter the amount again if amount is less than the price
amtPaid=float(input("Enter the amount paid💰:"))
while amtPaid<bill:
    print("Amount is not enough❌❌")
    amtPaid=float(input("Please enter the amt again❗:"))

def calculate_change(paid, total):
    change=paid-total
    return change

change=calculate_change(amtPaid,bill)
print("your change is🪙:",change)

def thx_msg(items):
    if items>5:
        return "WOW!, Big order,💗 THANK YOU FOR THE SUPPORT!🙏"
    else:
        return "THANKS FOR COMING!💗"

msg=thx_msg(total_items)
print(msg)


