palindrome=(9,3,5,5,3,9)

def check_palindrome(tpl):
    start=0
    end=len(tpl)-1

    while start <end:
        if tpl[start]!=tpl[end]:
            return False

        start +=1
        end-=1
#If the while loop runs over the whole tuple,.then its a palindrome
    return True
if check_palindrome(palindrome):
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")
