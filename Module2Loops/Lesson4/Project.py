print("====🍅GROCERY BILLING QUEUE🥕====")
print()
LowPriceItems=0
MediumPriceItems=0
HighPriceItems=0
customers_served=0
total_sales=0
billing=True
print()
 
while billing:                             
    name=input("Please enter your name:")
    NoOfItems=int(input(f"Hello {name}! How many items are you buying? "))
 
    if NoOfItems<= 0:
        print("Invalid input❌..Try again!")
        print()
       
    print("Billing your items..Please wait⏳")
    TotalNoOfCustumers=0
    item_number=1
 
    while item_number <=NoOfItems:       
        item_name= input("Enter the name of your item:")
        price=int(input("Enter the price of your account:"))
        quantity=int(input("Enter quantity:"))
 
        if price<=0 or quantity <=0:
            print("Invalid input❌..Try again")
        item_total=price*quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")
        TotalNoOfCustumers+=item_total
 
        if price<50:
            LowPriceItems=LowPriceItems+quantity
        elif price <= 100:
            MediumPriceItems=MediumPriceItems+quantity
        else:
            HighPriceItems=MediumPriceItems+quantity
 
        item_number+=1
 
    customers_served=customers_served+1
    total_sales=total_sales+TotalNoOfCustumers
    print()
    print("Billing in progress..Please wait⏳")
    print("Billing complete!✅🥳")
    nxtCustomer=input("Next customer? (yes/no): ").lower()
 
    if nxtCustomer!="yes":
        billing=False
        print()
        print()
 
 
print("===🥕GROCERY CATEGORY REPOR🍅===")
 
for i in range(1, 4):                  
    if i== 1:
        label, total = "Low price items", LowPriceItems
    elif i == 2:
        label, total = "Medium price items", MediumPriceItems
        label, total = "High price items", HighPriceItems
 
    if total > 0:
        print(f"  {label}: {total} ", end="")
 
        for item in range(total):          
            print("*", end="")
 
        print()
 
print(f"Customers served : {customers_served}")
print(f"Total sales      : {total_sales}")
print("==🍅GROCERY BILLING CLOSED🥕===")
