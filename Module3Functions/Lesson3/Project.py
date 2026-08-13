def calculate_change(paid, price):
    return paid-price
ticket_price=30
print("---🪙PARKING TICKET PAYMENT HELPER🪙---")
print(f"Ticket price: ${ticket_price}")
print("Accepted coin values: 1,2,5 and 10")

total_inserted=0
coins_inserted=0

while True:
    try:
        coin=int(input("Insert coins(1, 2, 5, 10):"))
    except ValueError:
        print("Invalid input❌.Please enter a valid coin")
        continue

    if coin!=1 and coin!=2 and coin!=5 and coin!=10:
        print("Error❗..Invalid coin!❌..Please use only 1, 2, 5, 10")
        continue
    total_inserted+=coin
    coins_inserted+=1
    print(f"Coins accepted..Total coins inserted:${total_inserted}")

    if total_inserted>ticket_price:
        print("Excess coin input❗")
        break

change_due= calculate_change(total_inserted, ticket_price)

if change_due==0:
    pass
else:
    print(f"Your change is: ${change_due}")

print()
print("===🧾TICKET RECEIPT🧾===")
print(f"Ticket price: ${ticket_price}")
print(f"Coin Inserted: {coins_inserted}")
print(f"Total paid: ${total_inserted}")
print(f"change given: ${change_due}")