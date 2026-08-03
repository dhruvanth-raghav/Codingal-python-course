def calculate_discount(price,discount):
    return price-(discount/100)*price

ActualPrice=float(input("Enter the actual price of the item:"))
discountPerc=float(input("Enter the discount percentage:"))

print(calculate_discount(ActualPrice,discountPerc))