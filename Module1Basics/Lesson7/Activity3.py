# Activity 3: Grading System

# Objective: Write a program to show students' grades by entering five subject marks and
sub1=float(input("Enter marks:"))
sub2=float(input("Enter marks:"))
sub3=float(input("Enter marks:"))
sub4=float(input("Enter marks:"))
sub5=float(input("Enter marks:"))

avg=(sub1+sub2+sub3+sub4+sub5)//5

if avg in range(91,101):
    print("A1")
elif avg in range(81,91):
    print("A2")
elif avg in range(71,81):
    print("B1")
elif avg in range(61,71):
    print("B2")
elif avg in range(51,61):
    print(" C1")
elif avg in range(41,51):
    print("D1")
else:
    print("F")





# then calculating average marks and grades.

#If the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2
