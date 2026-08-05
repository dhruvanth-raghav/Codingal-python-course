
def cube(num):
    '''this function returns the cube of the given number'''
    return num*num*num

def TorF(num):
    ''' this function will execute cube function if the user entered number is divisible by 3, otherwise return False'''
    if num%3==0:
        return cube(num)
    else:
        return False

a=int(input("Enter a number:"))
ans=TorF(a)
print(ans)