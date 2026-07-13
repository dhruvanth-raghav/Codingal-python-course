#find two ways of swaping variables
# 1st method
a=2
b=9
c=34
print(f"a={a} b={b} c={c}")
a , b , c= b , c ,a
print(f"a={a} b={b} c={c}")

#1st method(but with user input)
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number"))

a , b , c = b , c , a
print("~After swapping~")
print("a=",a)
print("b=",b)
print("c=",c)

#2nd method
a=2
b=5
c=78

#(d is a temp value)
d=a 
a=b
b=c
c=d
print("~After swapping~")
print("a=",a)
print("b=",b)
print("c=",c)

#2nd method(but with user input)
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number"))

#(d is a temp value)
d=a 
a=b
b=c
c=d
print("~After swapping~")
print("a=",a)
print("b=",b)
print("c=",c)

