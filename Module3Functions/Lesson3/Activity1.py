
def calculate_Change(paid, price):
    '''Sends the change back to the caller'''
    change=paid-price
    return change

snack_PRICE=25
print("==WELCOME TO THE SNACK VENDING MACHINE==")
print("-ONLY ONE SNACK AVAILABLE-")
print("~ Accepted coins:-1, 2, 5, 10 ~")

coins_inserted=0
total_money_inserted=0

while True:
    try:
        coin=int(input("Insert a coin: "))
    except ValueError:
        print("invalid coin,Try again with coin:-1, 2, 5, 10")
        continue
    if coin!=1 and coin!=2 and coin!=5 and coin!=10:
        print("Invalid coin! Try again with coins- 1, 2, 5, 10.\n")
        continue


    coins_inserted +=1
    total_money_inserted += coin


    print(f"Inserted{coin}.Total collected so far:{total_money_inserted}\n")


    if total_money_inserted>=snack_PRICE:
        print("Enough money inserted.\n")
        break

change_due=calculate_Change(total_money_inserted, snack_PRICE)
print("THX for buying the snack!")

if change_due==0:
    pass
else:
    print("Here is your change: Rs.", change_due)

