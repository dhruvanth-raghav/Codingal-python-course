print("===ATM CASH DISPENSER===")
customers_served=0
total_Dispensed=0
serving=True
note_100=note_50=note_20=note_10=note_5=note_1=0
while serving:
    name=input("Enter your name:")
    pin=input("Enter your PIN:")

    print(f"Hello{name}!Your pin matched!")
    amount=int(input("enter withdrawal amount:"))

    print(f"\nDispensing ₹{amount}for{name}:")
    remaining=amount   
    i=1
    while i<=6:
        if i==1: value=100
        elif i==2: value=50
        elif i==3: value=20
        elif i==4: value=10
        elif i==5: value=5
        else:
            value=1
        count= remaining//value
        if count>0:
            print(f"{count} X ₹{value} notes= {count*value}")
            remaining -=count*value

            if value==100:
                note_100 +=count
            elif value==50:
                    note_50 +=count
            elif value==20:
                    note_20 +=count
            elif value==10:
                    note_10+=count
            elif value==5:
                note_5 +=count
            else: 
                note_1 +=count
        i+=1
    customers_served+=1
    total_Dispensed+=amount
    print(f"Transaction complete for {name}!\n")
    again=input("Next customer? (yes/no):").lower()
    if again!="yes":
        serving=False



print("\n=== Daily Denomination Report ===")
for slot in range(1, 7):                      # outer for -- one denomination per loop
    if slot == 1: value, total = 100, note_100
    elif slot == 2: value, total = 50, note_50
    elif slot == 3: value, total = 20, note_20
    elif slot == 4: value, total = 10, note_10
    elif slot == 5: value, total = 5, note_5
    else: value, total = 1, note_1
    if total > 0:
        print(f"  {value}-unit notes dispensed : {total} ", end="")
        for note in range(total):             # inner for -- one symbol per note
            print("=", end="")
        print()

print(f"\nCustomers served : {customers_served}")
print(f"Total dispensed  : {total_Dispensed} units")
print("ATM session closed. Goodbye!")
