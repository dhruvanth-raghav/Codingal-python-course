try:
    num1=int(input("Enter a num1:"))
    num2=int(input("Enter a num2:"))
    result=num1/num2
    msg=f"{num1} / {num2} = {result}"
    print(msg)
except ValueError:
    print("Pls enter two valid numbers")

except ZeroDivisionError:
    print("pls do not enter 0 for Number2")

# except TypeError:
#     print("You cannot join int and str together!")
else:
    print("Program ran successfully!")
finally:
    print("This will run no matter what!..THE END!")
