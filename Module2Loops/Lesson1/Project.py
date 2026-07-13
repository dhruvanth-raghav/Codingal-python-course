print("********************************************************")
print("         🌴 HOLIDAY ACTIVITY PLANNER!🗼")
print("-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print()
choice=int(input("Enter 1 for Beach holiday or 2 for Mountain holiday: "))
print()
if choice==1:
    print("****🍃WELCOME TO THE BEACH🏖️****")
    print("Fun activies for you⬇️")
    print("1.Swimming 🏊‍♂️")
    print("2.Sandcastle building⌛⌛")
    print()
    beach=int(input("Choose an activity (1 or 2)⬆️:"))
    print()
    if beach==1:
        print("Pack your swimsuits👙 , sunscreen😎 , towel🚿 , and goggles🥽")
        print("--HAVE FUN SWIMMING🌊--")
    elif beach==2:
        print("Bring a bucket🪣 and a showel🥣")
        print("--HAVE FUN BUILDING🏰--")
    else:
         print("INVALID INPUT..TRY AGAIN❌") 
elif choice==2:
    print("****🧗WELCOME TO THE MOUNTAINS🏔️****") 
    print("Fun activities for you⬇️")
    print("1.Hiking🧗‍♀️")
    print("2.Camping⛺")
    print()
    mountain=int(input("Choose an activity(1 or 2)⬆️")) 
    print()
    if mountain==1:
        print("Wear comfortable shoes 👟 and carry a water bottle🥤") 
        print("--ENJOY THE VIEWS🌄")
    elif mountain ==2:
        print("Packa tent⛺ , sleeping bag 🛏️ , and a flashligt🔦")
        print("--ENJOY YOUR CAMPING⛺--")
    else:
        print("INVALID INPUT...TRY AGAIN❌")
else:
    print("INVALID INPUT...TRY AGAIN❌")
print()
print("-------------------------------")
print(  "HAVE A AMAZING VACATION 🧗‍♀️🌄")
print("-------------------------------")
      

