# Define function to calculate cube
def cube(num):
    return num*num*num
# Define a function which will execute cube function if the user entered number is divisible by 3, otherwise return False
def TorF(num):
    if num%3==0:
        return cube(num)
    else:
        return False

a=int(input("Enter a number:"))
ans=TorF(a)
print(ans)