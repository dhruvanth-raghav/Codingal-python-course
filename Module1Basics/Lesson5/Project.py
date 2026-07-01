#take temp input from user
temp=float(input("Enter the temperature"))
#check if temp is suitable for light clothes or jackets
if temp>=25:
    #if temp more than 25'c
    print("You can wear light clothes")
else:
    #if temp less than 25'c
    print("Wear a jacket or a pullover")