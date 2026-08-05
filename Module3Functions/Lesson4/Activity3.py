while True:
    try:
        coin=int(input("Insert a coin: "))
    except ValueError:
        print("Invalid coin..TRY AGAIN!..with coins:-1, 2, 5, 10")
        continue


    if coin!=1 and coin!=2 and coin!=5 and coin!=10:
        print("Invalid coin! Try again with coins- 1, 2, 5, 10.\n")
        continue