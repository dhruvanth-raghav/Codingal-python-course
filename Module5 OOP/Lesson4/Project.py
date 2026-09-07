class Account:
    def __init__(self):
        self.__pin="1234"

    def show_pin(self):
        masked_pin= "*" * len(self.__pin)
        print("PIN:",masked_pin)

    def set_pin(self, new_pin):
        self.__pin=new_pin

account=Account()
account.show_pin()
account.set_pin("dhruvanth0987654321")
account.show_pin()