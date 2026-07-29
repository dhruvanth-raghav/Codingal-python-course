#Flyod's triangle with emojis
print("FLOYD'S 📐")
rows=int(input("Enter the no.of rows:"))
i=1

for r in range(1, rows+1):
    for c in range(1, r+1):
        print("( ͡° ͜ʖ ͡°)",end="  ")
        i +=1
    print()

#Floyd's triangle with numbers
print("FLOYD'S 📐")
rows=int(input("Enter the no.of rows:"))
i=1

for r in range(1, rows+1):
    for c in range(1, r+1):
        print(i,end="  ")
        i +=1
    print()


