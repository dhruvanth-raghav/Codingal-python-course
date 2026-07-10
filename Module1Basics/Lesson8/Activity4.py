# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.
a = int(input("Enter the integer : "))
b = int(input("Enter the integer : "))
c = int(input("Enter the integer : "))
# 2) Calculate the average of `a`, `b`, and `c`:
#    - Add them and divide by 3
#    - Store the result in `avg`
#    - Print `avg`
avg = (a + b + c) / 3
print("The average is:", avg)

# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:
#    - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
#    - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.
#    - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.
#    - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.
#    - Else if `avg` is greater than only `a`, print that it is just higher than `a`.
#    - Else if `avg` is greater than only `b`, print that it is just higher than `b`.
#    - Else if `avg` is greater than only `c`, print that it is just higher than `c`.
if avg > a and avg > b and avg > c:
    print("The average is higher than a, b, and c.")
elif avg > a and avg > b:
    print("The average is higher than a and b.")
elif avg > a and avg > c:
    print("The average is higher than a and c.")
elif avg > b and avg > c:
    print("The average is higher than b and c.")
elif avg > a:
    print("The average is just higher than a.")
elif avg > b:
    print("The average is just higher than b.")
elif avg > c:
    print("The average is just higher than c.")
# 4) If none of the above conditions match, print "invalid input".
else:
    print("Invalid input.")