try:
    num=int(input("Enter a number:"))
    print("USer entered:",num)
except ValueError as ex:
    print("You entered a invalid number!")
    # print(ex)
#THESE EXCEPTIONS CONNOT BE CAUGHT BY PYTHON ON RUNTIME
#1:-IndentationError
#2:-SyntaxError
