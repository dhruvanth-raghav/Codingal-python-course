cost_amt=float(input("Enter original price:"))
sell_price=float(input("Enter the selling price:"))

if sell_price > cost_amt:
    print(f"Profit={sell_price-cost_amt}")
else:
    print("No profit")