items=["Pencil","Eraser","Protractor","Sharpener","Fevicol"]
stock_counts=[12,0,8,20,7]

#Create a dictionary where key is the item, value is the stock count
#DISCTIONARY COMPREHENSION


inventory={ element: stock for element, stock in zip(items, stock_counts)}
print(inventory)
# z=zip(items, stock_counts)
# print(list(z))
#Find only the items which are still in stock

in_stockItems=[elem for elem in items if inventory[elem]>0 ]
print("In stock items:",in_stockItems)


customer_choice=input("Enter the stationary items u wish to purchase:")
if customer_choice not in inventory or inventory[customer_choice]==0:
    print(customer_choice, "Is out of stock...Come tomorrow!")
    exit()

prices=[10,5,40,15,25]
markup= int(input("Enter the amount you want to add to every price:"))

marked_prices=list(map(lambda price:price + markup, prices))
#Map function allows us to do an operation on every element of the list
print("Increased prices are", marked_prices)

item_index=items.index(customer_choice)
print(f"Old price of {customer_choice} was {prices[item_index]} \n New price ={marked_prices[item_index]}")
