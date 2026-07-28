rows=int(input("Enter how many rows do you want?:"))
i=0
for r in range(1,rows+1):
    for c in range(1,r+1):
        i+=1
        print(i,end="  ")
    print()