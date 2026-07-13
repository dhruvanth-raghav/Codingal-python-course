# Lesson: SPCM2L1 — Nested Conditional Statements (Jr)
print("====================================")
print(" Welcome to Ride Builder! ")
print("====================================")
print()


print("Step 1 pick your vehicle:")
print("1.Bike")
print("2.Car")
print()
choice=int(input("Enter 1 or 2:"))

if choice== 1:
    print("Step 2 pick your bike type:")
    print("1.Scooty")
    print("2.SuperBike")
    typeChoice=int(input("Enter 1 or 2 :"))
    if typeChoice==1:
        print("You picked : Scooty")
        print("Top speed : 80 km/h")
        print("Best for : City roads")
    elif typeChoice==2:
        print("You picked : SuperBike")
        print("Top speed:400km/h")
        print("Best for: Races")
    else:
        print("Invalid input")
elif choice==2:
    print("Step2 pick your car type :")
    print("1.SUV")
    print("2.Sedan")
    carType=int(input("Enter 1 or 2 :"))
    if carType ==1:
        print("You picked:SUV")
        print("top speed: 310")
        print("No.of of seats: 8 seater")
    elif carType ==2:
        print("Ypu picked: Sedan")
        print("Top speed: 320")
        print("no.of seats: 5 seater")
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")       