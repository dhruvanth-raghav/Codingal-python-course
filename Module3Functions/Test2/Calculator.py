def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("DO NOT ENTER ZERO FOR THE SECOND NUMBER OR THE DENOMINATOR!")
        exit()
    

try:
    
    operation=input("Enter the opeation for the numbers:")
    num_1=float(input("Enter the first number:"))
    num_2=float(input("Enter the second number:"))

except ValueError:
    print("Enter a valid number!")
    exit()

if operation=="+" or operation=="add":
    print("The answer=",add(num_1, num_2))

elif operation=="-" or operation=="subtract" or operation=="sub":
    print("The answer=", subtract(num_1,num_2))

elif operation=="*" or operation=="multiply" or operation=="multiplication":
    print("The answer=", multiply(num_1,num_2))

elif operation=="/" or operation=="divide" or operation=="division":
    print("The answer=",divide(num_1,num_2))

else:
    print("INVALID OPERATION!")



