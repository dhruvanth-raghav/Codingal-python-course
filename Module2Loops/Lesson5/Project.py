#Flyod's triangle with emojis
print("===FLOYD'S TRIANGLE📐[with emojis]===")
rows=int(input("How many rows do u want for the FLOYD'S TIANGLE📐?:"))
i=1

for r in range(1, rows+1):
    for c in range(1, r+1):
        print("🕸️",end="  ")
        i +=1
    print()

#Floyd's triangle with numbers
print("FLOYD'S TRIANGLE📐[with numbers]")
rows=int(input("How many rows do you want for the FLOYD'S TRIANGLE:"))
i=1

for r in range(1, rows+1):
    for c in range(1, r+1):
        print(i,end="  ")
        i +=1
    print()


print("===INVERTED TRIANGLE===")
print()
rows=int(input("How many rows do you want for the inverted triangle?:"))
for i in range(1,rows+1):
    for r in range( rows-i):
        print("   ", end="")

    for c in range(1, i +1):
        print("🔥 ",end="")
    print()

#Experimenting different patterns
print("===NORMAL TRIANGLE🔼(in the middle)===")
rows=int(input("How many rows do you want for the triangle placed inn the middle?🔼:"))
for i in range(1,rows+1):
    for r in range( rows-i):
        print("  ", end="")

    for c in range(1, i +1):
        print("🔥  ",end="")
    print()

#Experimenting different patterns
print("===RIGHT ANGLE TRIANGLE(upside down..left side)===")
rows=int(input("How many rows do you want for the upside down right angle triangle placed on the left side?:"))
for i in range(1,rows+1):
    for r in range( rows-i):
        print("", end="")

    for c in range(1,rows- i +1):
        print(" 🔥 ",end="")
    print()

#Experimenting different patterns
print("===RECTANGLE===")
rows=int(input("How many rows do you want for the rectangle🧰:"))
for r in range(1,6):
    for c in range(1,6):
         print("🔥  ", end= "  ")
    print()

#Experimenting different patterns
print("===STRAIGHT LINEE📏===")
for r in range(1,6):
         print(" 🔥 ", end= "  ")
   


