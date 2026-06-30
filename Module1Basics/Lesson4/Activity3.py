# M1 L4 A3

# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.

# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.

# 3) Print the total marks stored in `sum`.

# 4) Calculate the percentage:

# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)

# - Multiply the result by 100

# Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.

math=int(input("Enter marks:"))
eng=int(input("Enter marks:"))
science=int(input("Enter marks:"))
hindi=int(input("Enter marks:"))

sum=math+eng+science+hindi
print("the total marks of all subjects=",sum)

perc=(sum/400)*100
print(perc)
