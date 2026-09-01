class OnlineProduct:
    def __init__(self, price):
        self.__price = price

    def sellPrice(self):
        print("Selling price of product = ", self.__price)

    def setPrice(self, price):
        self.__price = price
#===================================================================
laptop = OnlineProduct(40000)
laptop.sellPrice()

# laptop.__price += 50000
laptop.setPrice(50000)
laptop.sellPrice()
#you cannot directy change the value of aprivate attribute like this
laptop.__price = 100000
laptop.sellPrice()