#take one charcter input from user
char=input("Enter a character:")
#display the ASCI value according to the input
print("The ASCI value of",char,"is",ord(char))

ch=input("Enter a character to check it's type:")
if ch in range(48,58):
    print("Digits")
elif ch in range(65,91):
    print("Upper case")
elif ch in range(97,123):
    print("Lower case")
elif ch==32:
    print("Space")
else:
    print("Special character")

